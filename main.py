from engine import Engine

def run():
    engine = Engine()
    is_over = False
    while not is_over:
        is_over = engine.play()

if __name__ == '__main__':
    run()