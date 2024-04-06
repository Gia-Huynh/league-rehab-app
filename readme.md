I wasted lots of my time playing League so I'm trynna making this app to shut down LoL when I exceeded my time limit.  
  
Tính năng: 
- Ghi chép lại lịch sử chơi game để tránh đấu tập enjoyer (có thể có edge case chưa check). 
- Đọc lịch sử game từ file để resume.  
- Đọc file cấu hình. 
- Nhiều giới hạn khác nhau (cho 1 ngày, 1 tuần, 1 tháng,...).
- Allow for [Custom game, matched game] check with [Aram, Summoner's Rift] choice (Done).
- Thuật toán kiểm tra thời gian chơi so với các limit mình imposed.
- Running as system service (Done, Scheduled Task).
- Installer.
(Chưa xong)  
- Front end, User Interface (Tách rời với chương trình chính) (Có lẽ mình chỉ cần làm thêm code hỗ trợ setup ini file là được).
- Cho phép chỉnh lại deadline nhưng sẽ có delay (No).
- Cho phép emergency deadline removal (No).
- Cho phép temporal disable (No).

Todo List: Update Ini file by editing bat.