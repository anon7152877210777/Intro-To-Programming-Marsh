def greeting(user_info):
    parts = user_info.split()
    name = parts[0]
    hobby = parts[-1]
    return f"Hello, {name}! I also enjoy {hobby}!"
