# py_xlsx_textconv

git diff wrapper for Excel.
This is a python port of [git-xlsx-textconv](https://github.com/tokuhirom/git-xlsx-textconv)

## Install 

```
git clone https://github.com/tiibun/py-xlsx-textconv
pip install .
```

## Config

If `~/.config/git/attributes` does not exist, you need to creat and edit it.

```:~/.config/git/attributes
.xlsx diff=xlsx
.xlsm diff=xlsx
```

Add below to `~/.gitconfig`.

```:~/.gitconfig
[diff "xlsx"]
    binary = true
    textconv = py-xlsx-textconv
```

## LICENSE

MIT
