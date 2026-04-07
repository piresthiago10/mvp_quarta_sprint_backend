from flask_openapi3 import APIBlueprint
from flask import redirect

docs_bp = APIBlueprint("docs", __name__)


@docs_bp.get("/", methods=["GET"])
def home():
    """Redireciona para o index.html do frontend."""
    return redirect("/front/index.html")


@docs_bp.get("/docs", methods=["GET"])
def docs():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")
