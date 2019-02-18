from flask_nav.elements import Navbar, View, Link, Text, Separator,
from flask_nav.renderers import Renderer
from  dashApp.app import nav, Bootstrap
from dominate import tags

@nav.renderer()
class JustDivRenderer(Renderer):

    def visit_Navbar(self, node):

        sub = []
        for item in node.items:
            sub.append(self.visit(item))

        return tags.div('Navigation:', *sub)


    def visit_View(self, node):

        return tags.div('{} ({})'.format(node.title, node.get_url()))


    def visit_Subgroup(self, node):

        # almost the same as visit_Navbar, but written a bit more concise
        return tags.div(node.title,
                        *[self.visit(item) for item in node.items])


@nav.navigation



nav_bar = top_nav((View('Landing Page', 'index'), View('Visual One', 'visual_1'),
                View('Visual One', 'visual_1'), View('Visual Two', 'visual_2'),
                View('Visual Three', 'visual_3'), View('Visual Four', 'visual_4'),
                Link('Google', 'www.google.com'),  Separator(), Text('HR')))