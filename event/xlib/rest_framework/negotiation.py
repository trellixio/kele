from rest_framework.negotiation import DefaultContentNegotiation


class EventDefaultContentNegotiation(DefaultContentNegotiation):
    def get_accept_list(self, request):
        header = request.META.get('HTTP_ACCEPT', 'application/json')
        return [token.strip() for token in header.split(',')]
