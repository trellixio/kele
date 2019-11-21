from rest_framework.routers import SimpleRouter, Route


class EventRouter(SimpleRouter):
    custom_routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={'get': 'current'},
            name='{basename}-current',
            detail=False,
            initkwargs={'suffix': 'Current'}
        ),
        Route(
            url=r'^{prefix}/update{trailing_slash}$',
            mapping={'put': 'current_update'},
            name='{basename}-update',
            detail=False,
            initkwargs={}
        ),
    ]

    def __init__(self):
        self.routes += self.custom_routes
        super().__init__(trailing_slash=True)
