#fibanachi iterator1

# class FibonacciIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.limit <= 0:
#             raise StopIteration
#         elif self.limit == 1:
#             self.limit -= 1
#             return 0
#         else:
#             self.limit -= 1
#             self.a, self.b =self.b, self.a + self.b
#
#             return self.a
#
#
# # Example usage:
# fib_iterator = FibonacciIterator(10)
# for num in fib_iterator:
#     print(num)
#fibonachi2
class FibonacciIterator2:
    def __init__(self,first,second,limit):
        self.first = first
        self.second = second
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.first <= self.second:
            raise StopIteration
        elif self.limit == 1:
             self.limit -= 1
             return 0
        else:
            self.limit-= 1
            self.first, self.second =self.second,self.first +self.second
            return self.first
fib_iter2=FibonacciIterator2(2,5,5)
for i in fib_iter2:
    print(i)