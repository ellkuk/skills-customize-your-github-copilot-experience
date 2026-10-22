FREE_SHIPPING_THRESHOLD = 50.0


def calculate_subtotal(prices: list[float]) -> float:
    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative")
    return round(sum(prices), 2)


def apply_discount(subtotal: float, discount_percent: float) -> float:
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100 percent")
    discounted_total = subtotal * (1 - discount_percent / 100)
    return round(discounted_total, 2)


def qualifies_for_free_shipping(subtotal: float) -> bool:
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    return subtotal >= FREE_SHIPPING_THRESHOLD