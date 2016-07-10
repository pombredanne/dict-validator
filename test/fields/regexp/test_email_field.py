import unittest

from dict_validator.fields.regexp import EmailField


class DescribeTest(unittest.TestCase):

    def _ok(self, value, expected_errors=None, domain=None):
        self.assertEqual(
            sorted(EmailField(domain).validate(value)),
            expected_errors or [])

    def _nok(self, value, domain=None):
        self._ok(
            value,
            [([], 'Value \"{}\" did not match email regexp'.format(value))],
            domain)

    def test_ok(self):
        self._ok("test@example.com")
        self._ok("test.foo@example.bla.com")
        self._ok("test123@examp123e.com")
        self._ok("test-dff@example-ff.com")
        self._ok("test%%20dff@example-ff.com")
        self._ok("test+20dff@example-ff.com")

    def test_nok(self):
        self._nok("test@")  # missing domain
        self._nok("~~~@example.bla.com")  # wrong beginning
        self._nok("test123@examp++e.com")  # wrong domain
        self._nok("@example-ff.com")  # missing beginning
        self._nok("fdfdfdgdg")  # no @ char

    def test_ok_with_domain(self):
        self._ok("test@example.com", domain="example.com")

    def test_nok_with_wrong_domain(self):
        self._nok("test@not-example.com", domain="example.com")

    def test_deserialize(self):
        self.assertEqual(
            EmailField().deserialize("foobar@EXAMPLE.com"),
            "foobar@example.com")
