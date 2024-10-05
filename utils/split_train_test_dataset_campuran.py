import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset_campuran(source_folder, dest_folder, test_source_folder=None, train_ratio=0.7, val_ratio=0.3, class_exception=[], class_exception_test=[], rename_map={}):
    """
    Fungsi untuk membagi dataset menjadi folder train, validation, dan test (opsional) dengan pengecualian kelas tertentu.
    Selain itu, folder class yang disalin ke folder test dapat diubah namanya sesuai dengan mapping yang diberikan.
    
    Args:
    - source_folder: Folder sumber yang berisi sub-folder kelas untuk train dan validation.
    - dest_folder: Folder tujuan tempat dataset train, validation, dan test disimpan.
    - test_source_folder: Folder sumber tambahan untuk dataset test yang akan disalin ke 'dest_folder/test'.
    - train_ratio: Proporsi dataset untuk train.
    - val_ratio: Proporsi dataset untuk validation.
    - class_exception: Daftar kelas yang tidak akan disertakan dalam pembagian train dan val.
    - class_exception_test: Daftar kelas yang tidak akan disertakan dalam pembagian test.
    - rename_map: Dictionary untuk merename kelas pada folder test (contoh: {"Healthy": "healthy", "Cedar Rust": "rust"}).
    """
    # Pastikan proporsi pembagian bernilai 1
    assert train_ratio + val_ratio == 1, "Proporsi pembagian (train + val) harus sama dengan 1"

    # Buat folder tujuan jika belum ada
    for split in ['train', 'val']:
        split_folder = os.path.join(dest_folder, split)
        if not os.path.exists(split_folder):
            os.makedirs(split_folder)

    # Iterasi setiap sub-folder di folder sumber (misalnya, setiap class)
    for class_folder in os.listdir(source_folder):
        class_path = os.path.join(source_folder, class_folder)
        
        # Jika bukan folder, skip
        if not os.path.isdir(class_path):
            continue

        # Abaikan folder yang ada di dalam class_exception
        if class_folder in class_exception:
            print(f"Kelas '{class_folder}' diabaikan karena termasuk dalam class_exception (train/val).")
            continue

        # Dapatkan semua file dalam class folder
        files = os.listdir(class_path)
        
        # Bagi data menjadi train dan validation
        train_files, val_files = train_test_split(files, train_size=train_ratio, random_state=42)

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

        print(f"Class '{class_folder}' telah dibagi ke dalam train dan val.")

    print("Pembagian train dan val selesai!")

    # Proses untuk menyalin data dari test_source_folder ke test destination folder
    if test_source_folder:
        test_dest_folder = os.path.join(dest_folder, 'test')

        if not os.path.exists(test_dest_folder):
            os.makedirs(test_dest_folder)

        for class_folder in os.listdir(test_source_folder):
            class_path = os.path.join(test_source_folder, class_folder)
            
            # Jika bukan folder, skip
            if not os.path.isdir(class_path):
                continue

            # Abaikan folder yang ada di dalam class_exception_test
            if class_folder in class_exception_test:
                print(f"Kelas '{class_folder}' diabaikan karena termasuk dalam class_exception_test (test).")
                continue

            # Rename folder jika terdapat dalam rename_map, jika tidak gunakan nama asli
            dest_class_name = rename_map.get(class_folder, class_folder)

            # Salin keseluruhan file dari folder class_path ke test_dest_folder
            test_class_dest = os.path.join(test_dest_folder, dest_class_name)
            if not os.path.exists(test_class_dest):
                os.makedirs(test_class_dest)

            for file_name in os.listdir(class_path):
                shutil.copy(os.path.join(class_path, file_name), os.path.join(test_class_dest, file_name))

            print(f"Class '{class_folder}' telah disalin ke folder test dengan nama '{dest_class_name}'.")

        print("Penyalinan folder test selesai!")
