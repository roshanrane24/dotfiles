-- Leader
vim.g.mapleader = " "
-- Explorer
-- vim.keymap.set("n", "<leader>ex", vim.cmd.Ex)
-- Buffer
vim.keymap.set("n", "<C-b>n", vim.cmd.bnext)
vim.keymap.set("n", "<C-b>p", vim.cmd.bprev)
-- nvim tree
vim.keymap.set("n", "<F8>", vim.cmd.NvimTreeToggle)
