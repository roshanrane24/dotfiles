">>> OPTIONS >>>
set nocompatible
">>> Search
set hlsearch                "Search Highlighting
set incsearch               "Increamental Search
set ignorecase              "Ignore case while searching
set smartcase               "Auto Case sensitive
">>> Indentation
set autoindent              "New lines inherit the indentation of previous lines.
set expandtab               "Convert Tabs into Spaces
set tabstop=4               "Indent using four spaces.
set smarttab                "Insert “tabstop” number of spaces when the “tab” key is pressed.
set shiftwidth=4            "When shifting, indent using four spaces
set shiftround              "When shifting lines, round the indentation to the nearest multiple of “shiftwidth.”
filetype indent on			"Indent based on file
"set smartindent
">>> Performance
"set complete-=1            "Limit the files searched for auto-completes.
"set lazydraw               "Don’t update screen during macro and script execution.
">>> Text Rendering
set encoding=utf-8          "Use an encoding that supports unicode.
set linebreak               "Avoid wrapping a line in the middle of a word.
syntax enable               "Syantax Highlighting
set wrap                    "Enable line wrapping.
set display+=lastline       "Always try to show a paragraph’s last line.
set scrolloff=1             "The number of screen lines to keep above and below the cursor
set sidescrolloff=5         "The number of screen columns to keep to the left and right of the cursor.
"set spell                  "spell Check
">>> UI
set laststatus=2            "Alway show statusbar
set ruler                   "Line No. & Column No.(Cursor Position)
set wildmenu                "Display command line’s tab complete options as a menu.
set relativenumber          "Show line number on the current line and relative numbers on all other lines
set number          "Show line number on the current line
set mouse=a                 "Enable mouse for scrolling and resizing
set cursorline              "Highlight the line currently under cursor
set tabpagemax=50           "Maximum number of tab pages that can be opened from the command line.
set background=dark         "Use colors that suit a dark background
set showmode                "Show mode on statusbar
">>> Code Folding
set foldmethod=indent       "Fold based on indention levels.
set foldnestmax=3           "Only fold up to three nested levels.
set nofoldenable            "Disable folding by default.
">>> Misc
set nobackup                "Disable Backup Files
set nowritebackup           "Disable Backup
set noswapfile              "Diasble Swap Files
set cmdheight=2             "Commad Line height
set autoread                "Automatically re-read files if unmodified inside Vim
set backspace=indent,eol,start "Allow backspacing over indention, line breaks and insertion start.
set backupdir=~/.cache/vim: "Directory to store backup files
set dir=~/.cache/vim        "Directory to store swap files.
set formatoptions+=j        "Delete comment characters when joining lines.
set history=1000            "Increase the undo limit
set shell=/bin/sh           "Shell to execute commad
set hidden                  "Hide files in the background instead of closing them.
set showmatch               "Use % to jump between matching brackets
set autowrite               "Save when switching between
set ttyfast                 "More Chars to screen for redrawing
set showcmd
set list                    "show hidden characters
set listchars=tab:,trail:,extends:>,nbsp:#,precedes:<
"set paste                   "Paste from clipboard
set updatetime=300
set splitbelow
set splitright
set completeopt+=noinsert,menuone,noselect
set termguicolors
set background=dark
set shortmess+=c
if has("nvim-0.5.0") || has("patch-8.1.1564")
  " Recently vim can merge signcolumn and number column into one
  set signcolumn=number
else
  set signcolumn=yes
endif
">>> ALACRITTY
if !has('nvim')
  set ttymouse=sgr            "Termianl Mouse Supoort
endif
"<<< OPTIONS <<<

