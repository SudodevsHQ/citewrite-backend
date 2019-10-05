import wikipedia


class Wiki():
    def __init__(self, query):
        self.query = query
        self.result = {}

    def search(self):
        """
        {
            "1": {
                "title": "Amoeba",
                "summary" : "some short summary that will be something 3-4 sentences long"
                "image":"first image",
                "url" : "url"
            }
        }
        """
        try:
            searched = wikipedia.search(self.query)
            k = 0
            for i in searched[:3]:
                w = wikipedia.page(i)
                data = {
                    str(k): {
                        "title": w.title,
                        "summary": w.summary,
                        "image": w.images[0],
                        "url": w.url
                    }
                }
                self.result.update(data)
                k += 1
            k = 0
            return True
        except Exception as e:
            print(e)
            return False
