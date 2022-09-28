from django.views import generic


# 
#   Concurrency
# 
class PythonConcurrencyView(generic.TemplateView):
    template_name: str = "programming/python/concurrent_execution/concurrency.html"

class PythonConcurrencyThreadingView(generic.TemplateView):
    template_name: str = "programming/python/concurrent_execution/threading.html"

class PythonView(generic.TemplateView):
    template_name: str = "programming/python.html"

# 
#  Networking and Interprocess Communication
# 
class PythonNetworkingInterprocessCommunicationView(generic.TemplateView):
    template_name: str = "programming/python/networking_interprocess_communication/signal.html"