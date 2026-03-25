from flask import Blueprint, request, jsonify, redirect

docs_bp = Blueprint("docs", __name__)


@docs_bp.route("/", methods=["GET"])
def home():
    """Redireciona para o index.html do frontend."""
    return redirect("/front/index.html")


@docs_bp.route("/docs", methods=["GET"])
def docs():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")
