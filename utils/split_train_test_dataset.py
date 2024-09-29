import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(source_folder, dest_folder, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    """
    Fungsi untuk membagi dataset menjadi train, val, dan test sesuai dengan proporsi yang diberikan.
    
    Parameters:
    - source_folder (str): Path ke folder dataset awal yang berisi sub-folder class.
    - dest_folder (str): Path ke folder tujuan untuk menyimpan train, val, dan test.
    - train_ratio (float): Proporsi data untuk training (default 0.7).
    - val_ratio (float): Proporsi data untuk validation (default 0.15).
    - test_ratio (float): Proporsi data untuk testing (default 0.15).
    """
    # Pastikan proporsi pembagian bernilai 1
    assert train_ratio + val_ratio + test_ratio == 1, "Total proporsi train, val, dan test harus sama dengan 1!"

    # Buat folder tujuan jika belum ada
    for split in ['train', 'val', 'test']:
        split_folder = os.path.join(dest_folder, split)
        if not os.path.exists(split_folder):
            os.makedirs(split_folder)

    # Iterasi setiap sub-folder di folder sumber (misalnya, setiap class)
    for class_folder in os.listdir(source_folder):
        class_path = os.path.join(source_folder, class_folder)
        
        # Jika bukan folder, skip
        if not os.path.isdir(class_path):
            continue

        # Dapatkan semua file dalam class folder
        files = os.listdir(class_path)
        
        # Bagi data menjadi train dan sisa (val + test)
        train_files, temp_files = train_test_split(files, train_size=train_ratio, random_state=42)
        
        # Tentukan proporsi val dari sisa data
        val_ratio_adjusted = val_ratio / (val_ratio + test_ratio)
        
        # Bagi sisa data menjadi val dan test
        val_files, test_files = train_test_split(temp_files, train_size=val_ratio_adjusted, random_state=42)

        # Fungsi untuk menyalin file ke folder tujuan
        def copy_files(file_list, destination):
            dest_class_folder = os.path.join(dest_folder, destination, class_folder)
            if not os.path.exists(dest_class_folder):
                os.makedirs(dest_class_folder)
            for file_name in file_list:
                shutil.copy(os.path.join(class_path, file_name), os.path.join(dest_class_folder, file_name))

        # Salin file ke folder yang bersesuaian
        copy_files(train_files, 'train')
        copy_files(val_files, 'val')
        copy_files(test_files, 'test')

        print(f"Class '{class_folder}' telah dibagi ke dalam train, val, dan test.")

    print("Pembagian dataset selesai!")

# Contoh penggunaan
# split_dataset(
#     source_folder='data/original_dataset_cadangan',  # Path ke folder sumber
#     dest_folder='data/split_train_test_dataset_cadangan',                # Path ke folder tujuan
#     train_ratio=0.7,                            # Proporsi train
#     val_ratio=0.15,                             # Proporsi val
#     test_ratio=0.15                             # Proporsi test
# )