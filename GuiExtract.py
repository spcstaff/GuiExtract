import pandas as pd
import tkinter as tk
import model

#root is the frame
root = tk.Tk()

#generate the window and specify text
root.geometry("800x600+10+10")
my_label = tk.Label(root, text="Extract data")
my_label.pack()

# function to insert selection
def insert_selection():
    input_list.append(model.Input)

button2 = tk.Button(root, text="add selection", command=insert_selection).pack(side=tk.BOTTOM)

input_list = [model.Input]


# draw the table
def draw():
    for cur in input_list:
        cur.frame.pack(root)
        cur.county.pack(cur.frame)
        cur.state.pack(cur.frame)


#extract the file for a specific county and state
def extract_action():
    extract = pd.read_csv("alldata.csv", encoding='latin-1', header=0)
    for cur in input_list:
        state = cur.state.get()
        county = cur.county.get()
        query = 'STNAME == ["%s"] & CTYNAME == ["%s"]' % (state, county)
        print(query)
        target = extract.query('%s' % query)
        target.to_csv(path_or_buf="test4.csv")
        cur.state.delete(0, 'end')
        cur.county.delete(0, 'end')




input_state = tk.Entry(root)
input_county = tk.Entry(root)
input_state.insert(0, "input state")
input_county.insert(0, "input county")
input_state.pack()
input_county.pack()

button1 = tk.Button(root, text="extract", command=extract_action).pack(side=tk.BOTTOM)

root.mainloop()





