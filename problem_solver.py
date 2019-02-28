from SlideShow import SlideShow
from Picture import Picture
from file_writer import write_output

class ProblemSolver:

    def __init__(self, header, rows, output_file):
        self.output_file = output_file
        self.num_photos = header
        self.pictures = []
        for row in rows:
            self.pictures.append(Picture(row))

    def find_best_slide_show(self):
        print("TODO: Implement find best slide show")

    def output_solution(self):
        output = []
        output.append(self.slideShow.get_num_slides())
        output += self.slideShow.get_slide_ids()
        write_output(self.output_file, output)