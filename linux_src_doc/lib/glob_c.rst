.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/glob.c

.. _`glob_match`:

glob_match
==========

.. c:function:: bool __pure glob_match(char const *pat, char const *str)

    Shell-style pattern matching, like !fnmatch(pat, str, 0)

    :param pat:
        Shell-style pattern to match, e.g. "\*.[ch]".
    :type pat: char const \*

    :param str:
        String to match.  The pattern must match the entire string.
    :type str: char const \*

.. _`glob_match.description`:

Description
-----------

Perform shell-style glob matching, returning true (1) if the match
succeeds, or false (0) if it fails.  Equivalent to !fnmatch(@pat, \ ``str``\ , 0).

Pattern metacharacters are ?, \*, [ and \.
(And, inside character classes, !, - and ].)

This is small and simple implementation intended for device blacklists
where a string is matched against a number of patterns.  Thus, it
does not preprocess the patterns.  It is non-recursive, and run-time

.. _`glob_match.is-at-most-quadratic`:

is at most quadratic
--------------------

strlen(@str)\*strlen(@pat).

An example of the worst case is glob_match("\*aaaaa", "aaaaaaaaaa");
it takes 6 passes over the pattern before matching the string.

Like !fnmatch(@pat, \ ``str``\ , 0) and unlike the shell, this does NOT
treat / or leading . specially; it isn't actually used for pathnames.

Note that according to glob(7) (and unlike bash), character classes
are complemented by a leading !; this does not support the regex-style
[^a-z] syntax.

An opening bracket without a matching close is matched literally.

.. This file was automatic generated / don't edit.

