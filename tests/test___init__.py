import pickle

from matter_exceptions import BaseAPIException, DetailedException


def test_base_api_exception_should_not_override_payload():
    my_payload = {"my-data": 1}
    BaseAPIException(description="a test", payload=my_payload)
    assert my_payload == {"my-data": 1}


def test_base_api_exception_base_case():
    e = BaseAPIException(description="a test")
    assert e.data == {"type": None, "message": "a test", "success": False}


def test_detailed_exception_happy_path():
    e = DetailedException(message="ugly Error")
    assert e.message == "ugly Error"


def test_detailed_exception_converts_topic_to_lower_camel_case():
    e = DetailedException(message="an error")
    assert e.type == DetailedException.TOPIC.lower().replace(" ", "_")


def test_detailed_exception_pickle_round_trip():
    """Testing the __reduce__ method"""
    e = DetailedException(message="an error")
    pickled = pickle.dumps(e)
    unplicked = pickle.loads(pickled)
    assert e == unplicked
