class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{user}'s email address has been updated to {email}".format(user=self.name,
                                                                          email=self.email))

    def read_book(self, book, rating=None):
        if is_valid_rating(rating):
            self.books[book] = rating
        else:
            self.books[book] = None  # set rating to None so book is retained by user
            print("Rating {} is not valid. Must be a number from 0 to 4.".format(rating))

    def get_average_rating(self):
        # average rating given by user
        # since not all books are rated, need to count not None ratings only
        sum_of_ratings = 0
        number_of_ratings = 0
        for rating in self.books.values():
            if rating is not None:
                sum_of_ratings += rating
                number_of_ratings += 1

        # user can have books but no ratings, so make sure there's at least 1 rating
        if number_of_ratings > 0:
            average_rating = sum_of_ratings / number_of_ratings
        else:
            average_rating = -1 # so that we can still compare to other ratings

        return average_rating

    #
    # OVERRIDE BUILT IN METHODS
    #
    def __repr__(self):
        return "User: {user}, email: {email}, books read: {read}".format(user=self.name,
                                                                         email=self.email,
                                                                         read=len(self.books))

    def __eq__(self, other_user):
        # TODO: make sure other_user is of type User
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("ISBN for {} has been updated to {}".format(self.title, self.isbn))

    def add_rating(self, rating):
        # make sure rating is valid (could print/error but doing that for user)
        if is_valid_rating(rating):
            self.ratings.append(rating)

    def get_average_rating(self):
        if len(self.ratings) > 0:
            return sum(self.ratings) / len(self.ratings)
        else:
            return -1 # so we can compare with other ratings

    #
    # OVERRIDE BUILT IN METHODS
    #
    def __eq__(self, other):
        # TODO: make sure other is of type or subtype of Book
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{} by unknown".format(self.title)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_book = Fiction(title, author, isbn)
        return new_book

    def create_non_fiction(self, title, subject, level, isbn):
        new_book = NonFiction(title, subject, level, isbn)
        return new_book

    def add_book_to_user(self, book, email, rating=None):
        # get user by email
        current_user = self.users.get(email, None)

        if current_user is None:
            print("No user with email {}!".format(email))
            return

        current_user.read_book(book, rating)
        if rating is not None:
            book.add_rating(rating)

        if book in self.books:
            self.books[book] = self.books[book] + 1
        else:
            self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        # Make sure the email is unique (has not already been added)
        if email in self.users:
            print("User with email address '{}' already exists.".format(email))
            return

        user = User(name, email)
        self.users[email] = user

        # requirements say user_books defaults to None, but we need a list to iterate
        # over, so why not default to empty list? Could also check for list type here...
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.items():
            print(user)

    def most_read_book(self):
        most_read = None
        for book in self.books:
            if most_read is None or self.books[book] > self.books[most_read]:
                most_read = book

        return most_read

    def highest_rated_book(self):
        highest_rated = None
        for book in self.books:
            if highest_rated is None or book.get_average_rating() > highest_rated.get_average_rating():
                highest_rated = book

        return highest_rated

    def most_positive_user(self):
        most_positive = None
        for user in self.users.values():
            if most_positive is None or user.get_average_rating() > most_positive.get_average_rating():
                most_positive = user

        return most_positive

    def get_most_read_book(self):
        most_read = None
        for book in self.books:
            if most_read is None or self.books[book] > self.books[most_read]:
                most_read = book

        return most_read

# static method to check rating for users and books
def is_valid_rating(rating):
    # Rating can be None, or an integer from 0 to 4 inclusive
    if rating is None:
        return True
    else:
        if type(rating) == int and (0 <= rating <= 4):
            return True

    # Did not meet required conditions
    return False
