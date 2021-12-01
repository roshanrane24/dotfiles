-- Map leader to space
vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

local fn = vim.fn
local execute = vim.api.nvim_command

local function packer_init()
  local install_path = fn.stdpath "data" .. "/site/pack/packer/opt/packer.nvim"
  if fn.empty(fn.glob(install_path)) > 0 then
    execute("!git clone https://github.com/wbthomason/packer.nvim " .. install_path)
  end
  vim.cmd [[packadd! packer.nvim]]
  vim.cmd "autocmd BufWritePost plugins.lua PackerCompile"
end

local function sys_init()
  -- Performance
  require "impatient"
end

----- Start loading ----------
-- sys_init()

packer_init()

require("nvim-green.plugins").setup()

require("packer_compiled")

require("nvim-green.main").setup()

require("nvim-green.keymappings").setup()

vim.defer_fn(function()
  require("nvim-green.plugins").setup()
end, 0)

----- End loading ----------
