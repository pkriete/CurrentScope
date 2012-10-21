import sublime, sublime_plugin

class CurrentScopeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		locations = self.view.find_by_selector('entity.name.function, entity.name.type, meta.toc-list')
		selection = self.view.sel()[0]

		last = sublime.Region(0, 0)

		for l in locations:
			if l.a > selection.a:
				break
			last = l

		scope = self.view.substr(last)

		if scope:
			self.view.set_status('scope', "Scope `" + scope + "`")
		else:
			self.view.erase_status('scope')


class DetectScopeEventListener(sublime_plugin.EventListener):
	def on_load(self, view):
		view.run_command('current_scope')

	def on_selection_modified(self, view):
		view.run_command('current_scope')

	def on_modified(self, view):
		view.run_command('current_scope')