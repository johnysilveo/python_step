



# print(2/0)

# while True:
#     try:
    #     amount = (int(input('enter amount: ')))
    #     items_type = input('enter type: ')
    #     parts_number = int(input('enter part number: '))
    #     parts = amount / parts_number
    #     print('supply of ',amount,items_type, 'saved')
    #     print('each of ',parts_number, 'parts consist of' , parts,items_type)
    #
    # except ValueError:
    #     print('enter int')
    # except ZeroDivisionError:
    #     print('cant divide by zero')
    # # except BaseException:
    # #     print('base except')
    # finally:
    #     print('fin')

# try:
#     raise Exception
# except ValueError as ve:
#     print('some value')
# except Exception as ex:
#     print('some exception')
# print(type(ex,ve))
#
# def temp_func(num):
#     if num == 0:
#         raise num
#     else:
#         raise True
#
# try:
#     temp_func(1)
# except Exception as exe:
#     print(exe)
# while True:
#     try:
#         usd = float(input("Enter amount of USD: "))
#         rate = float(input("Enter the conversion rate: "))
#         if rate == 0:
#             raise Exception("Conversion rate cannot be zero!")
#         euro = usd * rate
#         print(f"The final conversion: {euro:.2f} EUR")
#
#     except ValueError:
#         print("Error: Please enter valid numeric values.")
#
#     except Exception as ex:
#         print(f"Error: {ex}")
#
#     finally:
#         print("Calculation complete.")
while True:
    try:
        grades = input('Enter grades separated by space (85 90 78): ')
        numbers = list(map(float, grades.split()))
        avg = sum(numbers) / len(numbers)
        print(f'Average grade is {avg}')
    except ValueError:
        print('Error: Please enter only numbers separated by space.')

    except ZeroDivisionError:
        print('Error: No grades entered.')
    finally:
        print('Calculation is completed')
    break

    
