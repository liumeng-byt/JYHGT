import win32gui
import win32con


class WindowsMsgR(object):
    def __init__(self):
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32gui.GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbarDemo"
        wc.lpfnWndProc = {win32con.WM_DESTROY: self.On_destroy, }
        classAtom = win32gui.RegisterClass(wc)
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(classAtom, "Taskbar Demo", style,0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,0, 0, hinst, None)
        hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        nid = (self.hwnd, 0, win32gui.NIF_ICON, win32con.WM_USER + 20, hicon, "Demo")
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
    def On_destroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        win32gui.PostQuitMessage(0)  # Terminate the app.

    def show_msg(self, title, msg):
        nid = (self.hwnd,  # 句柄
                0,  # 托盘图标ID
                win32gui.NIF_INFO,  # 标识
                  0,  # 回调消息ID
                  0,  # 托盘图标句柄
                  "TestMessage",  # 图标字符串
                  msg,  # 气球提示字符串
                  0,  # 提示的显示时间
                  title,  # 提示标题
                  win32gui.NIIF_INFO  # 提示用到的图标
                )

        win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, nid)


# if __name__ == '__main__':
#     WindowsMsgR().show_msg("标题", "text")