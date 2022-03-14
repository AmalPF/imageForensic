

def model_result_border_label(self):    # These are bootstrap label colors
    print("bootstrap setter function called")
    if self > 50:
        return "card border-left-danger shadow h-100 py-2"     # red
    else:
        return "card border-left-success shadow h-100 py-2"    # green

def model_result_text_label(self):
    print("bootstrap setter function called")
    if self > 50:
        return ""