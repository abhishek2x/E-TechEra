
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('certification/', views.skills, name="skills"),
    # path('about/', views.about, name="about"),

    path('user/edit/<int:pk>',
         views.LearnerUpdateView.as_view(success_url="/"), name="user_edit"),
    # path('user/', views.LearnerListView.as_view(), name="user_list"),
    path('user/<int:pk>', views.LearnerDetailView.as_view(), name="user_detail"),
]
