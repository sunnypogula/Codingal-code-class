def classify_event(is_dependent, is_mutually_exclusive):
    event_type = "Dependent" if is_dependent else "Independent"
    exclusivity = "Mutually Exclusive" if is_mutually_exclusive else "Not Mutually Exclusive"
    
    return f"{event_type}, {exclusivity}"

print(classify_event(is_dependent=True, is_mutually_exclusive=True))


print(classify_event(is_dependent=False, is_mutually_exclusive=False))