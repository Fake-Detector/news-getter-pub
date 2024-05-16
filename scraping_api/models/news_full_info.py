from grpc_api.protos import news_getter_pb2


class NewsFullInfo:
    def __init__(self, url: str, title: str, content: str, source_type: news_getter_pb2.Site, images=None, videos=None):
        self.url = url
        self.title = title
        self.content = content
        self.images = [] if images is None else images
        self.videos = [] if videos is None else videos
        self.source_type = source_type

