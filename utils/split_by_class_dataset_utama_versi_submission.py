import os
import pandas as pd
import shutil

def split_dataset_utama_versi_submission (train_csv_path, test_csv_path, train_folder, test_folder, dest_folder):
    """
    Fungsi untuk memisahkan dan menggabungkan dataset train dan test ke dalam folder class yang sesuai.
    
    Parameters:
    - train_csv_path (str): Path ke file train.csv
    - test_csv_path (str): Path ke file test.csv
    - train_folder (str): Path ke folder yang berisi gambar-gambar train
    - test_folder (str): Path ke folder yang berisi gambar-gambar test
    - dest_folder (str): Path folder tujuan untuk menyimpan dataset yang digabungkan
    """
    
    # Membaca file CSV train dan test
    train_df = pd.read_csv(train_csv_path)
    test_df = pd.read_csv(test_csv_path)

    # Gabungkan kedua DataFrame dengan menambahkan kolom 'source' untuk identifikasi
    train_df['source'] = 'train'
    test_df['source'] = 'test'
    combined_df = pd.concat([train_df, test_df], ignore_index=True)

    # Membuat folder tujuan jika belum ada
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Membuat folder class jika belum ada
    classes = ['healthy', 'multiple_diseases', 'rust', 'scab']
    for class_name in classes:
        class_folder = os.path.join(dest_folder, class_name)
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)

    # Menyalin file sesuai class dari combined_df
    for _, row in combined_df.iterrows():
        image_id = row['image_id']
        file_name = f'{image_id}.jpg'

        # Tentukan path sumber berdasarkan 'source'
        if row['source'] == 'train':
            source_path = os.path.join(train_folder, file_name)
        else:
            source_path = os.path.join(test_folder, file_name)

        # Menentukan kelas dari baris CSV
        for class_name in classes:
            if row[class_name] == 1:
                target_folder = os.path.join(dest_folder, class_name)
                if os.path.exists(source_path):  # Cek apakah file sumber ada
                    shutil.copy(source_path, target_folder)  # Salin file ke folder tujuan
                else:
                    print(f"File {source_path} tidak ditemukan dan dilewatkan.")
                break  # Karena satu file hanya memiliki satu class, cukup break

    print(f"Pemisahan dan penggabungan file gambar dari {train_folder} dan {test_folder} berdasarkan class selesai!")

# Contoh pemanggilan fungsi
# split_dataset_utama_versi_submission(
#     train_csv_path='data/original_dataset_utama/train.csv',                # Path ke file train.csv
#     test_csv_path='data/original_dataset_utama/submission_mix_transform.csv',                  # Path ke file test.csv
#     train_folder='data/original_dataset_utama/train',                      # Path ke folder train
#     test_folder='data/original_dataset_utama/test',                        # Path ke folder test
#     dest_folder='data/original_dataset_utama_versi_submission'             # Path folder tujuan untuk menyimpan dataset yang digabungkan
# )
