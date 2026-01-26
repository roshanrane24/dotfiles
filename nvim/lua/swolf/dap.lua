local dap = require('dap')
local dapui = require('dapui')

-- DAP UI Setup
dapui.setup({
    layouts = {
        {
            elements = { 'scopes', 'breakpoints', 'stacks', 'watches' },
            size = 40,
            position = 'left',
        },
        {
            elements = { 'console' },
            size = 0.25,
            position = 'bottom',
        },
    },
})

-- Auto-open/close UI
dap.listeners.after.event_initialized['dapui_config'] = function() dapui.open({ reset = true }) end
dap.listeners.before.event_terminated['dapui_config'] = function() dapui.close() end
dap.listeners.before.event_exited['dapui_config'] = function() dapui.close() end

-- Node.js Adapter (vscode-js-debug)
require('dap-vscode-js').setup({
    debugger_path = vim.fn.stdpath('data') .. '/mason/packages/js-debug-adapter',
    adapters = { 'pwa-node', 'pwa-chrome' },
})

-- Node.js Configurations
local js_filetypes = { 'javascript', 'typescript', 'javascriptreact', 'typescriptreact' }
for _, lang in ipairs(js_filetypes) do
    dap.configurations[lang] = {
        {
            type = 'pwa-node',
            request = 'launch',
            name = 'Launch Node File',
            program = '${file}',
            cwd = '${workspaceFolder}',
            sourceMaps = true,
            skipFiles = { '<node_internals>/**', 'node_modules/**' },
            resolveSourceMapLocations = { '${workspaceFolder}/**', '!**/node_modules/**' },
        },
        {
            type = 'pwa-node',
            request = 'attach',
            name = 'Attach to Node Process',
            processId = require('dap.utils').pick_process,
            cwd = '${workspaceFolder}',
            sourceMaps = true,
        },
    }
end

-- Python Adapter with Poetry
local python_path = vim.fn.exepath('python3')       -- Fallback
if vim.fn.glob('pyproject.toml') ~= '' then
    -- Use Poetry's virtualenv if available
    local poetry_python = vim.fn.system('poetry env info --path')
    if poetry_python ~= '' then
        python_path = poetry_python:gsub('\n$', '') .. '/bin/python'
    end
end
require('dap-python').setup(python_path)

-- Python Configurations
dap.configurations.python = {
    {
        type = 'python',
        request = 'launch',
        name = 'Launch Python File with Poetry',
        program = '${file}',
        pythonPath = python_path,
        cwd = '${workspaceFolder}',
        console = 'integratedTerminal',
    },
}


-- Keybinds for DAP
vim.keymap.set('n', '<leader>b', require('dap').toggle_breakpoint, { desc = 'Toggle Breakpoint' })
vim.keymap.set('n', '<F5>', require('dap').continue, { desc = 'Continue/Start Debugging' })
vim.keymap.set('n', '<F10>', require('dap').step_over, { desc = 'Step Over' })
vim.keymap.set('n', '<F11>', require('dap').step_into, { desc = 'Step Into' })
vim.keymap.set('n', '<F12>', require('dap').step_out, { desc = 'Step Out' })
vim.keymap.set('n', '<leader>dr', require('dap').repl.open, { desc = 'Open REPL' })
vim.keymap.set('n', '<leader>dt', require('dap').terminate, { desc = 'Terminate' })
vim.keymap.set('n', '<leader>dui', require('dapui').toggle, { desc = 'Toggle DAP UI' })
