from .models import Book, VocabularyCatalogue

from rest_framework import serializers, viewsets


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Book
        fields = "__all__"


class BookViewSet(viewsets.ModelViewSet):
    queryset         = Book.objects.all()
    serializer_class = BookSerializer


class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = VocabularyCatalogue
        fields = "__all__"


class CatalogueViewSet(viewsets.ModelViewSet):
    queryset         = VocabularyCatalogue.objects.all()
    serializer_class = CatalogueSerializer
