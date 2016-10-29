.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rhashtable.h

.. _`bucket_table`:

struct bucket_table
===================

.. c:type:: struct bucket_table

    Table of hash buckets

.. _`bucket_table.definition`:

Definition
----------

.. code-block:: c

    struct bucket_table {
        unsigned int size;
        unsigned int rehash;
        u32 hash_rnd;
        unsigned int locks_mask;
        spinlock_t *locks;
        struct list_head walkers;
        struct rcu_head rcu;
        struct bucket_table __rcu *future_tbl;
        struct rhash_head __rcu  *buckets[] ____cacheline_aligned_in_smp;
    }

.. _`bucket_table.members`:

Members
-------

size
    Number of hash buckets

rehash
    Current bucket being rehashed

hash_rnd
    Random seed to fold into hash

locks_mask
    Mask to apply before accessing locks[]

locks
    Array of spinlocks protecting individual buckets

walkers
    List of active walkers

rcu
    RCU structure for freeing the table

future_tbl
    Table under construction during rehashing

buckets
    size \* hash buckets

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
        size_t nelem_hint;
        size_t key_len;
        size_t key_offset;
        size_t head_offset;
        unsigned int insecure_max_entries;
        unsigned int max_size;
        unsigned int min_size;
        u32 nulls_base;
        bool insecure_elasticity;
        bool automatic_shrinking;
        size_t locks_mul;
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

insecure_max_entries
    Maximum number of entries (may be exceeded)

max_size
    Maximum size while expanding

min_size
    Minimum size while shrinking

nulls_base
    Base value to generate nulls marker

insecure_elasticity
    Set to true to disable chain length checks

automatic_shrinking
    Enable automatic shrinking of tables

locks_mul
    Number of bucket locks to allocate per cpu (default: 128)

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
        atomic_t nelems;
        unsigned int key_len;
        unsigned int elasticity;
        struct rhashtable_params p;
        struct work_struct run_work;
        struct mutex mutex;
        spinlock_t lock;
    }

.. _`rhashtable.members`:

Members
-------

tbl
    Bucket table

nelems
    Number of elements in table

key_len
    Key length for hashfn

elasticity
    Maximum chain length before rehash

p
    Configuration parameters

run_work
    Deferred worker to expand/shrink asynchronously

mutex
    Mutex to protect current/future table swapping

lock
    Spin lock to protect walker list

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

    Hash table iterator, fits into netlink cb

.. _`rhashtable_iter.definition`:

Definition
----------

.. code-block:: c

    struct rhashtable_iter {
        struct rhashtable *ht;
        struct rhash_head *p;
        struct rhashtable_walker *walker;
        unsigned int slot;
        unsigned int skip;
    }

.. _`rhashtable_iter.members`:

Members
-------

ht
    Table to iterate through

p
    Current pointer

walker
    Associated rhashtable walker

slot
    Current slot

skip
    Number of entries to skip in slot

.. _`rht_grow_above_75`:

rht_grow_above_75
=================

