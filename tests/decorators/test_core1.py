from decorators.core1 import uppercase


def test_uppercase_decorator():
    @uppercase
    def greetname(name):
        return f"hello, {name}"

    assert greetname("alice") == "HELLO, ALICE"
