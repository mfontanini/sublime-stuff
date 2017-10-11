import sublime
import sublime_plugin


class NamespaceGenerator(sublime_plugin.TextCommand):
    NAMESPACE_TEMPLATE = 'namespace {0} {{\n{1}\n}} // {0}'

    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                sublime.message_dialog("Need selection to generate namespace")
                return
            data = self.view.substr(region)
            namespaces = data.split('::')
            namespaces.reverse()

            result = ''
            for i in namespaces:
                result = NamespaceGenerator.NAMESPACE_TEMPLATE.format(
                    i,
                    result
                )

            self.view.replace(edit, region, result)
