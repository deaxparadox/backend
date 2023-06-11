from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.text import slugify
from django.urls import reverse

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

from time import sleep

from . import views
from .models import Post, Status

data: list[dict] = [
    dict(
        title="Test Blog 1",
        body="This is the test blog",
        status=Status.DRAFT
    ),
    dict(
        title="Test Blog 2",
        body="This is the test blog",
        status=Status.DRAFT
    )
]

class BlogTestCase(TestCase):
    def setUp(self):
        for blog in data:
            Post.objects.create(
                title=blog.get("title"),
                slug=slugify(blog.get("title")),
                body=blog.get("body"),
                status=blog.get("status")
            )

    def test_index(self):
        index = self.client.get("/")
        self.assertEqual(index.status_code, 200)
        self.assertTemplateUsed(index, 'base.html')
        self.assertTemplateUsed(index, "blog/index.html")
        self.assertEqual(index.resolver_match.func, views.index)

    def test_index_reverse(self):
        index = self.client.get(reverse("blog:index"))
        self.assertEqual(index.status_code, 200)
        self.assertTemplateUsed(index, 'base.html')
        self.assertTemplateUsed(index, "blog/index.html")
        self.assertEqual(index.resolver_match.func, views.index)

    def test_detail(self):
        for post, test_post in zip(Post.objects.all().order_by("created"), data):
            self.assertEqual(post.title, test_post['title'])
            detail = self.client.get(f"/{post.id}/{post.slug}/")
            self.assertEqual(detail.status_code, 200)
            self.assertTemplateUsed(detail, 'base.html')
            self.assertTemplateUsed(detail, "blog/detail.html")
            self.assertEqual(detail.resolver_match.func, views.detail)

    def test_detail_reverse(self):
        for post, test_post in zip(Post.objects.all().order_by("created"), data):
            self.assertEqual(post.title, test_post['title'])
            detail = self.client.get(reverse("blog:detail", kwargs={
                "id": post.id, "slug": post.slug
            }))
            self.assertEqual(detail.status_code, 200)
            self.assertTemplateUsed(detail, 'base.html')
            self.assertTemplateUsed(detail, "blog/detail.html")
            self.assertEqual(detail.resolver_match.func, views.detail)

    def test_detail_absolute(self):
        for post, test_post in zip(Post.objects.all().order_by("created"), data):
            self.assertEqual(post.title, test_post['title'])
            detail = self.client.get(post.get_absolute_url())
            self.assertEqual(detail.status_code, 200)
            self.assertTemplateUsed(detail, 'base.html')
            self.assertTemplateUsed(detail, "blog/detail.html")
            self.assertEqual(detail.resolver_match.func, views.detail)


class BlogBrowserTests(StaticLiveServerTestCase):
    URL = "http://localhost:8000{}"
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        for blog in data:
            Post.objects.create(
                title=blog.get("title"),
                slug=slugify(blog.get("title")),
                body=blog.get("body"),
                status=blog.get("status")
            )

        cls.selenium = Chrome()
        cls.selenium.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()

    
    def test_index(self):
        # blog 1
        self.selenium.get(f"{self.live_server_url}/")
        sleep(1)

        blog_1 = self.selenium.find_element(By.XPATH, '//*[@id="container"]/a[1]')
        blog_1.click()
        sleep(2)

        original_tab = self.selenium.current_window_handle
        self.selenium.switch_to.new_window("tab")
        new_tab = self.selenium.current_window_handle

        # blog 2
        self.selenium.get(f"{self.live_server_url}/")
        sleep(1)

        blog_1 = self.selenium.find_element(By.XPATH, '//*[@id="container"]/a[2]')
        blog_1.click()
        sleep(10)


