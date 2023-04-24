# 用python脚本辅助chatgpt翻译

——其实就是修改了一下剪贴板



最近感觉用chatgpt翻译东西很方便，银杏。（就是翻译一些关于spacex啊，nasa啊的内容）

但每次都要调教，而且隔一段时间他就可能会忘记上下文，好烦。

最开始我的解决办法挺笨的。就是吧要翻译的内容复制到记事本，然后在文本后边加上调教的内容，再喂给gpt。相当于每翻译一段话都调教一下。

但想到以前写过类似修改剪贴板的脚本时，问题就迎刃而解了

```python
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

```

请注意，运行此代码之前需要先安装 Pyperclip: `pip install pyperclip`

嗯！其实就是把复制的内容追加上一个字符串这么简单。现在可以直接复制英文文本喂给chatgpt了。

偷偷说一句，代码也是gpt写的。

