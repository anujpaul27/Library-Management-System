from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Book
from .serializer import *

# Book
class BookAPIView (APIView):
    def get (self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response (serializer.data)
    
    def post (self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else :
            return Response(serializer.errors)
            
class SpecificBookAPIView (APIView):
    def get (self, request, id):
        book = get_object_or_404(Book,pk=id)
        serializer = BookSerializer(book)
        return Response (serializer.data)
    
    def put (self, request, id):
        book = get_object_or_404(Book,pk=id)
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response (serializer.errors)
    
    def delete (self, request, id):
        book = get_object_or_404(Book,pk=id)
        book.delete()
        return Response("Complate Delete")
        
class BookModelView (ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer     
        
               
#Autho
class AuthorAPIView(APIView):
    def get (self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)
    
    def post (self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class AuthorModelView (ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
        

# Member
class MemberAPIView (ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
    
# BrrowRecord 
class BrrowRecordAPIView (ModelViewSet):
    queryset = BrrowRecord.objects.all()
    serializer_class = BrrowRecordSerializer