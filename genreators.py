#   Generators --->. A generator is a special type of function that produces values one at a time, on demand, instead of creating all values at once.
#################  Generator = "don't unnecessarily store all generated results at once"#######################
# generator uses yield like return for returning the value one at a time

# normal code using recursion

def square_numbers(nums):
    result = []

    for n in nums:
        result.append(n * n)

    return result


numbers = [1, 2, 3, 4, 5]
result = square_numbers(numbers)
print(result)

#############################################
return
 ↓
Give result
 ↓
FUNCTION ENDS
################################################

yield
 ↓
Give value
 ↓
PAUSE
 ↓
Continue later

####################################################


# when genrators uses ==>

def square_numbers(nums):
    for n in nums:
        yield n*n
numbers = [1, 2, 3, 4, 5]
result = square_numbers(numbers)
print(next(result))
print(next(result))   # while writing this you write with  for loop 

for m in result:
    print(m)

###########  generators are more efficient because it create one space t a time..........

# generators vs list
  ## LIST expression                      List
    #                                      ↓
    #                             Creates/stores all results
    # it uses []
numbers = [x * x for x in range(5)]   
for n in numbers:
    print(numbers)

  ## GENERATORS expression          Generator
    #                                   ↓
    #                                 Produces results when needed
    # it uses ()

numbers  = (x*x for x in range(5))
for num in numbers:
    print(numbers)


####  conceptually  -_>>>>>>>>>>
Huge Dataset
     ↓
Generator
     ↓
one record
     ↓
process
     ↓
next record
     ↓
process
     ↓
next record

This streaming-style processing can be useful when dealing with data that is too large or expensive to materialize all at once. Generator-based approaches are commonly discussed specifically for large-data processing and memory efficiency.


#   Important limitation: generators are usually one-use