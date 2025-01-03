--- Indentation
vim.opt.shiftwidth = 4
vim.opt.smartindent = true
-- Tabs
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.expandtab = true
vim.opt.smarttab = true
-- Rendering
vim.opt.encoding = "utf-8"
vim.opt.linebreak = true
vim.opt.syntax = "enable"
vim.opt.wrap = true
vim.opt.scrolloff = 1
vim.opt.sidescrolloff = 5
vim.opt.spell = true
-- UI
vim.opt.laststatus = 1
vim.opt.ruler = true
vim.opt.wildmenu = true
vim.opt.relativenumber = true
vim.opt.number = true
vim.opt.mouse = "a"
vim.opt.cursorline = true
vim.opt.tabpagemax = 50
vim.opt.background = "dark"
vim.opt.showmode = true
-- Misc
vim.opt.backup = true
vim.opt.writebackup = true
vim.opt.swapfile = true
vim.opt.cmdheight = 1
vim.opt.autoread = true
vim.opt.backspace = "indent,eol,start"
-- set backupdir=~/.cache/vim:     "Directory to store backup files
-- set dir=~/.cache/vim            "Directory to store swap files.
-- set formatoptions+=j            "Delete comment characters when joining lines.
vim.opt.history = 1000
vim.opt.shell = "/bin/sh"
vim.opt.hidden = true
vim.opt.showmatch = true
vim.opt.autowrite = true
vim.opt.ttyfast = true
vim.opt.showcmd = true
vim.opt.list = true
vim.opt.listchars = "tab:→  ,trail:•,extends:>,nbsp:#,precedes:<"
vim.opt.updatetime = 200
vim.opt.splitbelow = true
vim.opt.splitright = true
