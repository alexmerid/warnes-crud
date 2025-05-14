from .luminaria import init_luminaria_routes
from .referencia import init_referencia_routes
from .censista import init_censista_routes


def register_all_cruds(app, mysql):
    init_luminaria_routes(app, mysql)
    init_referencia_routes(app, mysql)
    init_censista_routes(app, mysql)
