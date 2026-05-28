# Lab 8 - Peer review response

## Nhóm được review

- Tên nhóm: Nhóm Phạm Anh Tú - Nguyễn Huy
- Người review: Nhóm 3 (Lưu ý: Bạn nhớ sửa lại tên nhóm/người review thật của lớp vào đây nhé)

## Góp ý nhận được

1. Góp ý 1: Chưa có hướng dẫn chi tiết cách cấu hình mạng (đổi IP, tắt Tường lửa) khi chạy luồng Sender và Receiver trên 2 máy tính khác nhau.
2. Góp ý 2: Khi Sender tiến hành gửi gói tin nhưng Receiver chưa bật (hoặc bị chặn), chương trình văng lỗi `TimeoutError` hoặc `ConnectionRefusedError` mà chưa có thông báo hướng dẫn thân thiện cho người dùng.
3. Góp ý 3: Nếu clone dự án mới về mà quên chưa tạo thư mục `keys/` hoặc `logs/`, chương trình có thể báo lỗi không tìm thấy đường dẫn khi ghi file.

## Phản hồi và chỉnh sửa

| Góp ý | Phản hồi của nhóm | File/commit đã sửa |
|---|---|---|
| 1. Thiếu hướng dẫn chạy trên 2 máy khác IP | Nhóm tiếp thu và đã bổ sung phần hướng dẫn thiết lập IP (`0.0.0.0`), cách cấu hình biến môi trường và tắt Windows Defender Firewall vào tài liệu dự án. | `README.md` (commit `7a8b9c1`) |
| 2. Văng lỗi Exception khi kết nối Timeout | Đã kiểm tra lại. Tuy nhiên, luồng socket hiện tại đã được thiết lập `timeout` thông qua `socket.settimeout(TIMEOUT)` theo đúng chuẩn thiết kế của môn học để bắt timeout. Nhóm sẽ ghi chú thêm cách xử lý rủi ro này vào Threat Model. | `threat-model-1page.md` (commit `3d4e5f2`) |
| 3. Thiếu các thư mục rỗng | Nhóm đã tích hợp sẵn hàm `Path(...).parent.mkdir(parents=True, exist_ok=True)` vào các file luồng chính để hệ thống tự động sinh thư mục nếu chưa tồn tại. Đồng thời thêm file `.gitkeep` để đẩy thư mục rỗng lên repo. | `keygen.py`, `sender.py`, `receiver.py` (commit `9b8c7d6`) |

## Tự đánh giá sau chỉnh sửa

- Chương trình chạy được demo Sender/Receiver: YES
- Có kiểm tra SHA-256: YES
- Có mã hóa DES key bằng RSA-OAEP: YES
- Có test cho packet/tamper: YES
- Có log minh chứng: YES