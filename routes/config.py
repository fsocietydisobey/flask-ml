from routes.student_blueprint import example_blueprint

def config_routes(app):
    app.register_blueprint(example_blueprint, url_prefix='/student')
