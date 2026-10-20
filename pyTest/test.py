import pytest
#assertion is a statement that checks if a condition is true. If the condition is false, it raises an AssertionError and stops the execution of the program. It is commonly used in testing to verify that the expected output matches the actual output.
# 
# 
class InvalidAmountError(Exception):
    pass

def pay(amount, pin):
    if amount <= 0:
        raise InvalidAmountError("Invalid amount")
    if pin != "1234":
        return "Invalid pin"
    return "Payment successful"
 
def test_valid_payment():
    assert pay(500,pin="1234") == "Payment successful"

def test_wrong_pin():
    assert pay(500,pin="0000") == "Invalid pin"

#parametrize: means “run the same test with different inputs”. Instead of writing 3 near-identical tests, you write 1 and give it a list of values.

#mark is a label to attach to tell this test is a parameterized test. It is used to group tests together and run them selectively. For example, you can run all tests marked as "parametrize" or "smoke" or "regression".
@pytest.mark.parametrize("amt",[0,-1, -100])
def test_invalid_amount(amt):
    with pytest.raises(InvalidAmountError):
        pay(amt, pin="1234")
