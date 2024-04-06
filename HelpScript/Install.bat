set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/c cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
mkdir "C:\Program Files\LolRehab"
xcopy . "C:\Program Files\LolRehab" /h /i /c /k /e /r /y
echo| SchTasks /Create /RU system /NP /XML  "LolRehab.xml" /TN LolRehab
Pause