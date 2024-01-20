from django.urls import include,path
from bakery import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('Admin/',views.admin,name='admin'),
    path('login/',views.login,name='login'),
    path('product/',views.product,name='product'),
    path('add/',views.addpro,name='add'),
    path('delete/<int:id>',views.deletepro,name='delete'),
    path('update/<int:id>',views.updatepro,name='update'),
    path('view customer/',views.userview,name='customer'),
    path('udelete/<int:id>',views.udelete,name='delete'),
    path('uupdate/<int:id>',views.uupdate),
    path('order/',views.vieworder),
    path('payment/',views.viewpayment),
    path('uHome/',views.uHome,name='uHome'),
    path('cart/<int:id>/<pr>',views.checkOut,name='cart'),
    path('logout/',views.Logout),
    path('pay/<int:id>/<pr>/<Product_name>',views.payment),
    path('confirm/<int:id>',views.confirm),
    path('myorders/',views.myorder),
    path('reject/<int:id>',views.reject),
    path('tHistory/',views.transaction),
    path('about/',views.about),
    path('contact/',views.contact)

]
