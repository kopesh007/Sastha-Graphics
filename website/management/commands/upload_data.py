from django.core.management.base import BaseCommand
from website.models import store_data

posts=[
    {"topic":"banner","name":"Marriage Banners","content":"Traditional and modern wedding banners with exquisite Tamil fonts and beautiful couple portraits.","img":"marriage_image.jpeg"},
    {"topic":"banner","name":"Cultural Banners","content":"Vibrant and energetic banners for temple festivals, Pongal celebrations, and grand grand cultural events.","img":"cultural_image.jpeg"},
    {"topic":"banner","name":"Politics Banners","content":"High-energy, bold, and powerful political banners designed to honor leaders and capture the crowd's attention.","img":"politics_image.jpeg"},
    {"topic":"poster","name":"Movie & Album Posters","content":"Cinematic, dramatic designs perfect for short films, music albums, and YouTube video thumbnails.","img":"movie_image.jpeg"},
    {"topic":"poster","name":"Event Announcements","content":"Eye-catching posters for shop openings, school functions, and special community ceremonies.","img":"event_image.jpeg"},
    {"topic":"poster","name":"Business Promotions","content":"Clean, professional advertising posters to grow your local business and reach your target customers.","img":"business_image.jpeg"},
    {"topic":"invitation","name":"Wedding & Muhurtham","content":"Luxurious gold-foiled, deeply traditional Tamil wedding cards featuring elegant deity motifs like Lord Ganesha.","img":"muhurtham.jpeg"},
    {"topic":"invitation","name":"Gruhapravesam (Housewarming)","content":"Warm and welcoming cards for your new home ceremony, blending modern style with classic aesthetics.","img":"house.jpeg"},
    {"topic":"invitation","name":"Kadhukuthu & Manjal Neerattu","content":"Beautiful, colorful designs specifically crafted for ear-piercing and coming-of-age cultural ceremonies.","img":"manjal.jpeg"},
    {"topic":"digital art","name":"Digital Arts and Oil Paintings","content":"Beautiful digital paintings and portraits mixing classic South Indian styles with modern digital brushes.","img":"digital_art.jpeg"},
    {"topic":"digital art","name":"Tamil Typography","content":"Stylized Tamil letters, poetry quotes, and names perfectly designed for logos, t-shirts, and social media.","img":"tamil_typo.jpeg"},
    {"topic":"digital art","name":"Resume & Patterns","content":"Intricate digital Kolam designs and floral patterns perfect for modern world job applications and promotions.","img":"resume.jpeg"},





    
]

class Command(BaseCommand):




    def handle(self,*args,**kwargs):
        for j in posts:
            store_data.objects.create(topic=j["topic"],name=j["name"],content=j["content"],imageurl=j["img"])
        
        self.stdout.write(self.style.SUCCESS('Uploaded ! '))

