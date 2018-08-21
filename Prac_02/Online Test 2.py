x = 15 / 3 + 2 * 4
print(x)

a = 5
b = 10
c = 0.5

a == b * c or c * 10 >= a
print("True")

for i in range(1, 10, 4):
    print(i, i * 2, end=" ")

z = 5 // 2
print(z)

x = 10
while x > 4:
    print(x, end=" ")
    x = x - 2
print("\n")
x = 5
for i in range(x):
    x = x + i
    print(x, end=" ")


nums1 = [1, -5, 2, 0, 4, 2, -3]
nums2 = [1, -5, 2, 4, 4, 2, 7]
result = 0
j = 0
while j < len(nums1):
    if nums1[j] != nums2[j]:
        result = result + 1
    j = j + 1
print (result)

girls = 0
boys = 0
children = girls + boys
girls = 15
boys = 12

print(girls, boys, children)

yep = 7 % 3
print(yep)

x = 1
y = 2
z = 3
if x < y:
    if y > 4:
        z = 5
    else:
        z = 6

print(z)