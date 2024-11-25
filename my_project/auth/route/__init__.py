"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each of your specific entities

    from my_project.auth.route.adress_machine_route import address_machine_bp
    from my_project.auth.route.currency_denomination_route import currency_denominations_bp
    from my_project.auth.route.employees_address_route import employess_address_bp
    from my_project.auth.route.employees_route import employees_bp
    from my_project.auth.route.food_machine_route import food_machine_bp
    from my_project.auth.route.loading_machine_route import loading_machine_bp
    from my_project.auth.route.loading_snacks_route import loading_snacks_bp
    from my_project.auth.route.machine_manifecture_route import machine_manifecture_bp
    from my_project.auth.route.menu_route import menu_bp
    from my_project.auth.route.money_loading_route import money_loading_bp
    from my_project.auth.route.money_transfer_route import money_transfer_bp
    from my_project.auth.route.saled_snacks_route import saled_snacks_bp
    from my_project.auth.route.service_route import service_bp
    from my_project.auth.route.snacks_creator_route import snacks_creator_bp
    from my_project.auth.route.snacks_route import snacks_bp

    # Register each blueprint with the app
    app.register_blueprint(address_machine_bp)
    app.register_blueprint(currency_denominations_bp)
    app.register_blueprint(employess_address_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(food_machine_bp)
    app.register_blueprint(loading_machine_bp)
    app.register_blueprint(loading_snacks_bp)
    app.register_blueprint(machine_manifecture_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(money_loading_bp)
    app.register_blueprint(money_transfer_bp)
    app.register_blueprint(saled_snacks_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(snacks_creator_bp)
    app.register_blueprint(snacks_bp)

