import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Procces time: {end - start:.6f} second")
        return result
    return wrapper


@time_decorator
def create_list(n):
    return list(range(1, n + 1))

n = int(input(" enter your number:"))
result = create_list(n)
print("list:", result)
