print("try:                                          # Try block begins")
try:                                                # Try block begins
    x = 1 / 0
except ZeroDivisionError:                           # Handles division by zero
    print("You can't divide by zero!")

print("try:                                          # Catch specific exception (ValueError)")
try:
    int("abc")                                      # Cannot convert string to int
except ValueError:
    print("Invalid integer!")

print("try:                                          # Catch multiple exceptions")
try:
    x = int("abc")
    y = 1 / 0
except (ValueError, ZeroDivisionError) as e:
    print("Caught error:", e)

print("try:                                          # Catch any exception (not recommended in large code)")
try:
    open("nonexistent.txt")                         # File does not exist
except Exception as e:
    print("General error:", e)

print("try/finally:                                 # Run cleanup code no matter what")
try:
    print("Doing something...")
finally:
    print("This always runs (finally block)")

print("try/except/else:                             # Run else if no exception occurs")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide.")
else:
    print("Success! Result:", result)

print("raise ValueError('Manual error')             # Manually raise an error")
try:
    raise ValueError("Manual error")
except ValueError as e:
    print("Caught manually raised error:", e)

print("assert 2 + 2 == 4                             # Assertion passes (nothing happens)")
assert 2 + 2 == 4                                    # Passes, no error

print("assert 2 + 2 == 5                             # Assertion fails")
try:
    assert 2 + 2 == 5                                # Fails, raises AssertionError
except AssertionError:
    print("Assertion failed!")

print("def divide(a, b):                            # Custom function with exception")
def divide(a, b):                                    # Function that handles division
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"

print("print(divide(10, 2))")                        # Should return 5.0
print(divide(10, 2))                                 # Output: 5.0

print("print(divide(10, 0))")                        # Should return error message
print(divide(10, 0))                                 # Output: Can't divide by zero
