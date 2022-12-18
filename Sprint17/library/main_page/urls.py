from django.urls import path, include
from .views import *
from authentication.views import CustomUserView
from author.views import AuthorView
from book.views import BookView
from order.views import OrderView, UsersOrderView
from rest_framework.authtoken.views import obtain_auth_token

ACTIONS = {
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
}


# router = routers.DefaultRouter()
# router.register('user', CustomUserView)
# router.register('book', BookView)
# router.register('author', AuthorView)
# router.register('order', OrderView)
# router.register('user/<int:id>/order/<int:pk>', UsersOrderView, basename='user/<int:id>/order/<int:pk>')

urlpatterns = [
    path('', home_page, name='home'),
    path('user/', include('authentication.urls')),
    # path('api/v1/', include(router.urls)),
    path('api/v1/user/<int:pk>', CustomUserView.as_view(ACTIONS)),
    path('api/v1/book/<int:pk>', BookView.as_view(ACTIONS)),
    path('api/v1/author/<int:pk>', AuthorView.as_view(ACTIONS)),
    path('api/v1/order/<int:pk>', OrderView.as_view(ACTIONS)),
    path('api/v1/user/<int:id>/order/<int:pk>', UsersOrderView.as_view(ACTIONS)),
]