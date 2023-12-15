from typing import List

def swap(arr, right_pos, left_pos):
  temp = arr[left_pos]
  arr[left_pos] = arr[right_pos]
  arr[right_pos] = temp


def bubble_sort(arr):
  for itm in arr:
    for idx in range(len(arr) - 1):
      if arr[idx] < arr[idx + 1]:
        swap(arr, idx, idx + 1)

myarray = [5, 7, 4, 3, 8, 10, 12, 6, 0, 41, 2]
bubble_sort(myarray)
print(myarray)