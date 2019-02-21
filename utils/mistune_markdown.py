import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


# The fastest markdown parser in pure Python with renderer features, inspired by marked.
# https://github.com/lepture/mistune

class ArticleRenderer(mistune.Renderer):
    """ 对文章进行 markdown显示，和 代码高亮 """

    def block_code(self, code, lang=None):
        """Rendering block level code. ``pre > code``.

        :param code: text content of the code block.
        :param lang: language of the given code.
        """
        code = code.rstrip('\n')  # 去掉尾部的换行符
        if not lang:
            code = mistune.escape(code)
            return '<pre><code>%s\n</code></pre>\n' % code

        # 给代码加上高亮  例如: lang='python'的话
        # ```python
        #   print('666')
        # ```
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


def article_markdown(text):
    """ 对传入的text文本进行markdown """
    renderer = ArticleRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(text)
