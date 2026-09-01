from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("Health", __name__, description="Health check endpoint")


@blp.route("/health")
class HealthCheck(MethodView):
    def get(self):
        return {"status": "ok"}, 200
