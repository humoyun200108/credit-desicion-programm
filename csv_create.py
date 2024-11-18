import pandas as pd

# Kredit uchun misol ma'lumotlar
data = {
    "Age": [25, 45, 35, 50, 23, 40, 60, 36, 29, 41, 31, 22, 47, 33, 38, 49, 52, 27, 55, 43],
    "Annual Income": [50000, 64000, 120000, 85000, 43000, 70000, 55000, 130000, 52000, 75000,
                      61000, 47000, 96000, 73000, 82000, 78000, 92000, 54000, 51000, 69000],  # Yillik daromad ($)
    "Credit History": [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0],  # 1 - yaxshi, 0 - yomon
    "Loan Amount": [2000, 5000, 12000, 10000, 2000, 7000, 3000, 11000, 2500, 7500,
                    4000, 6500, 8500, 5000, 6000, 8000, 7000, 5400, 6800, 7300],  # Kredit miqdori ($)
    "Loan Status": [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0]  # 1 - Tasdiqlangan, 0 - Rad etilgan
}

# Ma'lumotlar DataFrame ko'rinishida saqlanadi
df = pd.DataFrame(data)

# Faylni CSV formatida saqlash
df.to_csv("credit_data.csv", index=False)
print("credit_data.csv fayli muvaffaqiyatli yaratildi.")
