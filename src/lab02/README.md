# ЛР2 - Коллекции и матрицы
## Задание A
### 1. min_max
На вход функции подаётся список чисел. Первый элемент списка принимается за начальное значение минимума и максимума, далее с ними сравниваются последующие элементы. При необходимости значения переменных минимума и максимума обновляются. Функция возвращает кортеж, содержащий минимальный и максимальный элементы списка.

```python
def min_max(nums: list[float|int]) -> tuple[float|int, float|int]:
    """
    This function takes a list of numbers (integers or floats) and returns a tuple containing the minimum and maximum values from that list.
    """
    if not nums:
        raise ValueError('The list cannot be empty')
    for num in nums:
        if isinstance(num, bool) or not isinstance(num, (int, float)):
            raise TypeError('The list must contain only numbers')

    maxnums, minnums = nums[0], nums[0]
    for num in nums:
        if num > maxnums:
            maxnums = num
        elif num < minnums:
            minnums = num
    return minnums, maxnums

#test cases
print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([1.5,2,2.0,-3.1]))
print(min_max([]))
```
![результат задания 1.1](../../images/lab02/arrays_01.png)\
*результат задания 1.1*

### 2. unique_sorted

Так как использование встроенной сортировки запрещено, реализована пузырьковая сортировка (выполняется некоторое количество проходов по массиву с перебором пар соседних элементов до момента, пока значения не встанут в необходимом порядке).  
На вход функции подается список чисел. Далее создается пустой результирующий список, в который добавляются значения из входного при условии, что они в нём не повторяются. Функция возвращает результирующий список, отсортированный методом пузырьковой сортировки.

```python
def bubble_sort(nums: list[float|int]) -> list[float|int]:
    """
    This function takes a list of numbers (integers or floats) and sorts it in ascending order using the bubble sort algorithm.
    """
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def unique_sorted(nums: list[float|int]) -> list[float|int]:
    """
    This function returns a sorted list of numbers (integers or floats) with duplicates removed.
    """
    for num in nums:
        if isinstance(num, bool) or not isinstance(num, (int, float)):
            raise TypeError('The list must contain only numbers')
        
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)

    unique_sorted_nums = bubble_sort(unique_nums)
    return unique_sorted_nums

#test cases
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
```
![результат задания 1.2](../../images/lab02/arrays_02.png)\
*результат задания 1.2*

### 3. flatten

Функция получает на вход несколько списков или кортежей. Далее элементы объединяются в результирующий список, который возвращает функция. 

```python
def flatten(mat: list[list|tuple]) -> list:
    """
    This function returns a flattened version of matrix as a single list.
    """
    if not mat:
        raise ValueError('The matrix cannot be empty')
    res = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError('Each row must be a list or tuple')
        for el in row:
            res.append(el)
    return res
#test cases
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3,4,5)]))
print(flatten([[1], [], [2,3]]))
print(flatten([[1, 2], 'ab']))
```
![результат задания 1.3](../../images/lab02/arrays_03.png)\
*результат задания 1.3*

## Задание B
### helper functions for lib folder
Функция для проверки прямоугольности матрицы.
```python
def check_rec_mat(mat: list[list[int]]):
    """
    This function checks if the matrix is rectangular.
    """
    if not mat:
        return False
    for row in mat:
        if not isinstance(row, list):
            raise ValueError("Matrix must be a list of lists")
        if len(row) != len(mat[0]):
            return False
    return True
```
Функция для проверки типов элементов матрицы.
```python
def check_values(mat: list[list[int]]):
    """
    This function checks if all values in the matrix are floats or integers.
    """
    for row in mat:
        for el in row:
            if isinstance(el, bool) or not isinstance(el, (float, int)):
                raise ValueError("Matrix must contain only floats or integers")
```

### using helper functions in matrix
```python
from src.lib.check_mat_values_f import check_values
from src.lib.check_rec_mat_f import check_rec_mat
```

