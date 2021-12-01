local M ={}

function M.setup() 
    local utils = require('nvim-green.utils')

    local cmd = vim.cmd
    local indent = 4

    -- Search
    utils.opt('o', 'smartcase', true)
    utils.opt('o', 'ignorecase', true)
    utils.opt('o', 'incsearch', true)
    utils.opt('o', 'hlsearch', true)

    -- indentation
    cmd 'filetype plugin indent on'
    utils.opt('b', 'expandtab', true)
    utils.opt('b', 'shiftwidth', indent)
    utils.opt('b', 'smartindent', true)
    utils.opt('b', 'tabstop', indent)
    utils.opt('o', 'shiftround', true)

    -- text rendering
    cmd 'syntax enable'
    utils.opt('o', 'encoding', 'utf-8')
    -- utils.opt('o', 'roundbreak', true)
    utils.opt('o', 'wrap', true)
    -- utils.opt('o', 'display', 'lastline')
    utils.opt('o', 'scrolloff', 2 )
    utils.opt('o', 'sidescrolloff', 5 )

    -- UI
    utils.opt('o', 'laststatus', 2)
    utils.opt('o', 'ruler', true)
    utils.opt('o', 'wildmenu', true)
    utils.opt('o', 'number', true)
    utils.opt('o', 'relativenumber', true)
    utils.opt('o', 'mouse', 'a')
    utils.opt('o', 'cursorline', true)
    utils.opt('o', 'tabpagemax', 50)
    -- utils.opt('o', 'bakground', 'dark')
    utils.opt('o', 'showmode', true)

    -- Code Folding
    utils.opt('o', 'foldmethod', 'indent')
    utils.opt('o', 'foldnestmax', 4)
    utils.opt('o', 'foldenable', false)

    -- Misc
    utils.opt('o', 'hidden', true)
    utils.opt('o', 'splitbelow', true)
    utils.opt('o', 'splitright', true)
    utils.opt('o', 'wildmode', 'list:longest')
    utils.opt('o', 'backup', false)
    utils.opt('o', 'writebackup', false)
    utils.opt('o', 'swapfile', false)
    utils.opt('o', 'cmdheight', 1)
    utils.opt('o', 'autoread', true)
    utils.opt('o', 'history', 100)
    -- utils.opt('o', 'formatoptions', true)
    utils.opt('o', 'shell', '/bin/sh')
    utils.opt('o', 'showmatch', true)
    utils.opt('o', 'autowrite', true)
    utils.opt('o', 'ttyfast', true)
    utils.opt('o', 'showcmd', true)
    -- utils.opt('o', 'completeopt', 'menu:noinsert:menuone')
    utils.opt('o', 'signcolumn', 'number')

    -- colorscheme
    vim.cmd 'colorscheme gruvbox-material'

    -- Highlight on yank
    vim.cmd 'au TextYankPost * lua vim.highlight.on_yank {on_visual = false}'
end

return M
