from matter_exceptions import BaseAPIException, DetailedException


def test_should_not_override_payload():
    my_payload = {"my-data": 1}
    BaseAPIException(description="a test", payload=my_payload)
    assert my_payload == {"my-data": 1}


def test_detailed_exception():
    e = DetailedException(message="ugly Error")
    assert e.message == "ugly Error"
