🐺 Grey Wolf Optimizer (GWO) – Python Implementation

Repo này cung cấp mã nguồn cài đặt (implement) thuật toán Grey Wolf Optimizer (GWO) bằng Python và chạy demo tối ưu hóa hàm Sphere — một hàm benchmark phổ biến trong tối ưu hóa.

📌 1. Giới thiệu

Grey Wolf Optimizer (GWO) là thuật toán tối ưu hóa meta-heuristic được đề xuất bởi Mirjalili vào năm 2014. Thuật toán mô phỏng cấu trúc xã hội và chiến thuật săn mồi của bầy sói xám (Canis lupus), bao gồm ba con đầu đàn:

Alpha (α) — lời giải tốt nhất

Beta (β) — lời giải tốt thứ hai

Delta (δ) — lời giải tốt thứ ba

Các cá thể còn lại gọi là Omega (ω), di chuyển dựa trên vị trí của α, β và δ.

Thuật toán được ứng dụng rộng rãi trong:

Tối ưu hóa đa chiều

Machine learning (tối ưu tham số mô hình)

Điều khiển & Robotics

Tối ưu hóa kỹ thuật, bài toán phi tuyến

⚙️ 2. Yêu cầu môi trường

Cài đặt Python 3 và thư viện:

pip install numpy matplotlib
🧮 3. Hàm Sphere được tối ưu

Hàm Sphere là một hàm benchmark đơn giản:

<img width="189" height="108" alt="image" src="https://github.com/user-attachments/assets/e8ad3325-d587-437f-9262-69a06aa2511c" />


Đặc điểm:

Có nghiệm tối ưu toàn cục tại x = (0,0,…,0)

Là hàm lồi → dễ để kiểm tra khả năng hội tụ

📈 4. Kết quả chạy thử

Chương trình sẽ in ra:

Best position: [...]
Best value: <giá trị gần 0>

Và hiển thị đồ thị hội tụ thể hiện fitness giảm dần qua các vòng lặp.

Hình minh họa:
<img width="749" height="498" alt="image" src="https://github.com/user-attachments/assets/e8eedc29-5fcd-44c7-a20a-7084da2ed04b" />

Fitness giảm rất nhanh ở giai đoạn đầu (khai thác cao)

Chậm dần khi tiến gần nghiệm tối ưu

📌 5. Cách chạy chương trình

Trong terminal:

python main.py
