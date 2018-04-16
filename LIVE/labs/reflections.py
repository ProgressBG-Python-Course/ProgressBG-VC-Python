class Car:
  def __init__(self):
      pass

  def attach_engine(self,engine):
    self.engine = engine

   def run(self):
       self.engine.start()

class Engine:
  def start(self):
    print("Engine started!")



trinity5_8 = Engine()
ford = Car()
ford.attach_engine(trinity5_8)

ford.engine.start()
ford.run()