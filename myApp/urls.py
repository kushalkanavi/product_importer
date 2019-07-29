from django.conf.urls import url
from myApp.views import index, main, productSearch, addProduct, editProduct, deleteSingleProduct, deleteAllProduct, stream
from myApp.tasks import uploadFile
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'myApp/login_user.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'myApp/logged_out.html'}, name='logout'),

    url(r'^main/$', main.as_view(), name='main'),
    url(r'^upload_file/$', uploadFile, name='upload_file'),
    url(r'^product_search/$', productSearch, name='product_search'),

    url(r'^add_product/$', addProduct.as_view(), name='add_product'),
    url(r'^delete_all_product/$', deleteAllProduct.as_view(), name='delete_all_product'),
    url(r'^delete_single_product/(?P<id>\d+)/$', deleteSingleProduct.as_view(), name='delete_single_product'),
    url(r'^edit_product/(?P<id>\d+)/$', editProduct.as_view(), name='edit_product'),

    url(r'^stream/$', stream, name='stream'),

    url(r'^$', index.as_view(), name='index'),
]