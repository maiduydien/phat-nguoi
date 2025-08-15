from flask import Flask
from flask_cors import CORS
from app.api.endpointstest import router, routerOpenAI 


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Cho phép React gọi API

# Đăng ký các blueprint
app.register_blueprint(router)
app.register_blueprint(routerOpenAI, url_prefix="/openai")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
