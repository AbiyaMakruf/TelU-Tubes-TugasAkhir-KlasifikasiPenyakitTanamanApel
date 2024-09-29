import os
import pandas as pd
import shutil

# Load CSV
def split_dataset_utama(csv_file_train,source_folder_train,destination_folder_train,source_folder_test,destination_folder_test):
    csv_file = csv_file_train  # path ke file CSV
    df = pd.read_csv(csv_file)

    # Folder gambar awal
    source_folder = source_folder_train # path ke folder train

    # Folder tujuan
    destination_folder = destination_folder_train 
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Membuat folder class jika belum ada
    classes = ['healthy', 'multiple_diseases', 'rust', 'scab']
    for class_name in classes:
        class_folder = os.path.join(destination_folder, class_name)
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)

    # Menyalin file sesuai class
    for _, row in df.iterrows():
        image_id = row['image_id']
        file_name = f'{image_id}.jpg'
        source_path = os.path.join(source_folder, file_name)

        # Menentukan kelas dari baris CSV
        for class_name in classes:
            if row[class_name] == 1:
                target_folder = os.path.join(destination_folder, class_name)
                shutil.copy(source_path, target_folder)  # Salin file ke folder tujuan
                break  # Karena satu file hanya memiliki satu class, cukup break


    # Memindahkan folder test
    source_folder = source_folder_test  # path ke folder test
    destination_folder = destination_folder_test
    shutil.copytree(source_folder, destination_folder)

    print("Pemisahan file gambar berdasarkan class selesai!")

# Contoh penggunaan
# split_dataset_utama(
#     csv_file_train = 'data/original_dataset_utama/train.csv'
#     source_folder_train = 'data/original_dataset_utama/train'
#     destination_folder_train = 'data/split_train_test_dataset_utama/train'
#     source_folder_test = 'data/original_dataset_utama/test'
#     destination_folder_test = 'data/split_train_test_dataset_utama/test'
# )