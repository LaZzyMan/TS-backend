from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class RearEndServicesConfig(AppConfig):
    name = 'TS'
    verbose_name = 'Trajectory Data Manager'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

    menu = (
        ParentItem('App', children=[
            ChildItem('Trajectory Data', url='TS'),
        ], icon='fa fa-leaf'),
        ParentItem('User Group', children=[
            ChildItem('User', model='auth.user'),
            ChildItem('Group', model='auth.group'),
        ], icon='fa fa-users'),
        ParentItem('Account Management', children=[
            ChildItem('Password change', url='admin:password_change'),
            ChildItem('Log Out', url='admin:logout'),
        ], align_right=True, icon='fa fa-cog'),
    )

