from flask import Flask, render_template

app = Flask(__name__)


"""
ლექსიკონიდან ინფორმაციის წამოღება:
info = profiles[0] -> info არის ლექსიკონი
print(info.get("name"), info["name"]) -> get method ან პირდაპირ ['key']-ის დახმარებით
"""

books = [
    {
        "id": 1,
        "title": "Romeo and Juliet",
        "author": "William Shakespeare",
        "rating": 4.7,
        "img": "book1.jpg",

        "description": "Romeo and Juliet is a tragic love story about two young lovers whose families are enemies."
    },

    {
        "id": 2,
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "rating": 4.9,
        "img": "book2.jpg",

        "description": "The Little Prince tells the story of a young prince exploring planets and learning about life."
    },

    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "rating": 4.8,
        "img": "book3.jpg",

        "description": "1984 is a dystopian novel about a society controlled by surveillance and propaganda."
    }
]


@app.route("/")
def home():
    return render_template("about.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def index():
    return render_template("index.html", books=books)





@app.route("/book/<int:book_id>")
def view_book(book_id):

    for book in books:
        if book["id"] == book_id:
            return render_template("book_details.html", book=book)

    return "Book Not Found"


@app.route("/register")
def register():
    return render_template("register.html")





app.run(debug=True)