# Anything But Brunch
### _[Video Demo](https://youtu.be/OvBxFkCCr18)_
### _Description:_
Anything But Brunch is a café simulation that allows users to order items at any time of day, as long as they're not from the brunch menu (only available between 10:00-13:00). The programme displays menu items, prompts users for their order and once confirmed, displays a receipt to the user.

### _Main File & Functions:_
The programme uses the tabulate module to display a formatted menu, followed by a receipt of ordered items. The datetime module is used to determine the time of order, thereby allowing the programme to ensure brunch orders can only be placed between 10:00-13:00.

All five functions can be found in 'project.py', which also contains a main function that commits the programme to a while loop. This loop begins when the user is prompted to input their order, and is concluded when valid order conditions are met.

#### **get_menu(csv_file)**
uses csv.DictReader() to read menus inputted as csv files and returns them as dictionaries
#### **format_menu(day_menu, brunch_menu)**
receives menu dictionaries which are then combined, labelled and returned using tabulate()
#### **validate_order(day_menu, brunch_menu, request, current_time)**
validates each order request by matching it with items in either menus. If the request is a brunch item, the function checks current_time, determined by datetime.today(), for validity within brunch hours. Error messages are displayed if no matches are found, or if a brunch item is requested outside valid hours. If all conditions are met, the function returns order_valid as True, which prompts main() to append order dictionary with the requested item and its quantity (cumulative), thereby also restarting the while loop
#### **confirm_order(request, order)**
detects "done" in request and displays order dictionary as a list, before prompting the user to confirm order via "yes". This returns order_confirmed as True, which allows the programme to break out of the while loop in main(). If the answer to confirm order is not "yes", or if the order dictionary is empty, an error message is displayed and the while loop restarts until conditions are met
#### **get_receipt(order, day_menu, brunch_menu, current_datetime)**
calculates the price of each item type (item * quantity), then the sum of all items, inclusive of a 10% service fee. The total cost is presented in a tabulated receipt with current date/time

### _Supplementary Files & Functions:_
- **"test_project.py"** contains functions that test all five functions in project.py via pytest
- **"day_menu.csv"** contains non-brunch menu items and prices (customisable)
- **"brunch_menu.csv"** contains brunch menu items and prices (customisable)
- **"requirements.txt"** contains all pip-installable libraries

### _Further Work:_
The scope of this programme can be expanded to enable users to remove items from their order. An additional function that prompts payment from users may also add a dash of complexity and realism to this programme.