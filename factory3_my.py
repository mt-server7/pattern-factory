import abc

class Abstract_machine(abc.ABC):
    button: str
    def __init__(self, button: str) -> None:
        self.button = button

    @abc.abstractmethod
    def process(self) -> None:
        pass



class Start(Abstract_machine):
    def process(self) -> None:
        print('Process begin')
    

class Stop(Abstract_machine):
    def process(self) -> None:
        print('Process stopped')

class Pause(Abstract_machine):
    def process(self) -> None:
        print('Pause')


class Factory:
    @classmethod
    def create(cls, operation: str, button: str) -> Abstract_machine:
        operations = {
            '1': Start,
            '2': Stop,
            '3': Pause,
        }

        try:
            return operations[operation](button)
        except KeyError:
            raise ValueError(f'Unknown operation: {button}')

    

if __name__ == '__main__':
    while True:
        button = input('Enter operation: ')
        match button:
            case '1':
                operation = Factory.create('1', 'Start')
                operation.process()
            case '2':
                operation = Factory.create('2', 'Stop')
                operation.process()
                break
            case '3':
                operation = Factory.create('3', 'Pause')
                operation.process()
            case _:
                print('Error input!')
            