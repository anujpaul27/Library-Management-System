##Project Description
-The Library Management System (LMS) API is a web-based service designed to manage a library's book and author data. Built using Django and Django REST Framework, it provides a set of endpoints for performing standard CRUD (Create, Retrieve, Update, Delete) operations on these resources.

#Key features
-Book Management: This allows for the creation, viewing, updating, and deletion of book records. Each book entry includes details such as its title, author, ISBN, category, and availability status.
-Author Management: This provides functionality to manage author information, including their name and a short biography. The system correctly links authors to their respective books.
-Data Relationships: The API correctly handles the one-to-many relationship between authors and books. This is achieved through nested serializers, which display an author's complete details (including their name) directly within a book's JSON representation, rather than just their primary key.
-Clear Endpoints: The API uses a router to automatically generate clean and intuitive URL patterns for all operations. For example, a GET request to .../books/ retrieves a list of all books, while a GET to .../books/1/ retrieves the details of a single book with an ID of 1.
