from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from TS import views

router = DefaultRouter()
router.root_view_name = 'API List View'
router.register(r'upload', views.TDGeneralViewSet, base_name='tdgeneral')
router.register(r'login', views.TDGeneralViewSet, base_name='tdgeneral2')
router.register(r'register', views.TDInfoViewSet, base_name='tdinfo')

router.register(r'user', views.CountryGeoViewSet, base_name='country')
router.register(r'trace', views.CountryGeoViewSet, base_name='country')
router.register(r'poi', views.RegionGeoViewSet, base_name='region')
router.register(r'staypoint', views.AttackViewSet, base_name='attack')

router.register(r'identify0', views.WeaponViewSet, base_name='weapon')
router.register(r'identify1', views.TargetViewSet, base_name='target')
router.register(r'identify2', views.KeywordViewSet, base_name='wordcloud')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'schema', views.schema_view)
]

# urlpatterns = format_suffix_patterns(urlpatterns)
