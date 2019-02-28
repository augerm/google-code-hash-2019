class Slide:
    def __init__(self, picture_one, picture_two=None):
        self.id = picture_one.id
        if picture_two is not None:
            self.id += " {}".format(picture_two.id)