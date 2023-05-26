# py_xlsx_textconv

Excel to text covert tool for Git.
This is a python port of [git-xlsx-textconv](https://github.com/tokuhirom/git-xlsx-textconv)

When git diff or git log -p, extract cell values in excel and format:

```
[SheetName1][TAB][A1][TAB][B1][TAB][C1][TAB]...
[SheetName1][TAB][A2][TAB][B2][TAB][C2][TAB]...
```

and compare text formats.

Example: Excel  
![excel](https://raw.githubusercontent.com/tiibun/py-xlsx-textconv/main/excel.png)

git diff  
![git diff](https://raw.githubusercontent.com/tiibun/py-xlsx-textconv/main/diff.png)


And experimental VBA support. (v0.0.4)

## This does not compare

- Style
- Auto Shapes
- ... and so on


## Install 

```
pip install py-xlsx-textconv
```

## Configuration

If `~/.config/git/attributes` (Windows: %HOMEPATH%\.config\git\attributes) does not exist, you need to creat and edit it.

```:~/.config/git/attributes
.xlsx diff=xlsx
.xlsm diff=xlsx
```

Or if you prefered per project attribute file, create `.gitattributes` file and edit it above

Append to `~/.gitconfig` (Windows: %HOMEPATH%\.gitconfig).

```:~/.gitconfig
[diff "xlsx"]
    binary = true
    textconv = PYTHONUTF8=1 py-xlsx-textconv
```

If you would like to compare values only, append `-d` option.

```:~/.gitconfig
[diff "xlsx"]
    binary = true
    textconv = PYTHONUTF8=1 py-xlsx-textconv -d
```


## Development

Install [pdm](https://pdm.fming.dev/latest/).

```
# install dependencies
pdm sync -d

# test
pdm run test
```

## LICENSE

MIT
