import time

# damn its works wrong too, well leaving crutches for a while --J
def _example_func(max_val=100):
    _ = [i for i in range(max_val)]

def _arg_dec(func, args, kwargs):
    if args:
        if kwargs:
            def wrapper():
                func(*args, **kwargs)
        else:
            def wrapper():
                func(*args)
        return wrapper
    else:
        return func(**kwargs) if kwargs \
            else lambda: func()

def bench_test(count=10000, max_val=100):
    return bench_func(_example_func, count, max_val)


def bench_func(func, count=1, *args, **kwargs):
    fc = _arg_dec(func, args, kwargs)
    t1 = time.time()
    for _ in range(count):
        fc()
    t2 = time.time()
    return (t2 - t1)/count


