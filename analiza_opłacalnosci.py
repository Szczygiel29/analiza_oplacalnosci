import pandas as pd
import matplotlib.pyplot as plt

# Dane wejściowe dla silników spalinowych z różnymi paliwami
data = {
    'Silnik': ['Silnik 1', 'Silnik 2', 'Silnik 3'],
    'Moc (kW)': [100, 150, 200],
    'Zużycie biogazu (m3/h)': [10, 15, 20],
    'Zużycie benzyny (l/h)': [8, 12, 16],
    'Zużycie diesla (l/h)': [7, 10, 14],
    'Wartość opałowa biogazu (MJ/m3)': [22.67, 21.05, 23.71],
    'Wartość opałowa benzyny (MJ/l)': [34.2, 34.2, 34.2],
    'Wartość opałowa diesla (MJ/l)': [35.8, 35.8, 35.8],
    'Koszt biogazu (USD/m3)': [0.5, 0.5, 0.5],
    'Koszt benzyny (USD/l)': [1.2, 1.2, 1.2],
    'Koszt diesla (USD/l)': [1.0, 1.0, 1.0],
    'Koszt utrzymania biogazu (USD/h)': [5, 5, 5],
    'Koszt utrzymania benzyny (USD/h)': [6, 6, 6],
    'Koszt utrzymania diesla (USD/h)': [6.5, 6.5, 6.5],
    'Koszt serwisu biogazu (USD/h)': [2, 2, 2],
    'Koszt serwisu benzyny (USD/h)': [2.5, 2.5, 2.5],
    'Koszt serwisu diesla (USD/h)': [2.8, 2.8, 2.8],
    'Koszt amortyzacji biogazu (USD/h)': [3, 3, 3],
    'Koszt amortyzacji benzyny (USD/h)': [3.5, 3.5, 3.5],
    'Koszt amortyzacji diesla (USD/h)': [4, 4, 4]
}

# Koszty inwestycyjne
inwestycje = {
    'Biogaz': 200000,
    'Benzyna': 180000,
    'Diesel': 220000
}

# Okres inwestycji i czas pracy
okres_inwestycji = 10  # lata
czas_pracy_roczny = 2000  # godziny

# Tworzenie DataFrame z danymi
df = pd.DataFrame(data)

# Obliczanie dostarczonej energii z paliwa (MJ/h)
df['Dostarczona energia biogazu (MJ/h)'] = df['Zużycie biogazu (m3/h)'] * df['Wartość opałowa biogazu (MJ/m3)']
df['Dostarczona energia benzyny (MJ/h)'] = df['Zużycie benzyny (l/h)'] * df['Wartość opałowa benzyny (MJ/l)']
df['Dostarczona energia diesla (MJ/h)'] = df['Zużycie diesla (l/h)'] * df['Wartość opałowa diesla (MJ/l)']

# Obliczanie kosztów operacyjnych na godzinę pracy silnika
df['Koszt biogazu (USD/h)'] = df['Zużycie biogazu (m3/h)'] * df['Koszt biogazu (USD/m3)']
df['Koszt benzyny (USD/h)'] = df['Zużycie benzyny (l/h)'] * df['Koszt benzyny (USD/l)']
df['Koszt diesla (USD/h)'] = df['Zużycie diesla (l/h)'] * df['Koszt diesla (USD/l)']

# Dodanie kosztów utrzymania, serwisu i amortyzacji
df['Całkowity koszt biogazu (USD/h)'] = df['Koszt biogazu (USD/h)'] + df['Koszt utrzymania biogazu (USD/h)'] + df['Koszt serwisu biogazu (USD/h)'] + df['Koszt amortyzacji biogazu (USD/h)']
df['Całkowity koszt benzyny (USD/h)'] = df['Koszt benzyny (USD/h)'] + df['Koszt utrzymania benzyny (USD/h)'] + df['Koszt serwisu benzyny (USD/h)'] + df['Koszt amortyzacji benzyny (USD/h)']
df['Całkowity koszt diesla (USD/h)'] = df['Koszt diesla (USD/h)'] + df['Koszt utrzymania diesla (USD/h)'] + df['Koszt serwisu diesla (USD/h)'] + df['Koszt amortyzacji diesla (USD/h)']

# Obliczanie rocznych kosztów operacyjnych
df['Roczne koszty biogazu (USD)'] = df['Całkowity koszt biogazu (USD/h)'] * czas_pracy_roczny
df['Roczne koszty benzyny (USD)'] = df['Całkowity koszt benzyny (USD/h)'] * czas_pracy_roczny
df['Roczne koszty diesla (USD)'] = df['Całkowity koszt diesla (USD/h)'] * czas_pracy_roczny

