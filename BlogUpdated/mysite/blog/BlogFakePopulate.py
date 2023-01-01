from django.test import TestCase

import faker
import asyncio
from django.utils.text import slugify
from typing import Iterable
import random
from django.contrib.auth.models import User

from .models import Post





class Generate:
    def __init__(self) -> None:
        self.Statuses = [
            Post.Status.DRAFT,
            Post.Status.PUBLISHED,
        ]
        self.__content_len = [x for x in range(1,6)]
        self.fake = faker.Faker()
        self.tags = ['django', 'rest', 'channels', 'computer', 'network',\
            'entertainment', 'fashion', 'adult', 'video', 'audio', 'image']

    def Gentitle(self):
        return self.fake.name()

    def GenSub(self, title: str):
        return "from " + title + " to " + self.fake.name()

    def GenSlug(self, string: str):
        return slugify(string)

    def GenContent(self, loop: int = 1):
        loop = random.choice(self.__content_len)
        a = ""
        for _ in range(1, loop+1):
            a += self.fake.text()
        return a
    def Create(self):
        self.title = self.fake.sentence()
        self.slug = self.GenSlug(self.title)
        self.body = self.GenContent()

    

    def Populate(self):
        self.Create()
        Post.objects.create(
            title = self.title, slug=self.slug, body=self.body,
            author=User.objects.get(username='creator'),
            status=random.choice(self.Statuses)
        )


    def PopulateTags(self):
        for post in Post.objects.all():
            tags = post.tags.all()
            if len(tags) > 0:
                continue 
            create_tags = []
            for i in range(random.choice(self.__content_len)):
                tag = random.choice(self.tags)
                if tag not in create_tags:
                    create_tags.append(tag)
            post.tags.add(*create_tags)
