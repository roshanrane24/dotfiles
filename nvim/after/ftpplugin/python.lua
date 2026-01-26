-- Automatically tell pylsp to use Poetry's venv for the current project
local venv = vim.fn.trim(vim.fn.system("poetry env info --path 2>/dev/null"))
if vim.v.shell_error == 0 then
  vim.env.VIRTUAL_ENV = venv
  vim.env.PATH = venv .. "/bin:" .. vim.env.PATH
end

