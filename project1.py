class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.rows])

    def __add__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices have different dimensions")

        rows = [[sum(x) for x in zip(self.row_i, other.row_i)] for row_i, other_row in zip(self.rows, other.rows)]
        return Matrix(rows)

    def __sub__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices have different dimensions")

        rows = [[self.row_i[j] - other.row_i[j] for j in range(len(self.row_i))] for row_i, other_row in zip(self.rows, other.rows)]
        return Matrix(rows)

    def __mul__(self, other):
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Invalid dimensions for matrix multiplication")

        rows = [[sum(row_i[k] * other_row[k] for k in range(len(self.rows[0]))) for other_row in other.rows] for row_i in self.rows]
        return Matrix(rows)

    def transpose(self):
        return Matrix([[self.rows[j][i] for j in range(len(self.rows))] for i in range(len(self.rows[0]))])

    def determinant(self):
        if len(self) == 2 and len(self[0]) == 2:
            a, b = self[0]



