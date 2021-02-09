import pytest

from app.schemas.customer import CustomerInSchema


@pytest.fixture
def payload_customer():
    return {
        "cpf": "12345678901",
        "birth_date": "2000-01-01",
        "email": "foo@bar.com",
        "phone": "11 1111 1111",
        "salary": 1000.00,
    }


def test_when_cpf_does_not_contain_11_digits_raise_exception(payload_customer):
    payload_customer["cpf"] = "1234567890"

    with pytest.raises(ValueError, match="CPF must contain 11 digits"):
        CustomerInSchema(**payload_customer)


def test_cpf_should_only_return_digits(payload_customer):
    expected = payload_customer["cpf"]
    payload_customer["cpf"] = "123.456.789-01"
    customer = CustomerInSchema(**payload_customer)
    assert customer.cpf == expected
