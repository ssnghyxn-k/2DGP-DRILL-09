#world = []  # 단일 계층 구조

# world[0]: Background 객체들 -> 즉 맨 아레에 그려야 할 객체들
# world[1]: Forward ground 객체들 -> 위에 그려야 할 객체들
world = [ [], [] ]

def add_object(o, depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return  # 지우는 미션은 달성, 다른 요소는 더 이상 체크할 필요 없다
    print('Error: Object does not exist')  # 존재하지 않는 객체를 지운다고?