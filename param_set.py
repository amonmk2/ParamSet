#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog

import json
import pprint
import subprocess


def run_process(cmd):
    try:
        res = subprocess.run([cmd], stdout=subprocess.PIPE)
    except:
        print("Error.")


def create_button(root, label, btnlabel, cmd):
    lf = tk.LabelFrame(root, text=label)
    lf.pack(padx=5, pady=5, fill='x', side="top")
    b = tk.Button(lf, text=btnlabel, command=lambda: run_process(cmd))
    b.pack(padx=5, fill='x', side="left", expand=1)


def create_label(root, label):
    l = tk.Label(root, text=label, anchor='c')
    # l = tk.Label(root,text=label,background='#ffffff',anchor='c',bd=4,height=0,font=16)
    l.pack(fill='x', side='top')


def fileselect(e):
    filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                            filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    e.delete(0, 'end')
    e.insert(tk.END, filename)


def create_entry_filedialog(root, label, defvalue, state):
    lf = tk.LabelFrame(root, text=label)
# lf = tk.LabelFrame(root,text=label, width=80 , height=60)
    lf.pack(padx=5, pady=5, fill='x', side="top")
    e = tk.Entry(lf)
    e.pack(padx=5, fill='x', side="left", expand=1)
    fs = tk.Button(lf, text="...", command=lambda: fileselect(e))
    fs.pack(padx=5, fill='x', side="right")
    e.configure(state='normal')
    e.delete(0, 'end')
    e.insert('end', defvalue)
    if state != 'normal':
        e.configure(state=state)
    return e


def create_entry(root, label, defvalue, state):
    lf = tk.LabelFrame(root, text=label)
    lf.pack(padx=5, pady=5, fill='x', side="top")
    e = tk.Entry(lf, state=state)
    e.configure(state='normal')
    e.delete(0, 'end')
    e.insert('end', defvalue)
    if state != 'normal':
        e.configure(state=state)
    e.pack(padx=5, fill='x')
    return e


def create_spinbox(root, label, list1, defvalue, state):
    lf = tk.LabelFrame(root, text=label)
    lf.pack(padx=5, pady=5, fill='x', side="top")
    var = tk.StringVar()
    spb = tk.Spinbox(lf, values=list1, textvariable=var, state=state)
    spb.pack(padx=5, fill='x')
    var.set(defvalue)
    return spb


def create_listbox(root, label, list1, defvalue, state):
    lf = tk.LabelFrame(root, text=label)
    lf.pack(padx=5, pady=5, fill='x', side="top")
    scrbar = tk.Scrollbar(lf)
    scrbar.pack(side='right', fill='y')
    lstb = tk.Listbox(lf, height=5, selectmode="single",
                      yscrollcommand=scrbar.set, exportselection=0)
    lstb.configure(state='normal')
    for line in list1:
        lstb.insert('end', str(line))
    lstb.select_clear(defvalue)
    lstb.select_set(defvalue)
    lstb.see(defvalue)
    if state != 'normal':
        lstb.configure(state=state)
    lstb.pack(padx=5, fill='x')
    scrbar.config(command=lstb.yview)
    return lstb


def create_checkbutton(root, label, param, defvalue, state):
    lf = tk.LabelFrame(root, text=label)
    lf.pack(padx=5, pady=5, fill='x', side="top")
    opt = tk.BooleanVar()
    chkb = tk.Checkbutton(lf, text=str(param), variable=opt)
    chkb.pack(fill='x', side="left")
    opt.set(defvalue)
    chkb.configure(state=state)
    return opt


def create_radiobutton(root, label, list1, defvalue, state1):
    lf = tk.LabelFrame(root, text=label)
    lf.pack(padx=5, pady=5, fill='x', side="top")
    opt = tk.IntVar()
    cnt = 0
    for line in list1:
        b = tk.Radiobutton(lf, text=line, variable=opt,
                           value=cnt, state=state1)
        b.pack(fill='x', side="left")
        cnt = cnt+1
    opt.set(defvalue)
    return opt


def dump_param():
    for p in param_print_code.keys():
        exec(param_print_code[p])