.. c:function:: bool rht_grow_above_75(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if nelems > 0.75 \* table-size

    :param const struct rhashtable \*ht:
        hash table

    :param const struct bucket_table \*tbl:
        current table

.. _`rht_shrink_below_30`:

rht_shrink_below_30
===================

.. c:function:: bool rht_shrink_below_30(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if nelems < 0.3 \* table-size

    :param const struct rhashtable \*ht:
        hash table

    :param const struct bucket_table \*tbl:
        current table

.. _`rht_grow_above_100`:

rht_grow_above_100
==================

.. c:function:: bool rht_grow_above_100(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if nelems > table-size

    :param const struct rhashtable \*ht:
        hash table

    :param const struct bucket_table \*tbl:
        current table

.. _`rht_grow_above_max`:

rht_grow_above_max
==================

.. c:function:: bool rht_grow_above_max(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if table is above maximum

    :param const struct rhashtable \*ht:
        hash table

    :param const struct bucket_table \*tbl:
        current table

.. _`rht_for_each_continue`:

rht_for_each_continue
=====================

.. c:function::  rht_for_each_continue( pos,  head,  tbl,  hash)

    continue iterating over hash chain

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

.. _`rht_for_each`:

rht_for_each
============

.. c:function::  rht_for_each( pos,  tbl,  hash)

    iterate over hash chain

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

.. _`rht_for_each_entry_continue`:

rht_for_each_entry_continue
===========================

.. c:function::  rht_for_each_entry_continue( tpos,  pos,  head,  tbl,  hash,  member)

    continue iterating over hash chain

    :param  tpos:
        the type \* to use as a loop cursor.

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

    :param  member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.

.. _`rht_for_each_entry`:

rht_for_each_entry
==================

.. c:function::  rht_for_each_entry( tpos,  pos,  tbl,  hash,  member)

    iterate over hash chain of given type

    :param  tpos:
        the type \* to use as a loop cursor.

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

    :param  member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.

.. _`rht_for_each_entry_safe`:

rht_for_each_entry_safe
=======================

.. c:function::  rht_for_each_entry_safe( tpos,  pos,  next,  tbl,  hash,  member)

    safely iterate over hash chain of given type

    :param  tpos:
        the type \* to use as a loop cursor.

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  next:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as next in loop cursor.

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

    :param  member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.

.. _`rht_for_each_entry_safe.description`:

Description
-----------

This hash chain list-traversal primitive allows for the looped code to
remove the loop cursor from the list.

.. _`rht_for_each_rcu_continue`:

rht_for_each_rcu_continue
=========================

.. c:function::  rht_for_each_rcu_continue( pos,  head,  tbl,  hash)

    continue iterating over rcu hash chain

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

.. _`rht_for_each_rcu_continue.description`:

Description
-----------

This hash chain list-traversal primitive may safely run concurrently with
the \_rcu mutation primitives such as \ :c:func:`rhashtable_insert`\  as long as the
traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`rht_for_each_rcu`:

rht_for_each_rcu
================

.. c:function::  rht_for_each_rcu( pos,  tbl,  hash)

    iterate over rcu hash chain

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

.. _`rht_for_each_rcu.description`:

Description
-----------

This hash chain list-traversal primitive may safely run concurrently with
the \_rcu mutation primitives such as \ :c:func:`rhashtable_insert`\  as long as the
traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`rht_for_each_entry_rcu_continue`:

rht_for_each_entry_rcu_continue
===============================

.. c:function::  rht_for_each_entry_rcu_continue( tpos,  pos,  head,  tbl,  hash,  member)

    continue iterating over rcu hash chain

    :param  tpos:
        the type \* to use as a loop cursor.

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

    :param  member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.

.. _`rht_for_each_entry_rcu_continue.description`:

Description
-----------

This hash chain list-traversal primitive may safely run concurrently with
the \_rcu mutation primitives such as \ :c:func:`rhashtable_insert`\  as long as the
traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`rht_for_each_entry_rcu`:

rht_for_each_entry_rcu
======================

.. c:function::  rht_for_each_entry_rcu( tpos,  pos,  tbl,  hash,  member)

    iterate over rcu hash chain of given type

    :param  tpos:
        the type \* to use as a loop cursor.

    :param  pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.

    :param  tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 

    :param  hash:
        the hash value / bucket index

    :param  member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.

.. _`rht_for_each_entry_rcu.description`:

Description
-----------

This hash chain list-traversal primitive may safely run concurrently with
the \_rcu mutation primitives such as \ :c:func:`rhashtable_insert`\  as long as the
traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`rhashtable_lookup_fast`:

rhashtable_lookup_fast
======================

.. c:function:: void *rhashtable_lookup_fast(struct rhashtable *ht, const void *key, const struct rhashtable_params params)

    search hash table, inlined version

    :param struct rhashtable \*ht:
        hash table

    :param const void \*key:
        the pointer to the key

    :param const struct rhashtable_params params:
        hash table parameters

.. _`rhashtable_lookup_fast.description`:

Description
-----------

Computes the hash value for the key and traverses the bucket chain looking
for a entry with an identical key. The first matching entry is returned.

Returns the first entry on which the compare function returned true.

.. _`rhashtable_insert_fast`:

rhashtable_insert_fast
======================

.. c:function:: int rhashtable_insert_fast(struct rhashtable *ht, struct rhash_head *obj, const struct rhashtable_params params)

    insert object into hash table

    :param struct rhashtable \*ht:
        hash table

    :param struct rhash_head \*obj:
        pointer to hash head inside object

    :param const struct rhashtable_params params:
        hash table parameters

.. _`rhashtable_insert_fast.description`:

Description
-----------

Will take a per bucket spinlock to protect against mutual mutations
on the same bucket. Multiple insertions may occur in parallel unless
they map to the same bucket lock.

It is safe to call this function from atomic context.

Will trigger an automatic deferred table resizing if the size grows
beyond the watermark indicated by \ :c:func:`grow_decision`\  which can be passed
to \ :c:func:`rhashtable_init`\ .

.. _`rhashtable_lookup_insert_fast`:

rhashtable_lookup_insert_fast
=============================

.. c:function:: int rhashtable_lookup_insert_fast(struct rhashtable *ht, struct rhash_head *obj, const struct rhashtable_params params)

    lookup and insert object into hash table

    :param struct rhashtable \*ht:
        hash table

    :param struct rhash_head \*obj:
        pointer to hash head inside object

    :param const struct rhashtable_params params:
        hash table parameters

.. _`rhashtable_lookup_insert_fast.description`:

Description
-----------

Locks down the bucket chain in both the old and new table if a resize
is in progress to ensure that writers can't remove from the old table
and can't insert to the new table during the atomic operation of search
and insertion. Searches for duplicates in both the old and new table if
a resize is in progress.

This lookup function may only be used for fixed key hash table (key_len
parameter set). It will \ :c:func:`BUG`\  if used inappropriately.

It is safe to call this function from atomic context.

Will trigger an automatic deferred table resizing if the size grows
beyond the watermark indicated by \ :c:func:`grow_decision`\  which can be passed
to \ :c:func:`rhashtable_init`\ .

.. _`rhashtable_lookup_insert_key`:

rhashtable_lookup_insert_key
============================

.. c:function:: int rhashtable_lookup_insert_key(struct rhashtable *ht, const void *key, struct rhash_head *obj, const struct rhashtable_params params)

    search and insert object to hash table with explicit key

    :param struct rhashtable \*ht:
        hash table

    :param const void \*key:
        key

    :param struct rhash_head \*obj:
        pointer to hash head inside object

    :param const struct rhashtable_params params:
        hash table parameters

.. _`rhashtable_lookup_insert_key.description`:

Description
-----------

Locks down the bucket chain in both the old and new table if a resize
is in progress to ensure that writers can't remove from the old table
and can't insert to the new table during the atomic operation of search
and insertion. Searches for duplicates in both the old and new table if
a resize is in progress.

Lookups may occur in parallel with hashtable mutations and resizing.

Will trigger an automatic deferred table resizing if the size grows
beyond the watermark indicated by \ :c:func:`grow_decision`\  which can be passed
to \ :c:func:`rhashtable_init`\ .

Returns zero on success.

.. _`rhashtable_remove_fast`:

rhashtable_remove_fast
======================

.. c:function:: int rhashtable_remove_fast(struct rhashtable *ht, struct rhash_head *obj, const struct rhashtable_params params)

    remove object from hash table

    :param struct rhashtable \*ht:
        hash table

    :param struct rhash_head \*obj:
        pointer to hash head inside object

    :param const struct rhashtable_params params:
        hash table parameters

.. _`rhashtable_remove_fast.description`:

Description
-----------

Since the hash chain is single linked, the removal operation needs to
walk the bucket chain upon removal. The removal operation is thus
considerable slow if the hash table is not correctly sized.

Will automatically shrink the table via \ :c:func:`rhashtable_expand`\  if the
shrink_decision function specified at \ :c:func:`rhashtable_init`\  returns true.

Returns zero on success, -ENOENT if the entry could not be found.

.. _`rhashtable_replace_fast`:

rhashtable_replace_fast
=======================

.. c:function:: int rhashtable_replace_fast(struct rhashtable *ht, struct rhash_head *obj_old, struct rhash_head *obj_new, const struct rhashtable_params params)

    replace an object in hash table

    :param struct rhashtable \*ht:
        hash table

    :param struct rhash_head \*obj_old:
        pointer to hash head inside object being replaced

    :param struct rhash_head \*obj_new:
        pointer to hash head inside object which is new

    :param const struct rhashtable_params params:
        hash table parameters

.. _`rhashtable_replace_fast.description`:

Description
-----------

Replacing an object doesn't affect the number of elements in the hash table
or bucket, so we don't need to worry about shrinking or expanding the
table here.

Returns zero on success, -ENOENT if the entry could not be found,
-EINVAL if hash is not the same for the old and new objects.

.. This file was automatic generated / don't edit.
