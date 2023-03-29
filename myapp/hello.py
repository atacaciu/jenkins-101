import fire

def hello(name="Lume Lume"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)