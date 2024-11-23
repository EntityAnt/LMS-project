from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateApiView,
                       LessonDestroyApiView, LessonListApiView,
                       LessonRetrieveApiView, LessonUpdateApiView)
from users.views import UserViewSet, PaymentViewSet

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)
router.register("users", UserViewSet)
router.register("payments", PaymentViewSet)

urlpatterns = [
                  path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
                  path("lesson/new/", LessonCreateApiView.as_view(), name="new"),
                  path("lesson/edit/<int:pk>/", LessonUpdateApiView.as_view(), name="edit"),
                  path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="retrieve"),
                  path("lesson/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="delete"),

              ] + router.urls
