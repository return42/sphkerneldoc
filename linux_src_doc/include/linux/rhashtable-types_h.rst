.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rhashtable-types.h

.. _`rhashtable_compare_arg`:

struct rhashtable_compare_arg
=============================

.. c:type:: struct rhashtable_compare_arg

    Key for the function rhashtable_compare

.. _`rhashtable_compare_arg.definition`:

Definition
----------

.. code-block:: c

    struct rhashtable_compare_arg {
        struct rhashtable *ht;
        const void *key;
    }

.. _`rhashtable_compare_arg.members`:

Members
-------

ht
    Hash table

key
    Key to compare against

.. _`rhashtable_params`:

struct rhashtable_params
========================

.. c:type:: struct rhashtable_params

    Hash table construction parameters

.. _`rhashtable_params.definition`:

Definition
----------

.. code-block:: c

    struct rhashtable_params {
        u16 nelem_hint;
        u16 key_len;
        u16 key_offset;
        u16 head_offset;
        unsigned int max_size;
        u16 min_size;
        bool automatic_shrinking;
        u8 locks_mul;
        rht_hashfn_t hashfn;
        rht_obj_hashfn_t obj_hashfn;
        rht_obj_cmpfn_t obj_cmpfn;
    }

.. _`rhashtable_params.members`:

Members
-------

nelem_hint
    Hint on number of elements, should be 75% of desired size

key_len
    Length of key

key_offset
    Offset of key in struct to be hashed

head_offset
    Offset of rhash_head in struct to be hashed

max_size
    Maximum size while expanding

min_size
    Minimum size while shrinking

automatic_shrinking
    Enable automatic shrinking of tables

locks_mul
    Number of bucket locks to allocate per cpu (default: 32)

hashfn
    Hash function (default: jhash2 if !(key_len % 4), or jhash)

obj_hashfn
    Function to hash object

obj_cmpfn
    Function to compare key with object

.. _`rhashtable`:

struct rhashtable
=================

.. c:type:: struct rhashtable

    Hash table handle

.. _`rhashtable.definition`:

Definition
----------

.. code-block:: c

    struct rhashtable {
        struct bucket_table __rcu *tbl;
        unsigned int key_len;
        unsigned int max_elems;
        struct rhashtable_params p;
        bool rhlist;
        struct work_struct run_work;
        struct mutex mutex;
        spinlock_t lock;
        atomic_t nelems;
    }

.. _`rhashtable.members`:

Members
-------

tbl
    Bucket table

key_len
    Key length for hashfn

max_elems
    Maximum number of elements in table

p
    Configuration parameters

rhlist
    True if this is an rhltable

run_work
    Deferred worker to expand/shrink asynchronously

mutex
    Mutex to protect current/future table swapping

lock
    Spin lock to protect walker list

nelems
    Number of elements in table

.. _`rhltable`:

struct rhltable
===============

.. c:type:: struct rhltable

    Hash table with duplicate objects in a list

.. _`rhltable.definition`:

Definition
----------

.. code-block:: c

    struct rhltable {
        struct rhashtable ht;
    }

.. _`rhltable.members`:

Members
-------

ht
    Underlying rhtable

.. _`rhashtable_walker`:

struct rhashtable_walker
========================

.. c:type:: struct rhashtable_walker

    Hash table walker

.. _`rhashtable_walker.definition`:

Definition
----------

.. code-block:: c

    struct rhashtable_walker {
        struct list_head list;
        struct bucket_table *tbl;
    }

.. _`rhashtable_walker.members`:

Members
-------

list
    List entry on list of walkers

tbl
    The table that we were walking over

.. _`rhashtable_iter`:

struct rhashtable_iter
======================

.. c:type:: struct rhashtable_iter

    Hash table iterator

.. _`rhashtable_iter.definition`:

Definition
----------

.. code-block:: c

    struct rhashtable_iter {
        struct rhashtable *ht;
        struct rhash_head *p;
        struct rhlist_head *list;
        struct rhashtable_walker walker;
        unsigned int slot;
        unsigned int skip;
        bool end_of_table;
    }

.. _`rhashtable_iter.members`:

Members
-------

ht
    Table to iterate through

p
    Current pointer

list
    Current hash list pointer

walker
    Associated rhashtable walker

slot
    Current slot

skip
    Number of entries to skip in slot

end_of_table
    *undescribed*

.. This file was automatic generated / don't edit.

