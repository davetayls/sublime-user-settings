import sublime, sublime_plugin


class FormatInsideBracesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('reindent')
