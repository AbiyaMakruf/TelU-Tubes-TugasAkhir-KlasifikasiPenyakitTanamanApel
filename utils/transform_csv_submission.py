import pandas as pd

def transform_csv(input_file, output_file):
    # Membaca file CSV
    df = pd.read_csv(input_file)

    # Mendapatkan kolom-kolom class (selain 'image_id')
    class_columns = df.columns[1:]

    # Mengubah nilai tertinggi menjadi 1, dan sisanya 0
    for index, row in df.iterrows():
        max_column = row[class_columns].idxmax()  # Dapatkan kolom dengan nilai maksimum
        # Set kolom dengan nilai maksimum menjadi 1, sisanya 0
        df.loc[index, class_columns] = [1 if col == max_column else 0 for col in class_columns]

    # Menyimpan hasil transformasi ke file CSV baru
    df.to_csv(output_file, index=False)
    print(f"Hasil transformasi disimpan di: {output_file}")

# Contoh penggunaan
input_csv = 'data/original_dataset_utama/submission_mix.csv'  # Ganti dengan path ke file CSV input
output_csv = 'data/original_dataset_utama/submission_mix_transform.csv'  # Ganti dengan path untuk file CSV output

transform_csv(input_csv, output_csv)
