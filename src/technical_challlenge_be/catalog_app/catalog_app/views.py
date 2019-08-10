from .models import Book              , VocabularyCatalogue, Word
from rest_framework import serializers, viewsets           , status
from rest_framework.response import Response


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Book
        fields = "__all__"

    @staticmethod
    def save_worlds(data, context):
        request         = context['request']
        max_word_length = request.query_params.get('max_length')

        def max_word_length_filter(w, max_length):
            if isinstance(max_length, str):
                try:
                    max_length = int(max_length)
                except Exception as ext:
                    # todo handle exception
                    print(ext)
                    return True

            if not max_length:
                return True
            return len(w) >= max_length

        if 'content' in data:
            content = data['content']
            words   = content.split()
            for word in words:
                if max_word_length_filter(word, max_word_length):
                    Word.objects.create(value=word, vocabulary=data['vocabulary'])

    def create(self, validated_data):
        self.save_worlds(validated_data, context=self.context)
        return Book(**validated_data)


class BookViewSet(viewsets.ModelViewSet):
    queryset         = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        data             = request.data
        write_serializer = BookSerializer(data=data, context={'request': request})
        write_serializer.is_valid(raise_exception=True)
        instance = self.perform_create(write_serializer)

        read_serializer = BookSerializer(instance)

        return Response(read_serializer.data)


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
