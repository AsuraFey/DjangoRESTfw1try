from rest_framework import routers
from .api import Project_View_Set


router = routers.DefaultRouter()

router.register('api/projects', Project_View_Set, 'projects')

urlpatterns = router.urls
