from random import randint


class InterpreterProxy(object):

    def call(self, value, _type):
        print 'making request'


class AnInterpreterProxy(InterpreterProxy):

    def __init__(self):
        self.id = randint(12345, 45678)

    def call(self, value, _type):
        print "hello from proxy id: ", self.id


class Proxy(InterpreterProxy):

    def __init__(self, interpreters=None):
        self._interpreters = interpreters or []
        self._last_called = None

    def add_interpreter(self, interpreter):
        self._interpreters.append(interpreter)

    def get_interpreters(self):
        return self._interpreters

    def request(self, value, _type):
        if not self._interpreters:
            raise Exception("No interpreters registered!")

        if self._last_called is None:
            # First call, let's get the first interpreter on the list
            self._last_called = self._interpreters[0]
        else:
            # A new call. Let's get the last called and call the next on the
            # list of interpreters
            last_index = self._interpreters.index(self._last_called)
            new_index = (last_index + 1) % len(self._interpreters)
            self._last_called = self._interpreters[new_index]

            if new_index == 0:
                print 'calling the fist interpreter on the set'

        self._last_called.call(value, _type)


def build_proxy(validator=None):

    p = None
    if validator is not None:
        p = Proxy()
        p.add_interpreter(validator)
    else:
        # Instantiate some interpreter handlers for the proxy:
        int1 = AnInterpreterProxy()
        int2 = AnInterpreterProxy()
        int3 = AnInterpreterProxy()
        int4 = AnInterpreterProxy()

        # Let's create the proxy
        p = Proxy(interpreters=[int1, int2, int3])
        # We can also add them after Proxy creation
        p.add_interpreter(int4)
    return p


if __name__ == "__main__":
    proxy = build_proxy()

    # Let's make some proxy calls
    for _ in range(0, len(proxy.get_interpreters()) * 3):
        proxy.request()
