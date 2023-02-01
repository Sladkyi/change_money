from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import filters
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.request import Request


from change.models import Message
from change.models import Profile


class Command(BaseCommand):
    help = 'Run the command'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout = 0.5,
            read_timeout = 1.0
        )
        bot = Bot(
            request=request,
            base_file_url=settings.PROXY_URL, 
            token=settings.TOKEN
            )
        print(bot.get_me())



