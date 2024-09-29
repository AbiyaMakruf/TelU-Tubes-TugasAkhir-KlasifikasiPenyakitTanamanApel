from utils.split_by_class_dataset_utama_versi_submission import split_dataset_utama_versi_submission
from utils.split_by_class_dataset_utama import split_dataset_utama
from utils.split_train_test_dataset import split_dataset

split_dataset_utama(
    csv_file_train = 'data/ROOT/train.csv',
    source_folder_train = 'data/ROOT/train',
    destination_folder_train = 'data/original_dataset_utama/train',
    source_folder_test = 'data/ROOT/test',
    destination_folder_test = 'data/original_dataset_utama/test'
)

split_dataset_utama_versi_submission(
    train_csv_path='data/ROOT/train.csv',
    test_csv_path='data/ROOT/submission_mix_transform.csv',
    train_folder='data/ROOT/train',
    test_folder='data/ROOT/test',
    dest_folder='data/original_dataset_utama_versi_submission'
)

# Split Utama
split_dataset(
    source_folder='data/original_dataset_utama/train',
    dest_folder='data/split_train_test_dataset_utama',
    train_ratio=0.7,
    val_ratio=0.15,
    test_ratio=0.15
)

# Split Utama Versi Submission
split_dataset(
    source_folder='data/original_dataset_utama_versi_submission',
    dest_folder='data/split_train_test_dataset_utama_versi_submission',
    train_ratio=0.7,
    val_ratio=0.15,
    test_ratio=0.15
)

# Split Cadangan
split_dataset(
    source_folder='data/original_dataset_cadangan',
    dest_folder='data/split_train_test_dataset_cadangan',
    train_ratio=0.7,
    val_ratio=0.15,
    test_ratio=0.15
)