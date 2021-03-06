from django.test import TestCase, Client
from django.urls import reverse, resolve
from idp_data.idp_data.models import MunicipalityHostname, Municipality


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.muniCode = "wc001"
        self.hostname = "localhost"

    def test_events_GET_allowed(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )

        MunicipalityHostname.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        url = reverse('events') + "?hostname=" + self.hostname
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_event_POST_disallowed(self):
        url = reverse('events') + "?hostname=" + self.hostname
        response = self.client.post(url)

        self.assertEquals(response.status_code, 405)    #not allowed

    def test_event_DELETE_disallowed(self):
        url = reverse('events') + "?hostname=" + self.hostname
        response = self.client.delete(url)

        self.assertEquals(response.status_code, 405)    #not allowed


    def test_geography_details_GET_allowed(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )

        MunicipalityHostname.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        url = reverse('geo') + "?hostname=" + self.hostname
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Municipality.objects.count(), 1)
        self.assertEquals(MunicipalityHostname.objects.count(), 1)

    def test_geography_details_POST_disallowed(self):
        url = reverse('geo') + "?hostname=" + self.hostname
        response = self.client.post(url)

        self.assertEquals(response.status_code, 405)    #not allowed

    def test_geography_details_DELETE_disallowed(self):
        url = reverse('geo') + "?hostname=" + self.hostname
        response = self.client.delete(url)

        self.assertEquals(response.status_code, 405)    #not allowed