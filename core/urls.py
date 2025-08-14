from django.urls import path
from .views import GenerateAPIKeyView, EditorOnlyView

urlpatterns = [
    path('generate-key/', GenerateAPIKeyView.as_view(), name='generate-key'),
    path('editor-only/', EditorOnlyView.as_view(), name='editor-only'),
]
