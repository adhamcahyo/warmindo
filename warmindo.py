from warmindo.core.routing import Router
from warmindo.core.middleware import Middleware
from warmindo.modules.custom_auth import authenticate_user
from warmindo.modules.custom_helpers import calculate_square, generate_random_string
from warmindo.database.models import User, Base, create_engine

app = Router()
middleware = Middleware()

def custom_logging_middleware(request):
    print("Logging request:", request.method, request.url)

middleware.add_middleware(custom_logging_middleware)

@app.route("/login", methods=["POST"])
def login(request):
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if authenticate_user(username, password):
        return {"message": "Login successful!"}
    else:
        return {"message": "Login failed. Invalid credentials."}, 401

@app.route("/square/<int:num>")
def square(request, num):
    result = calculate_square(num)
    return {"result": result}

@app.route("/create_user", methods=["POST"])
def create_user(request):
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password_hash = data.get("password_hash")
    
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)
    
    user = User(username=username, email=email, password_hash=password_hash)
    session = engine.connect()
    session.add(user)
    session.commit()
    session.close()
    
    return {"message": "User created successfully"}

app.add_middleware(middleware)

if __name__ == "__main__":
    app.runserve()
