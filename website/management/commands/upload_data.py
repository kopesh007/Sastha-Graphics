from django.core.management.base import BaseCommand
from website.models import store_data

posts=[
    {"topic":"banner","name":"Marriage Banners","content":"Traditional and modern wedding banners with exquisite Tamil fonts and beautiful couple portraits.","img":"marriage_image.jpeg"},
    {"topic":"banner","name":"Cultural Banners","content":"Vibrant and energetic banners for temple festivals, Pongal celebrations, and grand grand cultural events.","img":"cultural_image.jpeg"},
    {"topic":"banner","name":"Politics Banners","content":"High-energy, bold, and powerful political banners designed to honor leaders and capture the crowd's attention.","img":"politics_image.jpeg"},
    {"topic":"poster","name":"Movie & Album Posters","content":"Cinematic, dramatic designs perfect for short films, music albums, and YouTube video thumbnails.","img":"movie_image.jpeg"},
    {"topic":"poster","name":"Event Announcements","content":"Eye-catching posters for shop openings, school functions, and special community ceremonies.","img":"event_image.jpeg"},
    {"topic":"poster","name":"Business Promotions","content":"Clean, professional advertising posters to grow your local business and reach your target customers.","img":"business_image.jpeg"}


    
]

class Command(BaseCommand):




    def handle(self,*args,**kwargs):
        for j in posts:
            store_data.objects.create(topic=j["topic"],name=j["name"],content=j["content"],imageurl=j["img"])
        
        self.stdout.write(self.style.SUCCESS('Uploaded ! '))

