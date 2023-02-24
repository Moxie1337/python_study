# generator is a specialize of iterator
# gen is called generator function(with yield)
def gen(num):
    while num > 0:
        yield num
        num -= 1
    return # 在生成器函数里, return = raise StopIteration

# instance g is called generator instance
# 生成器函数返回一个生成器对象,并不是返回一个值
# 只有当对生成器对象使用next()时，才会真正运行生成器对象的生成器函数本体
g = gen(5)
# generator can invoke next()
first = next(g)

for i in g:
    print(i)