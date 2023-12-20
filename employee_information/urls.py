from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
##############################  Admin Page ############################################
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('home', views.home, name="home-page"),
    # path('login', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    # path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    # path('about', views.about, name="about-page"),
    path ('register', views.registerpage, name="registerpage"),
    path ('log', views.loginpage, name="loginpage"),

#################################################################################################
  #################################### Vehicle Category   #########################################
    path('save_category', views.save_category, name="save-category-page"),
    path('vehicle_category', views.vehicle_Category, name="Vehicle_Category-page"),
    path('manage_category', views.manage_category, name="manage_category-page"),
    path('delete_category', views.delete_category, name="delete-category"),

#########################################    Expense Category #############################################
    path('save_expcategory', views.save_expcategory, name="save-expcategory-page"),
    path('expense_category', views.expense_Category, name="expense_Category-page"),
    path('manage_expcategory', views.manage_expcategory, name="manage_expcategory-page"),
    path('delete_expcategory', views.delete_expcategory, name="delete-expcategory"),



    #########################################    freight Category #############################################
    path('save_freightcategory', views.save_freightcategory, name="save-freightcategory-page"),
    path('freight_Category', views.freight_Category, name="freight_Category-page"),
    path('manage_freightcategory', views.manage_freightcategory, name="manage_freightcategory-page"),
    path('view_freight_category', views.view_freight_category, name="view-freight_category-page"),
    path('delete_freightcategory', views.delete_freightcategory, name="delete-freightcategory"),
    #  path('save_freight', views.save_freightcategory, name="save-freightcategory-page"),




     #########################################    Commodity Category #############################################
    path('save_commodity', views.save_comcategory, name="save-comcategory-page"),
    path('commodity', views.commodity, name="commodity-page"),
    path('manage_comcategory', views.manage_comcategory, name="manage_comcategory-page"),
    path('view_commodity', views.view_commodity, name="view-com_category-page"),
    path('delete_comcategory', views.delete_comcategory, name="delete-comcategory"),


#####################################################  Customer           #############################################################

 path('save_customer', views.save_customer, name="save-customer-page"),
    path('customer', views.customer, name="customer-page"),
    path('manage_customer', views.manage_customer, name="manage_customer-page"),
    path('view_customer', views.view_customer, name="view-customer-page"),
    path('delete_customer', views.delete_customer, name="delete-customer"),


#######################################################   Booking  #######################################

 path('save_booking', views.save_booking, name="save-booking-page"),
    path('booking', views.booking, name="booking-page"),
    path('manage_booking', views.manage_booking, name="manage_booking-page"),
    path('view_booking', views.view_booking, name="view-booking-page"),
    path('delete_booking', views.delete_booking, name="delete-booking"),






#######################################      Agent ###################################################


path('save_agent', views.save_agent, name="save-agent-page"),
    path('agent', views.agent, name="agent-page"),
    path('manage_agent', views.manage_agent, name="manage_agent-page"),
    path('view_agent', views.view_agent, name="view-agent-page"),
    path('delete_agent', views.delete_agent, name="delete-agent"),

################################################ vendor #####################################
path('save_vendor', views.save_vendor, name="save-vendor-page"),
    path('vendor', views.vendor, name="vendor-page"),
    path('manage_vendor', views.manage_vendor, name="manage_vendor-page"),
    path('view_vendor', views.view_vendor, name="view-vendor-page"),
    path('delete_vendor', views.delete_vendor, name="delete-vendor"),


##################################################

  path('save_curex', views.save_curex, name="save-curex-page"),
    path('curex', views.curex, name="curex-page"),
    path('manage_curex', views.manage_curex, name="manage_curex-page"),
    path('view_curex', views.view_curex, name="view-curex-page"),
    path('delete_curex', views.delete_curex, name="delete-curex"),
    ######################################################
 path('save_set', views.save_set, name="save-set-page"),

    path('set', views.set, name="set-page"),
    path('manage_set', views.manage_set, name="manage_set-page"),
    path('view_set', views.view_set, name="view-set-page"),
    path('delete_set', views.delete_set, name="delete-set"),
###################################################
path('save_consale', views.save_consale, name="save-consale-page"),

    path('consale', views.consale, name="consale-page"),
    path('manage_consale', views.manage_consale, name="manage_consale-page"),
    path('view_consale', views.view_consale, name="view-consale-page"),
    path('delete_consale', views.delete_consale, name="delete-consale"),
###################################################
path('save_conpur', views.save_conpur, name="save-conpur-page"),

    path('conpur', views.conpur, name="conpur-page"),
    path('manage_conpur', views.manage_conpur, name="manage_conpur-page"),
    path('view_conpur', views.view_conpur, name="view-conpur-page"),
    path('delete_conpur', views.delete_conpur, name="delete-conpur"),
###########################################################


path('save_pursol', views.save_pursol, name="save-pursol-page"),

    path('pursol', views.pursol, name="pursol-page"),
    path('manage_pursol', views.manage_pursol, name="manage_pursol-page"),
    path('view_pursol', views.view_pursol, name="view-pursol-page"),
    path('delete_pursol', views.delete_pursol, name="delete-pursol"),


######################################



