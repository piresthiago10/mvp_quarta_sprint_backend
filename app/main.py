from api import create_app
from config import ProductionConfig
from flask_cors import CORS

app = create_app(ProductionConfig)
CORS(app)
if __name__ == "__main__":
    app.run(debug=True)
