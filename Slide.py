class Slide:
    def __init__(self, picture_one, picture_two=None):
        self.id = picture_one.id
        self.pictures = [picture_one, picture_two]
        if picture_two is not None:
            self.id += " {}".format(picture_two.id)
        self.tags = {}
        for tag in picture_one.tags:
            self.tags[tag] = True
        for tag in picture_two.tags:
            self.tags[tag] = True

