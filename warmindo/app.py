from warmindo import Warmindo
from warmindo.core.middleware import Middleware
from warmindo.core.routing import Router
from warmindo.database_config import DATABASE_URI
from warmindo.models import db


app = Warmindo()
router = Router()
app.router = router

def home(request):
    pass

def show_post(request, post_id):
    pass

router.add_route('/', home)
router.add_route('/post/<int:post_id>', show_post)

app.add_middleware(Middleware)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db.init_app(app)

if __name__ == '__main__':
    app.run()
