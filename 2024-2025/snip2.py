from importlib.machinery import SourceFileLoader

foo = SourceFileLoader("snippet", "Z:/scripts/technical-art-class-scripts/2024-2025/snip2.py").load_module()
foo.MyClass()
snippet.placeruler()