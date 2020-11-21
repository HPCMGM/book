# 2. Python环境配置

## 2.1 头部信息配置

```bash
set ts=4 " 四个字符
set expandtab " 转换空格
set autoindent " 自动缩进
set nu! " 显示行号
syntax on " 语法高亮
set mouse=a " 启用鼠标
set textwidth=79 " 设置行最大宽度
set autoread " 自动刷新文件
set autowriteall " 自动刷新文件
set showmatch " 自动补全符号
set pastetoggle=<F12> " F12键复制保留格式

function HeaderPython()
    call append(0, "#!/usr/bin/env python")
    call append(1, "# -*- coding:utf-8 -*-")
    call append(2, "# Power by HPCM " . strftime('%Y-%m-%d %T', localtime()))
    call append(3, "# Filename " . expand("%:t"))
    endf
autocmd bufnewfile *.py call HeaderPython()
map <F5> :call RunPython()<CR>
func! RunPython()
    if &filetype == 'python'
        exec "!time python2.7 %"
    endif
endfunc
au BufWritePost * if getline(1) =~ "^#!/usr/bin/env python" | silent !chmod +x <afile> | endif | endif
```

## 2.2 F5运行py文件

```bash
au BufWritePost * if getline(1) =~ "^#!/usr/bin/env python" | silent !chmod +x <afile> | endif | endif
```

