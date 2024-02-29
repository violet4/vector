class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector([x * scalar for x in self.elements])
        else:
            raise ValueError("Scalar must be an integer or float")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __imul__(self, scalar):
        if isinstance(scalar, (int, float)):
            for i in range(len(self.elements)):
                self.elements[i] *= scalar
            return self
        else:
            raise ValueError("Scalar must be an integer or float")

    def __add__(self, other):
        if isinstance(other, Vector) and len(other.elements) == len(self.elements):
            return Vector([x + y for x, y in zip(self.elements, other.elements)])
        else:
            raise ValueError("Both operands must be Vectors of the same length")

    def __iadd__(self, other):
        if isinstance(other, Vector) and len(other.elements) == len(self.elements):
            for i in range(len(self.elements)):
                self.elements[i] += other.elements[i]
            return self
        else:
            raise ValueError("Both operands must be Vectors of the same length")

    def __sub__(self, other):
        if isinstance(other, Vector) and len(other.elements) == len(self.elements):
            return Vector([x - y for x, y in zip(self.elements, other.elements)])
        else:
            raise ValueError("Both operands must be Vectors of the same length")

    def __isub__(self, other):
        if isinstance(other, Vector) and len(other.elements) == len(self.elements):
            for i in range(len(self.elements)):
                self.elements[i] -= other.elements[i]
            return self
        else:
            raise ValueError("Both operands must be Vectors of the same length")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector([x / scalar for x in self.elements])
        else:
            raise ValueError("Scalar must be an integer or float")

    def __itruediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            for i in range(len(self.elements)):
                self.elements[i] /= scalar
            return self
        else:
            raise ValueError("Scalar must be an integer or float")

    def __repr__(self):
        return str(self.elements)
