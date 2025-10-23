from learn.models import Learn

class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")

        self.percent_off = self.session.get("percent_off")
        if not self.percent_off :
            self.percent_off = self.session["percent_off"] = 0
        if not cart :
            cart = self.session["cart"] = {}
        self.cart = cart

    def add_to_cart(self,learn):
        learn_id = str(learn.id)
        self.cart[learn_id] = {"price" : learn.price,"off":learn.precent_off,"discount_price":learn.discount_price}
        self.save()

    def remove_from_cart(self,learn_id:int):
        learn_id = str(learn_id)
        if learn_id in self.cart.keys() :
            del self.cart[learn_id]
        self.save()

    def clear(self):
        self.cart.clear()
        self.save()

    def get_total_price(self):
        return  sum([price["discount_price"] for price in self.cart.values()])

    def get_tax(self):
        return self.get_total_price() // 10

    def get_price_off(self):
        price = self.get_total_price() + self.get_tax()
        if self.percent_off != 0:
            return price * self.percent_off //100
        else:
            return 0

    def get_final_price(self):
        price = self.get_total_price() + self.get_tax()
        return price - self.get_price_off()

    def get_percent_tax(self):
        if self.get_total_price() == 0 :
            return "0"
        else:
            return "10"

    def save(self):
        self.session.modified = True

    def set_code(self,percent:int):
        self.session["percent_off"] = percent
        self.percent_off = percent
        self.save()

    def ids(self):
        return [int(item) for item in list(self.cart.keys())]

    def reget(self):
        learn_ids = self.ids()
        learns = Learn.objects.filter(id__in=learn_ids)
        self.clear()
        for learn in learns :
            self.add_to_cart(learn)

    def __iter__(self):
        learn_ids = self.cart.keys()
        learns = Learn.objects.filter(id__in=learn_ids)

        learn_map = {str(learn.id): learn for learn in learns}

        for learn_id, item in self.cart.items():
            temp_item = item.copy()
            temp_item['learn'] = learn_map.get(learn_id)
            yield temp_item
