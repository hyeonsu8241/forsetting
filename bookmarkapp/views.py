# from django.shortcuts import render
import ssl

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from bookmarkapp.models import Bookmark

# 북마크에서 사용할 title을 가져오기 위한 크롤링 모듈
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.core.validators import URLValidator

has_ownership = [account_ownership_required, login_required(login_url='/accounts/login/')]


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
class BookmarkListView(ListView):
    model = Bookmark
    context_object_name = 'bookmark_list'
    template_name = 'bookmarkapp/list.html'

    def get_context_data(self, **kwargs):
        object_list = Bookmark.objects.filter(user=self.request.user)
        return super(BookmarkListView, self).get_context_data(object_list=object_list, **kwargs)


@login_required(login_url='/accounts/login/')
def bookmark_create(request):
    url = request.POST.get('url')
    title = request.POST.get('title')
    new_bookmark = Bookmark()
    validator = URLValidator()
    user = request.user

    try:
        validator(url)  # url 유효성 검사

        # 타이틀 가져오기
        context = ssl._create_unverified_context()
        html = urlopen(url, context=context)
        bs_object = BeautifulSoup(html, "html.parser")

        if not title:
            title = bs_object.find("title").text

        # DB 등록
        new_bookmark.url = url
        new_bookmark.title = title
        new_bookmark.user = user
        new_bookmark.favicon_url = "http://www.google.com/s2/favicons?domain_url=" + url
        new_bookmark.save()

    except ValidationError as exception:
        # URL is NOT valid here.
        print(exception)

    return HttpResponseRedirect(reverse('bookmarkapp:list'))


@login_required(login_url='/accounts/login/')
def bookmark_delete(request, pk):
    bookmark = Bookmark.objects.get(pk=pk)
    if bookmark.user == request.user:
        bookmark.delete()
        return HttpResponseRedirect(reverse('bookmarkapp:list'))


@login_required(login_url='/accounts/login/')
def bookmark_update(request, pk):
    url = request.POST.get('url')
    title = request.POST.get('title')
    new_bookmark = Bookmark.objects.get(pk=pk)
    validator = URLValidator()
    user = request.user

    try:
        validator(url)  # url 유효성 검사

        # 타이틀 가져오기
        context = ssl._create_unverified_context()
        html = urlopen(url, context=context)
        bs_object = BeautifulSoup(html, "html.parser")

        if not title:
            title = bs_object.find("title").text

        # DB 등록
        new_bookmark.url = url
        new_bookmark.title = title
        new_bookmark.user = user
        new_bookmark.favicon_url = "http://www.google.com/s2/favicons?domain_url=" + url
        new_bookmark.save()

    except ValidationError as exception:
        # URL is NOT valid here.
        print(exception)

    return HttpResponseRedirect(reverse('bookmarkapp:list'))