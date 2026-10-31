# AR Drawing Sketchar — Terms & Privacy

Bộ tài liệu tiếng Anh cho **AR Drawing Sketchar**, package `com.khoaidev.ardrawingsketchar`, nhà phát triển **KhoaiStore**, email **hvdevelopapplication@gmail.com**. Đối chiếu source phiên bản **1.0.2 (3)** ngày **31/10/2026**.

## Trang công khai

- Privacy Policy: https://hoangvietonline.github.io/Ar_Drawing_Privacy_Policy/
- Terms of Use: https://hoangvietonline.github.io/Ar_Drawing_Privacy_Policy/terms.html
- Repo: https://github.com/hoangvietonline/Ar_Drawing_Privacy_Policy

GitHub Pages dùng nhánh `main`, thư mục gốc. HTML/CSS tĩnh, không cần build, không có JavaScript hoặc tài nguyên giao diện bên ngoài.

## Thư mục trong project, Git repo riêng

Bộ tài liệu nằm tại `ARDrawingSketchar/Ar drawing Privacy Policy/`, có `.git` riêng và remote trên. Project Android đã bỏ qua thư mục này bằng `.gitignore`; không thêm nó thành submodule hoặc commit vào repo Android.

Sửa `index.html`, `terms.html` và `styles.css`, cập nhật ngày sửa rồi commit/push từ thư mục này. Không push mã nguồn Android vào repo policy.

## Đóng gói bản đọc ngoại tuyến

Chạy từ thư mục này:

```sh
python3 sync_offline.py
```

Script đưa **toàn bộ** hai tài liệu vào `app/src/main/assets/legal/en-privacy.html` và `en-terms.html`, nhúng CSS và đổi liên kết giữa hai bản để đọc khi mất mạng. Hai file assets được Android đóng gói vào APK/AAB. Nếu repo policy nằm nơi khác, dùng `python3 sync_offline.py --project-root "/duong/dan/ARDrawingSketchar"`.

Ứng dụng đã dùng các URL trên trong `LegalUrls.kt` và có màn hình pháp lý với bản dự phòng ngoại tuyến. Hai file assets thuộc repo ứng dụng; repo website được quản lý độc lập.

## Phạm vi đối chiếu

Tài liệu bao gồm camera, ảnh/video không microphone, xử lý ảnh trên máy, lưu trữ/xuất/chia sẻ, AdMob và lựa chọn quảng cáo, ML Kit, Asset Delivery, backup Android, Google Play Billing, subscription/hủy/hoàn tiền, quyền nội dung và liên hệ.

Billing catalog hiện chưa có product ID. Terms chỉ áp dụng mua Premium khi được cung cấp, lấy giá và chu kỳ thật tại checkout, không dùng giá minh họa trong giao diện. Độ tuổi mục tiêu, thị trường và danh sách ad vendors trong tài khoản phát hành cần được chủ app đối chiếu thực tế; tài liệu này không tự xác nhận các cấu hình đó.

Nguồn đối chiếu: [Google Mobile Ads](https://developers.google.com/admob/android/privacy/play-data-disclosure), [ML Kit](https://developers.google.com/ml-kit/android-data-disclosure), [hủy Google Play subscription](https://support.google.com/googleplay/answer/7018481). `RESEARCH.md` lưu lịch sử nghiên cứu; source hiện tại và bản phát hành thực tế là cơ sở khi cập nhật Data safety.
