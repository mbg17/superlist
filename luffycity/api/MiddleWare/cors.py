class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class CorsMiddleware(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin']='*'
        if request.method=='OPTIONS':
            response['Access-Control-Allow-Headers']='Content-Type'
        return response