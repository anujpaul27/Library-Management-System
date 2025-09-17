from django.urls import path,include
from .views import *
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('Books',BookModelView)
router.register('Authors',AuthorModelView)
router.register('Members',MemberAPIView)
router.register('Brrows',BrrowRecordAPIView)


urlpatterns = [
    path('',include(router.urls)), 
    path('GET/Books/details/<int:id>', SpecificBookAPIView.as_view(), name ='get_book'),
    # path('GET/Authors', AuthorAPIView.as_view(), name ='get_atuthor')
    
]
  