import http.client
import re
from tkinter import *
def cut(info):
    Count = re.search('rank', info)
    end_Count = Count.end()
    info = info[end_Count:]
    return info
def get_info():
    conn.request("GET", "/api/npm-covid-data/africa", headers=headers)
    res = conn.getresponse()
    data = res.read()
    temp = data.decode("utf-8")
    return temp
def search(key_word, info):
    result = re.search(key_word, info)
    start = result.start()
    data = ''
    st = False
    i = 0
    while True:
        if info[i+start] == ',':
                return data
        if info[i+start] == ':':
            st = True
        elif st == True:
            if info[i+start] != '"':
                data += info[i+start]
        i += 1
def get_Count_info(info):
    Count = 'Country: '
    Count += search('Country', info)
    tc = 'Total Cases: '
    tc += search('TotalCases', info)
    td = 'Total Death: '
    td += search('TotalDeath', info)
    tt = 'Total Tests: '
    tt += search('TotalTests', info)
    result = Count + '\n' + tc + '\n' + td + '\n' + tt
    return result
def search_1_Count(info):
    Count = ent.get()
    info = cut(info)
    while True:
        result = search('Country', info)
        if Count == result:
            text = get_Count_info(info)
            search_Count['text'] = text
            break
        else:
            try:
                info = cut(info)
            except:
                search_Count['text'] = "error ! "
                break
def top_5(info):
    info = cut(info)
    text = get_Count_info(info)
    Count1['text'] = text
    info = cut(info)
    text = get_Count_info(info)
    Count2['text'] = text
    info = cut(info)
    text = get_Count_info(info)
    Count3['text'] = text
    info = cut(info)
    text = get_Count_info(info)
    Count4['text'] = text
    info = cut(info)
    text = get_Count_info(info)
    Count5['text'] = text
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "3254deee13mshe0f7ba29cf082dep1e663bjsnf9aa6df84466",
    'x-rapidapi-host':"vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
root = Tk()
root.title("Covid-19 in Africa")
root.geometry("400x600")
root.configure(bg = 'black')
root.resizable(False, False)
lab_top = Label(root, text="Top 5:",background="black", foreground="white", font="Arial 20")
lab_top.place(x = 0, y = 10)
lab_search = Label(root, text="Search",background="black", foreground="white", font="Arial 20")
lab_search.place(x = 200, y = 10)
Count1 = Label(root, text="1 country",background="black", foreground="white", font="Arial 14")
Count1.place(x =0, y = 100)
Count2 = Label(root, text="2 country",background="black", foreground="white", font="Arial 14")
Count2.place(x = 0, y = 200)
Count3 = Label(root, text="3 country",background="black", foreground="white", font="Arial 14")
Count3.place(x = 0, y = 300)
Count4 = Label(root, text="4 country",background="black", foreground="white", font="Arial 14")
Count4.place(x = 0, y = 400)
Count5 = Label(root, text="5 country",background="black", foreground="white", font="Arial 14")
Count5.place(x = 0, y = 500)
ent = Entry(root, width=20,bd=1)
ent.place(x = 200, y = 100)
but = Button(root, text='GO', width=3, height=1, bd=1, command = lambda: search_1_Count(info)).place(x = 300, y = 100)
search_Count = Label(root, text="",background="black", foreground="white", font="Arial 14")
search_Count.place(x = 200, y = 200)
info = get_info()
top_5(info)
root.mainloop()
