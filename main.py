from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
import config

#colors
white = "#FFFFFF"
black = "#333333"
red = "#EB5D51"
blue = "#0009FF"

window = Tk()
window.geometry('500x500')
window.title('Currency Converter')
window.configure(bg=white)
window.resizable(height=False, width=False)

#top section
top = Frame(window, width=500, height=100, bg=blue)
top.grid(row=0, column=0)

#main section
main = Frame(window, width=500, height=700, bg=white)
main.grid(row=1, column=0)

#icon
icon = Image.open('./img/logo.png')
icon = icon.resize((85, 85))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound=LEFT, text = "Currency Converter", height=35, padx=13, pady=30, font = ('Arial', 25), anchor=CENTER, bg=blue, fg=white)
app_name.place(x=50, y=0)

#main frame
result = Label(main, text = " ", width=24, height=2, padx=5, pady=25, font = ('Ivy', 20), anchor=CENTER, bg=white, fg=black, relief='solid')
result.place(x=50, y=10)

#test
currencies = [
    'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD',
    'MXN', 'SGD', 'HKD', 'NOK', 'KRW', 'TRY', 'INR', 'RUB', 'BRL', 'ZAR',
    'SAR', 'AED', 'THB', 'PLN', 'IDR', 'TWD', 'MYR', 'COP', 'CLP', 'ILS',
    'PHP', 'PKR', 'EGP', 'CZK', 'VND', 'ARS', 'NGN', 'DZD', 'KES', 'UAH',
    'IQD', 'QAR', 'XAU', 'BDT', 'LKR', 'NPR', 'CRC', 'HRK', 'HUF', 'RON'
]


#to and from
from_label = Label(main, text = "From", width=15, height=1, padx=0, pady=0, font = ('Ivy', 15), anchor=NW, bg=white, fg=black, relief='flat')
from_label.place(x=50, y=145)
from_box = ttk.Combobox(main, width=15, justify=CENTER, font=("Ivy", 12, 'bold'))
from_box['values'] = (currencies)
from_box.place(x=50, y=175)

to_label = Label(main, text = "To", width=15, height=1, padx=0, pady=0, font = ('Ivy', 15), anchor=NW, bg=white, fg=black, relief='flat')
to_label.place(x=290, y=145)
to_box = ttk.Combobox(main, width=15, justify=CENTER, font=("Ivy", 12, 'bold'))
to_box['values'] = (currencies)
to_box.place(x=290, y=175)

#input
value = Entry(main, width=21, justify=CENTER, font=('Ivy', 15), relief='solid')
value.place(x=119, y=220)

#function
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = from_box.get()
    currency_2 = to_box.get()
    amount = value.get()

    currency_symbols = {
    'USD': '$', 'EUR': '€', 'JPY': '¥', 'GBP': '£', 'AUD': '$', 'CAD': '$',
    'CHF': 'Fr', 'CNY': '¥', 'SEK': 'kr', 'NZD': '$',
    'MXN': '$', 'SGD': '$', 'HKD': '$', 'NOK': 'kr', 'KRW': '₩',
    'TRY': '₺', 'INR': '₹', 'RUB': '₽', 'BRL': 'R$', 'ZAR': 'R',
    'SAR': 'ر.س', 'AED': 'د.إ', 'THB': '฿', 'PLN': 'zł', 'IDR': 'Rp',
    'TWD': 'NT$', 'MYR': 'RM', 'COP': '$', 'CLP': '$', 'ILS': '₪',
    'PHP': '₱', 'PKR': '₨', 'EGP': '£', 'CZK': 'Kč', 'VND': '₫',
    'ARS': '$', 'NGN': '₦', 'DZD': 'د.ج', 'KES': 'KSh', 'UAH': '₴',
    'IQD': 'ع.د', 'QAR': 'ر.ق', 'XAU': 'Au', 'BDT': '৳', 'LKR': 'රු',
    'NPR': '₨', 'CRC': '₡', 'HRK': 'kn', 'HUF': 'Ft', 'RON': 'lei'
    }


    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
        "X-RapidAPI-Key": config.API_KEY,
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    from_currency_symbol = currency_symbols.get(currency_1, currency_1)
    to_currency_symbol = currency_symbols.get(currency_2, currency_2)

    response = requests.get(url, headers=headers, params=querystring)
    converted_amount = response.json()['result']['convertedAmount']
    formatted = "{:,.2f}".format(converted_amount)
    result['text'] = to_currency_symbol + formatted
    print(formatted)

#button
button = Button(main, text='Convert', width=19, padx=7, height=1, bg='#6495ed', fg=black, font=('Ivy', 15), relief='flat', command=convert)
button.place(x=121, y=270)



window.mainloop()