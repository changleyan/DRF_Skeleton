class ApiDBRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """

    default = 'default'                             # nombre de la base de datos principal en la configuracion DATABASES
    logs_db = 'logs_db'                             # nombre de la base de datos de logs en la configuracion DATABASES
    model_name_registro_action = 'registroaccion'   # nombre del modelo de registro de acciones
    app_name = 'core'                               # nombre de la aplicación instalada

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_name and model._meta.model_name == self.model_name_registro_action:
            return self.logs_db
        return self.default

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_name and model._meta.model_name == self.model_name_registro_action:
            return self.logs_db
        return self.default

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == self.app_name or obj2._meta.app_label == self.app_name:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_name and model_name == self.model_name_registro_action:
            return db == self.logs_db
        return db == self.default
