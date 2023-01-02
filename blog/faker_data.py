from .models import Category, Blog
from faker import Faker
from datetime import datetime


def run():
    fake = Faker(['en-US'])
    categories = (
        "Life",
        "Science",
        "Politics",
        "Sports",

    )

    for category in categories:
        new_category = Category.objects.create(name=category)
        for _ in range(20):
            Blog.objects.create(category=new_category,
                                title=fake.name(), content=fake.text())

    print('Finished')
