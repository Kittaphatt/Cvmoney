import tkinter as tk
import tkinter.ttk as tkk
from forex_python.converter import CurrencyRates
import datetime
from forex_python.bitcoin import BtcConverter


ValuesList = []

date_list = []
rates1_list = []
rates2_list = []
rates3_list = []

count = 0

Large_Font = ("Verdana", 30)
Large_Font11 = ("consolas ", 11)
Large_Font1 = ("consolas ", 10)

countries1 = {'AUD': "ดอลลาร์ออสเตรเลีย", 'BGN': "เลฟบัลแกเรีย", 'BRL': "เรียลบราซิล",
              'CAD': "ดอลลาร์แคนาดา", 'CHF': "ฟรังก์สวิส",
              'CNY': "หยวนจีน", 'CZK': "โครูนาสาธารณรัฐเช็ก", 'DKK': "โครนเดนมาร์ก",
              'EUR': "ยูโร", 'GBP': "ปอนด์สเตอร์ลิงสหราชอาณาจักร",
              'HKD': "ดอลลาร์ฮ่องกง", 'HRK': "คูนาโครเอเชีย", 'HUF': "ฟอรินต์ฮังการี",
              'IDR': "รูเปียห์อินโดนีเซีย", 'ILS': "นิวเชเกลอิสราเอล",
              'INR': "รูปีอินเดีย", 'ISK': "โครนาไอซ์แลนด์", 'JPY': "เยนญี่ปุ่น", 'KRW': "วอนเกาหลีใต้",
              'MXN': "เปโซเม็กซิโก",
              'MYR': "ริงกิตมาเลเซีย", 'NOK': "โครนนอร์เวย์", 'NZD': "ดอลลาร์นิวซีแลนด์",
              'PHP': "เปโซฟิลิปปินส์", 'PLN': "ซลอตีโปแลนด์",
              'RON': "ลิวโรมาเนีย", 'RUB': "รูเบิลรัสเซีย", 'SEK': "โครนาสวีเดน",
              'SGD': "ดอลลาร์สิงคโปร์", 'THB': "บาทไทย",
              'TRY': "ลีราตุรกี", 'USD': "ดอลลาร์สหรัฐ", 'ZAR': "แรนด์แอฟริกาใต้"}

countries2 = {'AUD': ["ดอลลาร์ออสเตรเลีย", "ออสเตรเลีย"], 'BGN': ["เลฟบัลแกเรีย", "บัลแกเรีย"],
              'BRL': ["เรียลบราซิล", "บราซิล"], 'CAD': ["ดอลลาร์แคนาดา", "แคนาดา"],
              'CHF': ["ฟรังก์สวิส", "สวิตเซอร์แลนด์"], 'CNY': ["หยวนจีน", "จีน"],
              'CZK': ["โครูนาสาธารณรัฐเช็ก", "เช็กเกีย"], 'DKK': ["โครนเดนมาร์ก", "เดนมาร์ก"],
              'EUR': ["ยูโร", "กลุ่มสหภาพยุโรป"], 'GBP': ["ปอนด์สเตอร์ลิงสหราชอาณาจักร", "อังกฤษ (สหราชอาณาจักร)"],
              'HKD': ["ดอลลาร์ฮ่องกง", "ฮ่องกง"], 'HRK': ["คูนาโครเอเชีย", "โครเอเชีย"],
              'HUF': ["ฟอรินต์ฮังการี", "ฮังการี"], 'IDR': ["รูเปียห์อินโดนีเซีย", "อินโดนีเซีย"],
              'ILS': ["นิวเชเกลอิสราเอล", "อิสราเอล"], 'INR': ["รูปีอินเดีย", "อินเดีย"],
              'ISK': ["โครนาไอซ์แลนด์", "ไอซ์แลนด์"], 'JPY': ["เยนญี่ปุ่น", "ญี่ปุ่น"],
              'KRW': ["วอนเกาหลีใต้", "เกาหลีใต้"], 'MXN': ["เปโซเม็กซิโก", "เม็กซิโก"],
              'MYR': ["ริงกิตมาเลเซีย", "มาเลเซีย"], 'NOK': ["โครนนอร์เวย์", "นอร์เวย์"],
              'NZD': ["ดอลลาร์นิวซีแลนด์", "นิวซีแลนด์"], 'PHP': ["เปโซฟิลิปปินส์", "ฟิลิปปินส์"],
              'PLN': ["ซลอตีโปแลนด์", "โปแลนด์"], 'RON': ["ลิวโรมาเนีย", "โรมาเนีย"],
              'RUB': ["รูเบิลรัสเซีย", "รัสเซีย"], 'SEK': ["โครนาสวีเดน", "สวีเดน"],
              'SGD': ["ดอลลาร์สิงคโปร์", "สิงคโปร์"], 'THB': ["บาทไทย", "ไทย"],
              'TRY': ["ลีราตุรกี", "ตุรกี"], 'USD': ["ดอลลาร์สหรัฐ", "สหรัฐอเมริกา"],
              'ZAR': ["แรนด์แอฟริกาใต้", "แอฟริกาใต้"]}


