from engine import Engine

def run():
    engine = Engine(size=4)
    is_over = False
    while not is_over:
        is_over = engine.next_turn()

if __name__ == '__main__':
    run()