import unittest
from io import StringIO
from unittest.mock import patch
import main  # Replace with the actual module name containing the Grocery Management System code


class TestGroceryManagementSystem(unittest.TestCase):

    def test_add_product(self):
        with patch('builtins.input', side_effect=['TestProduct', '10', '5.99']):
            main.add_product()
        self.assertEqual(len(main.items), 1)

    def test_view_items(self):
        main.items = [{"name": "TestProduct", "quantity": 15, "price": 7.99}]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main.view_items()
        output = mock_stdout.getvalue()
        self.assertIn('TestProduct', output)

    def test_update_product(self):
        main.items = [{"name": "TestProduct", "quantity": 10, "price": 5.99}]
        with patch('builtins.input', side_effect=['TestProduct', 'UpdatedProduct', '15', '7.99']):
            main.update_product()
        self.assertEqual(main.items[0]['name'], 'UpdatedProduct')

    def test_remove_product(self):
        main.items = [{"name": "TestProduct", "quantity": 10, "price": 5.99}]
        with patch('builtins.input', return_value='TestProduct'):
            main.remove_product()
        self.assertEqual(len(main.items), 0)

    def test_purchase_product(self):
        main.items = [{"name": "TestProduct", "quantity": 10, "price": 5.99}]
        with patch('builtins.input', return_value='TestProduct'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main.purchase_product()
        output = mock_stdout.getvalue()
        self.assertIn('Pay $5.99 at the checkout counter.', output)

    def test_place_order(self):
        main.items = [{"name": "TestProduct", "quantity": 10, "price": 5.99}]
        with patch('builtins.input', side_effect=['TestProduct', 'done']):
            main.place_order()
        self.assertEqual(len(main.orders), 1)

    def test_view_order(self):
        main.orders = [{"items": [{"name": "TestProduct", "quantity": 1, "price": 5.99}]}]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main.view_order()
        output = mock_stdout.getvalue()
        self.assertIn('Order 1:', output)

   # def test_update_order(self):
    #    main.orders = [{"items": [{"name": "TestProduct", "quantity": 1, "price": 5.99}]}]
    #    with patch('builtins.input', side_effect=['1', 'TestProduct', 'done']):
    #        main.update_order()
    #    self.assertEqual(len(main.orders[0]['items']), 1)

    def test_add_customer(self):
        with patch('builtins.input', side_effect=['TestCustomer', 'test@example.com']):
            main.add_customer()
        self.assertEqual(len(main.customers), 1)


if __name__ == '__main__':
    unittest.main()
