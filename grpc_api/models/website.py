from grpc_api.protos import news_getter_pb2

website_url = {
    news_getter_pb2.Site.AutoDetect: "",
    news_getter_pb2.Site.LentaRu: "lenta.ru/news",
    news_getter_pb2.Site.IzRu: "iz.ru",
    news_getter_pb2.Site.Ria: "ria.ru",
    news_getter_pb2.Site.Interfax: "interfax.ru",
    news_getter_pb2.Site.Tass: "tass.ru",
    news_getter_pb2.Site.BBC: "bbc.com",
    news_getter_pb2.Site.CNN: "edition.cnn.com",
}

website_url_regex = {
    news_getter_pb2.Site.LentaRu: "lenta\.ru\/(articles|news)",
    news_getter_pb2.Site.IzRu: "iz\.ru\/\d+",
    news_getter_pb2.Site.Ria: "ria\.ru\/\d+",
    news_getter_pb2.Site.Interfax: "interfax\.ru\/[a-z]*\/\d*",
    news_getter_pb2.Site.Tass: "tass\.ru\/[a-z]*\/\d*",
    news_getter_pb2.Site.BBC: "bbc\.com\/(?!russian)",
    news_getter_pb2.Site.CNN: "edition\.cnn\.com\/\d*\/\d*\/\d*\/.*\/index\.html",
}
