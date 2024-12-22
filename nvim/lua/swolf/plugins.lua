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
            vim.cmd[[colorscheme tokyonight]]
        end
    }
}
