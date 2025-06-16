from decimal import Decimal
from django.conf import settings

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        from main.models import Chip, Resistor, Capacitor

        keys = self.basket.keys()
        basket_copy = self.basket.copy()
        for key in keys:
            type_, product_id = key.split(':')
            product = None
            if type_ == 'chip':
                product = Chip.objects.filter(id=product_id).first()
            elif type_ == 'resistor':
                product = Resistor.objects.filter(id=product_id).first()
            elif type_ == 'capacitor':
                product = Capacitor.objects.filter(id=product_id).first()

            if product:
                item = basket_copy[key]
                item['product'] = product
                item['type'] = type_
                yield item

    def add(self, product, count=1, update_count=False, product_type=None):
        product_id = str(product.id)
        key = f"{product_type}:{product_id}"
        if key not in self.basket:
            self.basket[key] = {'count': 0, 'price': str(product.price), 'type': product_type}
        if update_count:
            self.basket[key]['count'] = count
        else:
            self.basket[key]['count'] += count
        self.save()

    def remove(self, product_type, product):
        key = f"{product_type}:{product.id}"
        if key in self.basket:
            del self.basket[key]
            self.save()

    def clear(self):
        self.session[settings.BASKET_SESSION_ID] = {}
        self.session.modified = True

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def __len__(self):
        return sum(item['count'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['count'] for item in self.basket.values())
