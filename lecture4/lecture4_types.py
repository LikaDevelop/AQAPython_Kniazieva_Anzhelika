def print_data(data: str) -> None:
    if type(data) is str:
        print(data)
    else: raise TypeError(f'Incorrect data type {type(data)}, should be string!')

print_data('cedwdui dnedn fheuowh')
print_data(12)