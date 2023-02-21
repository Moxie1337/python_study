
# class Philosopher:
#     def __init_subclass__(cls, default_name, **kwargs):
#         super().__init_subclass__(**kwargs)
#         print(f"Called __init_subclass({cls}, {default_name})")
#         cls.default_name = default_name

# class AustralianPhilosopher(Philosopher, default_name="Bruce"):
#     pass

# class GermanPhilosopher(Philosopher, default_name="Nietzsche"):
#     default_name = "Hegel"
#     print("Set name to Hegel")

# Bruce = AustralianPhilosopher()
# Mistery = GermanPhilosopher()
# print(Bruce.default_name)
# print(Mistery.default_name)
class PluginBase:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    @staticmethod
    def print_subclasses():
        for subclass in PluginBase.subclasses:
            print(subclass)


class P1(PluginBase):
    pass

class P2(PluginBase):
    pass

PluginBase().print_subclasses()