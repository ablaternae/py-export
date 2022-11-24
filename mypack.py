import export


def fee():
    return 'twee'


@export
def moo():
    return 'moow'


@export
class C:
    def init(self):
        super().__init__()
