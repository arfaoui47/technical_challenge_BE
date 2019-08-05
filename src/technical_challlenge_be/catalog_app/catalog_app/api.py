from rest_framework import routers
from .views import BookViewSet
from .views import CatalogueViewSet


router = routers.DefaultRouter()
router.register(r'Books'    , BookViewSet)
router.register(r'Catalogue', CatalogueViewSet)
urls = router.urls
