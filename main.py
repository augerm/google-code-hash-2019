import os
from file_reader import read_file
from file_writer import write_output

class PizzaSlicer:

    def __init__(self, header, rows, output_file):
        self.output_file = output_file
        self.rows = header['rows']
        self.cols = header['cols']
        self.min_ingredients = header['minIngredients']
        self.maxCellsPerClice = header['maxCellsPerSlice']
        self.rows = []
        self.slices = []
        for row in rows:
            self.rows.append(row['row'])

    def get_num_slices(self):
        return len(self.num_slices)

    def get_slices_formatted(self):
        formatted_slices = []
        for slice in self.slices:
            sliceStr = "{} {} {} {}".format(slice.row_start, slice.col_start, slice.row_end, slice.col_end)
            formatted_slices.append(sliceStr)
        return formatted_slices

    def output_solution(self):
        num_slices = self.get_num_slices()
        formatted_slices = self.get_slices_formatted()
        output = num_slices + formatted_slices
        write_output(self.output_file, output)


example_file = os.path.join('data', 'a_example.in')
small_file = os.path.join('data', 'b_small.in')
medium_file = os.path.join('data', 'c_medium.in')
big_file = os.path.join('data', 'd_big.in')

example = read_file(example_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])
small = read_file(small_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])
medium = read_file(medium_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])
big = read_file(big_file, ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice'], ['row'])

exampleSlicer = PizzaSlicer(example['header'], example['rows'], 'example.out')
smallSlicer = PizzaSlicer(small['header'], small['rows'], 'small.out')
mediumSlicer = PizzaSlicer(medium['header'], medium['rows'], 'medium.out')
bigSlicer = PizzaSlicer(big['header'], big['rows'], 'big.out')

