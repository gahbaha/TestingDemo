# conftest.py  (place this in the project root)
# Adds the src/ folder to Python's path so every test file can
# do  "import inventory"  without any extra setup.

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import cart
import inventory
import notifications
import orders





@pytest.fixture(autouse=True)
def reset_app_state():
    """Reset shared module state before every test."""
    inventory.reset_stock()
    notifications.clear()
    cart.reset_all_carts()
    orders._order_counter[0] = 1000
