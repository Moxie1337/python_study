def moxie(name=None, age=True, **kwargs):
    print(f'name : {name}, age : {age}, kwargs : {kwargs}')
    get_info(**kwargs)

def get_info(price=None, address=None):
    print(f'price : {price}, address : {address}')

moxie('moxie', price='123', address='buaa')