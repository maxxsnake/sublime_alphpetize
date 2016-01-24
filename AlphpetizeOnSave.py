import sublime
import sublime_plugin

class AlphetizeOnSave(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        settings = sublime.load_settings('Alphpetize.sublime-settings')
        if settings.get('sort_on_save'):
            import os
            filename = view.file_name()
            name, extension = os.path.splitext(filename)
            if extension == '.php':
                view.run_command('alphpetize', {'from_pre_save': 1})