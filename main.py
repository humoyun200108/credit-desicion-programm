import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Ma'lumotlarni yuklash va tayyorlash
data = pd.read_csv("credit_data.csv")
X = data[["Age", "Annual Income", "Credit History", "Loan Amount"]]  # Ustunlarni mos ravishda to‘g‘rilang
y = data["Loan Status"]

# Ma'lumotlarni bo‘lish
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 2. Modelni yaratish va o‘rgatish
model = DecisionTreeClassifier(max_depth=4, random_state=0)
model.fit(X_train, y_train)

# Test ma'lumotlarida aniqlik
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Modelning aniqligi:", accuracy)

# Aniqlik va xatoliklarni grafik ko‘rinishda chiqarish
def plot_accuracy_error():
    plt.figure(figsize=(8, 4))
    plt.bar(["Aniqlik", "Xatolik"], [accuracy, 1 - accuracy], color=["green", "red"])
    plt.ylim(0, 1)
    plt.ylabel("Qiymat")
    plt.title("Model Aniqligi va Xatoliklari")
    plt.show()

# Aniqlikni ko‘rsatish uchun grafikni chizish
plot_accuracy_error()

# 3. Tkinter interfeysini yaratish
root = tk.Tk()
root.title("Bank Kredit Qarori")

tk.Label(root, text="Yosh").grid(row=0, column=0)
yosh_entry = tk.Entry(root)
yosh_entry.grid(row=0, column=1)

tk.Label(root, text="Yillik Daromad ($)").grid(row=1, column=0)
daromad_entry = tk.Entry(root)
daromad_entry.grid(row=1, column=1)

tk.Label(root, text="Kredit Tarixi (1 - yaxshi, 0 - yomon)").grid(row=2, column=0)
kredit_tarixi_entry = tk.Entry(root)
kredit_tarixi_entry.grid(row=2, column=1)

tk.Label(root, text="Kredit Miqdori ($)").grid(row=3, column=0)
kredit_miqdori_entry = tk.Entry(root)
kredit_miqdori_entry.grid(row=3, column=1)

# Progress bar yaratish
progress_label = tk.Label(root, text="Jarayon davom etmoqda...")
progress_label.grid(row=5, column=0, columnspan=2)
progress_bar = Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=6, column=0, columnspan=2)

def baholash():
    try:
        # Foydalanuvchi kiritgan ma'lumotlarni olish
        yosh = int(yosh_entry.get())
        daromad = int(daromad_entry.get())
        kredit_tarixi = int(kredit_tarixi_entry.get())
        kredit_miqdori = int(kredit_miqdori_entry.get())

        # Yosh va daromad cheklovlarini qo‘shish
        if yosh < 21:
            messagebox.showinfo("Natija", "Kredit rad etilgan. Sabab: Yosh juda kichik")
            return
        if daromad < 15000:
            messagebox.showinfo("Natija", "Kredit rad etilgan. Sabab: Yillik daromad yetarli emas")
            return

        yangi_mijoz = [[yosh, daromad, kredit_tarixi, kredit_miqdori]]

        # Progress barni yangilash
        for i in range(101):
            progress_bar['value'] = i
            root.update_idletasks()

        # Model orqali bashorat qilish
        natija = model.predict(yangi_mijoz)

        if natija[0] == 1:
            ajratilgan_kredit = min(kredit_miqdori, daromad * 0.5)
            messagebox.showinfo("Natija", f"Kredit tasdiqlangan. Ajratilgan kredit miqdori: ${ajratilgan_kredit}")
        else:
            # Rad etilganlik sabablari
            sabablar = []
            if kredit_tarixi == 0:
                sabablar.append("Kredit tarixi yomon")
            if kredit_miqdori > daromad * 0.5:
                sabablar.append("Kredit miqdori yillik daromaddan yuqori")

            sabab_text = "\n".join(sabablar)
            messagebox.showinfo("Natija", f"Kredit rad etilgan. Sabablar:\n{sabab_text}")
    except ValueError:
        messagebox.showerror("Xatolik", "Iltimos, barcha maydonlarni to‘g‘ri kiriting.")

bahola_button = tk.Button(root, text="Baholash", command=baholash)
bahola_button.grid(row=4, column=1)

root.mainloop()
