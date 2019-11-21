from rest_framework.routers import SimpleRouter, Route


class EventRouter(SimpleRouter):
    custom_routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'current'},
            name='{basename}',
            detail=False,
            initkwargs={'suffix': 'Current'}
        )
    ]

    def __init__(self):
        self.routes += self.custom_routes
        super().__init__(trailing_slash=True)
