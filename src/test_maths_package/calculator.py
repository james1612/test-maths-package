class Calculator:
    def add(self, x: float, y: float) -> float:
        """
        Add two numbers together.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: The sum of x and y
        """
        return x + y
    
    def subtract(self, x: float, y: float) -> float:
        """
        Subtract y from x.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: The difference between x and y
        """
        return x - y
    
    def multiply(self, x: float, y: float) -> float:
        """
        Multiply two numbers together.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: The product of x and y
        """
        return x * y
    
    def divide(self, x: float, y: float) -> float:
        """
        Divide x by y.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: The quotient of x divided by y
            
        Raises:
            ZeroDivisionError: If y is zero
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
