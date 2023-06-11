import sys

class ActionTable():
    actions = {}

    @staticmethod
    def Create(action, reference):
        if action in ActionTable.actions:
            sys.stderr.write("Error: action " + action + " has already been declared.")
            raise Exception
        else:
            ActionTable.actions[action] = reference

    @staticmethod
    def Get(action):
        if action not in ActionTable.actions:
            sys.stderr.write("Error: action " + action + " has not been declared.")
            raise Exception
        return ActionTable.actions[action]