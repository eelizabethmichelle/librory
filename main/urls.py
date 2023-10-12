from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_item, delete_item
from main.views import get_item_json, create_ajax
from main.views import increment_amount, decrement_amount, increment_rented, decrement_rented

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('inc-amount/<int:id>/', increment_amount, name='inc_amount'),
    path('dec-amount/<int:id>/', decrement_amount, name='dec_amount'),
    path('inc-rented/<int:id>/', increment_rented, name='inc_rented'),
    path('dec-rented/<int:id>/', decrement_rented, name='dec_rented'),
]