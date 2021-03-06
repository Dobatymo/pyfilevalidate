from __future__ import generator_stop

import logging
import subprocess
import sys
from typing import Tuple

from plug import Filetypes

logger = logging.getLogger(__name__)

@Filetypes.plugin(["flac"])
class FLAC(object):

	def __init__(self, executable, warnings_as_errors=True):
		self.executable = executable
		self.wae = warnings_as_errors

	def validate(self, path, ext):
		# type: (str, str) -> Tuple[int, str]

		try:
			if self.wae:
				cmd = '"{}" -t -s -w "{}"'.format(self.executable, path)
			else:
				cmd = '"{}" -t -s "{}"'.format(self.executable, path)
			subprocess.check_output(cmd, stderr=subprocess.STDOUT)
			return (0, "")
		except subprocess.CalledProcessError as e:
			return (1, e.output.decode(sys.stdout.encoding))
