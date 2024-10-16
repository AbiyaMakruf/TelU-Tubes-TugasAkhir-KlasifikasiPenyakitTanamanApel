from split_by_class_dataset_utama_versi_submission import split_dataset_utama_versi_submission
from split_by_class_dataset_utama import split_dataset_utama
from split_train_test_dataset import split_dataset
from split_train_test_dataset_campuran import split_dataset_campuran
from downsampling import downsample_and_move_to_new_folder

split_dataset_utama(
    csv_file_train = 'data/ROOT/train.csv',
    source_folder_train = 'data/ROOT/train',
    destination_folder_train = 'data/original_dataset_utama/train',
    source_folder_test = 'data/ROOT/test',
    destination_folder_test = 'data/original_dataset_utama/test'
)
print("split_dataset_utama done")

split_dataset_utama_versi_submission(
    train_csv_path='data/ROOT/train.csv',
    test_csv_path='data/ROOT/submission_mix_transform.csv',
    train_folder='data/ROOT/train',
    test_folder='data/ROOT/test',
    dest_folder='data/original_dataset_utama_versi_submission'
)
print("split_dataset_utama_versi_submission done")

# Split Utama
split_dataset(
    source_folder='data/original_dataset_utama/train',
    dest_folder='data/split_train_test_dataset_utama',
    train_ratio=0.7,
    val_ratio=0.15,
    test_ratio=0.15
)

print("split_utama done")

# Split Utama Versi Submission
split_dataset(
    source_folder='data/original_dataset_utama_versi_submission',
    dest_folder='data/split_train_test_dataset_utama_versi_submission',
    train_ratio=0.7,
    val_ratio=0.15,
    test_ratio=0.15
)
print("split_utama_versi_submission done")

# Split Cadangan
split_dataset(
    source_folder='data/original_dataset_cadangan',
    dest_folder='data/split_train_test_dataset_cadangan',
    train_ratio=0.7,
    val_ratio=0.15,
    test_ratio=0.15
)
print("split_cadangan done")

# Split Campuran dataset utama
source_folder = "data/original_dataset_utama/train"
dest_folder = "data/split_train_test_dataset_campuran"
test_source_folder = "data/original_dataset_cadangan"
class_exception_train_val = ["multiple_diseases"]  # Pengecualian untuk train dan val
class_exception_test = ["Black Rot"]  # Pengecualian untuk test
rename_map = {"Healthy": "healthy", "Scab": "scab", "Cedar Rust": "rust"} 

# Membagi train dan val, serta menyalin test dengan pengecualian kelas yang ditentukan
split_dataset_campuran(
    source_folder, dest_folder, test_source_folder=test_source_folder,
    train_ratio=0.8, val_ratio=0.2,
    class_exception=class_exception_train_val, class_exception_test=class_exception_test, rename_map=rename_map
)
print("split_campuran done")


# Split Campuran dataset cadangan
source_folder = "data/original_dataset_cadangan/"
dest_folder = "data/split_train_test_dataset_campuran_dataset_cadangan"
test_source_folder = "data/original_dataset_utama/train"
class_exception_train_val = ["Black Rot"]  # Pengecualian untuk train dan val
class_exception_test = ["multiple_diseases"]  # Pengecualian untuk test
rename_map = {"Healthy": "healthy", "Scab": "scab", "Cedar Rust": "rust"} 

# Membagi train dan val, serta menyalin test dengan pengecualian kelas yang ditentukan
split_dataset_campuran(
    source_folder, dest_folder, test_source_folder=test_source_folder,
    train_ratio=0.8, val_ratio=0.2,
    class_exception=class_exception_train_val, class_exception_test=class_exception_test, rename_map=rename_map
)
print("split_campuran dataset cadangan done")


# Downsampling
base_dir = 'data/split_train_test_dataset_campuran/test'
dest_dir = 'data/split_train_test_dataset_campuran_balanced_test/'

# Panggil fungsi
downsample_and_move_to_new_folder(base_dir, dest_dir, seed=42)