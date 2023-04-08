# -----------------------------------------------------------------------------
# Getting Things GNOME! - a personal organizer for the GNOME desktop
# Copyright (c) The GTG Team
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

import re


# Tags with special meaning
ALLTASKS_TAG = "gtg-tags-all"
NOTAG_TAG = "gtg-tags-none"
SEP_TAG = "gtg-tags-sep"
SEARCH_TAG = "search"


def extract_tags_from_text(text):
    """ Given a string, returns a list of the @tags contained in that """

    return re.findall(r'(?:^|[\s])(@[\w\/\.\-\:\&]*\w)', text)
