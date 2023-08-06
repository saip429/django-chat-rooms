from django.test import TestCase
from .models import Topic

# Create your tests here.


# create topic test case
class MessageTestCase(TestCase):
    def setUp(self):
        Topic.objects.create(name="testTopic")

    def test_topic(self):
        topic = Topic.objects.get(name="testTopic")
        if topic:
            print(topic)
