import unittest
import method
import field


class AuthenticatorTests(unittest.TestCase):

    def test_administrator_is_always_authenticated(self):
        service = method.AuthenticationService()
        adminId = 12345
        self.assertTrue(service.is_authenticated(adminId))

    def test_normal_user_is_not_authenticated_initially(self):
        service = method.AuthenticationService()
        normalUserId = 11111
        self.assertFalse(service.is_authenticated(normalUserId))

    def test_administrator_role_is_always_authenticated(self):
        service = method.AuthenticationService()
        adminId = 123
        roleName = 'admin'
        self.assertTrue(service.is_authenticated(roleName, adminId))

    def test_user_role_is_not_authenticated_initially(self):
        service = method.AuthenticationService()
        normalUserId = 11112
        role_name = 'user'
        self.assertFalse(service.is_authenticated(role_name, normalUserId))

    def test_user_role_with_admin_id_is_not_authenticated_initially(self):
        service = method.AuthenticationService()
        adminId = 12345
        role_name = 'user'
        self.assertFalse(service.is_authenticated(role_name, adminId))


class ShoppingCartTests(unittest.TestCase):

    def test_cat_may_just_have_a_single_item(self):
        shoppingCart = field.ShoppingCart()
        shoppingCart.add(10)
        self.assertEqual(1, shoppingCart.number_of_products())

    def test_cat_may_have_more_than_a_single_item(self):
        shoppingCart = field.ShoppingCart()
        shoppingCart.add(10)
        shoppingCart.add(10)
        self.assertEqual(2, shoppingCart.number_of_products())

    def test_cat_may_have_no_item(self):
        shoppingCart = field.ShoppingCart()
        self.assertEqual(0, shoppingCart.number_of_products())

    def test_the_total_price_of_the_cart_is_total_of_its_contents(self):
        shoppingCart = field.ShoppingCart()
        shoppingCart.add(10)
        self.assertEqual(10, shoppingCart.calculate_total_price())

    def test_the_total_price_of_the_cart_is_total_of_its_contents_for_several_prices(self):
        shoppingCart = field.ShoppingCart()
        shoppingCart.add(10)
        shoppingCart.add(13)
        self.assertEqual(23, shoppingCart.calculate_total_price())

    def test_the_total_price_of_the_cart_is_zero_when_it_has_no_items(self):
        shoppingCart = field.ShoppingCart()
        self.assertEqual(0, shoppingCart.calculate_total_price())

    def test_has_discount_when_contains_at_least_one_premium_item(self):
        shoppingCart = field.ShoppingCart()
        shoppingCart.add(100)
        shoppingCart.add(10)
        self.assertTrue(shoppingCart.has_discount())

    def test_has_discount_when_contains_at_least_one_premium_item(self):
        shoppingCart = field.ShoppingCart()
        shoppingCart.add(50)
        shoppingCart.add(50)
        self.assertFalse(shoppingCart.has_discount())

    def test_doesnt_have_discount_when_all_its_items_are_cheap(self):
        shoppingCart = field.ShoppingCart()
        shoppingCart.add(10)
        shoppingCart.add(10)
        shoppingCart.add(10)
        shoppingCart.add(10)
        self.assertFalse(shoppingCart.has_discount())

    def test_has_discount_when_contains_no_items(self):
        shoppingCart = field.ShoppingCart()
        self.assertFalse(shoppingCart.has_discount())


if __name__ == "__main__":
    unittest.main()
