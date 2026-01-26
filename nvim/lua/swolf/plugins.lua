return {
    -- ColorScheme: Tokyonight
    {
        "folke/tokyonight.nvim",
        lazy = false,
        priority = 1000,
        opts = {},
        config = function()
            require("tokyonight").setup({
                style = "storm"
            })
            vim.cmd [[colorscheme tokyonight]]
        end
    },
    { 'williamboman/mason.nvim' },
    { 'williamboman/mason-lspconfig.nvim' },
    { 'neovim/nvim-lspconfig' },
    { 'hrsh7th/cmp-nvim-lsp' },
    { 'hrsh7th/nvim-cmp' },
    {
        'nvim-treesitter/nvim-treesitter',
        build = ":TSUpdate",
    },
    {
        "nvim-tree/nvim-tree.lua",
        version = "*",
        lazy = false,
        dependencies = {
            "nvim-tree/nvim-web-devicons",
        },
        config = function()
            require("nvim-tree").setup {}
        end,
    },
    {
        'nvim-telescope/telescope.nvim',
        tag = '0.1.8',
        -- branch = '0.1.x',
        dependencies = { 'nvim-lua/plenary.nvim' }
    },
    {
        "catgoose/nvim-colorizer.lua",
        event = "BufReadPre",
        opts = { -- set to setup table
            lazy_load = true,
            rgb_fn = true,
        },
    },
    {
        'mfussenegger/nvim-dap',
        dependencies = {
            -- DAP UI for better UX
            { 'rcarriga/nvim-dap-ui',        dependencies = { 'nvim-neotest/nvim-nio' } },
            -- Mason for installing debug adapters
            { 'jay-babu/mason-nvim-dap.nvim' },
            -- Node.js debugging support
            {
                'mxsdev/nvim-dap-vscode-js',
                dependencies = {
                    {
                        'microsoft/vscode-js-debug',
                        version = '1.x',
                        build = 'npm i && npm run compile vsDebugServerBundle && mv dist out',
                    },
                },
            },
            -- Python debugging support (optional)
            { 'mfussenegger/nvim-dap-python' },
        },
        config = function()
            -- Configuration goes here (Step 2)
        end,
    },
    {
        'xiyaowong/telescope-emoji.nvim',
        dependencies = { 'nvim-telescope/telescope.nvim' },
    }
}
