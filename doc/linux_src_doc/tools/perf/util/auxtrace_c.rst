.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/auxtrace.c

.. _`auxtrace_cache`:

struct auxtrace_cache
=====================

.. c:type:: struct auxtrace_cache

    hash table to implement a cache

.. _`auxtrace_cache.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_cache {
        struct hlist_head *hashtable;
        size_t sz;
        size_t entry_size;
        size_t limit;
        size_t cnt;
        unsigned int bits;
    }

.. _`auxtrace_cache.members`:

Members
-------

hashtable
    the hashtable

sz
    hashtable size (number of hlists)

entry_size
    size of an entry

limit
    limit the number of entries to this maximum, when reached the cache
    is dropped and caching begins again with an empty cache

cnt
    current number of entries

bits
    hashtable size (\ ``sz``\  = 2^\ ``bits``\ )

.. This file was automatic generated / don't edit.

