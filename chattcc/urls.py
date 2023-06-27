from django.contrib import admin
from django.urls import path, include
from users.views import UsersViewSet
from groups.views import GroupsViewSet, ListUsersGroups, ListGroupMessages, ListGroupTimeline
from chat.views import MessageViewSet
from login.views import verificaLogin, criaLogin
from timeline.views import create
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='Users')
router.register('groups', GroupsViewSet, basename='Groups')
router.register('messages', MessageViewSet, basename='Messages')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('groups/<int:pk>/users/', ListUsersGroups.as_view()),
    path('groups/<int:pk>/messages/', ListGroupMessages.as_view()),
    path('groups/<int:pk>/timeline/', ListGroupTimeline.as_view()),
    path('login/', verificaLogin),
    path('login/create/', criaLogin),
    path('timeline/create/', create),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
