"""
在剪贴板末尾追加指定字符串，并定期检测和更新剪贴板内容。
（死循环）

append_string (str): 要追加到剪贴板末尾的字符串。
interval (float): 检测剪贴板内容变化的时间间隔（秒）。

请注意，运行此代码之前需要先安装 Pyperclip: pip install pyperclip
"""

import pyperclip
import time

# 要追加到剪贴板末尾的字符串。
append_string = '''
---
翻译，英译汉，联系上下文，要通俗易懂，在合适的地方分段落。
专业术语：
---
'''
# 检测剪贴板内容变化的时间间隔（秒）。
interval = 0.5

# 初始化上次剪贴板内容为空
last_clipboard_text = ""

while True:
    # 获取当前剪贴板中的内容
    clipboard_text = pyperclip.paste()

    # 如果内容发生变化，则追加指定字符串并复制回剪贴板
    if clipboard_text != last_clipboard_text:
        new_text = clipboard_text + append_string
        pyperclip.copy(new_text)
        print(new_text)
        last_clipboard_text = new_text

    # 等待一段时间后继续循环
    time.sleep(interval)
