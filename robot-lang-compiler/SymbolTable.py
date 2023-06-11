import sys

class SymbolTable():
    def __init__(self):
        self.variables = {}

    def Create(self, variable, var_type, value):
        if var_type == "Item":
            for item in self.variables.values():
                if "Item" in item:
                    raise Exception("Error: Cannot carry more than one item at a time."	)
            self.variables[variable] = (var_type, value)
        elif variable in self.variables:
            sys.stderr.write("Error: Variable " + variable + " has already been declared.")
            raise Exception
        else:
            self.variables[variable] = (var_type, value)

    def Get(self, variable):
        if variable not in self.variables:
            sys.stderr.write("Error: Variable " + variable + " has not been declared.")
            raise Exception
        return self.variables[variable]

    def Set(self, variable, value):
        if variable in self.variables:
            if value[0] == self.variables[variable][0]:
                self.variables[variable] = value
            else:
                sys.stderr.write("Error: Cannot assign " + value[0] + " to " + self.variables[variable][0] + " variable " + variable)
                raise Exception
        else:
            sys.stderr.write("Error: Variable " + variable + " has not been declared.")
            raise Exception
        
    def Delete(self, variable):
        if variable in self.variables:
            del self.variables[variable]
        else:
            sys.stderr.write("Error: Cannot drop item " + variable + " because it is not being carried.")
            raise Exception
        
    def Check(self, item):
        if item in self.variables:
            return True
        else:
            return False

           