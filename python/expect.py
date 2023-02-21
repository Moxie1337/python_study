def print_except():
    def _moxie():
        pass
    moxie_ = 1
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(dir(inst))
        print(type(inst))
        print(inst.args)
        print(inst.__str__)

print_except()