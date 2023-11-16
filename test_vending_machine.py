"""
Pytest for vending machine project
Dustin Horne 100844416
November 16, 2023
For the 'vending_machine_graphical.py' script - WORKS
"""

from vending_machine import (VendingMachine, WaitingState, AddCoinsState,
DeliverProductState, CountChangeState,)

def test_VendingMachine():
# new machine object
    vending = VendingMachine()

# Add the states - ORG
# vending.add_state(WaitingState())
# vending.add_state(CoinsState())
# vending.add_state(DispenseState())
# vending.add_state(ChangeState())

# My revisions
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())
    


# Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'

# test that the first coin causes a transition to 'coins'
    vending.event = '200' # a twonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200 # pennies, was .total


# test that correct amount is read after each coin
    vending.event = "5"
    vending.update()
    assert vending.amount == 205
    
    vending.event = "10"
    vending.update()
    assert vending.amount == 215
    
    vending.event = "25"
    vending.update()
    assert vending.amount == 240
    
    vending.event = "100"
    vending.update()
    assert vending.amount == 340
    
    vending.event = "200"
    vending.update()
    assert vending.amount == 540
    
# Testing the amount of coins is enough
    vending.amount = 50  # Set amount to be sufficient for the product
    vending.event = "skittle"
    vending.update()
    assert vending.state.name == "count_change"
    assert vending.change_due == 45
    
#Testing when the coins aren't enough
    vending.amount = 20  # Set amount to be insufficient for the product
    vending.event = 'starburst'
    vending.update()
    assert vending.state.name == 'waiting'
    
#Testing when product is sold out
    product_name = "skittle"  
    VendingMachine.PRODUCTS[product_name] = (product_name, 5, 0)
    vending.event = "skittle"
    vending.update()
    assert f"Sorry, {product_name} is sold out."