class MyPage(tk.Tk):  # สำหรับไว้เปลี่ยนหน้า กำหนดขนาดต่าง ๆ
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "CV Money")
        container = tk.Frame(self)
        self.geometry("1000x700")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weigh=1)
        container.grid_columnconfigure(0, weigh=1)

        self.frames = {}
        for F in (StartPage, Detail, ShowMoney, Graph, MoneyInformation):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):  # คลาสที่ใช้แสดง "หน้าแรก" ของโปรแกรม
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='dark Orchid4')

        label = tk.Label(self, text="หน้าแรก", font=Large_Font, bg='dark Orchid4', fg='yellow', width=50)
        label.pack(pady=20, padx=10)

        button1 = tk.Button(self, text="แปลงสกุลเงิน", font=24,
                           command=lambda: controller.show_frame(ShowMoney),
                           fg="white", cursor='heart', pady=15, width=50, padx=20, bg="dark Orchid3")
        button1.pack(anchor='center', pady=5)  # กำหนดทิศของปุ่ม

        button2 = tk.Button(self, text="อัตราแลกเปลี่ยนเงิน", font=24,
                           command=lambda: controller.show_frame(Graph),
                            fg="white", cursor='heart', pady=15, width=50, padx=20, bg="dark Orchid3")
        button2.pack(anchor='center', pady=5)

        button3 = tk.Button(self, text="รายละเอียดสกุลเงิน", font=24,
                               command=lambda: controller.show_frame(Detail),
                               fg="white", cursor='heart', pady=15, width=50, padx=20, bg="dark Orchid3")
        button3.pack(anchor='center', pady=5)

        button4 = tk.Button(self, text="ออกจากโปรแกรม", font=24, command=self.quit,
                      fg="white", cursor='heart', pady=15, width=50, padx=20, bg="dark Orchid3")
        button4.pack(anchor='center', pady=5)


class Detail(tk.Frame):  # แสดงเพื่อแสดงรายละเอียดของสกุลเงิน
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="dark Orchid1")
        label = tk.Label(self, text="รายละเอียดสกุลเงิน", width=100, font=Large_Font,
                         fg='white', bg='dark Orchid4')
        label.pack(pady=5, padx=10)

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=1)

        my_canvas = tk.Canvas(frame)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        my_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = tk.Frame(my_canvas)

        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        for i, k in countries2.items():
            text_label2 = tk.Label(second_frame, text=f'ประเทศ{k[1]} ตัวย่อ {i} หน่วยเงินคือ {k[0]}',
                                   width=170, font=Large_Font11)
            text_label2.pack()

        button1 = tk.Button(self, text="หน้าแรก", font=15, width=50,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=5, padx=5)


class ShowMoney(tk.Frame):  # คลาสสำหรับการคำนวณหรือแปลงสกุลเงิน
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='dark Orchid1')
        label = tk.Label(self, text="คำนวณอัตราแลกเปลี่ยนเงินตรา", font=Large_Font, width=100,
                         fg='white', bg='dark Orchid4')
        label.pack(pady=20, padx=10)

        def rate():  # สำหรับดึงข้อมูลสกุลเงิน จาก forex_python.converter
            c = CurrencyRates()
            j = c.get_rates('USD')
            return j

        rates = rate()

        def show_money1():  # ส่วนของการคำนวณแปลงข้อมูลสกุลเงิน
            try:
                if om1.get() in rates and om2.get() in rates:  # ถ้า text(Key) มีใน ดิกชันนารี(Key)
                    ValuesList.append(countries1[om2.get()])  # ดึงข้อมูลจากดิกชันนารี ไปเก็บไว้ใน ValuesList
                    for i in ValuesList:  # เอาข้อมูลออกจาก List
                        x = float(rates[om2.get()] / rates[om1.get()])
                        total = float(entry_1.get()) * x
                        output1.configure(text="{:,.3f} {}".format(total, i))

            except:
                return output1.configure(text='กรุณาใส่จำนวนเงิน', fg='red')

        def clear():  # สำหรับเซ็ตเป็นค่าเริ่มต้น
            om1.set("กรุณาเลือกสกุลเงิน")
            om2.set("กรุณาเลือกสกุลเงิน")
            entry_1.delete(0, tk.END)

        KeysList = []

        for i, k in countries1.items():
            KeysList.append(i)
        om1 = tkk.Combobox(self, values=KeysList, font=Large_Font1, state='readonly', width=60)
        om1.pack(pady=10)
        om1.set('กรุณาเลือกสกุลเงิน')

        text_label = tk.Label(self, text="แปลงเป็น", bg="purple", font=20, fg="yellow", width=20)
        text_label.pack()

        om2 = tkk.Combobox(self, values=KeysList, font=Large_Font1, state='readonly', width=60)
        om2.pack(pady=10)
        om2.set('กรุณาเลือกสกุลเงิน')

        entry_1 = tk.Entry(self, width=60, font=Large_Font1)
        entry_1.pack(pady=5)

        go_button1 = tk.Button(self, text='แปลงสกุลเงิน', width=30, command=show_money1, font=Large_Font1,
                               fg='white', bg='dark Orchid4')
        go_button1.pack(pady=10)

        output1 = tk.Label(self, bg='light goldenrod', fg='red', width=50, font=Large_Font1)
        output1.pack(pady=5)

        reset = tk.Button(self, text="รีเช็ต", bg='gray85', command=clear, width=50, font=Large_Font1)
        reset.pack(pady=5)

        button1 = tk.Button(self, text="หน้าแรก", width=50, font=15,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)


