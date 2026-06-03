python_mock_exam = {
    1: {
        "question": "実行結果は？",
        "code": "x = [1, 2, 3]\nprint(len(x))",
        "choices": ["2", "3", "4", "エラー"],
        "answer": 2
    },
    2: {
        "question": "実行結果は？",
        "code": "print(type(3.14))",
        "choices": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'num'>"],
        "answer": 2
    },
    3: {
        "question": "実行結果は？",
        "code": "x = 10\ny = 3\nprint(x % y)",
        "choices": ["3", "1", "0", "エラー"],
        "answer": 2
    },
    4: {
        "question": "実行結果は？",
        "code": "s = 'hello'\nprint(s[1])",
        "choices": ["h", "e", "l", "エラー"],
        "answer": 2
    },
    5: {
        "question": "実行結果は？",
        "code": "x = True\ny = False\nprint(x and y)",
        "choices": ["True", "False", "None", "エラー"],
        "answer": 2
    },
    6: {
        "question": "実行結果は？",
        "code": "print(10 // 3)",
        "choices": ["3.33", "3", "4", "エラー"],
        "answer": 2
    },
    7: {
        "question": "実行結果は？",
        "code": "lst = [1, 2, 3]\nlst.append(4)\nprint(len(lst))",
        "choices": ["3", "4", "5", "エラー"],
        "answer": 2
    },
    8: {
        "question": "実行結果は？",
        "code": "x = 'Python'\nprint(x.upper())",
        "choices": ["python", "PYTHON", "Python", "エラー"],
        "answer": 2
    },
    9: {
        "question": "実行結果は？",
        "code": "d = {'a': 1, 'b': 2}\nprint(d['a'])",
        "choices": ["1", "2", "a", "エラー"],
        "answer": 1
    },
    10: {
        "question": "実行結果は？",
        "code": "for i in range(3):\n    print(i)",
        "choices": ["0 1 2", "1 2 3", "0 1 2 3", "エラー"],
        "answer": 1
    },
    11: {
        "question": "実行結果は？",
        "code": "print(2 ** 3)",
        "choices": ["6", "8", "9", "エラー"],
        "answer": 2
    },
    12: {
        "question": "実行結果は？",
        "code": "s = 'hello world'\nprint(s.split())",
        "choices": ["['hello world']", "['hello', 'world']", "('hello', 'world')", "エラー"],
        "answer": 2
    },
    13: {
        "question": "実行結果は？",
        "code": "x = [3, 1, 2]\nx.sort()\nprint(x)",
        "choices": ["[3, 1, 2]", "[1, 2, 3]", "[3, 2, 1]", "エラー"],
        "answer": 2
    },
    14: {
        "question": "実行結果は？",
        "code": "print('abc' * 2)",
        "choices": ["abc2", "abcabc", "abc abc", "エラー"],
        "answer": 2
    },
    15: {
        "question": "実行結果は？",
        "code": "x = None\nprint(x is None)",
        "choices": ["False", "True", "None", "エラー"],
        "answer": 2
    },
    16: {
        "question": "実行結果は？",
        "code": "a = [1, 2, 3]\nprint(a[-1])",
        "choices": ["1", "2", "3", "エラー"],
        "answer": 3
    },
    17: {
        "question": "実行結果は？",
        "code": "def greet(name):\n    return 'Hello ' + name\nprint(greet('World'))",
        "choices": ["Hello", "Hello World", "World", "エラー"],
        "answer": 2
    },
    18: {
        "question": "実行結果は？",
        "code": "x = [0, '', None, 1]\nprint(bool(x[0]))",
        "choices": ["True", "False", "None", "エラー"],
        "answer": 2
    },
    19: {
        "question": "実行結果は？",
        "code": "s = 'Python3'\nprint(len(s))",
        "choices": ["6", "7", "8", "エラー"],
        "answer": 2
    },
    20: {
        "question": "実行結果は？",
        "code": "t = (1, 2, 3)\nprint(t[0])",
        "choices": ["1", "2", "3", "エラー"],
        "answer": 1
    },
    21: {
        "question": "実行結果は？",
        "code": "x = 5\nif x > 3:\n    print('big')\nelse:\n    print('small')",
        "choices": ["small", "big", "3", "エラー"],
        "answer": 2
    },
    22: {
        "question": "実行結果は？",
        "code": "lst = list(range(5))\nprint(lst)",
        "choices": ["[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4]", "(0, 1, 2, 3, 4)", "エラー"],
        "answer": 2
    },
    23: {
        "question": "実行結果は？",
        "code": "d = {}\nd['key'] = 'val'\nprint(len(d))",
        "choices": ["0", "1", "2", "エラー"],
        "answer": 2
    },
    24: {
        "question": "実行結果は？",
        "code": "x = 'hello'\nprint(x.replace('l', 'r'))",
        "choices": ["herro", "helo", "herlo", "エラー"],
        "answer": 1
    },
    25: {
        "question": "実行結果は？",
        "code": "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(len(a))",
        "choices": ["3", "4", "2", "エラー"],
        "answer": 2
    },
    26: {
        "question": "Pythonでコメントを書くのに使う記号は？",
        "code": "",
        "choices": ["//", "/*", "#", "--"],
        "answer": 3
    },
    27: {
        "question": "実行結果は？",
        "code": "print(int('42'))",
        "choices": ["'42'", "42", "42.0", "エラー"],
        "answer": 2
    },
    28: {
        "question": "実行結果は？",
        "code": "s = 'abcdef'\nprint(s[2:4])",
        "choices": ["ab", "cd", "bc", "de"],
        "answer": 2
    },
    29: {
        "question": "実行結果は？",
        "code": "x = [1, 2, 3, 4, 5]\nprint(sum(x))",
        "choices": ["12", "15", "10", "エラー"],
        "answer": 2
    },
    30: {
        "question": "実行結果は？",
        "code": "print(max(3, 1, 4, 1, 5))",
        "choices": ["4", "3", "5", "エラー"],
        "answer": 3
    },
    31: {
        "question": "Pythonのリストで要素を末尾から削除するメソッドは？",
        "code": "",
        "choices": ["remove()", "delete()", "pop()", "cut()"],
        "answer": 3
    },
    32: {
        "question": "実行結果は？",
        "code": "x = 3\nwhile x > 0:\n    x -= 1\nprint(x)",
        "choices": ["1", "0", "-1", "エラー"],
        "answer": 2
    },
    33: {
        "question": "実行結果は？",
        "code": "print(str(100))",
        "choices": ["100", "'100'", "エラー", "int"],
        "answer": 1
    },
    34: {
        "question": "実行結果は？",
        "code": "lst = [1, 2, 3]\nprint(lst[1:3])",
        "choices": ["[1, 2]", "[2, 3]", "[1, 2, 3]", "エラー"],
        "answer": 2
    },
    35: {
        "question": "Pythonで等しくないことを確認する演算子は？",
        "code": "",
        "choices": ["!=", "<>", "=/=", "=/"],
        "answer": 1
    },
    36: {
        "question": "実行結果は？",
        "code": "x = [1, 2, 3]\nprint(x.index(2))",
        "choices": ["0", "1", "2", "エラー"],
        "answer": 2
    },
    37: {
        "question": "実行結果は？",
        "code": "print('  hello  '.strip())",
        "choices": ["'  hello  '", "'hello'", "hello", "エラー"],
        "answer": 3
    },
    38: {
        "question": "実行結果は？",
        "code": "a = {1, 2, 3}\nb = {2, 3, 4}\nprint(len(a & b))",
        "choices": ["1", "2", "3", "エラー"],
        "answer": 2
    },
    39: {
        "question": "Pythonで関数を定義するキーワードは？",
        "code": "",
        "choices": ["function", "def", "func", "define"],
        "answer": 2
    },
    40: {
        "question": "実行結果は？",
        "code": "x = [1, 2, 3]\nprint(x[::-1])",
        "choices": ["[1, 2, 3]", "[3, 2, 1]", "[3]", "エラー"],
        "answer": 2
    },
}
