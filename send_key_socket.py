import socket
import sys
from pathlib import Path

# Đường dẫn file khóa công khai đang có sẵn trên máy Receiver
KEY_PATH = Path("keys/receiver_public.pem")

def main():
    if not KEY_PATH.exists():
        print(f"[-] Lỗi: Không tìm thấy file {KEY_PATH}. Hãy chạy keygen.py trước!")
        sys.exit(1)

    # Hỏi IP máy của Tú (Sender) để kết nối
    target_ip = input("Nhập địa chỉ IP của máy nhận khóa (máy của Tú): ").strip()
    port = 6001

    print(f"[*] Đang kết nối tới {target_ip}:{port} để gửi khóa...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((target_ip, port))
            
            # Đọc file khóa và gửi toàn bộ qua socket
            key_data = KEY_PATH.read_bytes()
            sock.sendall(key_data)
            
            print("[+] Đã gửi file receiver_public.pem sang thành công!")
    except Exception as e:
        print(f"[-] Lỗi kết nối: {e}")

if __name__ == "__main__":
    main()