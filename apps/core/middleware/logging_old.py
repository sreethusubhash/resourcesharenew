from django.conf import settings
from apps.core.logging import Logging
from django.utils import timezone

logging=Logging(str(settings.BASE_DIR/'logs'/'req_res_logs.txt'))
def simple_logging_middleware(get_response):

    def middleware(request):
        
        #TODO:pre-processing->http request
        http_method=request.method
        url=request.get_full_path()
        host_port=request.get_host()
        content_type=request.headers['Content-Type']
        user_agent=request.headers['User-Agent']
        
        # print("Pre-processing happening here")
        # breakpoint()
        msg=f'{http_method} | {host_port}{url} | {content_type} | {user_agent}'
        logging.info(msg)
        
        response = get_response(request)#nxt middleware or the view
        
        #breakpoint()
        #TODO:post-processing->HTTPResponse
        #TODO:Investigate the response and decide on what to do log
        #TODO:Formulate ur msg
        #TODO:Log using the info level method
        
        return response
    return middleware
class viewExecutionTimeMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        #pre-processing
        #start timer
        start_time=timezone.now()
        
        response = self.get_response(request)
        
        #post-processing
        #stop timer
        http_method=request.method
        url=request.get_full_path()
        host_port=request.get_host()
        total_time=timezone.now()-start_time
        msg=f" Execution TIME{total_time}>>{http_method}|{host_port}{url}"
        logging.info(msg)
        return response
class viewExecutionTime2Middleware:
    
    def process_request(self, request):
        '''Called during pre-processing'''
        request.start_time=timezone.now()
        
    def process_response(self, request,response):
        #Called during post-processing
        
        start_time=timezone.now()-request.start_time
       
        http_method=request.method
        url=request.get_full_path()
        host_port=request.get_host()
        total_time=timezone.now()-start_time
        msg=f" Execution TIME{total_time}>>{http_method}|{host_port}{url}"
        logging.info(msg)
        return response
