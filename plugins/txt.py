from __future__ import generator_stop

from typing import Tuple

from plug import Filetypes


@Filetypes.plugin(["txt"])
class TXT(object):
	"""Trivial plugin to validate .txt files. It assumes all txt files are valid.
	["txt"] determins the list of file extensions this plugin can handle."""

	def __init__(self):
		"""Constructor is called once per program run."""
		pass

	def validate(self, path, ext):
		# type: (str, str) -> Tuple[int, str]

		"""validate() is called for every file
		path: complete/path/to/file.exe
		ext: just the extension of the file e.g. "exe"

		Should return (0, "") if everything is fine,
		or (1, error_msg_string) if errors were found."""
		return (0, "")
