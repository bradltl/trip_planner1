from langchain.tools import tool

class CalculatorTools():

    @tool("Make a calculation")
    def calculate(operation):
        """Use this tool to make a calculation.
        Examples: 200*7 ot 5000/2*10
        """

        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical operation."