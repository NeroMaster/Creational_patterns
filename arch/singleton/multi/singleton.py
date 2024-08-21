import threading


class Singleton:

  _instance = None
  _lock = threading.Lock()

  def __init__(self, customfield):
    self.customfield = customfield

  @classmethod
  def getInstance(cls, customfield):
    with cls._lock:
      if not cls._instance:
        cls._instance = cls(customfield)
    return cls._instance

  def getCustomField(self):
    return self.customfield


class ThreadFoo(threading.Thread):

  def run(self):
    singleton: Singleton = Singleton.getInstance("Foo")
    print(singleton.getCustomField())


class ThreadBoo(threading.Thread):

  def run(self):
    singleton: Singleton = Singleton.getInstance("Boo")
    print(singleton.getCustomField())


def main():
  print("If you see the same value, then singleton was reused!")
  threadFoo: threading.Thread = ThreadFoo()
  threadBoo: threading.Thread = ThreadBoo()

  threadFoo.start()
  threadBoo.start()


if __name__ == "__main__":
  main()
