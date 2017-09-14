print([(lambda x, y : '%d x %d = %d' % (x, y, x * y))(x, y) for x in range(2, 10) for y in range(1, 10)])
