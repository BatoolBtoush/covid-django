from django.urls import path, include
from .views import home, all_countries, MyRecords, delete


urlpatterns = [
    path("", home, name="home"),
    path("allcountries", all_countries, name="all_countries"),
    path("myrecords", MyRecords.as_view(), name="my_records"),
    # path("record-delete/<int:pk>", DeleteMyRecord.as_view(), name="record_delete"),
    path("record-delete/<int:id>", delete, name="record-delete"),

]
