sphinx-apidoc -o ~/RPG-forum-CMS/sphinx/ ~/RPG-forum-CMS/core/
mv modules.rst index.rst
sphinx-build -b html ~/RPG-forum-CMS/sphinx/ ~/RPG-forum-CMS/docs/
