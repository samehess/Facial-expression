from abc import ABC, abstractmethod

class FacialExpressionHandlerInterface(ABC):

    @abstractmethod
    def onAngry(self):
        pass

    @abstractmethod
    def onDisgust(self):
        pass

    @abstractmethod
    def onFear(self):
        pass

    @abstractmethod
    def onHappy(self):
        pass

    @abstractmethod
    def onSad(self):
        pass

    @abstractmethod
    def onSurprise(self):
        pass

    @abstractmethod
    def onNeutral(self):
        pass
