def bubble_sort(nums): # создание функции с одним параметром, который принимает массив.  
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True # флажок
    while swapped: # пока флажок поднят идем по циклу 
        swapped = False # случай, когда мы опускаем флаг 
        for i in range(len(nums) - 1): # перебираем все до последнего элемента 
            if nums[i] > nums[i + 1]: # если левый больше правого
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

# Проверяем, что оно работает
random_list_of_nums = [5, 2, 1, 8, 4]  
bubble_sort(random_list_of_nums)  
print(random_list_of_nums)
# повторил
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                swapped=True
                
check = [5, 2, 1, 8, 4] 
bubble_sort(check)
print(check)                 