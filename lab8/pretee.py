"""
CSCI-603 PreTee Lab
Author: RIT CS
Author: Vineet Singh     , vs9779@rit.edu
Author: Anirudh Narayanan, an9425@g.rit.edu

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import sys              # argv
import literal_node     # literal_node.LiteralNode
import variable_node    # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node       # print_node.PrintNode
import math_node        # math_node.MathNode
import syntax_error     # syntax_error.SyntaxError
import runtime_error    # runtime_error.RuntimeError

class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN


    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile=srcFile
        self.parseTrees = []
        self.symTbl = {}
        self.syntaxError = False
        self.lineNum = 0
        pass

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """
        try:
            if len(tokens) == 0 or tokens == None:
                raise syntax_error.SyntaxError("Incomplete statement :" + str(self.lineNum))

            # Check if first character is a math operator
            if tokens[0] in self.MATH_TOKENS:

                # Check if second character is a math operator
                if tokens[1] not in self.MATH_TOKENS:
                    left = self.__parse(tokens[1:])
                    right = self.__parse(tokens[2:])

                else:
                    left = self.__parse(tokens[1:])

                    # function to find the right most end of a math node
                    def expressionEndFind(node):
                        if isinstance(node, variable_node.VariableNode) or isinstance(node,
                                                                                      literal_node.LiteralNode) or node.right == None:
                            return node
                        else:
                            return expressionEndFind(node.right)

                    RightEnd = expressionEndFind(left)
                    if isinstance(RightEnd, variable_node.VariableNode):
                        pos = tokens.index(RightEnd.id)
                    else:
                        pos = tokens.index(str(RightEnd.val))

                    right = self.__parse(tokens[pos + 1:])

                return math_node.MathNode(left, right, tokens[0])

            # Check if first character is a digit
            elif tokens[0].isdigit():
                return literal_node.LiteralNode(int(tokens[0]))

            # Check if first character is an identifier
            elif tokens[0].isidentifier():
                return variable_node.VariableNode(tokens[0], self.symTbl)

            # Raise error if invalid token found
            else:
                raise syntax_error.SyntaxError("Invalid token "+ tokens[0] +" in Line: " + str(self.lineNum))
                return tokens[0]

        except  syntax_error.SyntaxError as e:
            self.syntaxError = True
            print("*** Syntax Error:", e)
            pass

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """

        # Open the source file
        with open(self.srcFile) as f:

            # Iterate on the line in the file
            for line in f:
                try:
                    self.lineNum += 1

                    # Nothing to parse if newline found
                    if line == "\n":
                        continue

                    # Convert line string to list
                    lineList = line.strip().split()

                    # Don't parse if line is commented
                    if len(lineList) == 0 or lineList[0] == self.COMMENT_TOKEN or lineList == "\n":
                        continue

                    # Assignment token found
                    if (lineList[0] == self.ASSIGNMENT_TOKEN):

                        # Raise error if nothing found to assign
                        if len(lineList) == 1:
                            raise syntax_error.SyntaxError("Incomplete statement :" + str(self.lineNum))

                        # Raise error if not identifier found to assign into
                        if not lineList[1].isidentifier():
                            raise syntax_error.SyntaxError("Bad assignment in:" + str(self.lineNum))


                        else:
                            parsedNode = self.__parse(lineList[2:])

                            # Raise error if pasring doesnt result in valid node
                            if not isinstance(parsedNode, literal_node.LiteralNode) and \
                                    not isinstance(parsedNode, variable_node.VariableNode) and \
                                    not isinstance(parsedNode, math_node.MathNode):
                                raise syntax_error.SyntaxError("Bad assignment in :" + str(self.lineNum))

                            else:
                                self.symTbl[lineList[1]] = parsedNode.evaluate()
                                var = variable_node.VariableNode(lineList[1], self.symTbl)
                                assign = assignment_node.AssignmentNode(var, parsedNode, self.symTbl, '=')
                                assign.evaluate()
                                self.parseTrees.append(assign)

                    # Print task found
                    elif lineList[0] == '@':
                        if len(lineList) == 1:
                            pNode=print_node.PrintNode()
                            self.parseTrees.append(pNode)
                            continue
                        else:
                            pNode = self.__parse(lineList[1:])
                            self.parseTrees.append(pNode)

                    # Invalid token found
                    else:
                        raise syntax_error.SyntaxError(
                            "Invalid token " + lineList[0] + " in Line: " + str(self.lineNum))
                except syntax_error.SyntaxError as e:
                    self.syntaxError = True
                    print("*** Syntax Error:", e)
                    pass

        f.close()


    def emit(self):
        """
        Prints an infix string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """

        # Iterate and print parse trees
        for node in self.parseTrees:
            if node==None:
                print("")
            elif isinstance(node, assignment_node.AssignmentNode):
                print(node.emit())
            else:
                print("print",end=" ")
                print(node.emit())
        pass

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """

        # Iterate and evalute all parse trees
        for node in self.parseTrees:
            if node==None:
                print("")
            if not(isinstance(node, assignment_node.AssignmentNode)) and node!=None:
                print(node.evaluate())
        pass

def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)

if __name__ == '__main__':
    main()