def dump_json():
    for i in param_json:
        if i == "//":
            continue
        for j in param_json[i]:
            param = j
            method = param_json[i][j]["method"]
            if method == "create_entry_filedialog":
                param_json[i][j]["defvalue"] = eval(param + ".get()")
            elif method == "create_entry":
                param_json[i][j]["defvalue"] = eval(param + ".get()")
            elif method == "create_spinbox":
                param_json[i][j]["defvalue"] = eval(param + ".get()")
            elif method == "create_listbox":
                param_json[i][j]["defvalue"] = eval(
                    param + ".curselection()[0]")
            elif method == "create_checkbutton":
                param_json[i][j]["defvalue"] = eval(param + ".get()")
            elif method == "create_radiobutton":
                param_json[i][j]["defvalue"] = eval(param + ".get()")
            else:
                True
    f2 = open("param_save.json", 'w')
    json.dump(param_json, f2, indent=2)
    # print(json.dumps(param_json,indent=2))


def check_param():
    rtn = 0
    msg = ""
    for i in param_json:
        if i == "//":
            continue
        for j in param_json[i]:
            param = j
            method = param_json[i][j]["method"]
            if method == "create_entry_filedialog" or method == "create_entry":
                if param_json[i][j]["defvalue"] == "":
                    msg += '"' + param + '"' + " is not defined.\n"
            else:
                True
    if msg != "":
        tkMessageBox.showerror('Error', msg)
        rtn = 1
    return rtn


def gen_print_create_entry_filedialog(param):
    return 'print(\'' + param + ' = \\"\' + ' + param + '.get() + \'\\"\')'


def gen_print_create_entry(param):
    return 'print(\'' + param + ' = \\"\' + ' + param + '.get() + \'\\"\')'


def gen_print_create_spinbox(param):
    return 'print(\'' + param + ' = \\"\' + ' + param + '.get() + \'\\"\')'


def gen_print_create_listbox(param):
    return 'print(\'' + param + ' = \\"\' + ' + param + '.get(' + param + '.curselection()) + \'\\"\')'


def gen_print_create_checkbutton(param):
    return 'print(\'' + param + ' = \\"' + param_hash[param]["bottuon_label"] + '\\"\') if ' + param + '.get()==True else print(\'' + param + '= \\"\\"\')'


def gen_print_create_radiobutton(param):
    return 'print(\'' + param + ' = \\"\' + [' + ",".join(list(map(lambda item: '"'+str(item)+'"', param_hash[param]["list"]))) + '][' + param + '.get()] + \'\\"\')'


def gen_print_create_label(param):
    return 'print(\'## ' + param + "  " + param_hash[param]["label"] + '\')'


def gen_print_create_button(param):
    return 'print(\'##' + param + "  " + param_hash[param]["label"] + param_hash[param]["btnlabel"] + param_hash[param]["cmd"] + '\')'


def okflow():
    # print_param()
    dump_param()
    dump_json()
    if check_param() == 0:
        root.destroy

# entry insert


def insert(event):
    for prm in dont_modify:
        exec(prm+".configure(state='normal')")

# entry lock


def lock(event):
    for prm in dont_modify:
        exec(prm+".configure(state='readonly')")


def gen_method_base(param, method, root, label):
    return param + " = " + method + "(" + root + "," + '"' + label + '"'


def gen_method_create_entry_filedialog(param, method, root, label, defvalue, state):
    code = gen_method_base(param, method, root, label) + "," + \
        '"' + defvalue + '"' + "," + '"' + state + '"' + ")"
    return code


def gen_method_create_entry(param, method, root, label, defvalue, state):
    code = gen_method_base(param, method, root, label) + "," + \
        '"' + defvalue + '"' + "," + '"' + state + '"' + ")"
    return code


def gen_method_create_spinbox(param, method, root, label, list, defvalue, state):
    code = gen_method_base(param, method, root, label) + "," + "[" + ",".join(list(map(lambda item: '"'+str(
        item)+'"', paramref["list"]))) + "]" + "," + '"' + defvalue + '"' + "," + '"' + state + '"' + ")"
    return code


def gen_method_create_listbox(param, method, root, label, list, defvalue, state):
    code = gen_method_base(param, method, root, label) + "," + "[" + ",".join(list(map(
        lambda item: '"'+str(item)+'"', paramref["list"]))) + "]" + "," + defvalue + "," + '"' + state + '"' + ")"
    return code


