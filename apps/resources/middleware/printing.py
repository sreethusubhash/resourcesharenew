def printing_middleware(get_response):
    def middleware(request):
        #pre-processing
        print('This is the preprocessing msg')
        response = get_response(request)
        #post-processing
        print('This is the postprocessing msg')
        return response
    return middleware