from django.db import models
import urllib.request as request
from bs4 import BeautifulSoup
# Create your models here.

OPEN_EDU_MAIN_URL = "https://openedu.ru"

class Last_lab(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Courses'
        #verbose_name_plural = 'courses'


def get_list():
    html_str = '<h3>Что было загруженно</h3>'

    # download cource names 
    html_file = (request.urlopen(OPEN_EDU_MAIN_URL)).read().decode('utf-8')
    soup = BeautifulSoup(html_file, 'lxml')

    found_cources_names = soup.findAll("div", attrs={"class":"course-title"})
    if (found_cources_names.__len__() == 0):
        return 'Parsing error ocured'
    for name in found_cources_names:
        html_str = html_str + '<p>' + name.a.text + '</p>'

    html_str += '<h3>Что добавленно в БД</h3>'
    db_items = Last_lab.objects.all()
    for downloaded_cource in found_cources_names :
        foundFlag = False
        for exist_cource in db_items:
            if (exist_cource.name == downloaded_cource.a.text):
                foundFlag = True
        if (not foundFlag):
            html_str = html_str + '<p>' + downloaded_cource.a.text + '</p>'
            Last_lab(name = downloaded_cource.a.text).save()

    html_str += '<h3>Что находится в БД</h3>'
    for item in Last_lab.objects.all():
        html_str = html_str + '<p>' + item.name + '</p>'

    return html_str
