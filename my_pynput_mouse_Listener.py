from pynput import mouse
cnt=0
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))
    cnt++
    bool_v=False if cnt>=5 else True
    return bool_v
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressfrom pynput import mouse')
    cnt++
    bool_v=False if cnt>=5 else True
    return bool_v

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))
    cnt++
    bool_v=False if cnt>=5 else True
    return bool_v
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y))) 
    if not pressed:
        # Stop listener
        return False
    cnt++
    bool_v=False if cnt>=5 else True
    return bool_v

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()