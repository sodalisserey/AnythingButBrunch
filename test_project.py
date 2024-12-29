import pytest
from project import get_menu, format_menu, validate_order, confirm_order, get_receipt


def test_get_menu():
    # Test for missing parameter
    with pytest.raises(TypeError):
        assert get_menu(None)

    # Input of csv results in creation of menu dictionary (items:price)
    assert get_menu("day_menu.csv") == (
        {"Cappuccino": 3.75, "Cookie": 3.25, "Croissant": 4.0, "Espresso": 2.75, "Matcha": 3.75, "Muffin": 3.75}
    )


def test_format_menu():
    # Test for missing parameters
    with pytest.raises(TypeError):
        assert format_menu(None)

    # Test for incomplete parameters
    with pytest.raises(TypeError):
        assert format_menu({"Cappuccino": 3.75})

    # Input of two dictionaries returns combined, tabulated menu
    assert format_menu({"Cappuccino": 3.75, "Croissant": 4.0},
                       {"Salad": 5.25, "Toastie": 5.5}) == (
               "╒═══════════════════════════╤═════════╕\n"
               "│ A L L - D A Y   M E N U   │         │\n"
               "│ Cappuccino                │  £ 3.75 │\n"
               "│ Croissant                 │  £ 4.00 │\n"
               "│ ------------------------- │ ------- │\n"
               "│ B R U N C H   M E N U     │         │\n"
               "│ Salad                     │  £ 5.25 │\n"
               "│ Toastie                   │  £ 5.50 │\n"
               "╘═══════════════════════════╧═════════╛"
           )

    assert format_menu({"Americano": 3.25},
                   {"Pancakes": 5.75}) == (
               "╒═══════════════════════════╤═════════╕\n"
               "│ A L L - D A Y   M E N U   │         │\n"
               "│ Americano                 │  £ 3.25 │\n"
               "│ ------------------------- │ ------- │\n"
               "│ B R U N C H   M E N U     │         │\n"
               "│ Pancakes                  │  £ 5.75 │\n"
               "╘═══════════════════════════╧═════════╛"
           )


def test_validate_order():
    # Test for missing parameters
    with pytest.raises(TypeError):
        assert validate_order(None)

    # Test for incomplete parameters
    with pytest.raises(TypeError):
        assert validate_order(({"Cappuccino": 3.75, "Croissant": 4.0}, {"Salad": 5.25, "Toastie": 5.5}))

    # Request for item not in menu returns False
    assert validate_order({"Cappuccino": 3.75, "Croissant": 4.0}, {"Salad": 5.25, "Toastie": 5.5},
                     "Americano", "10:00") == False

    # Request with typo returns False
    assert validate_order({"Cappuccino": 3.75, "Croissant": 4.0}, {"Salad": 5.25, "Toastie": 5.5},
                     "Cappuccinno", "10:00") == False

    # Request for lunch item outside of lunch hours returns False
    assert validate_order({"Cappuccino": 3.75, "Croissant": 4.0}, {"Salad": 5.25, "Toastie": 5.5},
                     "Salad", "15:00") == False

    # Request for lunch item within lunch hours returns True
    assert validate_order({"Cappuccino": 3.75, "Croissant": 4.0}, {"Salad": 5.25, "Toastie": 5.5},
                     "Salad", "11:00") == True

    # Request for day-menu item returns True
    assert validate_order({"Cappuccino": 3.75, "Croissant": 4.0}, {"Salad": 5.25, "Toastie": 5.5},
                     "Cappuccino", "12:00") == True


def test_confirm_order():
    # Test for missing parameters
    with pytest.raises(TypeError):
        assert confirm_order(None)

    # Test for incomplete parameters
    with pytest.raises(TypeError):
        assert confirm_order("Cappuccino")

    # Input of default answer "no" returns False
    assert confirm_order("Cappuccino", {"Muffin": 1, "Cookie": 2}) == False

    # Input of "done" request and "y" answer returns False with empty order dictionary
    assert confirm_order("done", {}, "y") == False

    # Input of non-empty order dictionary and "y" answer returns False with invalid request
    assert confirm_order("Cappuccino", {"Muffin": 1, "Cookie": 2}, "y") == False

    # Only input of "done" request, non-empty order dictionary and "y" answer returns True
    assert confirm_order("done", {"Muffin": 1, "Cookie": 2}, "y") == True


def test_get_receipt():
    # Test for missing parameters
    with pytest.raises(TypeError):
        assert get_receipt(None)

    # Test for missing parameters
    with pytest.raises(TypeError):
        assert get_receipt("Cappuccino")

    # Input of appropriate parameters returns tabulated receipt with date, service fee and total
    assert get_receipt({"Cappuccino": 2},
                       {"Cappuccino": 3.75, "Croissant": 4.0},
                       {"Salad": 5.25, "Toastie": 5.5},
                       "Thursday 12/12/24 16:00") == (
               "╒═══════════════════════════╤═════════╕\n"
               "│ Thursday 12/12/24 16:00   │         │\n"
               "│ ------------------------- │ ------- │\n"
               "│ R E C E I P T             │         │\n"
               "│ x2 Cappuccino             │  £ 7.50 │\n"
               "│ ------------------------- │ ------- │\n"
               "│ Service Fee               │  £ 0.75 │\n"
               "│ Total                     │  £ 8.25 │\n"
               "│ ------------------------- │ ------- │\n"
               "│ Thank you for your visit! │         │\n"
               "╘═══════════════════════════╧═════════╛"
           )

    # Inputted order of 100 cappuccinos returns correct grand total
    assert get_receipt({"Cappuccino": 100},
                       {"Cappuccino": 3.75, "Croissant": 4.0},
                       {"Salad": 5.25, "Toastie": 5.5},
                       "Thursday 12/12/24 16:00") == (
               "╒═══════════════════════════╤══════════╕\n"
               "│ Thursday 12/12/24 16:00   │          │\n"
               "│ ------------------------- │  ------- │\n"
               "│ R E C E I P T             │          │\n"
               "│ x100 Cappuccino           │ £ 375.00 │\n"
               "│ ------------------------- │  ------- │\n"
               "│ Service Fee               │  £ 37.50 │\n"
               "│ Total                     │ £ 412.50 │\n"
               "│ ------------------------- │  ------- │\n"
               "│ Thank you for your visit! │          │\n"
               "╘═══════════════════════════╧══════════╛"
           )

    # Inputted order of several items from both menus returned in tabulated receipt with date, service fee and total
    assert get_receipt({"Cappuccino": 1, "Croissant": 2, "Salad": 3, "Toastie": 4},
                       {"Cappuccino": 3.75, "Croissant": 4.0},
                       {"Salad": 5.25, "Toastie": 5.5},
                       "Thursday 12/12/24 16:00") == (
               "╒═══════════════════════════╤═════════╕\n"
               "│ Thursday 12/12/24 16:00   │         │\n"
               "│ ------------------------- │ ------- │\n"
               "│ R E C E I P T             │         │\n"
               "│ x1 Cappuccino             │  £ 3.75 │\n"
               "│ x2 Croissant              │  £ 8.00 │\n"
               "│ x3 Salad                  │ £ 15.75 │\n"
               "│ x4 Toastie                │ £ 22.00 │\n"
               "│ ------------------------- │ ------- │\n"
               "│ Service Fee               │  £ 4.95 │\n"
               "│ Total                     │ £ 54.45 │\n"
               "│ ------------------------- │ ------- │\n"
               "│ Thank you for your visit! │         │\n"
               "╘═══════════════════════════╧═════════╛"
           )