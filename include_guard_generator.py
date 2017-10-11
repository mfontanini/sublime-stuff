import sublime
import sublime_plugin


class IncludeGuardGenerator(sublime_plugin.TextCommand):
    GUARD_TEMPLATE = '#ifndef {0}\n#define {0}\n\n\n#endif // {0}\n'

    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                sublime.message_dialog("Need selection to generate include guard")
                return
            data = self.view.substr(region)
            result = IncludeGuardGenerator.GUARD_TEMPLATE.format(data)
            self.view.replace(edit, region, result)
