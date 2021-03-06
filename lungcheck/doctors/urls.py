from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='doctors/home/doctor.html'), name="doctor_home"),
	url(r'^register/$', views.doctor_register, name="doctor_register"),
	url(r'^login/$', views.doctor_login, name="doctor_login"),
	url(r'^apiregister/$', views.api_register, name="doctor_register_api"),
	url(r'^apilogin/$', views.api_login, name="doctor_login_api"),

	url(r'^patients$', TemplateView.as_view(template_name='doctors/home/patient.html'), name="patient_home"),
	url(r'^patients/register/$', views.patient_register, name="patient_register"),
	url(r'^patients/login/$', views.patient_login, name="patient_login"),
	url(r'^patients/apiregister/$', views.patient_api_register, name="patient_register_api"),
	url(r'^patients/apilogin/$', views.patient_api_login, name="patient_login_api"),

	url(r'^intranet/$', views.doctor_intranet, name="doctor_intranet"),
	url(r'^patients/intranet/$', views.patient_intranet, name="patient_intranet"),

	url(r'^forgot_password/$', views.forgot_password, name="forgot_password"),
	url(r'^new_password/$', views.forgot_password, name="new_password"),
	url(r'^confirm_mail/$', views.confirm_mail, name="confirm_mail"),
]

