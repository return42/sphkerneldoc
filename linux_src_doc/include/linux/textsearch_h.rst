.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/textsearch.h

.. _`ts_state`:

struct ts_state
===============

.. c:type:: struct ts_state

    search state

.. _`ts_state.definition`:

Definition
----------

.. code-block:: c

    struct ts_state {
        unsigned int offset;
        char cb[40];
    }

.. _`ts_state.members`:

Members
-------

offset
    offset for next match

cb
    control buffer, for persistent variables of \ :c:func:`get_next_block`\ 

.. _`ts_ops`:

struct ts_ops
=============

.. c:type:: struct ts_ops

    search module operations

.. _`ts_ops.definition`:

Definition
----------

.. code-block:: c

    struct ts_ops {
        const char *name;
        struct ts_config * (*init)(const void *, unsigned int, gfp_t, int);
        unsigned int (*find)(struct ts_config *, struct ts_state *);
        void (*destroy)(struct ts_config *);
        void * (*get_pattern)(struct ts_config *);
        unsigned int (*get_pattern_len)(struct ts_config *);
        struct module *owner;
        struct list_head list;
    }

.. _`ts_ops.members`:

Members
-------

name
    name of search algorithm

init
    initialization function to prepare a search

find
    find the next occurrence of the pattern

destroy
    destroy algorithm specific parts of a search configuration

get_pattern
    return head of pattern

get_pattern_len
    return length of pattern

owner
    module reference to algorithm

list
    *undescribed*

.. _`ts_config`:

struct ts_config
================

.. c:type:: struct ts_config

    search configuration

.. _`ts_config.definition`:

Definition
----------

.. code-block:: c

    struct ts_config {
        struct ts_ops *ops;
        int flags;
        unsigned int (*get_next_block)(unsigned int consumed,const u8 **dst,struct ts_config *conf, struct ts_state *state);
        void (*finish)(struct ts_config *conf, struct ts_state *state);
    }

.. _`ts_config.members`:

Members
-------

ops
    operations of chosen algorithm

flags
    flags

get_next_block
    fetch next block of data@consumed: number of bytes consumed by the caller
    \ ``dst``\ : destination buffer
    \ ``conf``\ : search configuration
    \ ``state``\ : search state

    Called repeatedly until 0 is returned. Must assign the
    head of the next block of data to &*dst and return the length
    of the block or 0 if at the end. consumed == 0 indicates
    a new search. May store/read persistent values in state->cb.

finish
    finalize/clean a series of \ :c:func:`get_next_block`\  calls@conf: search configuration
    \ ``state``\ : search state

    Called after the last use of \ :c:func:`get_next_block`\ , may be used
    to cleanup any leftovers.

.. _`textsearch_next`:

textsearch_next
===============

.. c:function:: unsigned int textsearch_next(struct ts_config *conf, struct ts_state *state)

    continue searching for a pattern

    :param conf:
        search configuration
    :type conf: struct ts_config \*

    :param state:
        search state
    :type state: struct ts_state \*

.. _`textsearch_next.description`:

Description
-----------

Continues a search looking for more occurrences of the pattern.
\ :c:func:`textsearch_find`\  must be called to find the first occurrence
in order to reset the state.

Returns the position of the next occurrence of the pattern or
UINT_MAX if not match was found.

.. _`textsearch_find`:

textsearch_find
===============

.. c:function:: unsigned int textsearch_find(struct ts_config *conf, struct ts_state *state)

    start searching for a pattern

    :param conf:
        search configuration
    :type conf: struct ts_config \*

    :param state:
        search state
    :type state: struct ts_state \*

.. _`textsearch_find.description`:

Description
-----------

Returns the position of first occurrence of the pattern or
UINT_MAX if no match was found.

.. _`textsearch_get_pattern`:

textsearch_get_pattern
======================

.. c:function:: void *textsearch_get_pattern(struct ts_config *conf)

    return head of the pattern

    :param conf:
        search configuration
    :type conf: struct ts_config \*

.. _`textsearch_get_pattern_len`:

textsearch_get_pattern_len
==========================

.. c:function:: unsigned int textsearch_get_pattern_len(struct ts_config *conf)

    return length of the pattern

    :param conf:
        search configuration
    :type conf: struct ts_config \*

.. This file was automatic generated / don't edit.

