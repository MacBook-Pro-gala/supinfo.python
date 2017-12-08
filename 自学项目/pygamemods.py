def pygamefrom(x, y, x1, y1, w):
    aa = x1
    bb = y1
    for a in range(y + 1):
        pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x1, x * w + y1))
        x1 = x1 + w
    x1 = aa
    y1 = bb
    for b in range(x + 1):
        pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x1 + y * w, y1))
        y1 = y1 + w