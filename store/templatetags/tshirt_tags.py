from django import template

register = template.Library()

@register.filter
def rupee(number):
    return f"₹ {number}"

@register.simple_tag
def min_price(tshirt):
    size=tshirt.sizevarient_set.all().order_by("price").first()
    return size.price

@register.simple_tag
def sale_price(tshirt):
    price=min_price(tshirt)
    discount=tshirt.discount
    return int(price-(price *(discount/100)))