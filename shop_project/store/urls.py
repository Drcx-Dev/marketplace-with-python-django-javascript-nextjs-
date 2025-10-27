from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryListView, ProductListView
from .views import RegisterView
from .views import UserListView
from .views import profile_view
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings    
from .views import ProfileEditView
from .views import RegisterView
from .views import UserListView
from .views import CustomTokenObtainPairView
from .views import AdminUserActions
from .views import CartViewSet






router = DefaultRouter()
router.register(r'categories', CategoryListView, basename='category')
router.register(r'products', ProductListView, basename='product')
router.register(r'users', UserViewSet,basename='user')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('admin-actions/<str:action_type>/<int:user_id>/', AdminUserActions.as_view(), name='admin_user_actions'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   