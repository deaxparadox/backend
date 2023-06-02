from django.test import TestCase
from django.urls import reverse

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from time import sleep


from .models import Question, Choice

class TestPages(TestCase):
    def setUp(self) -> None:
        # question 1
        self.question1 = Question.objects.create(question_text="What is hobby")
        self.question1.choice_set.create(choice_text="Painting")
        self.question1.choice_set.create(choice_text="Cooking")
        self.question1.choice_set.create(choice_text="Gaming")
        self.question1.choice_set.create(choice_text="Writing")

        # question 2
        self.question2 = Question.objects.create(question_text="What is favourite food?")
        self.question2.choice_set.create(choice_text="Biryani")
        self.question2.choice_set.create(choice_text="Fry Chicken")
        self.question2.choice_set.create(choice_text="Samosa")
        self.question2.choice_set.create(choice_text="Momos")
        
    def test_index(self):
        index = self.client.get("/")
        self.assertEqual(index.status_code, 200)
        self.assertTemplateUsed(index, "polls/index.html")
        
    def test_detail(self):
        detail = self.client.get(reverse("detail", args=(self.question1.id,)))
        self.assertEqual(detail.status_code, 200)
        self.assertTemplateUsed(detail, "polls/detail.html")
        self.assertContains(detail, self.question1.question_text)

    def test_votes(self):
        # In votes we get a redirection to result page
        votes = self.client.post(reverse("votes", args=(self.question1.id,)), {
            "choice": self.question1.choice_set.first().id
        })
        self.assertEqual(votes.status_code, 302)
        self.assertTemplateNotUsed(votes, "polls/result.html")
        self.assertEqual(self.question1.choice_set.first().votes, 1)

        self.assertEqual(votes.url, f"/{self.question1.id}/result/")

class TestBrowserPages(TestCase):
    def setUp(self) -> None:
        self.chrome = Chrome()
        self.local = "http://localhost:8000{}"

    def test_process(self):
        # visiting Polls (or index) page
        self.chrome.get(self.local.format(reverse("index")))
        self.assertEqual(self.chrome.title, "Polls")

        # find the first question and click it.
        q = self.chrome.find_element(By.XPATH, '/html/body/ul/li[1]/a')
        q.click()

        # get a detail page,
        # select 1 choice
        # click vote
        self.assertEqual(self.chrome.title, "Polls Detail")
        choice = self.chrome.find_element(By.ID, "choice1").click()
        vote = self.chrome.find_element(By.XPATH, "/html/body/form/input[2]")

        # after click on vote,
        # django will redirect to result page.
        vote.click()
        self.assertEqual(self.chrome.title, "Polls Result")

        sleep(2)

    def tearDown(self) -> None:
        self.chrome.quit()