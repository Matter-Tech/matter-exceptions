import pickle

from matter_exceptions.exceptions.fastapi import NotFoundError
from matter_exceptions.exceptions.general import AuthenticationFailedError
from matter_exceptions.exceptions.api import ConflictError


def test_base_api_exception_should_not_override_payload():
    my_payload = {"my-data": 1}
    e = ConflictError(description="a test", detail=my_payload)
    assert e.detail == {"my-data": 1}


def test_base_api_exception_base_case():
    e = ConflictError(description="a test")
    assert e.detail== None
    assert e.as_json() == '{"status_code": 409, "description": "a test", "detail": null}'


def test_base_fastapi_exception_should_not_override_payload():
    my_payload = {"my-data": 1}
    NotFoundError(description="a test", detail=my_payload)
    assert my_payload == {"my-data": 1}


def test_base_fastapi_exception_base_case():
    e = NotFoundError(description="a test")
    assert e.detail== "Not Found"
    assert e.as_json() == '{"status_code": 404, "description": "a test", "detail": "Not Found"}'


def test_detailed_exception_happy_path():
    e = AuthenticationFailedError(description="ugly Error")
    assert e.detail == None
    assert e.type == "authentication_failed_error"
    assert e.description == "Authentication Failed Error: ugly Error"


def test_detailed_exception_converts_topic_to_lower_camel_case():
    e = AuthenticationFailedError(description="an error")
    assert e.type == AuthenticationFailedError.TOPIC.lower().replace(" ", "_")


def test_detailed_exception_pickle_round_trip():
    """Testing the __reduce__ method"""
    e = AuthenticationFailedError(description="an error")
    pickled = pickle.dumps(e)
    unplicked = pickle.loads(pickled)
    assert e == unplicked