### transpose
Функция принимает на вход матрицу, представляющую собой список списков. Далее матрица проверяется на прямоугольность и тип элементов.\
Создается новая матрица. Для каждого столбца исходной матрицы создается строка в новой. В неё последовательно добавляются элементы этого столбца из каждой строки исходной матрицы. Полученные строки добавляются в новую матрицу, в результате чего исходная матрица транспонируется. 
```python
def transpose(mat: list[list[int]]) -> list[list[int]]:
    """
    This function transposes the given matrix.
    """
    if len(mat) == 0:
        return []
    if not check_rec_mat(mat):
        raise ValueError("Matrix is not rectangular")
    check_values(mat)
    new_mat = []
    for i in range(len(mat[0])):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        new_mat.append(new_row)
    return new_mat

#test cases
print(transpose([[1,2,3]]))
print(transpose([[1],[2],[3]]))
print(transpose([[1,2], [3,4]]))
print(transpose([]))
print(transpose([[1,2],[3]]))
```
![результат задания 2.1](../../images/lab02/matrix_01.png)\
*результат задания 2.1*

### row_sums
Функция принимает на вход матрицу, представляющую собой список списков. Далее матрица проверяется на прямоугольность и тип элементов. \
Функция возвращает список, в который последовательно добавлены суммы строк матрицы.
```python
def row_sums(mat: list[list[float|int]]) -> list[float]:
    """
    This function calculates the sum of each row in the given matrix.
    """
    if not check_rec_mat(mat):
        raise ValueError("Matrix is not rectangular")
    check_values(mat)
    res = [sum(row) for row in mat]
    return res

#test cases
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1,1], [10,-10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1, 2], [3]]))
```
![результат задания 2.2](../../images/lab02/matrix_02.png)\
*результат задания 2.2*

### col_sums
Функция принимает на вход матрицу, представляющую собой список списков. Далее матрица проверяется на прямоугольность и тип элементов. \
Функция возвращает список, в который последовательно добавлены суммы столбцов матрицы. Для вычисления суммы последовательно складываются элементы каждой строки, имеющие одинаковый индекс.
```python
def col_sums(mat: list[list[float|int]]) -> list[float]:
    """
    This function calculates the sum of each column in the given matrix.
    """
    if not check_rec_mat(mat):
        raise ValueError("Matrix is not rectangular")
    check_values(mat)
    res = [sum(row[i] for row in mat) for i in range(len(mat[0]))]
    return res

#test cases
print(col_sums([[1, 2,3], [4,5,6]]))
print(col_sums([[-1,1], [10,-10]]))
print(col_sums([[0,0], [0,0]]))
print(col_sums([[1, 2], [3]]))
```
![результат задания 2.3](../../images/lab02/matrix_03.png)\
*результат задания 2.3*

## Задание C

Функция принимает на вход запись студента, представленную в виде кортежа, содержащего ФИО, группу и GPA. Проверяется корректность количества элементов записи, ФИО и группы, а также тип и диапазон значения GPA. Из ФИО выделяется фамилия и формируются инициалы имени и отчества.
Функция возвращает строку с фамилией, инициалами, группой и GPA, округленным до двух знаков после запятой. 

