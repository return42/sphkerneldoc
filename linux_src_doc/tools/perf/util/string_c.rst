.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/string.c

.. _`argv_free`:

argv_free
=========

.. c:function:: void argv_free(char **argv)

    free an argv \ ``argv``\  - the argument vector to be freed

    :param char \*\*argv:
        *undescribed*

.. _`argv_free.description`:

Description
-----------

Frees an argv and the strings it points to.

.. _`argv_split`:

argv_split
==========

.. c:function:: char **argv_split(const char *str, int *argcp)

    split a string at whitespace, returning an argv

    :param const char \*str:
        the string to be split

    :param int \*argcp:
        returned argument count

.. _`argv_split.description`:

Description
-----------

Returns an array of pointers to strings which are split out from
\ ``str``\ .  This is performed by strictly splitting on white-space; no
quote processing is performed.  Multiple whitespace characters are
considered to be a single argument separator.  The returned array
is always NULL-terminated.  Returns NULL on memory allocation
failure.

.. _`strglobmatch`:

strglobmatch
============

.. c:function:: bool strglobmatch(const char *str, const char *pat)

    glob expression pattern matching

    :param const char \*str:
        the target string to match

    :param const char \*pat:
        the pattern string to match

.. _`strglobmatch.description`:

Description
-----------

This returns true if the \ ``str``\  matches \ ``pat``\ . \ ``pat``\  can includes wildcards
('\*','?') and character classes ([CHARS], complementation and ranges are
also supported). Also, this supports escape character ('\') to use special
characters as normal character.

.. _`strglobmatch.note`:

Note
----

if \ ``pat``\  syntax is broken, this always returns false.

.. _`strlazymatch`:

strlazymatch
============

.. c:function:: bool strlazymatch(const char *str, const char *pat)

    matching pattern strings lazily with glob pattern

    :param const char \*str:
        the target string to match

    :param const char \*pat:
        the pattern string to match

.. _`strlazymatch.description`:

Description
-----------

This is similar to strglobmatch, except this ignores spaces in
the target string.

.. _`strtailcmp`:

strtailcmp
==========

.. c:function:: int strtailcmp(const char *s1, const char *s2)

    Compare the tail of two strings

    :param const char \*s1:
        1st string to be compared

    :param const char \*s2:
        2nd string to be compared

.. _`strtailcmp.description`:

Description
-----------

Return 0 if whole of either string is same as another's tail part.

.. _`strxfrchar`:

strxfrchar
==========

.. c:function:: char *strxfrchar(char *s, char from, char to)

    Locate and replace character in \ ``s``\ 

    :param char \*s:
        The string to be searched/changed.

    :param char from:
        Source character to be replaced.

    :param char to:
        Destination character.

.. _`strxfrchar.description`:

Description
-----------

Return pointer to the changed string.

.. _`ltrim`:

ltrim
=====

.. c:function:: char *ltrim(char *s)

    Removes leading whitespace from \ ``s``\ .

    :param char \*s:
        The string to be stripped.

.. _`ltrim.description`:

Description
-----------

Return pointer to the first non-whitespace character in \ ``s``\ .

.. _`rtrim`:

rtrim
=====

.. c:function:: char *rtrim(char *s)

    Removes trailing whitespace from \ ``s``\ .

    :param char \*s:
        The string to be stripped.

.. _`rtrim.description`:

Description
-----------

Note that the first trailing whitespace is replaced with a \ ``NUL-terminator``\ 
in the given string \ ``s``\ . Returns \ ``s``\ .

.. This file was automatic generated / don't edit.

