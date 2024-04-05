I wasted lots of my time playing League so I'm trynna making this app to shut down LoL when I exceeded my time limit.  
  
Todo list: 
- Ghi chép lại lịch sử chơi game để tránh đấu tập enjoyer (probably done, có thể có edge case chưa check). 
- Đọc lịch sử game từ file để resume (Done).  
- Reading Ini file (Done).  
- Thuật toán kiểm tra thời gian chơi so với các limit mình imposed (Done).  
(Chưa xong)  
- Front end, User Interface (Tách rời với chương trình chính).
- Cho phép chỉnh lại deadline nhưng sẽ có delay.
- Cho phép emergency deadline removal.
- Cho phép temporal disable.
- Gradual time tightening (7 game in 7 days, 4 game in 7 days, etc...)
.After everything is done and finish:
- Running as system service.
- Installer.


Buoc 1: Convert sex.py sang file exe. (DONE)
Buoc 2: Test cach nao do de khoi tao Windows Service chay sex.exe
Buoc 3: Viet ham wrapper de thuc hien khoi tao, disable, uninstall sex.exe
Buoc 4: Convert wrapper do thanh mot standalone application de nguoi dung co the bat/tat-install de dang.
Buoc 4: Them option install hard core va gan cung du lieu hardcore for extreme league fanboy.

Bakup: SchTasks /Create /TN LolRehab /RU "SYSTEM" /NP /SC ONLOGON /TR ""
/it
Todo List: Update Ini file by editing bat.
Todo List: Launch Scheduled Task.
Todo List: Allow for [Custom game, matched game] check with [Aram, Summoner's Rift] choice