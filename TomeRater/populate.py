from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

# Test - average rating for user with books but no rating should be -1
print ("Marvin's average rating before: {}".format(Tome_Rater.users["marvin@mit.edu"].get_average_rating()))

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

# Test - now that Marvin has ratings, show new average
print ("Marvin's average rating now: {}".format(Tome_Rater.users["marvin@mit.edu"].get_average_rating()))

#Uncomment these to test your functions:
print("Catalog:")
Tome_Rater.print_catalog()
print("Users:")
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())

# Negative test cases to show validation at work
Tome_Rater.add_book_to_user(novel1, "nobody@home.com", 3)
Tome_Rater.add_book_to_user(novel2, "david@computation.org", 10)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", -1)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 2.5)
Tome_Rater.add_book_to_user(nonfiction1, "david@computation.org", "A+")
Tome_Rater.add_user("Alan Turing", "alan@turing.com")

# Test unused function to change email
Tome_Rater.users["david@computation.org"].change_email("dmarr@computation.org")
