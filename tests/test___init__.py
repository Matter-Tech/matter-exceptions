from unittest import TestCase

from matter_exceptions import BaseAPIException


class TestBaseAPIException(TestCase):
    def test_should_not_override_payload(self):
        my_payload = {"my-data": 1}
        BaseAPIException(description="a test", payload=my_payload)
        assert my_payload != {"my-data": 1}
