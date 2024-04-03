from django.conf import settings
from .import views
from django.urls import path
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
    # path('admin/', admin.site.urls),
    
      path('adminhome/',views.adminhome),
      path('policehome/',views.policehome),
      path('login/',views.login),
      path('',views.eg3),
      path('aboutus/',views.aboutus),
      path('register/',views.register),
      path('userhome/',views.userhome),
      path('reportpolice/',views.reportpolice),
      path('reportuser/',views.reportuser),
      path('surveillance/',views.surveillance),
      path('addpolice/',views.addpolice),
      path('viewpolice/',views.viewpolice),
       path('viewuser/',views.viewuser),
      path('deletepolice/',views.deletepolice),
      path('editpolice/',views.editpolice),
      path('detect/',views.detect),
      path('missing/',views.missing),
      path('missing3/',views.missing3),
      path('deleteperson/',views.deleteperson),
      path('editperson/',views.editperson),
      path('viewcase/',views.viewcase),
      path('investigatingcase/',views.investigatingcase),
      path('transfercase/',views.transfercase),
      path('logout/',views.logout),



      

      # pathe=register/
    # path('about/',views.about),
    # path('contact/',views.contact1),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)