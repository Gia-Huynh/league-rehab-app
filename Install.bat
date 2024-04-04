set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/c cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
echo| SchTasks /Create /RU system /NP /TN "LolRehab" /SC ONLOGON /TR "C:\Users\Za\Desktop\SchoolWork\Nam 4\LinhTinhT\league-rehab-app\dist\sex.exe"
pause