# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# url -> 이미지 변경을 위한 모듈들
# from urllib.parse import urlparse
# from django.core.files import File
# from utils.file import download, get_buffer_ext


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmark', null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    favicon_url = models.URLField("favicon_url", blank=True)
    url = models.URLField("url")

    def __str__(self):
        return self.url
    #
    # def save(self, *args, **kwargs):
    #     # ImageField에 파일이 없고, url이 존재하는 경우에만 실행
    #     if self.favicon_url and not self.thumbnail:
    #         thumbnail_url = self.favicon_url
    #
    #         if thumbnail_url:
    #             temp_file = download(thumbnail_url)
    #             file_name = '{favicon_url}_{urlparse}.{ext}'.format(
    #                 favicon_url=self.favicon_url,
    #                 # url의 마지막 '/' 내용 중 확장자 제거
    #                 # ex) url = 'https://~~~~~~/bag-1623898_960_720.jpg'
    #                 #     -> 'bag-1623898_960_720.jpg'
    #                 #     -> 'bag-1623898_960_720'
    #                 urlparse=urlparse(thumbnail_url).path.split('/')[-1].split('.')[0],
    #                 ext=get_buffer_ext(temp_file)
    #             )
    #             self.thumbnail.save(file_name, File(temp_file))
    #             super().save()
    #
    #     else:
    #         super().save()
