import logging

#Get the logging instance
logger=logging.getLogger('logging_mw')#__name__.'logging_mw'-unique d for url mapping
def simple_logging_middleware(get_response):

    def middleware(request):
        
        #TODO:pre-processing->http request
        http_method=request.method
        url=request.get_full_path()
        host_port=request.get_host()
        content_type=request.headers['Content-Type']
        user_agent=request.headers['User-Agent']
        
        msg=f'{http_method} | {host_port}{url} | {content_type} | {user_agent}'
        logger.info(msg)
        
        response = get_response(request)#nxt middleware or the view
        
        #breakpoint()
        #TODO:post-processing->HTTPResponse
        #TODO:Investigate the response and decide on what to do log
        #TODO:Formulate ur msg
        #TODO:Log using the info level method
        
        return response
    return middleware
# logger.info("msg")
# logger.error("msg")
# logger.critical("msg")
# logger.warning("msg")
# logger.debug("msg")
