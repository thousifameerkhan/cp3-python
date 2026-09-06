from decorators.core2 import hello_deco


def test_hello_deco():
    @hello_deco
    def localtest():
        return "hello, from the inside test file"

    # Execute the function to get the actual result!
    result = localtest()

    # Now assert against the result.
    # Note: If you used the wrapper fix from earlier, localtest()
    # will actually return "hello, from the inside test file",
    # not "hello world from decorator".
    assert result == "hello world from decorator"