path('save_rent', views.save_rent, name="save-rent-page"),

    path('rent', views.rent, name="rent-page"),
    path('manage_rent', views.manage_rent, name="manage_rent-page"),
    path('view_rent', views.view_rent, name="view-rent-page"),
    path('delete_rent', views.delete_rent, name="delete-rent"),

#######################################################################
      path('save_bin', views.save_bin, name="save-bin-page"),
    path('bin', views.bin, name="bin-page"),
    path('manage_bin', views.manage_bin, name="manage_bin-page"),
    path('view_bin', views.view_bin, name="view-bin-page"),
    path('delete_bin', views.delete_bin, name="delete-bin"),
    #############################################################

        path('save_spe', views.save_spe, name="save-spe-page"),
    path('spe', views.spe, name="spe-page"),
    path('manage_spe', views.manage_spe, name="manage_spe-page"),
    path('view_spe', views.view_spe, name="view-spe-page"),
    path('delete_spe', views.delete_spe, name="delete-spe"),
    

     path('save_upd', views.save_upd, name="save-upd-page"),
    path('upd', views.upd, name="upd-page"),
    path('manage_upd', views.manage_upd, name="manage_upd-page"),
    path('view_upd', views.view_upd, name="view-upd-page"),
    path('delete_upd', views.delete_upd, name="delete-upd"),

################################ track update
path('get_booking_updates', views.get_booking_updates, name="get_booking_updates"),
# path('search_booking', views.search_booking, name="search_booking"),
path('update', views.update, name="update-page"),
################################ search booking
path('get_booking_invoice', views.get_booking_invoice, name="get_booking_invoice"),

############################## pdf url
path('generate_booking_invoice', views.generate_booking_invoice, name="generate_booking_invoice"),


    ############################### Carrier#####################
    # ################################################
 path('save_carrier', views.save_carcategory, name="save-carcategory-page"),
    path('carrier', views.carrier, name="carrier-page"),
    path('manage_carcategory', views.manage_carcategory, name="manage_carcategory-page"),
    path('view_carrier', views.view_carrier, name="view-car_category-page"),
    path('delete_carcategory', views.delete_carcategory, name="delete-carcategory"),



############################################ Vessel #############################################




path('save_vessel', views.save_vescategory, name="save-vescategory-page"),
    path('vessel', views.vessel, name="vessel-page"),
    path('manage_vescategory', views.manage_vescategory, name="manage_vescategory-page"),
    path('view_vessel', views.view_vessel, name="view-ves_category-page"),
    path('delete_vescategory', views.delete_vescategory, name="delete-vescategory"),


############################### contract Owner###############################




path('save_contract', views.save_concategory, name="save-concategory-page"),
    path('contract', views.contract, name="contract-page"),
    path('manage_concategory', views.manage_concategory, name="manage_concategory-page"),
    path('view_contract', views.view_contract, name="view-con_category-page"),
    path('delete_concategory', views.delete_concategory, name="delete-concategory"),



##############################################    Expense Chart        #############################################

    path('expense_chart/', views.expense_chart, name="expense_chart"),
    path('vehicle_chart/', views.vehicle_chart, name="vehicle_chart"),
      path('bok_chart', views.bok_chart, name="bok_chart"),

   path('con_menu/', views.con_menu, name="con_menu"),
    path('log_cat', views.log_cat, name="log_cat"),
 path('', views.main, name="main"),
    path('emp_cat', views.emp_cat, name="emp_cat"),
##########################################    Vehicle         ################################################################
   path('save_vehicle', views.save_vehicle, name="save-vehicle-page"),
   path('vehicle', views.vehicle, name="Vehicle-page"),
   path('manage_vehicle', views.manage_vehicle, name="manage_vehicle-page"),
   path('delete_vehicle', views.delete_vehicle, name="delete-vehicle"),
   path('view_vehicle', views.view_vehicle, name="view-vehicle-page"),

#########################################    Expense   #############################################

   path('save_expense', views.save_expense, name="save-expense-page"),
   path('expense', views.expense, name="expense-page"),
   path('manage_expense', views.manage_expense, name="manage_expense-page"),
   path('delete_expense', views.delete_expense, name="delete-expense"),
   path('view_expense', views.view_expense, name="view-expense-page"),

   ############################## Departments   #####################################################################
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
##########################################   Positions ########################################################
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
##########################   Employeee #######################################################
    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),

####################################    CSV ####################################################
path('vehicle_csv', views.vehicle_csv, name="vehicle_csv-page"),
path('bok_csv', views.bok_csv, name="bok_csv-page"),

# path('booking_chart', views.booking_chart, name="booking_chart-page"),
################################################ PDF ###################################################
 path('vehicle_pdf',views.vehicle_pdf, name="vehicle_pdf-page"),
path('bok_pdf',views.bok_pdf, name="bok_pdf-page"),
#  path('bok_pdf/<str:order_no>/', views.bok_pdf, name='bok_pdf'),
 ####################################### Passwords Reset ###############################################

path('reset_password/', auth_views.PasswordResetView.as_view(template_name="employee_information/password_reset.html"), name="reset_password"),
path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="employee_information/password_reset_sent.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="employee_information/password_reset_done.html"), name="password_reset_confirm"),
path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="employee_information/password_reset_complete.html"), name="password_reset_complete"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)