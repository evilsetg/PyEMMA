
# This file is part of PyEMMA.
#
# Copyright (c) 2017 Computational Molecular Biology Group, Freie Universitaet Berlin (GER)
#
# PyEMMA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def _ProgressReporter_pyemma_config(cls):
    # monkey patch the getter to respect pyemmas config.

    @cls.show_progress.getter
    def show_progress(self):
        """ whether to show the progress of heavy calculations on this object. """
        from pyemma import config
        # no value yet, obtain from config
        if not hasattr(self, "_show_progress"):
            val = config.show_progress_bars
            self._show_progress = val
        # config disabled progress?
        elif not config.show_progress_bars:
            return False

        return self._show_progress

    cls.show_progress = show_progress
    return cls


from progress_reporter import ProgressReporter as _impl
ProgressReporter = _ProgressReporter_pyemma_config(_impl)
