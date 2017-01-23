.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/argv_split.c

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

.. c:function:: char **argv_split(gfp_t gfp, const char *str, int *argcp)

    split a string at whitespace, returning an argv

    :param gfp_t gfp:
        the GFP mask used to allocate memory

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

The source string at \`str' may be undergoing concurrent alteration via
userspace sysctl activity (at least).  The \ :c:func:`argv_split`\  implementation
attempts to handle this gracefully by taking a local copy to work on.

.. This file was automatic generated / don't edit.

