class SlideShow:
    def __init__(self):
        self.slides = []

    def get_num_slides(self):
        return len(self.slides)

    def get_slide_ids(self):
        slide_ids = []
        for slide in self.slides:
            slide_ids.append(slide.id)
        return slide_ids

    def get_score(self, slide_one, slide_two):
        slide_one.get_overlap_details(slide_two)
        print("TODO: IMmplement get score")