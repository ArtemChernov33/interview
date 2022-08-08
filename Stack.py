OPEN_BRACKET_ROUND = '('
OPEN_BRACKET_SQUARE = '['
OPEN_BRACKET_CURLY = '{'
CLOSE_BRACKET_ROUND = ')'
CLOSE_BRACKET_SQUARE = ']'
CLOSE_BRACKET_CURLY = '}'

# def is_brackets_balanced(items):
#     brackets = []
#     for item in items:
#         for bracket in item:
#             if bracket == OPEN_BRACKET_ROUND:
#                 brackets.append(bracket)
#             elif bracket == CLOSE_BRACKET_ROUND:
#                 if OPEN_BRACKET_ROUND not in brackets:
#                     return False
#                 brackets.remove(OPEN_BRACKET_ROUND)
#
#             elif bracket == OPEN_BRACKET_SQUARE:
#                 brackets.append(bracket)
#             elif bracket == CLOSE_BRACKET_SQUARE:
#                 if OPEN_BRACKET_SQUARE not in brackets:
#                     return False
#                 brackets.remove(OPEN_BRACKET_SQUARE)
#
#             elif bracket == OPEN_BRACKET_CURLY:
#                 brackets.append(bracket)
#             elif bracket == CLOSE_BRACKET_CURLY:
#                 if OPEN_BRACKET_CURLY not in brackets:
#                     return False
#                 brackets.remove(OPEN_BRACKET_CURLY)
#     return not brackets
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.size()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def is_brackets_balanced(items):
    brackets_round = Stack()
    brackets_square = Stack()
    brackets_curly = Stack()

    for item in items:
        for bracket in item:
            if bracket == OPEN_BRACKET_ROUND:
                brackets_round.push(bracket)
            elif bracket == CLOSE_BRACKET_ROUND:
                if brackets_round.is_empty():
                    return False
                brackets_round.pop()

            elif bracket == OPEN_BRACKET_SQUARE:
                brackets_square.push(bracket)
            elif bracket == CLOSE_BRACKET_SQUARE:
                if brackets_square.is_empty():
                    return False
                brackets_square.pop()

            elif bracket == OPEN_BRACKET_CURLY:
                brackets_curly.push(bracket)
            elif bracket == CLOSE_BRACKET_CURLY:
                if brackets_curly.is_empty():
                    return False
                brackets_curly.pop()

    return (brackets_round.is_empty()
            and brackets_curly.is_empty()
            and brackets_square.is_empty())

def main():
    BALLANCED_LIST = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}'
        ]

    UNBALLANCED_LIST = [
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]

    print(is_brackets_balanced(BALLANCED_LIST))
    print(is_brackets_balanced(UNBALLANCED_LIST))

if __name__ == '__main__':
    main()