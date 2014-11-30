使用 Pelican 搭建的一个静态网站并使用 GitHub Pages 提供服务。

开发环境搭建
=============
如下的命令列表会在当前目录建立 foshuo 目录，并在该目录中创建开发环境。

.. code-block:: bash
    :linenos: table

    mkdir foshuo
    cd foshuo
    virtualenv --python=python3 pyenv3
    source pyenv3/bin/activate
    echo "Installing pelican and its plugins and themes..."
    #git clone git@github.com:lennyhbt/pelican.git
    pip install -e "git+git@github.com:lennyhbt/pelican.git#egg=pelican"
    git clone --recursive git@github.com:lennyhbt/pelican-plugins.git
    #git clone --recursive git@github.com:lennyhbt/pelican-themes.git
    git clone git@github.com:lennyhbt/foshuo-theme.git

    echo "cloning foshuo blog..."
    git clone git@github.com:lennyhbt/lennyhbt.github.io.git foshuo
    echo "Done, your site is at foshuo doc."
