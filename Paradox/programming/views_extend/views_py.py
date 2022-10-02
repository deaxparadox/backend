from django.views import generic

# 
# Python 
# 
class PythonView(generic.TemplateView):
    template_name: str = "programming/python.html"

# 
# Basics
#
class PythonBasicsTypesVarComm(generic.TemplateView):
    template_name: str = "programming/python/basics/data_types_variables/data_types_variables.html"
# 
class PythonBasicsListTuple(generic.TemplateView):
    template_name: str = "programming/python/basics/array_tuple/array_tuple.html"


# 
#   Concurrency
# 
class PythonConcurrencyView(generic.TemplateView):
    template_name: str = "programming/python/concurrent_execution/concurrency/concurrency.html"

class PythonConcurrencyThreadingView(generic.TemplateView):
    template_name: str = "programming/python/concurrent_execution/threading/threading.html"


# 
#  Networking and Interprocess Communication
# 
class PythonNetworkingInterprocessCommunicationView(generic.TemplateView):
    template_name: str = "programming/python/networking_interprocess_communication/signal/signal.html"