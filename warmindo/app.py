from warmindo.core.routing import Router
from warmindo.core.middleware import Middleware
from warmindo.modules.custom_auth import authenticate_user
from warmindo.modules.custom_logging import configure_custom_logging
from warmindo.modules.custom_helpers import calculate_square, generate_random_string
from warmindo.database.models import User, Base, create_engine
from warmindo.core.response import Response  # Mengimpor kelas Response dari modul yang sesuai

app = Router()
middleware = Middleware()

def custom_logging_middleware(request):
    configure_custom_logging()
    return None

middleware.add_middleware(custom_logging_middleware)

@app.route("/login", methods=["POST"])
def login(request):
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if authenticate_user(username, password):
        return Response({"message": "Login successful!"})  # Menggunakan kelas Response untuk merespons
    else:
        return Response({"message": "Login failed. Invalid credentials."}, status=401)  # Menggunakan kelas Response dengan status 401

@app.route("/square/<int:num>")
def square(request, num):
    result = calculate_square(num)
    return Response({"result": result})  # Menggunakan kelas Response untuk merespons

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
    
    return Response({"message": "User created successfully"})  

app.add_middleware(middleware)

if __name__ == "__main__":
    app.runserve()
