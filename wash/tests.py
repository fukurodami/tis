from django.test import TestCase, Client
from .models import Service, Order
from .forms import OrderForm


class TestCalls(TestCase):
    def setUp(self):
        Service.objects.create(
            title="Разовый", description="единичный визит", coast=250)

        Order.objects.create(street="qwe", build="1", home="1", title_id=1,
                             phone="+79009210534", time="10:00"
                             )

    def test_service(self):
        one = Service.objects.get(title="Разовый")
        self.assertEqual(one.title, "Разовый")
        self.assertEqual(one.description, "единичный визит")
        self.assertEqual(one.coast, 250)

    def test_order_title(self):
        one = Order.objects.get(title_id=1)
        self.assertEqual(one.title_id, 1)

    def form_order_is_valid(self):
        data_test = {
            'title': 1,
            'streeet': 'qwe',
            'build': 'qwe',
            'home': 'qwe',
            'time': '10:00',
            'phone': 'qwe'
        }
        form = OrderForm(data=data_test) 
        self.assertTrue(form.is_valid)

    def form_order_no_valid(self):
        data_test = {}
        form = OrderForm(data=data_test)
        self.assertFalse(form.is_valid())

    def view_catalog_response(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/login.html')


