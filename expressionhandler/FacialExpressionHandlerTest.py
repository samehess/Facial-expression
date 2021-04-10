from abc import ABC, abstractmethod

from expressionhandler.FacialExpressionHandler import FacialExpressionHandlerInterface


class FacialExpressionHandlerTest(FacialExpressionHandlerInterface):

    def onAngry(self):
        # Actions.moveRight()
        # Keys.onClick(Right)
        print("move right")

    def onDisgust(self):
        print("move left")

    def onFear(self):
        pass

    def onHappy(self):
        pass

    def onSad(self):
        pass

    def onSurprise(self):
        pass

    def onNeutral(self):
        pass