class Graph(tk.Frame):  # คลาสสำหรับการแสดงกราฟ เพื่อดูแนวโน้มของค่าเงิน
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='dark Orchid1')

        label = tk.Label(self, text="กราฟ", font=Large_Font, width=100,
                         fg='white', bg='dark Orchid4')
        label.pack(pady=5, padx=10)

        button1 = tk.Button(self, text="หน้าแรก", width=50, font=15,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=5, padx=5)

        button2 = tk.Button(self, text="ข้อมูลราคาย้อนหลัง", width=50, font=15,
                            command=lambda: controller.show_frame(MoneyInformation))
        button2.pack(pady=5, padx=5)

        text_label = tk.Label(self, text='กรุณาเลือกสกุลเงิน', bg='purple', fg='yellow', font=10, width=20)
        text_label.pack(pady=5)

        def select():  # ส่วนนี้สำหรับดึงข้อมูลย้อนหลังจาก forex_python.bitcoin
            try:

                days = om2.get()
                num = om1.get()
                b = BtcConverter()
                end_date = datetime.datetime.today()
                start_date2 = datetime.datetime.today() - datetime.timedelta(days=int(f'{days}'))
                T = b.get_previous_price_list(f'{num}', start_date2, end_date)
                B = b.get_previous_price_list('USD', start_date2, end_date)

                for k, v in T.items():
                    date_list.append(k)
                    rates1_list.append(v)
                for k, v in B.items():
                    rates2_list.append(v)

                def resets():  # สำหรับลบข้อมูล
                    global count
                    count += 1
                    if count % 2 == 0:
                        canvas1.pack_forget()
                        toolbar.pack_forget()
                        reset.pack_forget()
                    else:
                        canvas1.pack_forget()
                        toolbar.pack_forget()
                        reset.pack_forget()

                def show_money1():  # ส่วนการคำนวณเพื่อเอาข้อมูลไปใช้
                    for i, k in enumerate(rates1_list):
                        x = float(rates1_list[i] / rates2_list[i])
                        total = float(1 * x)
                        total2 = float("{:,.3f}".format(total))
                        rates3_list.append(total2)
                    return rates3_list

                rates = show_money1()

                from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
                from matplotlib.figure import Figure

                f = Figure(figsize=(1, 1), dpi=70)  # ปรับขนาดให้พอดีจอ และความเข้มของเส้น
                a = f.add_subplot(111)  # ขนาดของกราฟที่แสดง
                a.plot(date_list, rates, "ro")
                a.plot(date_list, rates)

                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                toolbar = NavigationToolbar2Tk(canvas, self)
                toolbar.update()

                canvas1 = canvas._tkcanvas
                canvas1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                reset = tk.Button(self, text="ลบข้อมูล", width=50, font=Large_Font1, command=resets)
                reset.pack()

                # สำหรับลบข้อมูลที่อยู่ใน list ทั้งหมด
                rates.clear()
                date_list.clear()
                rates1_list.clear()
                rates2_list.clear()
                rates3_list.clear()
                ###
            except:
                return 0

        KeysList = []

        for i, k in countries1.items():
            KeysList.append(i)
        om1 = tkk.Combobox(self, values=KeysList, font=Large_Font1, state='readonly', width=60)
        om1.pack(pady=5)
        om1.set('กรุณาเลือกสกุลเงิน')

        day31 = []
        for i in range(1, 366):
            day31.append(i)
        om2 = tkk.Combobox(self, values=day31, font=Large_Font1, state='readonly', width=60)
        om2.pack(pady=5)
        om2.set('กรุณาเลือกเพื่อดูข้อมูลย้อนหลัง')

        btn = tk.Button(self, text='ดูกราฟ', fg='white', bg='dark Orchid4',
                        command=select, width=25, font=Large_Font1)
        btn.pack(pady=5)


