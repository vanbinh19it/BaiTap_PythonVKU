import zipfile
import os

def compress_files(zip_name, files_to_compress):
    """Nén các tệp thành một tệp ZIP"""
    try:
        # Tạo tệp ZIP với chế độ ghi
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files_to_compress:
                if os.path.exists(file):
                    # Thêm tệp vào ZIP
                    zipf.write(file)
                    print(f"Đã nén: {file}")
                else:
                    print(f"Tệp không tồn tại: {file}")
        print(f"Đã tạo tệp nén: {zip_name}")
    except Exception as e:
        print(f"Lỗi khi nén: {e}")

def extract_files(zip_name, extract_path="."):
    """Giải nén tệp ZIP"""
    try:
        if not os.path.exists(zip_name):
            print(f"Tệp ZIP không tồn tại: {zip_name}")
            return
        
        # Mở tệp ZIP với chế độ đọc
        with zipfile.ZipFile(zip_name, 'r') as zipf:
            # Giải nén tất cả tệp vào thư mục đích
            zipf.extractall(extract_path)
            print(f"Đã giải nén tất cả tệp vào: {extract_path}")
    except Exception as e:
        print(f"Lỗi khi giải nén: {e}")

def main():
    """Chương trình chính"""
    while True:
        print("\nChọn chức năng:")
        print("1. Nén tệp")
        print("2. Giải nén tệp")
        print("3. Thoát")
        
        choice = input("Nhập lựa chọn (1-3): ")
        
        if choice == '1':
            # Nén tệp
            zip_name = input("Nhập tên tệp ZIP đầu ra (ví dụ: output.zip): ")
            files = input("Nhập danh sách tệp cần nén (cách nhau bởi dấu cách): ").split()
            compress_files(zip_name, files)
        
        elif choice == '2':
            # Giải nén tệp
            zip_name = input("Nhập tên tệp ZIP cần giải nén: ")
            extract_path = input("Nhập thư mục đích (nhấn Enter để giải nén tại thư mục hiện tại): ") or "."
            extract_files(zip_name, extract_path)
        
        elif choice == '3':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()