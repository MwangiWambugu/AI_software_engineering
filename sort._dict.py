# manual implementation of sorting a dictionary by a unique key
def sort(d):
    numeric_items = {k: v for k, v in d.items() if isinstance(k, (int, float))}
    return dict(sorted(numeric_items.items()))


# copilot implementation of sorting a dictionary by a unique key
def sort_by_key(d):
    return dict(sorted(d.items()))