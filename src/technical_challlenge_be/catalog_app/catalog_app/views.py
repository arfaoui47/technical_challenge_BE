from .models import Book, VocabularyCatalogue, Word

from rest_framework import serializers, viewsets, status


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Book
        fields = "__all__"

    def create(self, validated_data):
        self.save_worlds(validated_data)
        return Book(**validated_data)

    def save_worlds(self, data):
        def filtered(word, filter):
            return False

        if 'content' in data:
            content = data['content']
            words   = content.split()
            for word in words:
                if not filtered(word, filter):
                    Word.objects.create(value=word, vocabulary=data['vocabulary'])


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


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Word
        fields = "__all__"


class WordViewSet(viewsets.ModelViewSet):
    queryset         = Word.objects.all()
    serializer_class = WordSerializer
