# -coffee
This Python code implements a straightforward restaurant menu system. Initially, it showcases a menu, listing various items and their respective prices from a pre-defined dictionary (`dict_menu`). Each entry in this dictionary corresponds to a menu item, paired with its price.

Next, the code prompts users to place their orders, iterating through the process until they signal completion by typing "no". With each valid order, the code tallies the item's price into a cumulative total (`price`) and records the item and its price as a tuple in an `invoice` list.

Upon order completion, signified by the entry of "no", the code generates an invoice. It presents the items ordered alongside their individual prices by iterating over the `invoice` list. Subsequently, it displays the total bill calculated from the cumulative sum of all ordered items' prices.

Furthermore, the code incorporates error handling. It validates user input against the menu items. If an invalid item is entered, the code prompts the user to input a valid menu item.

Overall, this code offers a simplistic yet functional restaurant ordering system. It empowers customers to select from a provided menu and delivers a detailed invoice, elucidating their order specifics and the resulting total bill.
