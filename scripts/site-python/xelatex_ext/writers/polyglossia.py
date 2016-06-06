# -*- coding: utf-8; mode: python -*-
# pylint: disable=C0330, R0903

u"""
    sphinx.writers.polyglossia
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright:  Copyright (C) 2016 Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    Manage culturally-determined typographical (and other) rules and hyphenation
    patterns with the `polyglossia`_ package.  The `polyglossia`_ package
    provides multilingual support for Plain XeTeX or XeLaTeX, it is the
    alternative to Babel for users of XeLaTeX and LuaLaTeX. At the time
    (04/2016) 76 different languages are suported (`polyglossia (github)`_).

    _`polyglossia`: https://www.ctan.org/tex-archive/macros/latex/contrib/polyglossia
    _`polyglossia (github)`: https://github.com/reutenauer/polyglossia/

"""

# ==============================================================================
#  imports ...
# ==============================================================================

from docutils import utils

# ==============================================================================
class Polyglossia(object):
# ==============================================================================

    """Language specifics for XeTeX."""

    language_codes = {
        # code              Polyglossia-name    comment
        "am"              : "amharic"
        # , "af"                                # afrikaans"
        , "ar"              : "arabic"
        , "ast"             : "asturian"
        , "bg"              : "bulgarian"
        , "bn"              : "bengali"
        , "bo"              : "tibetan"
        , "br"              : "breton"
        , "ca"              : "catalan"
        , "cop"             : "coptic"
        , "cs"              : "czech"
        , "cy"              : "welsh"
        , "da"              : "danish"
        , "de"              : "german"          # new spelling (de_1996)
        , "de-1901"         : "ogerman"         # old spelling
        # , "de-AT"
        # , "de-AT-1901"
        , "dsb"             : "lsorbian"
        , "dv"              : "divehi"          # Maldivian
        , "el"              : "greek"           # monotonic (el-monoton)
        , "el-polyton"      : "polutonikogreek"
        , "en"              : "english"         # TeX' default language
        , "en-AU"           : "australian"
        # , "en-CA"                             # canadian
        , "en-GB"           : "british"
        , "en-NZ"           : "newzealand"
        , "en-US"           : "american"
        , "eo"              : "esperanto"
        , "es"              : "spanish"
        , "et"              : "estonian"
        , "eu"              : "basque"
        , "fa"              : "farsi"
        , "fi"              : "finnish"
        , "fr"              : "french"
        # , "fr-CA"                             # canadien
        , "fur"              : "friulan"
        , "ga"              : "irish"           # Irish Gaelic
        , "gl"              : "galician"
        , "grc"             : "ancientgreek"    # Ancient Greek
        # , "grc-ibycus"                        # Ibycus encoding
        , "he"              : "hebrew"
        , "hi"              : "hindi"
        , "hy"              : "armenian"
        , "hr"              : "croatian"
        , "hsb"             : "usorbian"
        , "hu"              : "magyar"
        , "ia"              : "interlingua"
        , "id"              : "bahasai"         # Bahasa (Indonesian)
        , "is"              : "icelandic"
        , "it"              : "italian"
        , "ja"              : "japanese"        # supported?
        , "kk"              : "kazakh"          # supported?
        , "km"              : "khmer"
        , "kn"              : "kannada"
        , "ko"              : "korean"
        , "la"              : "latin"
        , "lo"              : "lao"
        , "lt"              : "lithuanian"
        , "lv"              : "latvian"
        , "ml"              : "malayalam"
        , "mn"              : "mongolian"       # supported? Mongolian, Cyrillic script (mn-cyrl)
        , "mr"              : "marathi"
        , "ms"              : "bahasam"         # Bahasa (Malay)
        , "nb"              : "norsk"           # Norwegian Bokmal
        , "nl"              : "dutch"
        , "nn"              : "nynorsk"         # Norwegian Nynorsk
        , "no"              : "norsk"           # Norwegian (Bokmal)
        , "oc"              : "occitan"
        , "pl"              : "polish"
        , "pms"             : "piedmontese"
        , "pt"              : "portuges"
        , "pt-BR"           : "brazil"
        , "rm"              : "romansh"
        , "ro"              : "romanian"
        , "ru"              : "russian"
        , "sa"              : "sanskrit"
        , "sco"             : "scottish"
        , "se"              : "samin"           # North Sami
        , "sh-cyrl"         : "serbian"         # Serbo-Croatian, Cyrillic script
        , "sh-latn"         : "croatian"        # Serbo-Croatian, Latin script
        , "sk"              : "slovak"
        , "sl"              : "slovenian"
        , "sq"              : "albanian"
        , "sr"              : "serbian"         # Serbian, Cyrillic script (contributed)
        , "sv"              : "swedish"
        , "syc"             : "syriac"
        , "ta"              : "tamil"
        , "te"              : "telugu"
        , "th"              : "thai"
        , "tk"              : "turkmen"
        , "tr"              : "turkish"
        , "uk"              : "ukrainian"
        , "ur"              : "urdu"
        , "vi"              : "vietnamese"
        # , "???"             : "nko"
    }

    # normalize (downcase) keys
    language_codes = dict([(k.lower(), v) for (k,v) in language_codes.items()])

    def __init__(self, lang_code, builder=None, other_lcodes=None):
        u"""Build :py:class:`Polyglossia` instance.

        :param str lang_code:
            Language code of the default language

        :param sphinx.builders.Builder builder:  (optional)
            Sphinx builder object

        :param list other_lcodes: (optional)
            List of language codes of other languages, used by the document.
        """

        self.builder      = builder
        self.lang_code    = lang_code
        self.other_lcodes = other_lcodes
        self.other_langs  = set()

        self.language     = self.langcode2name(self.lang_code)
        for lc in self.other_lcodes:
            self.other_langs.add(self.langcode2name(lc))

    def __call__(self):
        content = [
            r"\usepackage{polyglossia}"
            , r"\setdefaultlanguage{%s}" % self.language]
        if self.other_langs:
            content.append(r"\setotherlanguages{%s}"
                         % ",".join(sorted(self.other_langs)))
        return '\n'.join(content)

    def langcode2name(self, lang_code):
        """Return `polyglossia`_ (XeTeX) language name of `language_code`"""
        retVal = ""
        for tag in utils.normalize_language_tag(lang_code):
            retVal = self.language_codes.get(tag, "")
            if retVal:
                break
        if not retVal and self.builder is not None:
            self.builder.warn(
                'Language "%s" not supported by LaTeX (polyglossia)'
                %  lang_code)
        return retVal

    def foreignlanguage(self, langcode):
        lang = self.langcode2name()
        if not lang:
            return None
        self.other_langs.add(lang)
        startTag = "\foreignlanguage{%s}{" % lang
        endTag   = "}"
