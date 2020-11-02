import time

# сразу задание с **, пишем декоратор в качестве объета класса,
# а также его использование в качестве контекстный менеджера

class Timer:
	def __init__(self, num_runs = 10):
		self.num_runs = num_runs

	def __enter__(self, *args):
		self.start = time.time()
		return self.start

	def __exit__(self, *args):
		self.end = time.time()
		print("Выполнение заняло %.5f секунд " % (self.end - self.start))

	def __call__(self, func):
		def timer():
			avg_time = 0
			for _ in range(self.num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
				avg_time += (t1 - t0)
				avg_time /= self.num_runs
				print("Выполнение заняло %.5f секунд" % avg_time)
		return timer

# Проверка в качестве декоратора
print("Проверка в качестве декоратора")
obj = Timer(num_runs = 10)
@obj
def f():
	i = 0
	numbers = [1, 2, 3]
	while i < 4**1000:
		i = numbers[-1] + numbers[-2]
		numbers.append(i)
		i +=1
	print(sum(numbers))
f()

print("Проверка в качестве к-м")
# Проверка как к-м
if __name__ == "__main__":
	with Timer() as t:
		a = list(range(1**6, 1, -1))
		a.sort()



