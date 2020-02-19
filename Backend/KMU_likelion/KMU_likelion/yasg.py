from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from accounts.urls import router as accounts_router
from Admission.urls import router as addmission_router
from Board.urls import router as board_router
from Main.urls import router as main_router

router = routers.DefaultRouter()
router.registry.extend(accounts_router.registry)
router.registry.extend(addmission_router.registry)
router.registry.extend(board_router.registry)
router.registry.extend(main_router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="KMU-LIKELION API",
        default_version='v1',
        description="국민대 멋사만의 홈페이지를 만드는 KMU-LIKELION 프로젝트",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gjdigj@naver.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=router.urls,
)
