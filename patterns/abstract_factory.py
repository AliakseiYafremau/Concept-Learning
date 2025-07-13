from abc import ABC, abstractmethod


# Абстрактные инструменты
class Button(ABC):
    @abstractmethod
    def toggle(cls): 
        ...

class Screen(ABC):
    @abstractmethod
    def render(cls):
        ...

# Абстрактная фабрика инструментов
class UtilsFactory(ABC):
    @abstractmethod
    def create_button(cls) -> Button:
        ...

    @abstractmethod
    def create_screen(cls) -> Screen:
        ...

# Конкретные реализации абстрактных инструментов: светлые и зеленые
class LightButton(Button):
    def toggle(self):
        print("Toggle the light button")

class LightScreen(Screen):
    def render(self):
        print("Render some light")

class GreenButton(Button):
    def toggle(self):
        print("Toggle the green button")

class GreenScreen(Screen):
    def render(self):
        print("Render some light")

# Конкретные фабрики
class LightUtilsFactory(UtilsFactory):
    def create_button(self) -> Button:
        return LightButton()
    
    def create_screen(self) -> Screen:
        return LightScreen()

class GreenUtilsFactory(UtilsFactory): 
    def create_button(self) -> Button:
        return GreenButton()
    
    def create_screen(self) -> Screen:
        return GreenScreen()


def run(factory: UtilsFactory) -> None:
    # Мы не знаем ни о семействе, ни о конткретных обьектах
    button = factory.create_button()
    screen = factory.create_screen()

    button.toggle()
    screen.render()

if __name__ == "__main__":
    light_utils = LightUtilsFactory()
    green_utils = GreenUtilsFactory()

    print("LightUtilsFactory:")
    run(light_utils)

    print("---")

    print("GreenUtilsFactory:")
    run(green_utils)