```python
def format_record(rec: tuple[str, str, float]) -> str:
    """
    Returns a formatted string containing a student's surname, initials,
    group, and GPA.
    Raises:
    ValueError:
        If the record does not contain three elements.
        If the full name is empty or does not contain 2 or 3 parts.
        If any part of the full name contains non-alphabetic characters.
        If the group is empty.
        If the GPA is outside the range from 0.0 to 5.0.

    TypeError:
        If the record is not a tuple.
        If the full name is not a string.
        If the group is not a string.
        If the GPA is not a number (int or float), including bool.
    """
    if not isinstance(rec, tuple):
        raise TypeError('Record must be a tuple')
    if len(rec) != 3:
            raise ValueError('Record must contain 3 elements: full name, group, and GPA. Check that you have entered all the necessary information, separated by commas.')

    fio, group, gpa = rec
    
    if not isinstance(fio, str):
        raise TypeError('Full name must be a string')
    if not fio:
        raise ValueError('Full name cannot be empty')

    name_parts = fio.strip().split()

    if len(name_parts) not in (2, 3):
        raise ValueError('Full name must contain at least Surname and First name')
    if any(not part.isalpha() for part in name_parts):
        raise ValueError("Full name must contain only alphabetic characters")

    surname = name_parts[0].capitalize()
    initials = ''.join(part[0].upper() + '.' for part in name_parts[1:])

    if not isinstance(group, str):
        raise TypeError('Group must be a string')
    group = group.strip()
    if not group:
        raise ValueError('Group cannot be empty')
  
    if isinstance(gpa,bool) or not isinstance(gpa, (int, float)):
        raise TypeError('GPA must be a number.')
    if not 0.0 <= gpa <= 5.0:
        raise ValueError('GPA must be in the range from 0.0 to 5.0.')
    
    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'

#test cases

print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5.0) ))
print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", 3.999) ))


#additional test cases for checking ValueError

print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", -1.999) ))
print(format_record( (" Анна ", "ACC-01", 3.7) ))
print(format_record( ("  ", "ABB-01", 3.999) ))
print(format_record( ("Петров Пётр", "", 3.999) ))
print(format_record( ("Пе67ов Пётр Пет42вич", "IKBO-12", 5.0) ))

#additional test cases for checking TypeError

print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", "3.999") ))
print(format_record( ("Петров Пётр", "IKBO-12", True) ))
print(format_record( (["Иванов Иван"], "BIVT-25", 3.999) ))
print(format_record( ["Иванов Иван", "BIVT-25", 4.6] ))

```
![результат задания 3](../../images/lab02//tuples_test_cases/correct_cases.png)\
*результат задания 3*

### ValueError

#### Входные данные: ("  сидорова  анна   сергеевна ", "ABB-01", -1.999)
![ошибка: gpa не в диапазоне от 0.0 до 5.0](../../images/lab02/tuples_test_cases/ValueError/VE_gpa_range.png)\
*ошибка: gpa не в диапазоне от 0.0 до 5.0*

#### Входные данные: (" Анна ", "ACC-01", 3.7)
![ошибка: введено только имя](../../images/lab02/tuples_test_cases/ValueError/Full_name_len.png)\
*ошибка: введено только имя*

#### Входные данные: ("  ", "ABB-01", 3.999)
![ошибка: пустое фио](../../images/lab02/tuples_test_cases/ValueError/empty_full_name.png)\
*ошибка: пустое фио*

#### Входные данные: ("Петров Пётр", "", 3.999)
![ошибка: пустая группа](../../images/lab02/tuples_test_cases/ValueError/empty_group.png)\
*ошибка: пустая группа*

#### Входные данные: ("Пе67ов Пётр Пет42вич", "IKBO-12", 5.0)
![ошибка: фио содержит не только буквы](../../images/lab02/tuples_test_cases/ValueError/full_name_alphabet.png)\
*ошибка: фио содержит не только буквы*

### TypeError

#### Входные данные: ("  сИдОРова  анна   сергеевна ", "ABB-01", "3.999")
![ошибка: gpa не является числом](../../images/lab02/tuples_test_cases/TypeError/gpa_is_not_number.png)\
*ошибка: gpa не является числом*

#### Входные данные: ("Петров Пётр", "IKBO-12", True)
![ошибка: gpa - булева переменная](../../images/lab02/tuples_test_cases/TypeError/gpa_is_bool.png)\
*ошибка: gpa - булева переменная*

#### Входные данные: (["Иванов Иван"], "BIVT-25", 3.999)
![ошибка: фио не является строкой](../../images/lab02/tuples_test_cases/TypeError/fio_is_not_str.png)\
*ошибка: фио не является строкой*

#### Входные данные: ["Иванов Иван", "BIVT-25", 4.6]
![ошибка: введен не кортеж](../../images/lab02/tuples_test_cases/TypeError/rec_is_not_tuple.png)\
*ошибка: введен не кортеж*






