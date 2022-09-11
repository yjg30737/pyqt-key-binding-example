# pyqt-key-binding-example
Example and personal practice of show and edit every key mapping data with table widget

This can get all key mapping data of application.

## Requirements
* PyQt5

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-key-binding-example.git --upgrade`

## Example
```python
if __name__ == "__main__":
    import sys
    app = DarkNotepadApp(sys.argv) # https://github.com/yjg30737/pyqt-dark-notepad
    # or you can make your own application
    w = KeyBindingWindow()
    w.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/189506381-06ef7ae0-f6cd-4e8f-882d-367e9b853de1.mp4

## Note
If this were C++ Qt, I would do it with orthodox way such as using `QStandardItemEditorCreator`. But that is nowhere to be found in PyQt/PySide, so i have to do it on my own.

I'm still working on it.

Still a lot of things need to be fixed or taken care of such as inconsistent order of key mapping list, database feature.

btw, You see that second column's cell? Looks ugly, right? Sadly, I don't even care about style anymore. The style took a lot of time and make me so dizzy that i can't focus on the real goal.

## See Also
* <a href="https://doc.qt.io/qtforpython/examples/example_widgets_itemviews_stardelegate.html">Star Delegate Example</a> - nice article to read if you want to make QTableWidget/QTableView with certain form included complicated designed widget inside each cells.
