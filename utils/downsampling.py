import os
import random
import shutil

def downsample_and_move_to_new_folder(base_dir, dest_dir, seed=42):
    # Set seed untuk konsistensi pemilihan gambar acak
    random.seed(seed)

    # Membuat folder tujuan jika belum ada
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Langkah 1: Identifikasi jumlah gambar di setiap kelas dan temukan jumlah gambar paling sedikit
    class_image_count = {}  # Dictionary untuk menyimpan jumlah gambar di setiap kelas

    for class_folder in os.listdir(base_dir):
        class_path = os.path.join(base_dir, class_folder)
        if os.path.isdir(class_path):  # Pastikan ini adalah direktori
            # Hitung jumlah gambar di folder kelas ini
            image_count = len([file for file in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, file))])
            class_image_count[class_folder] = image_count

    # Menemukan jumlah gambar paling sedikit
    min_images = min(class_image_count.values())
    print(f"Jumlah gambar paling sedikit adalah {min_images}. Akan dipindahkan {min_images} gambar untuk setiap kelas.\n")

    # Langkah 2: Pindahkan min_images gambar dari setiap kelas ke folder baru
    for class_folder, total_images in class_image_count.items():
        class_path = os.path.join(base_dir, class_folder)
        dest_class_path = os.path.join(dest_dir, class_folder)  # Folder tujuan untuk kelas ini

        # Buat folder tujuan untuk kelas ini jika belum ada
        if not os.path.exists(dest_class_path):
            os.makedirs(dest_class_path)

        # Dapatkan semua gambar di folder kelas ini
        all_images = os.listdir(class_path)

        # Pilih subset gambar yang ingin dipindahkan
        images_to_move = random.sample(all_images, min_images)

        # Pindahkan gambar ke folder tujuan
        for image in images_to_move:
            src_path = os.path.join(class_path, image)  # Path asal gambar
            dest_path = os.path.join(dest_class_path, image)  # Path tujuan gambar
            shutil.copy(src_path, dest_path)  # Memindahkan gambar ke folder baru

        print(f"Folder '{class_folder}' dipindahkan {min_images} gambar ke '{dest_class_path}'.")

    print("\nProses pemindahan gambar ke folder baru selesai.")
