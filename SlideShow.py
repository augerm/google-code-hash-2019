import copy
from Slide import Slide

class SlideShow:
    def __init__(self, pictures):
        self.pictures = pictures
        self.slides = self.create_slides()

    def create_slides(self):
        pictures_copy = copy.deepcopy(self.pictures)
        slides = []
        for picture in pictures_copy:
            if picture.orientation == "V":
                slides.append(Slide(picture))
            else:
                best_match = self.get_best_vertical_match(picture, pictures_copy)
                slides.append(Slide(picture, best_match))
        return slides

    def get_most_similar_arr(self, picture):
        for picture_comparison in self.pictures:
            if picture.id == picture_comparison.id:
                continue
            else:
                print("TODO: Implement later")

    def get_best_vertical_match(self, picture, pictures_copy):
        return pictures_copy.pop()

    def add_slide(self, slide):
        self.slides.append(slide)

    def get_num_slides(self):
        return len(self.slides)

    def get_slide_ids(self):
        slide_ids = []
        for slide in self.slides:
            slide_ids.append(slide.id)
        return slide_ids

    def get_score(self):
        score = 0
        for i in range(0, len(self.slides) - 1):
            score += self.slides[i].get_score(self.slides[i + 1])
        score += self.slides[len(self.slides) - 1].get_score(self.slides[0])
        return score