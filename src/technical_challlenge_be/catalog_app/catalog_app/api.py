from rest_framework import routers
from .views import BookViewSet
from .views import CatalogueViewSet
from .views import WordViewSet


router = routers.DefaultRouter()
router.register(r'Books'    , BookViewSet)
router.register(r'Catalogue', CatalogueViewSet)
router.register(r'Word'     , WordViewSet)
urls = router.urls
