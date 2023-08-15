"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart

@pytest.fixture
def cart():
    return Cart()
@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(500) is None
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product)
        assert product in cart.products
        assert cart.products[product] == 1

    def test_remove_product(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_all_product(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product,)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.clear()
        assert len(cart.products) == 0

    def test_buy_success(self, cart, product):
        initial_quantity = product.quantity
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == initial_quantity - 10
        assert len(cart.products) == 0

    def test_buy_failure(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()
        assert product.quantity == 1000
        assert len(cart.products) == 1