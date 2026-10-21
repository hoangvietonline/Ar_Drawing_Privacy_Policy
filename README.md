# AR Drawing Sketchar — Privacy Policy

Trang Privacy Policy tiếng Anh dành cho **AR Drawing Sketchar**, nhà phát triển **KhoaiStore**, liên hệ **hvdevelopapplication@gmail.com**.

Được soạn ngày **21/10/2026** dựa trên mã nguồn hiện tại của app. Không cần Node.js, framework, build, hay tài nguyên bên ngoài để hiển thị. Toàn bộ nội dung luôn có trong HTML, kể cả khi tắt JavaScript.

## Đưa vào repo GitHub riêng

1. Tạo repo GitHub riêng. Với GitHub Free, chọn **Public** để sử dụng GitHub Pages.
2. Upload **nội dung bên trong thư mục này** vào thư mục gốc repo mới: `index.html`, `styles.css`, `.nojekyll`, `README.md`, `RESEARCH.md`. Không upload toàn bộ project Android.
3. Mở **Settings → Pages → Build and deployment**.
4. Chọn **Deploy from a branch**, nhánh **main**, thư mục **/ (root)**, rồi **Save**.
5. Đợi GitHub triển khai; lấy URL tại **Settings → Pages → Visit site**. Nếu repo thuộc `hoangvietonline`, URL thường có dạng `https://hoangvietonline.github.io/TEN-REPO/`.
6. Kiểm tra URL công khai ở cửa sổ ẩn danh, trên điện thoại, và thử liên kết email.

Tài liệu chính thức: [Tạo GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

Repo riêng của trang: [hoangvietonline/Ar_Drawing_Privacy_Policy](https://github.com/hoangvietonline/Ar_Drawing_Privacy_Policy). Thư mục này dùng Git riêng với nhánh `main`; remote `origin` trỏ tới repo chính sách. Không dùng remote của project Android để cập nhật trang.

Sau khi bật Pages từ `main` và `/ (root)`, URL dự kiến là [AR Drawing Sketchar Privacy Policy](https://hoangvietonline.github.io/Ar_Drawing_Privacy_Policy/). Xác nhận trạng thái triển khai tại Settings → Pages trước khi dùng URL trong Play Console.

## Gắn vào ứng dụng và Google Play

- Điền URL GitHub Pages đã hoạt động vào mục **Privacy policy** của Play Console.
- Cho mục **Settings → Privacy policy** trong app mở URL đó hoặc hiển thị toàn bộ nội dung chính sách. Code hiện tại còn thông báo mẫu “Privacy information will be available here.”, nên bước tích hợp này vẫn cần thực hiện sau khi có URL.
- Đối chiếu **Data safety** với bản phát hành và SDK thực tế. Không suy ra “không thu thập dữ liệu” chỉ từ việc app không có máy chủ riêng. Xem `RESEARCH.md`.
- Kiểm tra tên nhà phát triển, email và tên app khớp trang Google Play. Cập nhật chính sách nếu đổi chức năng, thêm quảng cáo/analytics/tài khoản hoặc thay đổi SDK/backup.
- Độ tuổi mục tiêu và quốc gia phát hành chưa được cung cấp. Chính sách không tự đặt mốc 13 tuổi và không tuyên bố app đã đáp ứng chương trình Families. Nếu nhắm tới trẻ em, cần kiểm tra riêng khai báo độ tuổi và điều kiện sử dụng các SDK trước khi phát hành.

## Sửa nội dung

Sửa trực tiếp `index.html`; đổi ngày “Last updated” khi thực hành xử lý dữ liệu thay đổi. Giao diện nằm trong `styles.css`. Không có công cụ theo dõi, font từ xa, biểu mẫu gửi dữ liệu hoặc JavaScript trong trang này.

`RESEARCH.md` lưu bằng chứng và nguồn tham khảo cho nhà phát triển; nội dung chính sách công khai nằm ở `index.html`.
