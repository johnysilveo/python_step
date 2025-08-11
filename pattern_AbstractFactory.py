from abc import ABC,abstractmethod



# Abstract Factry interface

class UIfactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factory

class LightThemeFactory(UIfactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()

class DarkThemeFactory(UIfactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()

# Abstract Products

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Concrete Products

class LightButton(Button):
    def click(self):
        print('Light themed clicked')

class LightCheckbox(Checkbox):
    def check(self):
        print('Light check')


class DarkButton(Button):
    def click(self):
        print('Dark themed clicked')


class DarkCheckbox(Button):
    def click(self):
        print('Dark check')

def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.click()
    checkbox.check()

lightFactory = LightThemeFactory()
client_code(lightFactory)