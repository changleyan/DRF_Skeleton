class ApiDBRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    base = 'default'
    db_logs = 'base_logs'

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """

        if model._meta.model_name == 'log':
            return self.db_logs
        elif model._meta.app_label == 'api' or model._meta.app_label == 'auth' \
                or model._meta.app_label == 'contenttypes' or model._meta.app_label == 'admin' \
                or model._meta.app_label == 'sessions' or model._meta.app_label == 'oauth2_provider':
            return self.base
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.model_name == 'log':
            return self.db_logs
        elif model._meta.app_label == 'api' or model._meta.app_label == 'auth' \
                or model._meta.app_label == 'contenttypes' or model._meta.app_label == 'admin' \
                or model._meta.app_label == 'sessions' or model._meta.app_label == 'oauth2_provider':
            return self.base
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'auth' or obj2._meta.app_label == 'auth' \
                or obj1._meta.app_label == 'api' or obj2._meta.app_label == 'api' \
                or obj1._meta.app_label == 'oauth2' or obj2._meta.app_label == 'oauth2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if model_name == 'log':
            return db == self.db_logs
        elif app_label == 'api' or app_label == 'auth' \
                or app_label == 'contenttypes' or app_label == 'admin' \
                or app_label == 'sessions' or app_label == 'oauth2_provider':
            return db == self.base
        return None
