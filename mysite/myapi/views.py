# from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Author
from .serializers import AuthorSerializers
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# from rest_framework.generics import GenericAPIView
from .import services


# class AuthorViewSet(ModelViewSet):
#     queryset =Author.objects.all()
#     serializer_class =AuthorSerializers

class AuthorView(APIView):

        def get_object(self, pk):
            try:
                model = Author.objects.get(pk=pk)
            except Exception:
                raise NotFound("Author not found -----------")
            return model

        def get(self, request, *args, **kwargs):
            if kwargs.get("pk"):
                author = services.get_author_one(kwargs.get("pk"))
                serializer = AuthorSerializers(author, many=False)
                return Response(author)
            else:
                authors = Author.objects.all()
                author = services.get_author_one(kwargs.get("pk"))
                serializer = AuthorSerializers(author, many=True)
                return Response(authors)

        def post(self, request):
            serializer = AuthorSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        def put(self, request, *args, **kwargs):
            author = self.get_object(kwargs.get("pk"))
            serializer = AuthorSerializers(data=request.data, instance=author)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        def delete(self, request, *args, **kwargs):
            author = self.get_object(kwargs.get("pk"))
            author.delete()
            return Response({"state": "deleted"})


