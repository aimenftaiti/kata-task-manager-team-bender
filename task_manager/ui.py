class ConsoleInteractor:
    def read_input(self) -> str:
        return input()
    
    def print_error(self, error) -> None:
        print(error)

class UI:
    def __init__(self, interactor=None):
        if interactor is None:
            self.interactor = ConsoleInteractor()
        else:
            self.interactor = interactor()