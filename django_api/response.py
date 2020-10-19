from django.http import JsonResponse


class Response:

    def base(self, values=None, message="", status=200):
        if values is None:
            values = []

        return JsonResponse({
            'status': status,
            'message': message,
            'values': values
        }, status=status)

    @staticmethod
    def ok(values=None, message=""):
        return Response().base(values=values, message=message, status=200)

    @staticmethod
    def badRequest(values=None, message=""):
        return Response().base(values=values, message=message, status=400)