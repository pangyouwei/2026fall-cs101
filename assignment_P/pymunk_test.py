import pymunk


def main():
    space = pymunk.Space()
    space.gravity = (0, -900)

    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 10))
    body.position = (0, 100)
    space.add(body, pymunk.Circle(body, 10))

    for _ in range(60):
        space.step(1 / 60)

    assert body.position.y < 100
    print(f"Pymunk {pymunk.version} 导入成功")
    print(f"重力模拟验证通过：1 秒后位置 {tuple(body.position)}")


if __name__ == "__main__":
    main()
