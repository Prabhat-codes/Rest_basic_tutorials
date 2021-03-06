from django.urls import path, include
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns

# Function based views
# urlpatterns=[
#     path('snippets/',views.snippet_list), 
#     path('snippets/<int:pk>/',views.snippet_detail),
# ]

# Class based views

urlpatterns=[
    path('snippets/',views.SnippetList.as_view()), 
    path('snippets/<int:pk>/',views.SnippetDetail.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)