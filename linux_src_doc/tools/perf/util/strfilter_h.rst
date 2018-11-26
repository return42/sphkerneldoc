.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/strfilter.h

.. _`strfilter__new`:

strfilter__new
==============

.. c:function:: struct strfilter *strfilter__new(const char *rules, const char **err)

    Create a new string filter

    :param rules:
        Filter rule, which is a combination of glob expressions.
    :type rules: const char \*

    :param err:
        Pointer which points an error detected on \ ``rules``\ 
    :type err: const char \*\*

.. _`strfilter__new.description`:

Description
-----------

Parse \ ``rules``\  and return new strfilter. Return NULL if an error detected.
In that case, \*@err will indicate where it is detected, and \*@err is NULL
if a memory allocation is failed.

.. _`strfilter__or`:

strfilter__or
=============

.. c:function:: int strfilter__or(struct strfilter *filter, const char *rules, const char **err)

    Append an additional rule by logical-or

    :param filter:
        Original string filter
    :type filter: struct strfilter \*

    :param rules:
        Filter rule to be appended at left of the root of
        \ ``filter``\  by using logical-or.
    :type rules: const char \*

    :param err:
        Pointer which points an error detected on \ ``rules``\ 
    :type err: const char \*\*

.. _`strfilter__or.description`:

Description
-----------

Parse \ ``rules``\  and join it to the \ ``filter``\  by using logical-or.
Return 0 if success, or return the error code.

.. _`strfilter__and`:

strfilter__and
==============

.. c:function:: int strfilter__and(struct strfilter *filter, const char *rules, const char **err)

    Append an additional rule by logical-and

    :param filter:
        Original string filter
    :type filter: struct strfilter \*

    :param rules:
        Filter rule to be appended at left of the root of
        \ ``filter``\  by using logical-and.
    :type rules: const char \*

    :param err:
        Pointer which points an error detected on \ ``rules``\ 
    :type err: const char \*\*

.. _`strfilter__and.description`:

Description
-----------

Parse \ ``rules``\  and join it to the \ ``filter``\  by using logical-and.
Return 0 if success, or return the error code.

.. _`strfilter__compare`:

strfilter__compare
==================

.. c:function:: bool strfilter__compare(struct strfilter *filter, const char *str)

    compare given string and a string filter

    :param filter:
        String filter
    :type filter: struct strfilter \*

    :param str:
        target string
    :type str: const char \*

.. _`strfilter__compare.description`:

Description
-----------

Compare \ ``str``\  and \ ``filter``\ . Return true if the str match the rule

.. _`strfilter__delete`:

strfilter__delete
=================

.. c:function:: void strfilter__delete(struct strfilter *filter)

    delete a string filter

    :param filter:
        String filter to delete
    :type filter: struct strfilter \*

.. _`strfilter__delete.description`:

Description
-----------

Delete \ ``filter``\ .

.. _`strfilter__string`:

strfilter__string
=================

.. c:function:: char *strfilter__string(struct strfilter *filter)

    Reconstruct a rule string from filter

    :param filter:
        String filter to reconstruct
    :type filter: struct strfilter \*

.. _`strfilter__string.description`:

Description
-----------

Reconstruct a rule string from \ ``filter``\ . This will be good for
debug messages. Note that returning string must be freed afterward.

.. This file was automatic generated / don't edit.

