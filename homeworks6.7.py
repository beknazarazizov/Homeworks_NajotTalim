if __name__ == '__main__':


# class FibonacciIterator:
#     def __init__(self):
#         self.prev = 0
#         self.curr = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = self.prev
#         self.prev, self.curr = self.curr, self.prev + self.curr
#         return result
#
# # Example usage:
# fib_iter = FibonacciIterator()
# for i in fib_iter:
#     print(i)
#     def fibonacci_generator():
#         first, second = 0, 1
#         while True:
#             yield first
#             first, second = second, first + second
#
#
#     # Example usage:
#     fib_gen = fibonacci_generator()
#     for _ in range(10):
#         print(next(fib_gen))
#
    def programming_language_generator():
        languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Swift", "Rust", "Go", "PHP", "C#"]
        for language in languages:
            yield language


    # Example usage:
    # gen = programming_language_generator()
    # x=0
    # for i in gen:
    #     x+=1
    #     print(i)
    #     digte=len(i)
    #     if digte==5:
    #         gen.throw(ValueError("valueerror"))
    #
    # gen = programming_language_generator()
    # x = 0
    # for i in gen:
    #     x += 1
    #     print(i)
    #     digte = len(i)
    #     if digte == 5:
    #         gen.close()
    gen = programming_language_generator()




