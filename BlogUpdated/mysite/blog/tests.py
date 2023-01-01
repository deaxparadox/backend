from django.test import TestCase, Client
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from .models import Post

class Data:
    name = "Nitish Kushwaha"

class Post1():
    title=Data.name
    slug=slugify(Data.name)
    body="This is my first post"


# class PostTestCase(TestCase):
#     def setUp(self) -> None:
#         Post.objects.create(
#             title=Post1.title,
#             slug=Post1.slug,
#             body=Post1.body
#         )
    
#     def testFirstPost(self):
#         mypost = Post.objects.get(title=Post1.title)
#         print(mypost.created)
#         print(mypost.updated)
#         print(mypost.publish)

#         self.assertEqual("Nitish Kushwaha", mypost.title)
#         self.assertEqual("nitish-kushwaha", mypost.slug)
#         self.assertEqual("This is my first post", mypost.body)

class TempatesTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_BlogShare(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        print(response.has_header("text/html; charset=utf-8"))
        # self.assertTemplateUsed(response.templates, 'list.html')