from django.test import TestCase
from .models import Flight,Airport

# Create your tests here.
class ModelTestCase(TestCase):
    def test_is_valid(self):
        a1 = Airport.objects.create(code="TIA",location="Kathamndu")
        a2 = Airport.objects.create(code="PKA",location="pokhara")
        fl = Flight.objects.create(origin=a1,destination=a2,duration=1)
        self.assertTrue(fl.is_valid_flight())

    def test_count_arrivals(self):
        a1 = Airport.objects.create(code="TIA",location="Kathamndu")
        a2 = Airport.objects.create(code="PKA",location="pokhara")
        fl = Flight.objects.create(origin=a1,destination=a2,duration=1)
        value = a1.count_arrivals()
        self.assertEqual(value,1)