class MoneyInformation(tk.Frame):  # คลาสสำหรับแสดงข้อมูลสกุลเงินย้อนหลัง
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='dark Orchid1')

        label = tk.Label(self, text="ข้อมูลราคาย้อนหลัง", font=Large_Font, width=100,
                         fg='white', bg='dark Orchid4')
        label.pack(pady=5, padx=10)

        button1 = tk.Button(self, text="หน้าแรก", width=50, font=15,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=5, padx=5)

        button2 = tk.Button(self, text="กราฟ", width=50, font=15,
                            command=lambda: controller.show_frame(Graph))
        button2.pack(pady=5, padx=5)

        text_label = tk.Label(self, text='กรุณาเลือกสกุลเงิน', bg="purple", fg='yellow', font=10, width=20)
        text_label.pack(pady=5)

        def select():  # ส่วนนี้สำหรับดึงข้อมูลย้อนหลังจาก forex_python.bitcoin
            try:
                days = om2.get()
                num = om1.get()
                b = BtcConverter()
                end_date = datetime.datetime.today()
                start_date2 = datetime.datetime.today() - datetime.timedelta(days=int(f'{days}'))
                T = b.get_previous_price_list(f'{num}', start_date2, end_date)
                B = b.get_previous_price_list('USD', start_date2, end_date)

                for k, v in T.items():
                    date_list.append(k)
                    rates1_list.append(v)
                for k, v in B.items():
                    rates2_list.append(v)

                def resets():  # สำหรับลบข้อมูล
                    global count
                    count += 1
                    if count % 2 == 0:
                        output1.pack_forget()
                        frame.pack_forget()
                        my_canvas.pack_forget()
                        my_scrollbar.pack_forget()
                        reset.pack_forget()
                    else:
                        output1.pack_forget()
                        frame.pack_forget()
                        my_canvas.pack_forget()
                        my_scrollbar.pack_forget()
                        reset.pack_forget()

                def show_money1():  # ส่วนการคำนวณ เพื่อแปลงข้อมูล จาก บิตคอย เป็นสกุลเงินต่าง ๆ
                    for i, k in enumerate(rates1_list):
                        x = float(rates1_list[i] / rates2_list[i])
                        total = float(1 * x)
                        total2 = float("{:,.3f}".format(total))
                        rates3_list.append(total2)
                    return rates3_list

                rates = show_money1()

                date_rates = []
                for i, k in enumerate(date_list):
                    date_rates.append([date_list[i], rates[i]])
                dict_rate = {i[0]: i[1] for i in date_rates}

                output = ""
                for k, v in dict_rate.items():
                    output += "{}    1 USD เท่ากับ {:,.3f} {}  ".format(k, v, num) + '\n'

                frame = tk.Frame(self)
                frame.pack(fill=tk.BOTH, expand=1)

                my_canvas = tk.Canvas(frame)
                my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

                my_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

                second_frame = tk.Frame(my_canvas)

                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

                output1 = tk.Label(second_frame, text=output, width=193, bg='white', font=Large_Font1)
                output1.pack(pady=10)

                reset = tk.Button(self, text="ลบข้อมูล", width=50, font=Large_Font1, command=resets)
                reset.pack()

                # ลบข้อมูลที่อยู่ใน list ทั้งหมด เพื่อเตรียมพื้นที่ไว้สำหรับการแสดงค่าเงินอื่น ๆ เพิ่มเติม
                date_rates.clear()
                date_list.clear()
                rates.clear()
                dict_rate.clear()
                rates1_list.clear()
                rates2_list.clear()
                rates3_list.clear()
                ##
            except:
                return 0

        KeysList = []

        for i, k in countries1.items():
            KeysList.append(i)
        om1 = tkk.Combobox(self, values=KeysList, font=Large_Font1, state='readonly', width=60)
        om1.pack(pady=5)
        om1.set('กรุณาเลือกสกุลเงิน')

        day31 = []
        for i in range(1, 366):
            day31.append(i)
        om2 = tkk.Combobox(self, values=day31, font=Large_Font1, state='readonly', width=60)
        om2.pack(pady=5)
        om2.set('กรุณาเลือกเพื่อดูข้อมูลย้อนหลัง')

        btn2 = tk.Button(self, text='ดูข้อมูลราคาย้อนหลัง', fg='white', bg='dark Orchid4',
                         command=select, width=25, font=Large_Font1)
        btn2.pack(pady=10)


app = MyPage()
app.mainloop()
