from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import *

class NewsFeed(Feed):
   title = 'News Medical Parkinsons Disease News Feed'
   link = '/news/'
   description = 'Latest Parkinsons Disease News and Research.'
   language = 'en-GB'

   def items(self):
       return News.pubdate.all()

   def item_title(self, item):
       return item.title

   def item_description(self, item):
       return truncatewords(item.body, 30)

