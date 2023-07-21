from warmindo import Warmindo
from .database_config import DATABASE_URI
from .models import Post

app = Warmindo()

@app.route('/')
def home():
    # Ambil semua postingan dari basis data dan tampilkan di halaman
    posts = Post.query.all()
    posts_html = ""
    for post in posts:
        posts_html += f"<h2>{post.title}</h2><p>{post.content}</p>"

    return f"<h1>Selamat datang di Blog Kami!</h1>{posts_html}"

if __name__ == '__main__':
    app.run()