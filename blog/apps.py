from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    BaseTemplate='blog/base.html'
