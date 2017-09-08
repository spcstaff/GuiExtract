import tkinter


class Input:

    def __init__(self):
        self.frame = tkinter.Frame
        self.state = tkinter.Entry(Input.frame)
        self.county = tkinter.Entry(Input.frame)

    def get_state(self):
        return self.state.get()

    def get_county(self):
        return self.county.get()