.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/textsearch.c

.. _`textsearch_register`:

textsearch_register
===================

.. c:function:: int textsearch_register(struct ts_ops *ops)

    register a textsearch module

    :param struct ts_ops \*ops:
        operations lookup table

.. _`textsearch_register.description`:

Description
-----------

This function must be called by textsearch modules to announce
their presence. The specified &\ ``ops``\  must have \ ``name``\  set to a
unique identifier and the callbacks \ :c:func:`find`\ , \ :c:func:`init`\ , \ :c:func:`get_pattern`\ ,
and \ :c:func:`get_pattern_len`\  must be implemented.

Returns 0 or -EEXISTS if another module has already registered
with same name.

.. _`textsearch_unregister`:

textsearch_unregister
=====================

.. c:function:: int textsearch_unregister(struct ts_ops *ops)

    unregister a textsearch module

    :param struct ts_ops \*ops:
        operations lookup table

.. _`textsearch_unregister.description`:

Description
-----------

This function must be called by textsearch modules to announce
their disappearance for examples when the module gets unloaded.
The \ :c:type:`struct ops <ops>` parameter must be the same as the one during the
registration.

Returns 0 on success or -ENOENT if no matching textsearch
registration was found.

.. _`textsearch_find_continuous`:

textsearch_find_continuous
==========================

.. c:function:: unsigned int textsearch_find_continuous(struct ts_config *conf, struct ts_state *state, const void *data, unsigned int len)

    search a pattern in continuous/linear data

    :param struct ts_config \*conf:
        search configuration

    :param struct ts_state \*state:
        search state

    :param const void \*data:
        data to search in

    :param unsigned int len:
        length of data

.. _`textsearch_find_continuous.description`:

Description
-----------

A simplified version of \ :c:func:`textsearch_find`\  for continuous/linear data.
Call \ :c:func:`textsearch_next`\  to retrieve subsequent matches.

Returns the position of first occurrence of the pattern or
\ ``UINT_MAX``\  if no occurrence was found.

.. _`textsearch_prepare`:

textsearch_prepare
==================

.. c:function:: struct ts_config *textsearch_prepare(const char *algo, const void *pattern, unsigned int len, gfp_t gfp_mask, int flags)

    Prepare a search

    :param const char \*algo:
        name of search algorithm

    :param const void \*pattern:
        pattern data

    :param unsigned int len:
        length of pattern

    :param gfp_t gfp_mask:
        allocation mask

    :param int flags:
        search flags

.. _`textsearch_prepare.description`:

Description
-----------

Looks up the search algorithm module and creates a new textsearch
configuration for the specified pattern.

.. _`textsearch_prepare.note`:

Note
----

The format of the pattern may not be compatible between
the various search algorithms.

Returns a new textsearch configuration according to the specified
parameters or a \ :c:func:`ERR_PTR`\ . If a zero length pattern is passed, this
function returns EINVAL.

.. _`textsearch_destroy`:

textsearch_destroy
==================

.. c:function:: void textsearch_destroy(struct ts_config *conf)

    destroy a search configuration

    :param struct ts_config \*conf:
        search configuration

.. _`textsearch_destroy.description`:

Description
-----------

Releases all references of the configuration and frees
up the memory.

.. This file was automatic generated / don't edit.

