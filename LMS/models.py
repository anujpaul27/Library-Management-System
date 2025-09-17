from django.db import models

class Author (models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    
    def __str__(self):
        return self.name

class Book (models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved'),
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.IntegerField(unique=True)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
class Member (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_created=True)
    
    def __str__(self):
        return self.name
    
class BrrowRecord (models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='borrow_record')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrow_record')
    brrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, auto_now_add=True)
    
    def __str__(self):
        return f'{self.memeber.name} borrowed {self.book.title}'