def gen_method_create_checkbutton(param, method, root, label, bottuon_label, defvalue, state):
    code = gen_method_base(param, method, root, label) + "," + '"' + bottuon_label + \
        '"' + "," + '"' + defvalue + '"' + "," + '"' + state + '"' + ")"
    return code


def gen_method_create_radiobutton(param, method, root, label, list, defvalue, state):
    code = gen_method_base(param, method, root, label) + "," + "[" + ",".join(list(map(lambda item: '"'+str(
        item)+'"', paramref["list"]))) + "]" + "," + '"' + defvalue + '"' + "," + '"' + state + '"' + ")"
    return code


def gen_method_create_label(param, method, root, label):
    code = gen_method_base(param, method, root, label) + ")"
    return code


def gen_method_create_button(param, method, root, label, btnlabel, cmd):
    code = gen_method_base(param, method, root, label) + "," + '"' + \
        paramref["btnlabel"] + '"' + "," + '"' + paramref["cmd"] + '"' + ")"
    return code


root = tk.Tk()
root.title("parameter")
root.config()

scrbar = tk.Scrollbar(root)
scrbar.config()
scrbar.pack(side='right', fill='y')

#
# json -> param_hash
#
param_hash = dict()
param_print_code = dict()
with open('param.json') as f:
    param_json = json.load(f)
# pprint.pprint(param_json, width=40)
for i in sorted(param_json.keys()):
    if i == "//":
        continue
    for j in param_json[i].keys():
        param = j
        param_hash[j] = dict.copy(param_json[i][j])
        method = param_hash[j]["method"]
        paramref = param_hash[j]
     #   if method != "create_button" :
        param_print_code[param] = eval("gen_print_"+method+"(param)")
        # print("gen_print_"+method+"(param)")
        # print(param_print_code[param])
        if method == "create_entry_filedialog":
            exec(gen_method_create_entry_filedialog(param, method, "root", str(
                paramref["label"]), str(paramref["defvalue"]), str(paramref["state"])))
        elif method == "create_entry":
            exec(gen_method_create_entry(param, method, "root", str(
                paramref["label"]), str(paramref["defvalue"]), str(paramref["state"])))
        elif method == "create_spinbox":
            exec(gen_method_create_spinbox(param, method, "root", str(
                paramref["label"]), list, str(paramref["defvalue"]), str(paramref["state"])))
            # exec( gen_method_create_spinbox(param , method , "root" , str(paramref["label"]), list , str(paramref["defvalue"])) )
        elif method == "create_listbox":
            exec(gen_method_create_listbox(param, method, "root", str(
                paramref["label"]), list, str(paramref["defvalue"]), str(paramref["state"])))
        elif method == "create_checkbutton":
            exec(gen_method_create_checkbutton(param, method, "root", str(paramref["label"]), str(
                paramref["bottuon_label"]), str(paramref["defvalue"]), str(paramref["state"])))
        elif method == "create_radiobutton":
            exec(gen_method_create_radiobutton(param, method, "root", str(
                paramref["label"]), list, str(paramref["defvalue"]), str(paramref["state"])))
        elif method == "create_label":
            exec(gen_method_create_label(
                param, method, "root", str(paramref["label"])))
        elif method == "create_button":
            exec(gen_method_create_button(param, method, "root", str(
                paramref["label"]), str(paramref["btnlabel"]), str(paramref["cmd"])))
        else:
            print("#NO Method : " + method)


#
# lock entry
#
dont_modify = []
for p in param_hash.keys():
    if (param_hash[p]["method"] == "create_entry" or param_hash[p]["method"] == "create_entry_filedialog"):
        if (param_hash[p]["state"] == "disabled" or param_hash[p]["state"] == "readonly"):
            dont_modify.append(p)

root.bind('<Shift-Button-3>', insert)  # insert text
root.bind('<Escape>', lock)  # lock text

#
# OK / CANCEL
#
ok_cancel = tk.Frame(root)
ok_cancel.config()
ok_cancel.pack(side="bottom")

ok = tk.Button(ok_cancel, text="  OK  ", command=okflow)
ok.pack(side="left")

cancel = tk.Button(ok_cancel, text="CANCEL", command=root.destroy)
cancel.pack(side="right")


root.mainloop()
