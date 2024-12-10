import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('upload_times.csv')

# Generate a box plot comparing put_object and upload_file
plt.figure(figsize=(10, 6))
df.boxplot(column=['put_object', 'upload_file'])
plt.title('Comparación de tiempo entre los 2 métodos')
plt.ylabel('Tiempo (segundos)')
plt.xlabel('Método')
plt.grid(True)
plt.savefig('box_plot_comparison.png')

# Determine the range for the histograms
min_time = min(df['put_object'].min(), df['upload_file'].min())
max_time = max(df['put_object'].max(), df['upload_file'].max())

# Generate histograms for put_object and upload_file
plt.figure(figsize=(12, 6))

# Histogram for put_object
plt.subplot(1, 2, 1)
plt.hist(df['put_object'], bins=10, range=(min_time, max_time), color='blue', alpha=0.7)
plt.title('Histograma de put_object')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Frecuencia')

# Histogram for upload_file
plt.subplot(1, 2, 2)
plt.hist(df['upload_file'], bins=10, range=(min_time, max_time), color='green', alpha=0.7)
plt.title('Histograma de upload_file')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.savefig('histograms_comparison.png')