class Picture:
    def __init__(self, data):
        self.orientation = data['orientation']
        self.tags_length = data['tags_length']
        self.tags = data['tags']
        self.id = data['id']
