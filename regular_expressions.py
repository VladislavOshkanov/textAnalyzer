# -*- coding: utf-8 -*-
import re
import sys

from constants import dashes

dashes_no_repeats = dashes[:]
dashes_no_repeats.remove("--+")
matching_dashes = dashes_no_repeats + ["-+"]


no_punctuation               = re.compile("^\w+$")
numerical_expression         = re.compile(u"(\d+(?:,\d+)*(?:\.\d+)*(?![a-zA-ZÀ-ż])\s*)")
repeated_dash_converter = re.compile("--+")
dash_converter = re.compile("|".join(dashes_no_repeats))
right_single_quote_converter = re.compile(u"(['’]+)(?=\W|$)\s*", re.UNICODE)
simple_dash_finder           = re.compile("(-\s*)")
advanced_dash_finder         = re.compile("(" + "|".join(matching_dashes) + ")\s*")
url_file_finder              = re.compile("(?:[-a-zA-Z0-9@%._\+~#=]{2,256}://)?"
                                          "(?:www\.)?[-a-zA-Z0-9@:%\._\+~#=]{2,"
                                          "256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#"
                                          "?&//=]*\s*")
shifted_ellipses             = re.compile("([\.\!\?¿¡]{2,})\s*")
shifted_standard_punctuation = re.compile(u"([\(\[\{\}\]\)\!¡\?¿#\$%;~&+=<>|/:,—…])\s*")
multi_single_quote_finder    = re.compile("('{2,})\s*")


