from django.test import TestCase

import faker
import asyncio
from django.utils.text import slugify
from typing import Iterable
import random
from letter.models import Letter

fake = faker.Faker()


class AsyncGenerate:
    async def Gentitle(self):
        return fake.name()

    async def GenSub(self, title: str):
        return "from " + title + " to " + fake.name()

    async def GenSlug(self, string: str):
        return slugify(string)

    async def GenContent(self):
        a = ""
        for _ in range(5):
            a += fake.text()
        return a
    async def Create(self):
        self.title = await self.Gentitle()
        self.subject = await self.GenSub(self.title)
        self.slug = await self.GenSlug(self.subject)
        self.content = await self.GenContent()

    async def Populate(self):
        self.Create()
        Letter.objects.create(
            title=self.title, subject=self.subject,
            slug=self.slug, content=self.content,
            status=Letter.Status.DELIVERED
        )

class Generate:
    def __init__(self) -> None:
        self.Statuses = [
            Letter.Status.SENT,
            Letter.Status.TRAVELING,
            Letter.Status.DELIVERED,
            Letter.Status.PENDING
        ]
        self.__content_len = [x for x in range(6)]

    def Gentitle(self):
        return fake.name()

    def GenSub(self, title: str):
        return "from " + title + " to " + fake.name()

    def GenSlug(self, string: str):
        return slugify(string)

    def GenContent(self, loop: int = 1):
        loop = random.choice(self.__content_len)
        a = ""
        for _ in range(loop):
            a += fake.text()
        return a
    def Create(self):
        self.title = self.Gentitle()
        self.subject = self.GenSub(self.title)
        self.slug = self.GenSlug(self.subject)
        self.content = self.GenContent()

    def Populate(self):
        self.Create()
        Letter.objects.create(
            title=self.title, subject=self.subject,
            slug=self.slug, content=self.content,
            status=random.choice(self.Statuses)
        )
