########################################################
#
# CMPSC 132: Homework 5
#
#
# For each function, minimal test cases are provided.
# - You may test individual functions separately
#   or test all functions at once.
# - Read the comments at the end of this file
#   to learn how to do it
#
########################################################


student_name = "Krish Chavan"
student_email = "ksc5629@psu.edu"
student_section = "003"



# DO NOT modify this class
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.data) 

    __repr__ = __str__
                          




    
#=============================================== Part I ==============================================

class Stack:
    """
    >>> x = Stack()
    >>> x.isEmpty()
    True
    >>> len(x)
    0
    >>> x.peek()
    >>> x.pop()
    >>> x
    Top: None
    Stack: 
    >>> x.push(2)
    >>> x.isEmpty()
    False
    >>> len(x)
    1
    >>> x.peek()
    2
    >>> x.pop()
    2
    >>> x
    Top: None
    Stack: 
    >>> x.push(2)
    >>> x.push(4)
    >>> x.push(6)
    >>> x.isEmpty()
    False
    >>> len(x)
    3
    >>> x
    Top: Node(6)
    Stack: 6 <= 4 <= 2
    >>> x.peek()
    6
    >>> x.pop()
    6
    """

    # DO NOT modify this method
    def __init__(self):
        self.top = None
    
    # DO NOT modify this method
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.data))
            temp=temp.next
        out=' <= '.join(out)
        return ('Top: {}\nStack: {}'.format(self.top,out))

    # DO NOT modify this method
    __repr__=__str__


    

    def isEmpty(self):
        return self.top == None



    
    def __len__(self): 
        temp = self.top
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
    


    def push(self, data):
        if (data == None): return
        node = Node(data)
        node.next = self.top
        self.top = node
        
            
     
    def pop(self):
        if (self.isEmpty()): return None
        remove = self.top
        self.top = self.top.next
        return remove.data


        
    def peek(self):
        if self.isEmpty(): return None
        return self.top.data
        


    

#=============================================== Part II==============================================


class Calculator:

    # DO NOT modify this member
    precedence = { '+':1, '-':1, '*':2, '/':2, '^':3 }
    
    # DO NOT modify this method
    def __init__(self):
        self.__expr = None

        
    # DO NOT modify this method
    @property
    def expr(self):
        return self.__expr


    # DO NOT modify this method
    @expr.setter
    def expr(self, new_expr):
        if isinstance(new_expr, str) and self._validate(new_expr):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

        


        
    def _isNumber(self, token):
        """
        >>> x=Calculator()
        >>> x._isNumber('5')
        True
        >>> x._isNumber('+5')
        True
        >>> x._isNumber('-5')
        True
        >>> x._isNumber('5.')
        True
        >>> x._isNumber('-5.')
        True
        >>> x._isNumber('+5.')
        True
        >>> x._isNumber('0.5')
        True
        >>> x._isNumber('-0.5')
        True
        >>> x._isNumber('.5')
        True
        >>> x._isNumber('-.5')
        True
        >>> x._isNumber(' 4.560 ')
        True
        >>> x._isNumber('4 56')
        False
        >>> x._isNumber('4.56a')
        False
        >>> x._isNumber('-4.56a')
        False
        >>> x._isNumber('4.5a6')
        False
        """
        
        try:
            float(token)
            return True
        except ValueError:
            return False



        
    def _validate(self, expr):
        """
        >>> x=Calculator(); x._validate('2 ^ 4')
        True
        >>> x=Calculator(); x._validate('2')
        True
        >>> x=Calculator(); x._validate('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
        True
        >>> x=Calculator(); x._validate('2 * 5.34 + 3 ^ 2 + 1 + 4')
        True
        >>> x=Calculator(); x._validate('2.1 * 5 + 3 ^ 2 + 1 + 4')
        True
        >>> x=Calculator(); x._validate('( 2.5 )')
        True
        >>> x=Calculator(); x._validate ('( ( 2 ) )')
        True
        >>> x=Calculator(); x._validate ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
        True
        >>> x=Calculator(); x._validate ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
        True
        >>> x=Calculator(); x._validate ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
        True
        >>> x=Calculator(); x._validate('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
        True
        >>> x = Calculator(); x._validate('2 * 5 + 3 ^ + -2 + 1 + 4')
        False
        >>> x = Calculator(); x._validate('2 * 5 + 3 ^ - 2 + 1 + 4')
        False
        >>> x = Calculator(); x._validate('2    5')
        False
        >>> x = Calculator(); x._validate('25 +')
        False
        """
        
        # expr = expr.strip()
        # for char in range(len(expr)):
        #     if (Calculator._isNumber(char) == False):




    # self.__expr must be a valid expression
    # validity of self.__expr is checked when calling the property method @expr.setter
    # - see @expr.setter for detail
    def _getPostfix(self):
        """
        Required: _getPostfix must create and use a Stack for expression processing
        >>> x=Calculator()
        >>> x.expr = '2 ^ 4'; x._getPostfix()
        '2.0 4.0 ^'
        >>> x.expr = '2'; x._getPostfix()
        '2.0'
        >>> x.expr = '2.1 * 5 + 3 ^ 2 + 1 + 4.45'; x._getPostfix()
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
        >>> x.expr ='2 * 5.34 + 3 ^ 2 + 1 + 4'; x._getPostfix()
        '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x.expr = '2.1 * 5 + 3 ^ 2 + 1 + 4'; x._getPostfix()
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x.expr = '( 2.5 )'; x._getPostfix()
        '2.5'
        >>> x.expr = '( ( 2 ) )'; x._getPostfix()
        '2.0'
        >>> x.expr = '2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )'; x._getPostfix()
        '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x.expr = '( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )'; x._getPostfix()
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x.expr = '( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )'; x._getPostfix()
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        """

        ## YOUR CODE STARTS HERE
        ratorStack = Stack()  # must use ratorStack to get a postfix expression of self.__expr 
        pass

    


    # This property method must
    # 1. converts self.__expr to a postfix expression by calling self._getPostfix
    # 2. use a stack to compute the final result of the postfix expression
    @property
    def value(self):
        '''
        >>> x=Calculator()
        >>> x.expr = '4 + 3 - 2'; x.value
        5.0
        >>> x.expr = '-2 + 3.5'; x.value
        1.5
        >>> x.expr = '4 + 3.65 - 2 / 2'; x.value
        6.65
        >>> x.expr = '23 / 12 - 223 + 5.25 * 4 * 3423'; x.value
        71661.91666666667
        >>> x.expr = ' 2 - 3 * 4'; x.value
        -10.0
        >>> x.expr = '7 ^ 2 ^ 3'; x.value
        5764801.0
        >>> x.expr = ' 3 * ( ( ( 10 - 2 * 3 ) ) )'; x.value
        12.0
        >>> x.expr = '8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3'; x.value
        28.6
        >>> x.expr = '2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4'; x.value
        -2.0
        >>> x.expr = ' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2'; x.value
        1442.7777777777778
        '''

        if not isinstance(self.__expr, str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # must use calcStack to compute the expression

        ## YOUR CODE STARTS HERE
        pass





    
if __name__ == '__main__':
    import doctest
    
    ## Uncomment this line if you want to run doctest by function.
    ## Replace get_words with the name of the function you want to run
    doctest.run_docstring_examples(Calculator._isNumber, globals(), verbose=True, name='hw5')

    ## Uncomment this line if you want to run the docstring
    ## in all functions
    # doctest.testmod()











        



    

