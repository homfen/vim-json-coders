# vim-json-coders
Encode(compress) or Decode(pretty) json file in vim.

Use Vundle to install, add these below to .vimrc:
```
Plugin 'homfen/vim-json-coders'

nnoremap de :%!python ~/.vim/bundle/vim-json-coders/json-decoder.py<CR>
nnoremap en :%!python ~/.vim/bundle/vim-json-coders/json-encoder.py<CR>
```
