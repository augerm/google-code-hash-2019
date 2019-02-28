import copy
from Slide import Slide

class SlideShow:
    def __init__(self, pictures):
        self.pictures = pictures
        self.slides = self.create_slides()

    def create_slides(self):
        pictures_copy = copy.deepcopy(self.pictures)
        slides = []

        my_sorted_verticles = self.sortVerticalsByDifficulty()


        for picture in pictures_copy:
            if picture.orientation == "H":
                slides.append(Slide(picture))

        while len(my_sorted_verticles) != 0:
            best_match_index = self.get_best_vertical_match(my_sorted_verticles[0][0], my_sorted_verticles)
            if best_match_index is not None:
                slides.append(Slide(my_sorted_verticles[0][0], my_sorted_verticles[best_match_index][0]))
                del my_sorted_verticles[best_match_index]
            del my_sorted_verticles[0]
        return slides

    def get_best_vertical_match(self, picture, pictures_copy):
        smallest_difficulty = 1000000000
        smallest_difficulty_match_index = None

        for i in range(len(pictures_copy)):
            difficulty = self.get_difficulty_score(picture, pictures_copy[i][0])
            if difficulty < smallest_difficulty:
                smallest_difficulty = difficulty
                smallest_difficulty_match_index = i

        return smallest_difficulty_match_index

    def createVerticalList(self):
        pictures_copy = copy.deepcopy(self.pictures)
        verticle_slides = []
        for picture in pictures_copy:
            if picture.orientation == 'V':
                verticle_slides.append(picture)

        return verticle_slides

    def get_most_similar_arr(self, picture):
        for picture_comparison in self.pictures:
            if picture.id == picture_comparison.id:
                continue
            else:
                print("TODO: Implement later")


    def sortVerticalsByDifficulty(self):
        my_verticle_slides = self.createVerticalList()
        vertical_slides_difficulty = []

        for i in range(len(my_verticle_slides)):
            first_slide = my_verticle_slides[i]
            total_difficulty_score = 0
            for j in range(len(my_verticle_slides)):
                second_slide = my_verticle_slides[j]
                if first_slide.id != second_slide.id:
                    difficulty_score = self.get_difficulty_score(first_slide, second_slide)
                    total_difficulty_score += difficulty_score
            difficulty_arr = [first_slide, total_difficulty_score]
            vertical_slides_difficulty.append(difficulty_arr)

        vertical_slides_difficulty.sort(reverse=False, key=self.sortCriteria)
        return vertical_slides_difficulty

    def sortCriteria(self, difficultyArr):
        return difficultyArr[1]

    def get_difficulty_score(self, slide1, slide2):
        difficulty = slide1.get_overlap_details(slide2)
        difficulty_score = (difficulty['different'] - difficulty['same']) * -1
        return difficulty_score

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