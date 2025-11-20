from django.urls import path, include
# from .views import PersonList, PersonCreate, PersonUpdate
from .views import PersonCrud
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r"person", PersonCrud)

urlpatterns = [
    path("", include(route.urls))
    # path('list/', PersonCrud.as_view({'get': 'list'}), name='list'),
    # path("create/", PersonCrud.as_view({'post': 'create'})),
    # path("update/<int:pk>/", PersonCrud.as_view({'put': 'update', 'patch': 'partial_update'})),
    # path("delete/<int:pk>/", PersonCrud.as_view({'delete': 'destroy'})),
    # # Retrieve, Update, Delete
    # path('get/retrive/<int:pk>/', PersonCrud.as_view({'get': 'retrieve'}), name='book-detail'),

    # generics
    # path("list/", PersonList.as_view(), name="List"),
    # path("create/", PersonCreate.as_view(), name="create"),
    # path("update/<int:pk>/", PersonUpdate.as_view(), name="update")
]