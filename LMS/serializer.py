from rest_framework import serializers
from LMS.models import Book, Author, Member, BrrowRecord

class AuthorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Author 
        fields = ['id','name','biography'] 
    
        
class BookSerializer (serializers.ModelSerializer):
    # This fiedls are creating for all fields show in the book view 
    # author = AuthorSerializer()
    author_name = serializers.SerializerMethodField(method_name='get_author_name')
    class Meta:
        model = Book
        fields = ['id','title','author_name','isbn','category','status']
        
    def get_author_name(self, obj):
        return obj.author.name
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','name', 'email', 'membership_date']
        

class BrrowRecordSerializer (serializers.ModelSerializer):
    class Meta:
        model = BrrowRecord
        fields = ['id','book','member', 'brrow_date', 'return_date']
       
