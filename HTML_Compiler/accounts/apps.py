from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'accounts'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
    	import users.signals