文章与页面
==============
``article``:
按照时间排序，例如博客中的文章。

``pages``:
如“关于”，“联系”等页面，固定的内容不经常改变的页面。
在 content 目录下创建 pages 文件夹，该文件夹下的所有文件都用于生成 pages。
或者在 Pelican 配置中设置其他的目录。

``status: hidden`` 元标签可以使该页面不在菜单或导航栏显示。

文件元数据
=========================
元数据可以任意定义，模板中可以使用元数据，常用的元数据如下::

    :date: 2010-10-03 10:20
    :modified: 2010-10-04 18:40
    :tags: thats, awesome
    :category: yeah
    :slug: my-super-post
    :lang: zh
    :authors: Alexis Metaireau, Conan Doyle
    :summary: Short version for index and feeds
    :status: draft/hidden

html中的缩写abbr标签支持 ``:abbr:`HTML (HyperText Markup Language)`.``

内部链接
=========
链接到内部的内容
---------------------
Pelican 3.1 开始，链接根据源文件的层级组织来指定。
支持相对于当前的路径，及相对于 content 目录的绝对路径，例如::

    `a link relative to the current file <{filename}../article2.rst>`_
    `a link relative to the content root <{filename}/article2.rst>`_

链接到静态的文件
-----------------
语法与链接到内部内容一样，但是需要在 pelicanconf.py 中配置 ``STATIC_PATHS`` 静态源目录在。
Pelican 默认配置包含 images 目录，但其他的目录则必须手动添加。
从 Pelican 3.5 开始，同时包含静态文件和源内容的目录不会暴露源文件的内容，但该目录也要在添加到 STATIC_PATHS 配置中。

附件文件
----------
从 Pelican 3.5 开始，静态文件可以 “附加” 到一个 page 或 article ，
语法是： ```附件文件<{attach}path/to/file>`_`` ，语法与 {filename} 类似，但附件可以把静态文件放到与文档相同的输出目录或其子目录（源中在内容文档的子目录）。

链接到 tags 和 categories
---------------------------
语法::

    `标签<{tag}tagname>_`
    `分类<{category}foobar>_`

翻译
=====
为文章和页面添加 lang 元标签并配置 DEFAULT_LANG 。
Pelican 根据文章或页面的 slug 元标签来判断两个或多个内容是否为同一内容的多个翻译，否则 Pelican 会根据文件名来猜测。
``:lang:`` 标签指定内容的语言。

源代码语法高亮
===============
遵从rst的语法::

    ..code-block:: identifier

        <indented code block goes here>

选项见下表

=============   ============  =========================================
Option          Valid values  Description
=============   ============  =========================================
anchorlinenos   N/A           If present wrap line numbers in <a> tags.
classprefix     string        String to prepend to token class names
hl_lines        numbers       List of lines to be highlighted.
lineanchors     string        Wrap each line in an anchor using this
                              string and -linenumber.
linenos         string        If present or set to "table" output line
                              numbers in a table, if set to
                              "inline" output them inline. "none" means
                              do not output the line numbers for this
                              table.
linenospecial   number        If set every nth line will be given the
                              'special' css class.
linenostart     number        Line number for the first line.
linenostep      number        Print every nth line number.
lineseparator   string        String to print between lines of code,
                              '\n' by default.
linespans       string        Wrap each line in a span using this and
                              -linenumber.
nobackground    N/A           If set do not output background color for
                              the wrapping element
nowrap          N/A           If set do not wrap the tokens at all.
tagsfile        string        ctags file to use for name definitions.
tagurlformat    string        format for the ctag links.
=============   ============  =========================================

可以在 Pelican 配置文件中配置 ``PYGMENTS_RST_OPTIONS`` 来设定默认选项。

草稿
=====
添加 ``Status: draft`` 元标签的内容会输出到 drafts 目录，且不会在文章及页面显示。
