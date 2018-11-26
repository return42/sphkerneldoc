.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/cmdline.c

.. _`get_option`:

get_option
==========

.. c:function:: int get_option(char **str, int *pint)

    Parse integer from an option string

    :param str:
        option string
    :type str: char \*\*

    :param pint:
        (output) integer value parsed from \ ``str``\ 
    :type pint: int \*

.. _`get_option.description`:

Description
-----------

     Read an int from an option string; if available accept a subsequent
     comma as well.

.. _`get_option.return-values`:

Return values
-------------

     0 - no int in string
     1 - int found, no subsequent comma
     2 - int found including a subsequent comma
     3 - hyphen found to denote a range

.. _`get_options`:

get_options
===========

.. c:function:: char *get_options(const char *str, int nints, int *ints)

    Parse a string into a list of integers

    :param str:
        String to be parsed
    :type str: const char \*

    :param nints:
        size of integer array
    :type nints: int

    :param ints:
        integer array
    :type ints: int \*

.. _`get_options.description`:

Description
-----------

     This function parses a string containing a comma-separated
     list of integers, a hyphen-separated range of _positive_ integers,
     or a combination of both.  The parse halts when the array is
     full, or when no more numbers can be retrieved from the
     string.

     Return value is the character in the string which caused
     the parse to end (typically a null terminator, if \ ``str``\  is
     completely parseable).

.. _`memparse`:

memparse
========

.. c:function:: unsigned long long memparse(const char *ptr, char **retptr)

    parse a string with mem suffixes into a number

    :param ptr:
        Where parse begins
    :type ptr: const char \*

    :param retptr:
        (output) Optional pointer to next char after parse completes
    :type retptr: char \*\*

.. _`memparse.description`:

Description
-----------

     Parses a string into a number.  The number stored at \ ``ptr``\  is
     potentially suffixed with K, M, G, T, P, E.

.. _`parse_option_str`:

parse_option_str
================

.. c:function:: bool parse_option_str(const char *str, const char *option)

    Parse a string and check an option is set or not

    :param str:
        String to be parsed
    :type str: const char \*

    :param option:
        option name
    :type option: const char \*

.. _`parse_option_str.description`:

Description
-----------

     This function parses a string containing a comma-separated list of
     strings like a=b,c.

     Return true if there's such option in the string, or return false.

.. This file was automatic generated / don't edit.

