from flask import Blueprint

class Bootstrap(object):

    def __init__(self, prefix):
        self.__prefix = prefix

    def register_blueprints(self, app, blueprints):
        for blueprint in blueprints:
            self.register_blueprint(app, blueprint)

    def register_blueprint(self, app, blueprint):
         app.register_blueprint(blueprint, url_prefix=self.__prefix)
