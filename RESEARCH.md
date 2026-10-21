# Cơ sở soạn Privacy Policy

Ngày đối chiếu: **21/10/2026**. Phạm vi: source app hiện tại, phiên bản cấu hình `1.0.0`. Đây là hồ sơ bằng chứng cho nội dung, không phải kết quả kiểm tra lưu lượng mạng hoặc xác nhận phê duyệt Google Play.

## Bằng chứng trong project Android

Các đường dẫn dưới đây tính từ gốc project Android, không phải gốc repo chính sách.

| Hạng mục | Bằng chứng | Nội dung phản ánh trong chính sách |
| --- | --- | --- |
| Danh tính app | `app/src/main/res/values/strings.xml`, `app/build.gradle.kts` | AR Drawing Sketchar; package `com.khoaidev.ardrawingsketchar`. Tên KhoaiStore và email do chủ app cung cấp. |
| Quyền | `app/src/main/AndroidManifest.xml` | CAMERA; WRITE_EXTERNAL_STORAGE tối đa API 28. Không khai báo quyền microphone, vị trí hoặc đọc toàn thư viện ảnh. |
| Camera và video | `engine/camera/src/main/kotlin/com/khoaidev/ardrawingsketchar/engine/camera/CameraXSketchCameraController.kt` | Ghi file trên thiết bị; không bật audio khi quay. |
| Chọn ảnh | `app/src/main/java/com/khoaidev/ardrawingsketchar/feature/sketch/SketchScreen.kt`, `SketchImageSource.kt` cùng thư mục | `GetContent`; sao chép ảnh đã chọn vào cache. |
| Xóa nền | `app/src/main/java/com/khoaidev/ardrawingsketchar/feature/sketch/camera/SubjectBackgroundRemover.kt`, `gradle/libs.versions.toml` | ML Kit subject segmentation `16.0.0-beta1`, cài module qua Google Play services. |
| Tải mẫu | `app/src/main/java/com/khoaidev/ardrawingsketchar/templates/TemplateRepository.kt`, `app/build.gradle.kts` | Play Asset Delivery `2.3.0`; tải asset pack. |
| Hồ sơ trên máy | `app/src/main/java/com/khoaidev/ardrawingsketchar/feature/profile/ProfileRepository.kt` | File JSON trong app storage chứa favorites, album URI, phiên vẽ, thời lượng, thời điểm và template. |
| Project vẽ | `data/src/main/kotlin/com/khoaidev/ardrawingsketchar/data/local/FileDrawingProjectDataSource.kt`, `app/src/main/java/com/khoaidev/ardrawingsketchar/di/AppModule.kt` | Lưu dự án vào `filesDir/drawing_projects`. |
| Xuất và chia sẻ | `app/src/main/java/com/khoaidev/ardrawingsketchar/utils/MediaFileStore.kt`, `ImageShareUtils.kt` cùng thư mục | MediaStore/lưu file; Android share chooser, cấp quyền đọc file đã chọn. |
| Xóa album | `ProfileRepository.deleteAlbumEntry` | Chỉ bỏ bản ghi album; không khẳng định xóa ảnh đã xuất khỏi gallery. |
| Backup | Manifest và `app/src/main/res/xml/backup_rules.xml`, `data_extraction_rules.xml` | `allowBackup=true`; không có exclude chủ động cho app files. Chính sách đã đề cập backup/transfer theo thiết bị. |
| Quảng cáo/tài khoản | Các dependency và source của `app`, `data`, `engine/camera` | Chưa tìm thấy AdMob, Firebase Analytics, billing hoặc đăng nhập/server tài khoản do app triển khai. Không bảo đảm các bản app tương lai có cùng hành vi. |
| Trang web chính sách | `index.html`, `styles.css` | HTML/CSS cục bộ, không JS/cookie/form/analytics do trang tự thêm. Có đề cập nhà cung cấp hosting GitHub Pages. |

## Nguồn chính thức đã đối chiếu

1. [Google Play — User Data / Privacy Policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en#privacy-policy): dùng để kiểm tra phạm vi công bố, thông tin liên hệ, retention/deletion và tính truy cập công khai của trang.
2. [ML Kit — Terms & Privacy](https://developers.google.com/ml-kit/terms): cơ sở cho phần xử lý ảnh trên thiết bị.
3. [ML Kit — Android data disclosure](https://developers.google.com/ml-kit/android-data-disclosure): cơ sở cho phần dữ liệu kỹ thuật. Đối chiếu lại khi thay đổi SDK.
4. [Play Asset Delivery — Terms of service and data safety](https://developer.android.com/guide/playcore/asset-delivery): cơ sở cho phần tải mẫu qua Google Play.
5. [Android Auto Backup](https://developer.android.com/identity/data/autobackup): cơ sở cho phần sao lưu và device transfer; không suy ra toàn bộ media đều sẽ được sao lưu.
6. [GitHub General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement): cơ sở cho phần hosting website.
7. [GitHub Pages — Creating a site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site): hướng dẫn triển khai static site.

## Những điểm phải đối chiếu trước khi nộp bản phát hành

- Kiểm tra merged manifest và dependency của **đúng bản release**; báo cáo này dựa vào source, không phải phân tích AAB cuối cùng.
- Hoàn thành biểu mẫu Data safety theo định nghĩa hiện hành và toàn bộ SDK. Ảnh xử lý cục bộ, chia sẻ theo lựa chọn người dùng, backup hệ thống và dữ liệu SDK có cách phân loại khác nhau; trang chính sách không tự thay thế biểu mẫu đó.
- Không khẳng định “không thu thập dữ liệu” hoặc “không chia sẻ dữ liệu” trên Play Console nếu chưa đối chiếu mục đích xử lý và các ngoại lệ trong hướng dẫn chính thức.
- Không cam kết thời hạn xóa dữ liệu Google bằng một số ngày do nhà phát triển tự đặt. Với dữ liệu trên máy, mô tả điều kiện lưu/xóa; với email hỗ trợ, mô tả tiêu chí giữ lại để xử lý yêu cầu và nghĩa vụ pháp lý.
- Nếu thêm AdMob, đăng nhập, đồng bộ cloud, microphone hoặc SDK analytics, sửa nội dung trước khi phát hành thay đổi.
- Cần chọn độ tuổi mục tiêu và thị trường phát hành thực tế. Mục Children's privacy mô tả hành vi hiện tại, không xác nhận đủ điều kiện Families hoặc tuân thủ mọi luật quốc gia.
- Sau khi có URL thật, tích hợp liên kết trong app. Không tự đổi app trong phạm vi bộ tài liệu này.
