#insertion sort

def isort(xs: list[int]) -> None:
    i: int = 1
    j: int
    while i < len(xs):
        j = i
        while j > 0 and xs[j] < xs[j - 1]:
            swap(xs, j, j - 1)
            j -= 1

        i += 1

def swap(xs: list[int], i: int, j: int) -> None:
    temp: int = xs[i]
    xs[i] = xs[j]
    xs[j] = temp

nums: list[int] = [2, 3, 1, 4]
isort(nums)
print(nums)


#range
print(range(0, 1000, 1))

start: int = 0
stop: int = 101
step: int = 10

a_range: range = range(start, stop, step)
print(a_range.start)
print(a_range.stop)
print(a_range.step)

print(a_range[0])
print(a_range[1])
print(a_range[2])
print(len(a_range))
print(f"Max value in range: {a_range[len(a_range) - 1]}")


#for... in

letters: list[str] = ["a","b","c","d","e","f","g"]

#each letter in list
for letter in letters:
    print(letter)

#every other letter in range
for i in range(0, len(letters), 2):
print(letters[i])


#question

xs: list[str] = ["hello", "world"]
for word in xs:
    print("iteration!")