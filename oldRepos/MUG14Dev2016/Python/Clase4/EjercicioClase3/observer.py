from random import randint


class Notifier(object):
    def __init__(self):
        self.channels = {}
        self.subscribers = []

    def notify(self, sender, channel, message):
        for listener in self.channels.get(channel):
            listener.listen(sender, message)

    def add_subscriber(self, channel, subscriber):
        if self.channels.get(channel) is not None:
            self.channels.get(channel).append(subscriber)
        else:
            self.channels[channel] = [subscriber, ]

    def remove_subscriber(self, channel, subscriber):
        try:
            self.channels[channel].remove(subscriber)
        except ValueError:
            pass


class Observer(object):
    def __init__(self, name=None):
        self.name = name or randint(23456, 43567)

    def listen(self, sender, message):
        """
        Listener receiving a message.
        """
        print "\t(({} got msg from '{}')) --> {}".format(
            self.name, sender, message
        )


###############################################################################

if __name__ == "__main__":
    # Our observers
    obs1 = Observer(name="obs1")
    obs2 = Observer(name="obs2")
    obs3 = Observer(name="obs3")
    obs4 = Observer(name="obs4")

    # Our notifier
    ntf = Notifier()

    # Observers for channel #1
    ntf.add_subscriber("ch1", obs1)
    ntf.add_subscriber("ch1", obs2)
    # Observers for channel #2
    ntf.add_subscriber("ch2", obs1)
    ntf.add_subscriber("ch2", obs3)
    # Observers for channel #3
    ntf.add_subscriber("ch3", obs4)

    # Let's send some notifications
    ntf.notify(sender="mati", channel="ch1", message="hello, pals!")
    ntf.notify(sender="mati", channel="ch2", message="hello, dudes!!")
    ntf.notify(sender="mati", channel="ch3", message="hello, mate")
