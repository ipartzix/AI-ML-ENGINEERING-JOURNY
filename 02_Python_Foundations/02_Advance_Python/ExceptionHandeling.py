a = int(input("enter a number : "))

try:
    b = (10 / a)
except ZeroDivisionError:
    print("u can not enter 0")
print(b)
print("done")
# exception handling with try and expect


"""
PYTHON ERROR HANDLING – COMPLETE REFERENCE
Each block demonstrates:
1. Error name
2. Definition
3. Example code
"""

# --------------------------------------------------
# 1. SYNTAX ERROR
# Definition:
# Occurs when Python grammar rules are violated.
# Detected before execution, cannot be handled by try-except.

# Example (DO NOT RUN – will crash the program)
# if x > 5
#     print("Hello")


# --------------------------------------------------
# 2. ZERODIVISIONERROR
# Definition:
# Raised when division by zero occurs.

try:
    x = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: cannot divide by zero")

# --------------------------------------------------
# 3. NAMEERROR
# Definition:
# Raised when a variable is used before it is defined.

try:
    print(a)
except NameError:
    print("NameError: variable is not defined")

# --------------------------------------------------
# 4. TYPEERROR
# Definition:
# Raised when an operation is applied to incompatible data types.

try:
    result = 5 + "10"
except TypeError:
    print("TypeError: unsupported operand types")

# --------------------------------------------------
# 5. VALUEERROR
# Definition:
# Raised when a function receives the correct type but invalid value.

try:
    num = int("abc")
except ValueError:
    print("ValueError: invalid literal for int()")

# --------------------------------------------------
# 6. INDEXERROR
# Definition:
# Raised when accessing an index outside the list range.

try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("IndexError: list index out of range")

# --------------------------------------------------
# 7. KEYERROR
# Definition:
# Raised when accessing a non-existing dictionary key.

try:
    data = {"name": "Python"}
    print(data["age"])
except KeyError:
    print("KeyError: key not found in dictionary")

# --------------------------------------------------
# 8. ATTRIBUTEERROR
# Definition:
# Raised when accessing a method or attribute that does not exist.

try:
    x = 10
    x.append(5)
except AttributeError:
    print("AttributeError: invalid attribute access")

# --------------------------------------------------
# 9. FILENOTFOUNDERROR
# Definition:
# Raised when trying to open a file that does not exist.

try:
    file = open("unknown.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: file does not exist")

# --------------------------------------------------
# 10. IMPORTERROR
# Definition:
# Raised when a module cannot be imported.

try:
    import unknownmodule
except ImportError:
    print("ImportError: module not found")

# --------------------------------------------------
# 11. OVERFLOWERROR
# Definition:
# Raised when a numerical result is too large to represent.

import math

try:
    value = math.exp(1000)
except OverflowError:
    print("OverflowError: result too large")

# --------------------------------------------------
# 12. MEMORYERROR
# Definition:
# Raised when the program runs out of memory.

try:
    big_list = [1] * (10 ** 10)
except MemoryError:
    print("MemoryError: insufficient memory")


# --------------------------------------------------
# 13. RECURSIONERROR
# Definition:
# Raised when maximum recursion depth is exceeded.

def recursive_fun():
    return recursive_fun()


try:
    recursive_fun()
except RecursionError:
    print("RecursionError: maximum recursion depth exceeded")

# --------------------------------------------------
# 14. MULTIPLE EXCEPT BLOCKS
# Definition:
# Handling different exceptions separately.

try:
    a = int("xyz")
    b = 10 / 0
except ValueError:
    print("ValueError occurred")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")

# --------------------------------------------------
# 15. MULTIPLE EXCEPTIONS IN SINGLE BLOCK

try:
    a = int("xyz")
except (ValueError, TypeError):
    print("Handled multiple exceptions")

# --------------------------------------------------
# 16. GENERIC EXCEPTION
# Definition:
# Handles any exception using base Exception class.

try:
    x = 10 / 0
except Exception as e:
    print("Generic Exception:", e)

# --------------------------------------------------
# 17. TRY – EXCEPT – ELSE – FINALLY
# Definition:
# else → runs if no exception occurs
# finally → always runs

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result:", result)
finally:
    print("Execution completed")


# --------------------------------------------------
# 18. USER-DEFINED EXCEPTION
# Definition:
# Custom exception created by programmer.

class AgeError(Exception):
    pass


try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Age must be 18 or above")
except AgeError as e:
    print("Custom Exception:", e)

# --------------------------------------------------
# 19. LOGICAL ERROR
# Definition:
# Program runs but gives incorrect output.

# Logical mistake: should be a * b
a = 5
b = 10
print("Logical Error Output:", a + b)
