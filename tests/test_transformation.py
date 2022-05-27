from shorthand import T


def test_add():
    assert list(map(T.add(1), [1, 2, 3])) == [2, 3, 4]


def test_sub_by():
    assert list(map(T.sub_by(1), [1, 2, 3])) == [0, 1, 2]


def test_sub_from():
    assert list(map(T.sub_from(1), [1, 2, 3])) == [0, -1, -2]


def test_mul():
    assert list(map(T.mul(2), [1, 2, 3])) == [2, 4, 6]


def test_div_by():
    assert list(map(T.div_by(2), [1, 2, 3])) == [.5, 1., 1.5]


def test_div_from():
    assert list(map(T.div_from(6), [1, 2, 3])) == [6., 3., 2.]


def test_floordiv_by():
    assert list(map(T.floordiv_by(2), [1, 2, 3])) == [0., 1., 1.]


def test_floordiv_from():
    assert list(map(T.floordiv_from(7), [1, 2, 3])) == [7., 3., 2.]


def test_pow():
    assert list(map(T.pow(3), [1, 2, 3])) == [1., 8., 27.]


def test_attr():
    class C:
        def __init__(self, v):
            self.v = v

    assert list(map(T.attr("v"), [C(1), C(4)])) == [1, 4]


def test_attr_with_default():
    class C:
        def __init__(self, v):
            self.v = v

    class D:
        pass

    assert list(map(T.attr("v", -1), [C(1), D(), C(4)])) == [1, -1, 4]


def test_do():
    d = []
    assert list(map(T.do(d.append), range(5))) == [0, 1, 2, 3, 4]
    assert d == [0, 1, 2, 3, 4]


def test_do_with_params():
    class M:
        def __call__(self, x, p, q):
            self.params = x, p, q

    m = M()
    list(map(T.do(m, 1, q=True), ["x"]))
    assert m.params == ("x", 1, True)


def test_pipe():
    d = []
    assert list(map(T.do(d.append) >> T.mul(2), range(5))) == [0, 2, 4, 6, 8]
    assert d == [0, 1, 2, 3, 4]


def test_repeat_str():
    assert list(map(T.repeat("*"), range(3))) == ["", "*", "**"]


def test_get():
    assert list(map(T.get("A"), [{"A": 1, "B": 2}, {"C": 3, "A": 4}])) == [1, 4]


def test_get_with_default():
    assert list(map(T.get("A", 999), [{"A": 1, "B": 2}, {}, {"C": 3, "A": 4}])) == [1, 999, 4]


def test_item():
    assert list(map(T.item(1), [[0, 1], [2, 3, 4], [5, 6]])) == [1, 3, 6]


def test_select():
    assert list(map(T.select(lambda x: x > 0, lambda x: 1, lambda x: -1), [-1, 9, 4, -4])) == [-1, 1, 1, -1]


def test_val():
    assert list(map(T.val(999), [1, 2, 3])) == [999, 999, 999]


def test_me():
    assert list(map(T.me(), [1, 2, 3])) == [1, 2, 3]


def test_safe():
    assert list(map(T.safe(lambda x: 0/x, 999), [-3, -1, 0, 4, 3, 0, 2, 0])) == [0, 0, 999, 0, 0, 999, 0, 999]


def test_error():
    result = list(map(T.error(lambda x: 0/x), [-3, -1, 0, 4, 3]))
    assert result[:2] == [None, None] and isinstance(result[2], ZeroDivisionError) and result[3:] == [None, None]


def test_attribute_level_transformation():
    assert list(map(T["a"].add(1), [{"a": 0}, {"a": 1}])) == [{"a": 1}, {"a": 2}]


def test_attribute_level_transformation_with_pipe():
    result = list(map(T["a"].add(1) >> T["b"].sub_by(2), [{"a": 0, "b": 4}, {"a": 1, "b": 5}]))
    assert result == [{"a": 1, "b": 2}, {"a": 2, "b": 3}]


def test_wrap_in_dict():
    assert list(map(T.wrap("a"), [1, 2, "x"])) == [{"a": 1}, {"a": 2}, {"a": "x"}]


def test_wrap_in_dict_with_default_value():
    result = list(map(T.wrap("a", 999) >> T["b"].sub_by(900), [1, 2]))
    assert result == [{"a": 1, "b": 99}, {"a": 2, "b": 99}]


def test_project_to_dict():
    result = list(map(T.project({"a": T.me(), "b": T.add(10)}), range(3)))
    assert result == [{"a": 0, "b": 10}, {"a": 1, "b": 11}, {"a": 2, "b": 12}]


def test_project_to_list():
    result = list(map(T.project([T.me(), T.add(10)]), range(3)))
    assert result == [[0, 10], [1, 11], [2, 12]]


def test_project_to_tuple():
    result = list(map(T.project((T.me(), T.add(10))), range(3)))
    assert result == [(0, 10), (1, 11), (2, 12)]
