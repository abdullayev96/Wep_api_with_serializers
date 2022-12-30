from django.urls import path,include
from rest_framework import routers
from .views import AuthorView



# router = routers.DefaultRouter()
# # router.register(r"authors", AuthorViewSet)
# router.register(r"category", CategoryViewSet)
# router.register(r"books", BookViewsSet)

urlpatterns =[
    # path('', include(router.urls))
    path('authors/list/', AuthorView.as_view(), name="author-list"),
    path('authors/<int:pk>/detail', AuthorView.as_view(), name="author-list"),
    path('authors/create/', AuthorView.as_view(), name="author-create"),
]