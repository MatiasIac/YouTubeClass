from interpreter import build_validator
from proxy import build_proxy


# Get out Interpreter/Factory pieces
validator = build_validator(with_observer=True)

# Get our Proxy and set it up with a couple of (identical, yes) validators
proxy = build_proxy()
proxy.add_interpreter(validator)
proxy.add_interpreter(validator)

# Run some (notified :) ) validations to see how things go:
data = [
    ('this one is too long', 'text'),  # False
    ('good one', 'text'),  # True

    ('objeto no nulo', 'constraint'),  # True
    (None, 'constraint'),  # False

    (22, 'number'),  # True
    (22.0, 'number'),  # False

    ('Crear reglas:', 'header'),  # True
    ('Crear reglas', 'header')  # False
]

# Let's make some proxy calls
for _ in range(0, len(proxy.get_interpreters()) * 3):
    for value, _type in data:
        proxy.request(value, _type)
