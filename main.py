import os
from file_reader import read_file
from file_writer import write_output
from problem_solver import ProblemSolver

# Input

files = ['a_example.txt', 'b_loveley_landscapes.txt', 'c_memorable_moments.txt', 'd_pet_pictures.txt', 'e_shiny_selfies.txt']
header_rows = ['rows', 'cols', 'minIngredients', 'maxCellsPerSlice']
col_headers = ['row']

# End Input

example_file = os.path.join('data', files[0])
example = read_file(example_file, header_rows, col_headers)
exampleSlicer = ProblemSolver(example['header'], example['rows'], os.path.join('output', 'example.txt'))
exampleSlicer.output_solution()

small_file = os.path.join('data', files[1])
small = read_file(small_file, header_rows, col_headers)
smallSlicer = ProblemSolver(small['header'], small['rows'], os.path.join('output', 'small.txt'))
smallSlicer.output_solution()

medium_file = os.path.join('data', files[2])
medium = read_file(medium_file, header_rows, col_headers)
mediumSlicer = ProblemSolver(medium['header'], medium['rows'], os.path.join('output', 'medium.txt'))
mediumSlicer.output_solution()

big_file = os.path.join('data', files[3])
big = read_file(big_file, header_rows, col_headers)
bigSlicer = ProblemSolver(big['header'], big['rows'], os.path.join('output', 'big.txt'))
bigSlicer.output_solution()

biggest_file = os.path.join('data', files[3])
biggest = read_file(biggest_file, header_rows, col_headers)
biggestSlicer = ProblemSolver(biggest['header'], biggest['rows'], os.path.join('output', 'big.txt'))
biggestSlicer.output_solution()