">>> PLUGINS >>>
" >>> NerdTree
let g:NERDTreeGitStatusWithFlags = 1
let g:NERDTreeChDirMode=2
let g:NERDTreeIgnore=['\.rbc$', '\~$', '\.pyc$', '\.db$', '\.sqlite$', '__pycache__', 'node_modules']
let g:NERDTreeSortOrder=['^__\.py$', '\/$', '*', '\.swp$', '\.bak$', '\~$']
let g:NERDTreeShowBookmarks=1
let g:nerdtree_tabs_focus_on_files=1
let g:NERDTreeMapOpenInTabSilent = '<RightMouse>'
set wildignore+=*/tmp/*,*.so,*.swp,*.zip,*.pyc,*.db,*.sqlite
">>> SimplyFold
let g:SimpylFold_docstring_preview=1
let g:SimpylFold_fold_docstring=1
let b:SimpylFold_fold_docstring=1
let g:SimpylFold_fold_import=1
let b:SimpylFold_fold_import=1
let g:SimpylFold_fold_blank=0
let b:SimpylFold_fold_blank=0
">>> ALE
" let g:ale_linter={
"       \ 'python': ['flake8', 'pylint'],
"       \ 'javascript': ['prettier', 'eslint'],
"       \ 'typescript': ['prettier', 'eslint']}
" "      \ 'css': ['prettier'],
" "      \ 'html': ['prettier'],
" "      \ 'vue': ['prettier'],
" "      \ 'yaml': ['prettier'],
" "      \ 'sql': ['sql-lint'],
" "      \ 'vim': ['vimls'],
" "      \ 'docker': ['docker-lint'],
" "      \ 'go': ['bingo'],
" "      \ 'shell': ['shellcheck'],
" "      \ 'c++': ['clangd'],
" "      \ 'c': ['clangd'],
" "      \ 'markdown': ['prettier']
" 
" let g:ale_fixers = {'python':['autopep8', 'isort'],
"       \ 'javascript':['prettier']}
" let g:ale_disable_lsp = 1
" let g:ale_virtualenv_dir_names = []
">>> FZF
let g:fzf_action = {
  \ 'ctrl-t': 'tab split',
  \ 'ctrl-h': 'split',
  \ 'ctrl-v': 'vsplit' }

let g:fzf_colors =
\ { 'fg':      ['fg', 'Normal'],
  \ 'bg':      ['bg', 'Normal'],
  \ 'hl':      ['fg', 'Comment'],
  \ 'fg+':     ['fg', 'CursorLine', 'CursorColumn', 'Normal'],
  \ 'bg+':     ['bg', 'CursorLine', 'CursorColumn'],
  \ 'hl+':     ['fg', 'Statement'],
  \ 'info':    ['fg', 'PreProc'],
  \ 'border':  ['fg', 'Ignore'],
  \ 'prompt':  ['fg', 'Conditional'],
  \ 'pointer': ['fg', 'Exception'],
  \ 'marker':  ['fg', 'Keyword'],
  \ 'spinner': ['fg', 'Label'],
  \ 'header':  ['fg', 'Comment'] }

" See `man fzf-tmux` for available options
if exists('$TMUX')
  let g:fzf_layout = { 'tmux': '-p90%,60%' }
else
  let g:fzf_layout = { 'window': { 'width': 0.9, 'height': 0.6 } }
endif
">>> Rainbow
let g:rainbow_active = 1
">>> Polyglot
"let g:polyglot_disabled = ['autoindent']
let g:polyglot_disabled = ['sensible']
">>> AirLine
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail_improved'
let g:airline_powerline_fonts = 1
"let g:airline_statusline_ontop = 1
let g:airline#extensions#whitespace#enabled = 0
let g:airline_theme='badwolf'
">>> COC
let g:coc_global_extensions = ['coc-json', 'coc-git', 'coc-html',
                          \ 'coc-sh', 'coc-sql', 'coc-clangd',
                          \ 'coc-clang-format-style-options',
                          \ 'coc-cmake', 'coc-css', 'coc-flutter',
                          \ 'coc-fzf-preview', 'coc-go', 'coc-graphql',
                          \ 'coc-htmldjango', 'coc-java', 'coc-tsserver',
                          \ 'coc-xml', 'coc-yaml', 'coc-pydocstring',
                          \ 'coc-pyright', 'coc-snippets', 'coc-diagnostic',
                          \ 'coc-java', 'coc-toml']

">>> Vim-Plug
call plug#begin('~/.vim/plugged')

Plug 'scrooloose/nerdtree'                          "NERDtree
Plug 'tmhedberg/SimpylFold'							"Code Follding
"Plug 'dense-analysis/ale'							"SyantaxChecking
Plug 'nvie/vim-flake8'								"PEP-8 Python Syntax
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }	"Fuzzy Finder
Plug 'tpope/vim-fugitive'							"Git
Plug 'luochen1990/rainbow'						    "Rainbow Brackets
Plug 'tpope/vim-surround'							"Surround
Plug 'preservim/tagbar'								"Tagbar
Plug 'Shougo/neopairs.vim'                          "AutoComplete Brackets&Quotes
Plug 'sheerun/vim-polyglot'							"Language Pack
Plug 'jeetsukumaran/vim-buffergator'				"Buffer Window
Plug 'vim-airline/vim-airline'                      "Airline Status
Plug 'vim-airline/vim-airline-themes'               "Airline Status Themes
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'preservim/nerdcommenter'                      "NERDCommentator
Plug 'RRethy/vim-hexokinase'                        "Colorizer from code
"COC
Plug 'neoclide/coc.nvim', {'branch': 'release'}
"COLORSCHEME
Plug 'morhetz/gruvbox'
Plug 'tomasr/molokai'
Plug 'joshdick/onedark.vim'
Plug 'nanotech/jellybeans.vim'
Plug 'mhartington/oceanic-next'
Plug 'altercation/solarized'
Plug 'ajh17/spacegray.vim'
Plug 'zeis/vim-kolor'
Plug 'sainnhe/vim-color-forest-night'

call plug#end()
"<<< PLUGINS <<<

">>> KEYBINDS >>>
">>> NERDtree
nmap <F10> :NERDTreeToggle<CR>
">>> FZF
nnoremap <silent> <c-p> :FZF<CR>
">>> Splits
" navigate split screens easily
nmap <silent> <c-k> :wincmd k<CR>
nmap <silent> <c-j> :wincmd j<CR>
nmap <silent> <c-h> :wincmd h<CR>
nmap <silent> <c-l> :wincmd l<CR>
">>> Buffers
nnoremap <C-b>c :BufCurOnly<CR>
nnoremap <C-b>k :bd<CR>
nnoremap <C-b>n :bn<CR>
nnoremap <C-b>p :bp<CR>
">>> Git Fugitive
nnoremap <C-g>b :call <SID>ToggleBlame()<CR>
nnoremap <C-g>a :Git add %<CR>
nnoremap <C-g>c :Git commit %<CR>
nnoremap <C-g>s :Gstatus<CR>
nnoremap <C-g>d :Gvdiff<CR>
nnoremap <C-g>i :Gedit :0<CR>
">>> ALE
nnoremap <F5> :ALEFix<CR>
nmap <silent> <C-k> <Plug>(ale_previous_wrap)
nmap <silent> <C-j> <Plug>(ale_next_wrap)
nnoremap <F6> :ALEGoToDefinition<CR>
nnoremap <F7> :ALEHover<CR>
">>> NayVy
nnoremap <leader><F8> :NayvyImportFZF<CR>
nnoremap <F8> :NayvyImport<CR>
nnoremap <leader><F9> :NayvyTestGenerateFZF<CR>
nnoremap <F9> :NayvyTestGenerate<CR>
">>> Tagbar
nmap <leader><F4> :TagbarToggle<CR>
">>> Ex
nnoremap <silent> <esc> :noh<cr><esc>
">>> COC
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

nnoremap <silent> <F1> :call <SID>show_documentation()<CR>

autocmd CursorHold * silent call CocActionAsync('highlight')

nmap <F2> <Plug>(coc-rename)

xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

"<<< KEYBINDS <<<

">>> EX >>>
:au FocusLost * silent! wa
">>> Buffers
command! BufCurOnly execute '%bdelete|edit#|bdelete#'
">>> Git
function! s:ToggleBlame()
    if &l:filetype ==# 'fugitiveblame'
        close
    else
        Gblame
    endif
endfunction
">>> NayVy
">>> COC
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction
"<<< Ex <<<
">>> COLORSCHEME
colorscheme everforest
