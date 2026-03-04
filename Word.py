class Word:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def display_info(self):
        print(f"The Front: {self.front} ---------- The Back: {self.back}")