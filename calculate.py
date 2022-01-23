import app


class Calculator:
    # set total variable to allow separate operations to be performed in series
    total = float
    # record requested operations
    requested_operations = list

    def _multiply(self):
        pass

    def _add(self):
        pass

    def _subtract(self):
        pass

    def _divide(self):
        pass

    # apply precision set by user
    def _round_to_precision(self):
        pass

    def _to_arch(self):
        pass

    # split equation by operation and assign order of operations
    def split_by_operation(self, equation: list):
        pass

    def __init__(self):
        self.precision = app.precision
