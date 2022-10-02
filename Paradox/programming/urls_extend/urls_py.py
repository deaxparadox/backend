from django.urls import path 

from ..views_extend import views_py
urlpatterns = [
    path("py/", views_py.PythonView.as_view(), name="programming_py"),

    # Basics
    path("py/basics/type_var/", views_py.PythonBasicsTypesVarComm.as_view(), name="programming_py_type_var_comm"),
    path("py/basics/list_tuple/", views_py.PythonBasicsListTuple.as_view(), name="programming_py_list_tuple"),

    # Concurrent execution
    path("py/concurrent/", views_py.PythonConcurrencyView.as_view(), name="programming_py_concurrent_execution"),
    path("py/concurrent/threading/", views_py.PythonConcurrencyThreadingView.as_view(), name="programming_py_concurrent_execution_threading"),

    # NetworkingAndInterprocessCommunication
    path("py/net_inter_com/signal/", views_py.PythonNetworkingInterprocessCommunicationView.as_view(), name="programming_py_net_inter_com_signal"),
]
