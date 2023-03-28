import multiprocessing

bind = "127.0.0.1:8010"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 2
reload = True 
# print_config = True 
accesslog = "-"

wsgi_app = "backend.wsgi:application"