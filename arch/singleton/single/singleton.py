class Singleton:

  _instance = None

  def __init__(self, customfield):
    self.customfield = customfield
  
  @classmethod
  def getInstance(cls, customfield):
    if not cls._instance:
      cls._instance = cls(customfield)
    return cls._instance

  def getCustomField(self):
    return self.customfield


def main():
  print("If you see the same value, then singleton was reused!")
  singleton = Singleton.getInstance("BOO!")
  print(singleton.getCustomField())
  anotherSingleton = Singleton.getInstance("FOO!")
  print(anotherSingleton.getCustomField())
