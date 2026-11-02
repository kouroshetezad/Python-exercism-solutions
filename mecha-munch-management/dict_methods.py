"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    shopping_card = {}
    for item in notes:
        shopping_card[item] = 1
    return shopping_card


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for key, value in recipe_updates:
        ideas[key] = value
    return ideas
    
def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """
    Combine user's cart with aisle and refrigeration info, sorted in reverse alphabetical order.
    
    :param cart: dict - user's shopping cart (item -> quantity)
    :param aisle_mapping: dict - item -> [aisle, refrigeration (True/False)]
    :return: dict - fulfillment cart (item -> [quantity, aisle, refrigeration])
    """
    fulfillment_cart = {}
    
    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle_info = aisle_mapping[item]
            fulfillment_cart[item] = [quantity] + aisle_info
    
    sorted_fulfillment_cart = dict(sorted(fulfillment_cart.items(), key=lambda x: x[0], reverse=True))
    
    return sorted_fulfillment_cart

    
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, aisle in fulfillment_cart.items():
        
        if store_inventory[item][0] > 0:
            store_inventory[item][0] -= aisle[0]
        if store_inventory[item][0] == 0:
             store_inventory[item][0] = "Out of Stock"
    return store_inventory
            
        

    
