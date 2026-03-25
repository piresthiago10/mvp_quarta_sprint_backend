from flask_openapi3 import OpenAPI, Info, Tag
from database.database import db

info = Info(title="IndividuoGenZ", version="1.0.0")


def create_app(config_class):
    app = OpenAPI(
        __name__, info=info, static_folder="../front", static_url_path="/front"
    )

    app.config.from_object(config_class)

    db.init_app(app)

    from routers.individuos import individuo_bp
    from routers.docs import docs_bp

    app.register_blueprint(docs_bp)
    app.register_blueprint(individuo_bp)

    with app.app_context():
        db.create_all()

    return app
