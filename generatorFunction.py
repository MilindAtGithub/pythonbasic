# This is the generator function which work like stream
# We are going to use Yield which has the following fucntionality
    # The yield statement suspends function’s execution and sends a value back to caller,
    # but retains enough state to enable function to resume where it is left off. When resumed,
    # the function continues execution immediately after the last yield run.
    # This allows its code to produce a series of values over time,
    # rather them computing them at once and sending them back like a list.


def generate():
    yield 1
    yield 'Milind'
    print("After String Printing")
    yield 90.67


for i in generate():
    print(i)
    print("Call from Loop")


# This is the square fucntion which will return the square as needed
def square():
    for i in range(100):
        yield i*i

# Calling the Square
for k in square():
    if (k > 200):
        break
    else:
        print(k)
        print("Next Val")
