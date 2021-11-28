from tree_sitter import Language, Parser
from git import Repo
import os
import glob
import shutil

#link_of_repo=input('enter link: ')
Repo.clone_from('https://github.com/SrijanReddy/Plant-Disease-Detection-using-CNN','clones');
py_links,js_links,go_links,rby_links=[],[],[],[]
fpath=glob.glob('clones/*')

for i in fpath:
    if '.py' in i:
        py_links.append(i)
    if '.js' in i:
        js_links.append(i)
    if '.go' in i:
        go_links.append(i)
    if '.rb' in i:
        rby_links.append(i)
txt=[]
for f in py_links:
    with open(f) as fle:
        try:
            lines = fle.read()

            txt.append(lines)
        except:
            print('cant open')
            pass

Language.build_library( 'build/my-languages.so',['tree-sitter-python','tree-sitter-ruby','tree-sitter-javascript','tree-sitter-go'])
py_lang= Language('build/my-languages.so', 'python')
pyth_parser=Parser()
pyth_parser.set_language(py_lang)

js_lang= Language('build/my-languages.so', 'javascript')
js_parser=Parser()
js_parser.set_language(js_lang)

ruby_lang= Language('build/my-languages.so', 'ruby')
rby_parser=Parser()
rby_parser.set_language(ruby_lang)

go_lang=Language('build/my-languages.so','go')
goparser = Parser()
goparser.set_language(go_lang)
