require('mason').setup({})

require('mason-nvim-dap').setup({
    ensure_installed = { 'js-debug-adapter', 'python' },
    automatic_installation = true,
    handlers = {},
})
require('mason-lspconfig').setup({
    ensure_installed = { 'lua_ls' }, -- Ensure Pyright is installed
    handlers = {
        function(server_name)
            if server_name == 'pyright' then
                vim.lsp.config('pyright', {
                    capabilities = require('cmp_nvim_lsp').default_capabilities(),
                    filetypes = { 'python' },
                    before_init = function()
                        print('Attempting to start Pyright')
                    end,
                    on_init = function(client)
                        print('Pyright initialized for root: ' .. client.config.root_dir)
                    end,
                    on_error = function(err)
                        print('Pyright error: ' .. vim.inspect(err))
                    end,
                    on_new_config = function(config, root_dir)
                        -- Dynamically detect Poetry venv path from project root
                        local env_path = vim.fn.trim(vim.fn.system('cd "' ..
                        root_dir .. '" && poetry env info -p 2>/dev/null'))
                        if string.len(env_path) > 0 then
                            local python_path = env_path ..
                            '/bin/python'                                 -- Adjust for Windows if needed: '/Scripts/python.exe'
                            config.settings.python.pythonPath = python_path
                            vim.notify('Pyright using Poetry pythonPath: ' .. python_path, vim.log.levels.INFO)
                        else
                            -- Fallback to system Python
                            local fallback = vim.fn.exepath('python3')
                            config.settings.python.pythonPath = fallback
                            vim.notify('Pyright fallback pythonPath: ' .. fallback, vim.log.levels.WARN)
                        end
                    end,
                    settings = {
                        python = {
                            analysis = {
                                typeCheckingMode = "basic",
                                autoSearchPaths = true,
                                useLibraryCodeForTypes = true,
                                diagnosticMode = 'workspace',
                            },
                        },
                    },
                    root_dir = require('lspconfig.util').root_pattern('pyproject.toml', '.git'),
                })
            else
                require('lspconfig')[server_name].setup({
                    capabilities = require('cmp_nvim_lsp').default_capabilities()
                })
            end
        end,
    },
})
