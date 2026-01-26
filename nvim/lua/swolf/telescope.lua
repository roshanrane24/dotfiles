local builtin = require('telescope.builtin')
local telescope = require('telescope')

telescope.load_extension('emoji')

vim.keymap.set('n', '<C-p>', builtin.find_files, { desc = 'Telescope find files' })
vim.keymap.set('n', '<leader>f', builtin.live_grep, { desc = 'Telescope live grep' })
vim.keymap.set('n', '<leader>F', builtin.grep_string, { desc = 'Telescope grep selected' })
vim.keymap.set('n', '<C-b>b', builtin.buffers, { desc = 'Telescope buffers' })
vim.keymap.set('n', '<leader>fh', builtin.help_tags, { desc = 'Telescope help tags' })
vim.keymap.set('n', '<leader>pp', builtin.commands, { desc = 'Telescope Commands' })

-- Git
vim.keymap.set('n', '<C-g>g', builtin.git_files, { desc = 'Telescope Git ls' })
vim.keymap.set('n', '<C-g>cc', builtin.git_commits, { desc = 'Telescope Git List Commits with diff preview' })
vim.keymap.set('n', '<C-g>cb', builtin.git_bcommits, { desc = 'Telescope Git List Commits with diff preview (Buffer)' })
vim.keymap.set('n', '<C-g>b', builtin.git_branches, { desc = 'Telescope Git List Branches' })
vim.keymap.set('n', '<C-g>s', builtin.git_status, { desc = 'Telescope Git Status' })

-- Tree Sitter
vim.keymap.set('n', '<leader>ts', builtin.treesitter, { desc = 'Telescope Treesitter' })

-- emoji
vim.keymap.set('n', '<leader>;', function () telescope.extensions.emoji.emoji() end, { desc = 'Find emoji 😎' })

-- Config
-- telescope.setup {
--     extensions = {
--         emoji = {
--             action = function(emoji)
--                 -- Insert or copy
--                 vim.fn.setreg('+', emoji.value)
--                 print('Copied: ' .. emoji.value)
--             end,
--         },
--     },
-- }
