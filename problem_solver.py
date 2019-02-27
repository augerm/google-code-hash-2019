from file_writer import write_output

class ProblemSolver:

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
        # TODO: Generate solution array and output to file
        output = ['test', 'testing2', 'testing3']
        write_output(self.output_file, output)