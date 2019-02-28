class SlideShow:
    def __init__(self):
        self.slides = []

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