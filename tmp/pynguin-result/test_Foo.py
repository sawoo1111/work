# Automatically generated by Pynguin.
import Demo as module0


def test_case_0():
    var0 = module0.Demo()
    assert var0 is not None


def test_case_1():
    var0 = 'rL*}_|+n>'
    var1 = module0.Demo()
    assert var1 is not None
    var2 = var1.bar(var0)
    assert var2 == 'rL*}_|+n>rL*}_|+n>'


def test_case_2():
    var0 = module0.Demo()
    assert var0 is not None
    var1 = 'rL*}_|+n>'
    var2 = module0.Demo()
    assert var2 is not None
    var3 = var2.bar(var1)
    assert var3 == 'rL*}_|+n>rL*}_|+n>'
    var4 = module0.Demo()
    assert var4 is not None
