import zipfile
import os

# Hàm nén tệp
def compress_file(input_file, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file)
    print(f"Đã nén {input_file} thành {output_zip}")

# Hàm giải nén tệp
def decompress_file(zip_file, output_dir):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(output_dir)
    print(f"Đã giải nén {zip_file} vào {output_dir}")

# Chương trình chính
choice = input("Bạn muốn nén (c) hay giải nén (d)? ").lower()

if choice == 'c':
    file_to_compress = input("Nhập đường dẫn tệp cần nén: ")
    zip_name = input("Nhập tên tệp nén (ví dụ: output.zip): ")
    compress_file(file_to_compress, zip_name)
elif choice == 'd':
    zip_to_decompress = input("Nhập đường dẫn tệp nén: ")
    extract_dir = input("Nhập thư mục giải nén: ")
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)
    decompress_file(zip_to_decompress, extract_dir)
else:
    print("Lựa chọn không hợp lệ!")