import time
import logging

logger = logging.getLogger('__main__')  # Use the logger defined in settings

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        request.ip_address = self.get_client_ip(request)

        response = self.get_response(request)

        execution_time = time.time() - request.start_time
        log_message = f"IP: {request.ip_address}, Path: {request.path}, Time Taken: {execution_time:.4f}s"

        logger.info(log_message)  # Write log to file

        return response

    def get_client_ip(self, request):
        """Get the real client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
