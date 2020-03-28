# coding=utf-8
import codecs
import re

from observer import Observer, Notifier


class Context(object):
    def __init__(self, expression):
        self.expression = expression


class ExpressionBase(object):

    validators = []

    def __init__(self, context):
        self.context = context

    def validate(self, value):

        checks = []
        for validator in self.validators:
            checks.append(validator(value))

        return all(checks)

    def constructor(self):
        pass

    def interpret(self):
        pass


class HeaderExpression(ExpressionBase):
    validators = []
    header_str = 'Crear reglas:'

    def interpret(self):
        if not self.context:
            raise Exception('Incorrect syntax for NumberExpression')

        if self.context.expression == self.header_str:
            self.validators.append(lambda x: x == self.header_str)
            print '[header - interpret] correct header expression'
        else:
            print '[header - interpret] WRONG header expression'


class NumberExpression(ExpressionBase):
    validators = []
    number_str = 'es entero'

    def interpret(self):
        if not self.context.expression:
            raise Exception('Incorrect syntax for NumberExpression')

        for rule in self.context.expression:
            if rule == self.number_str:
                self.validators.append(lambda x: isinstance(x, int))
                print '[number - interpret] correct number expression'
            else:
                raise Exception('Invalid rule: %s', rule)


class StringExpression(ExpressionBase):
    validators = []
    non_empty_str = u'tipo no vacío'
    length_left = 'no mayor a '
    length_right = ' caracteres'

    @staticmethod
    def _extract_length(length_str):
        match = re.search(r'\d{2}', length_str)
        if match is not None:
            return int(match.group())

    def interpret(self):
        if not self.context.expression:
            raise Exception('Incorrect syntax for StringExpression')

        for rule in self.context.expression:

            if rule == self.non_empty_str:
                self.validators.append(lambda x: bool(x))
                print '[string - interpret] non-empty string expression'

            elif self.length_left in rule and self.length_right in rule:
                num = self._extract_length(rule)
                self.validators.append(lambda x: len(x) <= num)
                print (
                    '[string - interpret] max-length %s string '
                    'expression' % num
                )

            else:
                raise Exception('Invalid rule: %s', rule)


class ConstraintExpression(ExpressionBase):
    validators = []
    constraint_str = 'objeto no nulo'

    def interpret(self):
        if not self.context:
            raise Exception('Incorrect syntax for ConstraintExpression')

        if self.context.expression == self.constraint_str:
            self.validators.append(lambda x: bool(x))
            print '[constraint - interpret] correct constraint expression'
        else:
            print '[constraint - interpret] WRONG constraint expression'


class Validator(object):

    # Markers
    header_str = 'Crear reglas:'
    const_str = 'objeto no nulo'

    # Map
    handler_map = {
        'header': HeaderExpression,
        'text': StringExpression,
        'number': NumberExpression,
        'constraint': ConstraintExpression
    }

    def __init__(self, filename, notifier=None):
        self.filename = filename
        self.notifier = notifier
        self.handlers = {}
        self.tree = []
        self.data = None

    def parse_file(self):

        # Let's read the file and start working on it
        content = codecs.open(self.filename, encoding='utf-8').read()
        content = content.split('\n    si')

        # After splitting, we expect a list of 3 elements
        if len(content) != 3:
            raise Exception(
                'Invalid file format. Parse should get 3 sections and '
                'it got %s', len(content)
                )

        # Let's start putting the data together, easy stuff first
        fst = content[0]
        data = {
            'header': self.header_str if self.header_str in fst else None,
            'constraint': self.const_str if self.const_str in fst else None
        }

        for group in content[1:]:
            group = group.strip().split('\n')

            key = None
            if 'texto' in group[0]:
                key = 'text'
            elif u'número' in group[0]:
                key = 'number'
            else:
                raise Exception('Invalid group content: %s', group[0])

            data[key] = [elem.strip() for elem in group[1:]]

        self.data = data

    def build_tree(self):

        # Let's put the tree together
        for element in self.data:
            # Pick the class from the map
            handlerClass = self.handler_map.get(element)

            # Build a context
            ctx = Context(self.data.get(element))

            # Call the handler class
            handler = handlerClass(ctx)

            # Save the handler instance internally
            self.handlers[element] = handler

            # Run the interpreter for the given class
            handler.interpret()

            # And add it to the tree
            self.tree.append(handler)

    def validate(self, value, kind):
        if self.notifier is not None:
            self.notifier.notify(
                'factory validator', kind, 'validating %s' % kind
            )

        handler = self.handlers.get(kind)
        return handler.validate(value)

    call = validate


###############################################################################

def build_validator(with_observer=False):

    ntf = None
    if with_observer:
        # Our observers
        obs_number = Observer(name='obs_number')
        obs_header = Observer(name='obs_header')
        obs_string = Observer(name='obs_string')
        obs_constr = Observer(name='obs_constr')

        # Howdy to our notifier!
        ntf = Notifier()

        # Let's make some channels for each group in our synctax and work
        # the plumbing for notifications
        ntf.add_subscriber('header', obs_header)
        ntf.add_subscriber('constraint', obs_constr)
        ntf.add_subscriber('number', obs_number)
        ntf.add_subscriber('text', obs_string)

    # Now let's put together our steaming factory
    validator = Validator(filename='rules.txt', notifier=ntf)

    # Let's put a context together
    validator.parse_file()

    # We parsed the file already, let's now do some actual syntax parsing
    validator.build_tree()

    return validator

if __name__ == "__main__":

    validator = build_validator()

    # Run some (notified :) ) validations to see how things go:
    print validator.validate('this one is too long', 'text')  # False
    print validator.validate('good one', 'text')  # True

    print validator.validate('objeto no nulo', 'constraint')  # True
    print validator.validate(None, 'constraint')  # False

    print validator.validate(22, 'number')  # True
    print validator.validate(22.0, 'number')  # False

    print validator.validate('Crear reglas:', 'header')  # True
    print validator.validate('Crear reglas', 'header')  # False