# Obliczanie całkowitych kosztów inwestycji + eksploatacji na okres inwestycji
df['Całkowite koszty biogazu (USD)'] = df['Roczne koszty biogazu (USD)'] * okres_inwestycji + inwestycje['Biogaz']
df['Całkowite koszty benzyny (USD)'] = df['Roczne koszty benzyny (USD)'] * okres_inwestycji + inwestycje['Benzyna']
df['Całkowite koszty diesla (USD)'] = df['Roczne koszty diesla (USD)'] * okres_inwestycji + inwestycje['Diesel']

# Wyświetlanie wyników
print(df[['Silnik', 'Całkowite koszty biogazu (USD)', 'Całkowite koszty benzyny (USD)', 'Całkowite koszty diesla (USD)']])

# Tworzenie wykresu całkowitych kosztów inwestycji + eksploatacji
plt.figure(figsize=(12, 8))

bar_width = 0.25
r1 = range(len(df['Silnik']))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.bar(r1, df['Całkowite koszty biogazu (USD)'], color='blue', width=bar_width, edgecolor='grey', label='Biogaz')
plt.bar(r2, df['Całkowite koszty benzyny (USD)'], color='green', width=bar_width, edgecolor='grey', label='Benzyna')
plt.bar(r3, df['Całkowite koszty diesla (USD)'], color='red', width=bar_width, edgecolor='grey', label='Diesel')

plt.xlabel('Silnik', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(df['Silnik']))], df['Silnik'])
plt.ylabel('Całkowite koszty (USD)')
plt.title('Porównanie całkowitych kosztów inwestycji i eksploatacji dla różnych paliw')
plt.legend()

# Wyświetlanie wykresu
plt.tight_layout()
plt.show()

# Wykres rocznych kosztów operacyjnych
plt.figure(figsize=(12, 8))

plt.bar(r1, df['Roczne koszty biogazu (USD)'], color='blue', width=bar_width, edgecolor='grey', label='Biogaz')
plt.bar(r2, df['Roczne koszty benzyny (USD)'], color='green', width=bar_width, edgecolor='grey', label='Benzyna')
plt.bar(r3, df['Roczne koszty diesla (USD)'], color='red', width=bar_width, edgecolor='grey', label='Diesel')

plt.xlabel('Silnik', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(df['Silnik']))], df['Silnik'])
plt.ylabel('Roczne koszty operacyjne (USD)')
plt.title('Porównanie rocznych kosztów operacyjnych dla różnych paliw')
plt.legend()

# Wyświetlanie wykresu
plt.tight_layout()
plt.show()

# Wykres szczegółowy kosztów operacyjnych na godzinę
# Wykres szczegółowy kosztów operacyjnych na godzinę
plt.figure(figsize=(12, 8))

categories = ['Koszt paliwa (USD/h)', 'Koszt utrzymania (USD/h)', 'Koszt serwisu (USD/h)', 'Koszt amortyzacji (USD/h)']

# Przygotowanie danych do wykresu
biogaz_costs = df[['Koszt biogazu (USD/h)', 'Koszt utrzymania biogazu (USD/h)', 'Koszt serwisu biogazu (USD/h)', 'Koszt amortyzacji biogazu (USD/h)']].sum()
benzyna_costs = df[['Koszt benzyny (USD/h)', 'Koszt utrzymania benzyny (USD/h)', 'Koszt serwisu benzyny (USD/h)', 'Koszt amortyzacji benzyny (USD/h)']].sum()
diesel_costs = df[['Koszt diesla (USD/h)', 'Koszt utrzymania diesla (USD/h)', 'Koszt serwisu diesla (USD/h)', 'Koszt amortyzacji diesla (USD/h)']].sum()

# Tworzenie wykresu
bar_width = 0.25
r1 = range(len(categories))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.bar(r1, biogaz_costs, color='blue', width=bar_width, edgecolor='grey', label='Biogaz')
plt.bar(r2, benzyna_costs, color='green', width=bar_width, edgecolor='grey', label='Benzyna')
plt.bar(r3, diesel_costs, color='red', width=bar_width, edgecolor='grey', label='Diesel')

plt.xlabel('Koszty', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(categories))], categories)
plt.ylabel('Koszt operacyjny (USD/h)')
plt.title('Szczegółowy wykres kosztów operacyjnych na godzinę')
plt.legend()

# Wyświetlanie wykresu
plt.tight_layout()
plt.show()
