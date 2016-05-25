# vim-json-coders
encoder or decoder json in vim

Use Vundle to install, add these below to .vimrc:
```
Plugin 'homfen/vim-json-coders'

nnoremap de :%!python ~/.vim/bundle/vim-json-coders/json-decoder.py<CR>
nnoremap en :%!python ~/.vim/bundle/vim-json-coders/json-encoder.py<CR>
```
