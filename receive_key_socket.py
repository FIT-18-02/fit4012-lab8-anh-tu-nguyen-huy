import socket
import os
from pathlib import Path

# Cấu hình mở cổng trên máy của Tú
HOST = "0.0.0.0"  # Đón nhận từ mọi IP bên ngoài kết nối vào
PORT = 6001       # Cổng riêng biệt dùng để nhận khóa (không trùng với cổng 6000 của bài lab)

def main():
    # Đảm bảo thư mục keys tồn tại trên máy bạn
    Path("keys").mkdir(parents=True, exist_ok=True)
    save_path = Path("keys/receiver_public.pem")

    print(f"[*] Đang mở cổng {PORT} chờ máy bạn mình gửi khóa công khai...")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        
        conn, addr = server.accept()
        with conn:
            print(f"[+] Đã kết nối với máy gửi khóa: {addr[0]}")
            
            # Nhận toàn bộ dữ liệu file khóa đổ về
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data += chunk
            
            # Ghi dữ liệu vào thư mục keys
            if data:
                save_path.write_bytes(data)
                print(f"[+] Đã nhận và lưu khóa thành công vào: {save_path}")
            else:
                print("[-] Lỗi: Gói dữ liệu khóa nhận được bị rỗng.")

if __name__ == "__main__":
    main()