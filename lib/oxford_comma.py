def oxford_comma(items):
    pass
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{item[0]} and {item[1]}"
    else:
        return f"{', '.join(items[:-1])}, and {items[-1]}"
    
