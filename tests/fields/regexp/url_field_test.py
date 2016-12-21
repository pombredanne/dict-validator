import unittest

from dict_validator.fields.regexp import UrlField


class UrlFieldTest(unittest.TestCase):

    def _ok(self, value):
        self.assertEqual(sorted(UrlField().validate(value)), [])

    def _nok(self, value):
        self.assertEqual(
            sorted(UrlField().validate(value)),
            [([], u'Value "{}" did not match url regexp'.format(value))])

    def test_ok(self):
        self._ok("http://www.example.com?foo=bar&zoo=loo#fff")

    def test_ok_ssl(self):
        self._ok("http://www.example.com?foo=bar#fff")

    def test_ok_no_protocol(self):
        self._ok("www.example.com?foo=bar#fff")

    def test_nok_wrong_protocol(self):
        self._nok("bla://www.example.com?foo=bar#fff")

    def test_nok_no_domain(self):
        self._nok("http://foo=bar#fff")


class ConfiguredUrlFieldTest(unittest.TestCase):

    def setUp(self):
        self._field = UrlField(protocol="ftp", domain="example.com",
                               path="/foobar")

    def test_ok(self):
        self.assertEqual(sorted(self._field.validate(
            "ftp://example.com/foobar?ffff#dffdf")), [])

    def _nok(self, val):
        self.assertEqual(
            sorted(self._field.validate(val)),
            [([], 'Value "{}" did not match url regexp'.format(val))])

    def test_nok_wrong_protocol(self):
        self._nok("http://example.com/foobar?ffff#dffdf")

    def test_nok_wrong_domain(self):
        self._nok("ftp://not-example.com/foobar?ffff#dffdf")

    def test_nok_wrong_path(self):
        self._nok("ftp://example.com/zooloo?ffff#dffdf")
