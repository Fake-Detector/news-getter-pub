class NewsShortInfo:
    def __init__(self, url: str, content: str, title: str = "", image: str = ""):
        self.url = url
        self.content = content
        self.title = title
        self.image = image
