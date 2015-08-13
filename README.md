# test1 remote 333
export EDITOR=vim

#PS1='[\u@\h \W]\$ '  # Default
PS1='😂 \[\e[1;32m\][\u@\h \W]\$\[\e[0m\] '

export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced


# test1 remote 222


set tabstop=4
set shiftwidth=4
set smarttab
set expandtab
set softtabstop=4
set nu
set number
colorscheme delek

syntax on

autocmd BufRead *.py set smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class

" This will show any extraneous whitespace at the end of lines, and make visible any tab characters
set list
set listchars=tab:>-,trail:^
