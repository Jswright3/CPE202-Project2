"""Contains code for Infix to Postfix
and Postfix evaluation
CPE202
Project 2

Author:
    John Wright
"""
from stacks import StackLinked

def infix_to_postfix(infix_expr):
   """Takes str infix expression and turns it into a postfix expression using a stack
   Args:
      infix_expr (str): infix expression
   Returns:
      (str) postfix expression
   """
   infix_expr = infix_expr.replace(' ', '')
   precedent = {'-': 1, '+': 1, '/': 2, '*': 2, '^': 3, '~': 1}
   postfix_expr = []
   op_stack = StackLinked()
   for i in infix_expr:
      if i.isdigit():
         postfix_expr.append(i)
      elif i == '(':
         op_stack.push(i)
      elif i == ')':
         while op_stack.top is not None and op_stack.peek() != '(':
            postfix_expr.append(op_stack.pop())
         if op_stack.peek() == '(':
            op_stack.pop()
      else:
         while op_stack.top is not None and lower_precedence(op_stack, i, precedent):
            postfix_expr.append(op_stack.pop())
         op_stack.push(i)
   while op_stack.top is not None:
      postfix_expr.append(op_stack.pop())
   postfix_expr = ''.join([str(i)+' ' for i in postfix_expr])
   postfix_expr = postfix_expr.strip()
   if infix_to_postfix_notvalid(postfix_expr):
   #   raise SyntaxError('Outputted Postfix Expression Invalid')
   #return postfix_expr

def lower_precedence(op_stack, i, precedent):
   """Checks if the precedent of the i is less than the precedent of the top of the stack
   Args:
      op_stack (StackLinked): operator stack
      i (any): current element in infix_expr
      precedent (dict): precedents of expressions
   Returns:
      (bool) if precedent i is less than precedent of the top of the stack
   """
   try:
      if precedent[i] <= precedent[op_stack.peek()]:
         return True
      return False
   except KeyError:
      return False

def postfix_eval(postfix_expr):
   """Solves a given postfix expression
   Args:
      postfix_expr (str): postfix expression
   Returns:
      (int) solution to postfix expression
   """
   if postfix_valid(postfix_expr) is False:
      raise SyntaxError
   postfix_expr = postfix_expr.replace(' ','')
   solve_stack = StackLinked()
   for i in postfix_expr:
      if i == '~':
         a = solve_stack.pop()
         a *= -1
         solve_stack.push(a)
      elif i.isdigit():
         solve_stack.push(i)
      else:
         a = solve_stack.pop()
         b = solve_stack.pop()
         if i == '^':
            solve_stack.push(int(b)**int(a))
         elif i == '/' and a == 0:
            raise ZeroDivisionError
         else:
            solve_stack.push(eval(str(b) + i + str(a)))
   return solve_stack.pop()

def postfix_valid(postfix_expr):
   """Checks if a given postfix expression is valid
   Args:
      postfix_expr(str): postfix expression
   Returns:
      (bool)
   """
   op_count = 0
   int_count = 0
   parentheses_stack = StackLinked()
   postfix_expr = postfix_expr.replace(' ', '')
   for i in postfix_expr:
      if i =='~':
         pass
      elif i == '(':
         parentheses_stack.push(i)
      elif i == ')':
         parentheses_stack.pop(i)
      elif i.isdigit():
         int_count += 1
      else:
         op_count += 1
   first = postfix_expr[0]
   second = postfix_expr[1]
   length = len(postfix_expr)
   last = postfix_expr[length - 1]

   if first.isdigit() and second.isdigit() and not last.isdigit() and parentheses_stack.top is None:
      if int_count - 1 == op_count:
         return True
   return False

def infix_to_postfix_notvalid(postfix_expr):
   """checks if the postfix form infix_to_postfix returns is not valid
   Args:
      postfix_expr (str): postfix expression
   Returns:
      (bool): If postfix_expr is not valid
   """
   if postfix_valid(postfix_expr):
      return False
   return True
