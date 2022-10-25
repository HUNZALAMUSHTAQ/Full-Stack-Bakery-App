from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys= cart.keys()
    for id in keys:
        if int(id) == product.id :
            return True
    # print(keys)
    print("blahhh :",product , cart)
    return False

@register.filter(name='cart_count')
def cart_count(product , cart):
    keys= cart.keys()
    for id in keys:
        if int(id) == product.id :
            return cart.get(id)
    # print(keys)
    print("blahhh :",product , cart)
    return 0

@register.filter(name='price_total')
def price_total(product , cart):
    return  product.price * cart_count(product,cart)

@register.filter(name='total_cart_price')
def total_cart_price(product , cart ):
    sum = 0 
    for p in product:
        sum += price_total(p,cart)
    return sum 
@register.filter(name="multiply")
def multiply(num1,num2):
    return num1 * num2 