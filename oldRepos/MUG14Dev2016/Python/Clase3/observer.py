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

class Observer(object):
    def __init__(self, name=None):
        self.name = name or randint(23456, 43567)

    def listen(self, sender, message):
        print "(User: {}, Sender: {}) --> {}".format(self.name, sender, message)


observer1 = Observer()
observer2 = Observer(name='usuario 1')
observer3 = Observer()
observer4 = Observer(name='usuario 2')

notifier = Notifier()

notifier.add_subscriber('channel1', observer1)
notifier.add_subscriber('channel1', observer2)
notifier.add_subscriber('channel2', observer3)
notifier.add_subscriber('channel2', observer4)

notifier.notify(sender="pepe", channel="channel1", message="Hola a todos")
notifier.notify(sender="pepe", channel="channel2", message="Python rocks!")
