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
        unsigned int nest;
        unsigned int rehash;
        u32 hash_rnd;
        unsigned int locks_mask;
        spinlock_t *locks;
        struct list_head walkers;
        struct rcu_head rcu;
        struct bucket_table __rcu *future_tbl;
        struct rhash_head __rcu *buckets[] ____cacheline_aligned_in_smp;
    }

.. _`bucket_table.members`:

Members
-------

size
    Number of hash buckets

nest
    Number of bits of first-level nested table.

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

.. _`rht_grow_above_75`:

rht_grow_above_75
=================

.. c:function:: bool rht_grow_above_75(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if nelems > 0.75 \* table-size

    :param ht:
        hash table
    :type ht: const struct rhashtable \*

    :param tbl:
        current table
    :type tbl: const struct bucket_table \*

.. _`rht_shrink_below_30`:

rht_shrink_below_30
===================

.. c:function:: bool rht_shrink_below_30(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if nelems < 0.3 \* table-size

    :param ht:
        hash table
    :type ht: const struct rhashtable \*

    :param tbl:
        current table
    :type tbl: const struct bucket_table \*

.. _`rht_grow_above_100`:

rht_grow_above_100
==================

.. c:function:: bool rht_grow_above_100(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if nelems > table-size

    :param ht:
        hash table
    :type ht: const struct rhashtable \*

    :param tbl:
        current table
    :type tbl: const struct bucket_table \*

.. _`rht_grow_above_max`:

rht_grow_above_max
==================

.. c:function:: bool rht_grow_above_max(const struct rhashtable *ht, const struct bucket_table *tbl)

    returns true if table is above maximum

    :param ht:
        hash table
    :type ht: const struct rhashtable \*

    :param tbl:
        current table
    :type tbl: const struct bucket_table \*

.. _`rht_for_each_continue`:

rht_for_each_continue
=====================

.. c:function::  rht_for_each_continue( pos,  head,  tbl,  hash)

    continue iterating over hash chain

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from
    :type head: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

.. _`rht_for_each`:

rht_for_each
============

.. c:function::  rht_for_each( pos,  tbl,  hash)

    iterate over hash chain

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

.. _`rht_for_each_entry_continue`:

rht_for_each_entry_continue
===========================

.. c:function::  rht_for_each_entry_continue( tpos,  pos,  head,  tbl,  hash,  member)

    continue iterating over hash chain

    :param tpos:
        the type \* to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from
    :type head: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

    :param member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.
    :type member: 

.. _`rht_for_each_entry`:

rht_for_each_entry
==================

.. c:function::  rht_for_each_entry( tpos,  pos,  tbl,  hash,  member)

    iterate over hash chain of given type

    :param tpos:
        the type \* to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

    :param member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.
    :type member: 

.. _`rht_for_each_entry_safe`:

rht_for_each_entry_safe
=======================

.. c:function::  rht_for_each_entry_safe( tpos,  pos,  next,  tbl,  hash,  member)

    safely iterate over hash chain of given type

    :param tpos:
        the type \* to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param next:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as next in loop cursor.
    :type next: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

    :param member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.
    :type member: 

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

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from
    :type head: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

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

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

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

    :param tpos:
        the type \* to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the previous \ :c:type:`struct rhash_head <rhash_head>`\  to continue from
    :type head: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

    :param member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.
    :type member: 

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

    :param tpos:
        the type \* to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct rhash_head <rhash_head>`\  to use as a loop cursor.
    :type pos: 

    :param tbl:
        the \ :c:type:`struct bucket_table <bucket_table>`\ 
    :type tbl: 

    :param hash:
        the hash value / bucket index
    :type hash: 

    :param member:
        name of the \ :c:type:`struct rhash_head <rhash_head>`\  within the hashable struct.
    :type member: 

.. _`rht_for_each_entry_rcu.description`:

Description
-----------

This hash chain list-traversal primitive may safely run concurrently with
the \_rcu mutation primitives such as \ :c:func:`rhashtable_insert`\  as long as the
traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`rhl_for_each_rcu`:

rhl_for_each_rcu
================

.. c:function::  rhl_for_each_rcu( pos,  list)

    iterate over rcu hash table list

    :param pos:
        the \ :c:type:`struct rlist_head <rlist_head>`\  to use as a loop cursor.
    :type pos: 

    :param list:
        the head of the list
    :type list: 

.. _`rhl_for_each_rcu.description`:

Description
-----------

This hash chain list-traversal primitive should be used on the
list returned by rhltable_lookup.

.. _`rhl_for_each_entry_rcu`:

rhl_for_each_entry_rcu
======================

.. c:function::  rhl_for_each_entry_rcu( tpos,  pos,  list,  member)

    iterate over rcu hash table list of given type

    :param tpos:
        the type \* to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct rlist_head <rlist_head>`\  to use as a loop cursor.
    :type pos: 

    :param list:
        the head of the list
    :type list: 

    :param member:
        name of the \ :c:type:`struct rlist_head <rlist_head>`\  within the hashable struct.
    :type member: 

.. _`rhl_for_each_entry_rcu.description`:

Description
-----------

This hash chain list-traversal primitive should be used on the
list returned by rhltable_lookup.

.. _`rhashtable_lookup`:

rhashtable_lookup
=================

.. c:function:: void *rhashtable_lookup(struct rhashtable *ht, const void *key, const struct rhashtable_params params)

    search hash table

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param key:
        the pointer to the key
    :type key: const void \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_lookup.description`:

Description
-----------

Computes the hash value for the key and traverses the bucket chain looking
for a entry with an identical key. The first matching entry is returned.

This must only be called under the RCU read lock.

Returns the first entry on which the compare function returned true.

.. _`rhashtable_lookup_fast`:

rhashtable_lookup_fast
======================

.. c:function:: void *rhashtable_lookup_fast(struct rhashtable *ht, const void *key, const struct rhashtable_params params)

    search hash table, without RCU read lock

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param key:
        the pointer to the key
    :type key: const void \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_lookup_fast.description`:

Description
-----------

Computes the hash value for the key and traverses the bucket chain looking
for a entry with an identical key. The first matching entry is returned.

Only use this function when you have other mechanisms guaranteeing
that the object won't go away after the RCU read lock is released.

Returns the first entry on which the compare function returned true.

.. _`rhltable_lookup`:

rhltable_lookup
===============

.. c:function:: struct rhlist_head *rhltable_lookup(struct rhltable *hlt, const void *key, const struct rhashtable_params params)

    search hash list table

    :param hlt:
        hash table
    :type hlt: struct rhltable \*

    :param key:
        the pointer to the key
    :type key: const void \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhltable_lookup.description`:

Description
-----------

Computes the hash value for the key and traverses the bucket chain looking
for a entry with an identical key.  All matching entries are returned
in a list.

This must only be called under the RCU read lock.

Returns the list of entries that match the given key.

.. _`rhashtable_insert_fast`:

rhashtable_insert_fast
======================

.. c:function:: int rhashtable_insert_fast(struct rhashtable *ht, struct rhash_head *obj, const struct rhashtable_params params)

    insert object into hash table

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param obj:
        pointer to hash head inside object
    :type obj: struct rhash_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_insert_fast.description`:

Description
-----------

Will take a per bucket spinlock to protect against mutual mutations
on the same bucket. Multiple insertions may occur in parallel unless
they map to the same bucket lock.

It is safe to call this function from atomic context.

Will trigger an automatic deferred table resizing if residency in the
table grows beyond 70%.

.. _`rhltable_insert_key`:

rhltable_insert_key
===================

.. c:function:: int rhltable_insert_key(struct rhltable *hlt, const void *key, struct rhlist_head *list, const struct rhashtable_params params)

    insert object into hash list table

    :param hlt:
        hash list table
    :type hlt: struct rhltable \*

    :param key:
        the pointer to the key
    :type key: const void \*

    :param list:
        pointer to hash list head inside object
    :type list: struct rhlist_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhltable_insert_key.description`:

Description
-----------

Will take a per bucket spinlock to protect against mutual mutations
on the same bucket. Multiple insertions may occur in parallel unless
they map to the same bucket lock.

It is safe to call this function from atomic context.

Will trigger an automatic deferred table resizing if residency in the
table grows beyond 70%.

.. _`rhltable_insert`:

rhltable_insert
===============

.. c:function:: int rhltable_insert(struct rhltable *hlt, struct rhlist_head *list, const struct rhashtable_params params)

    insert object into hash list table

    :param hlt:
        hash list table
    :type hlt: struct rhltable \*

    :param list:
        pointer to hash list head inside object
    :type list: struct rhlist_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhltable_insert.description`:

Description
-----------

Will take a per bucket spinlock to protect against mutual mutations
on the same bucket. Multiple insertions may occur in parallel unless
they map to the same bucket lock.

It is safe to call this function from atomic context.

Will trigger an automatic deferred table resizing if residency in the
table grows beyond 70%.

.. _`rhashtable_lookup_insert_fast`:

rhashtable_lookup_insert_fast
=============================

.. c:function:: int rhashtable_lookup_insert_fast(struct rhashtable *ht, struct rhash_head *obj, const struct rhashtable_params params)

    lookup and insert object into hash table

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param obj:
        pointer to hash head inside object
    :type obj: struct rhash_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

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

Will trigger an automatic deferred table resizing if residency in the
table grows beyond 70%.

.. _`rhashtable_lookup_get_insert_fast`:

rhashtable_lookup_get_insert_fast
=================================

.. c:function:: void *rhashtable_lookup_get_insert_fast(struct rhashtable *ht, struct rhash_head *obj, const struct rhashtable_params params)

    lookup and insert object into hash table

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param obj:
        pointer to hash head inside object
    :type obj: struct rhash_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_lookup_get_insert_fast.description`:

Description
-----------

Just like \ :c:func:`rhashtable_lookup_insert_fast`\ , but this function returns the
object if it exists, NULL if it did not and the insertion was successful,
and an ERR_PTR otherwise.

.. _`rhashtable_lookup_insert_key`:

rhashtable_lookup_insert_key
============================

.. c:function:: int rhashtable_lookup_insert_key(struct rhashtable *ht, const void *key, struct rhash_head *obj, const struct rhashtable_params params)

    search and insert object to hash table with explicit key

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param key:
        key
    :type key: const void \*

    :param obj:
        pointer to hash head inside object
    :type obj: struct rhash_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_lookup_insert_key.description`:

Description
-----------

Locks down the bucket chain in both the old and new table if a resize
is in progress to ensure that writers can't remove from the old table
and can't insert to the new table during the atomic operation of search
and insertion. Searches for duplicates in both the old and new table if
a resize is in progress.

Lookups may occur in parallel with hashtable mutations and resizing.

Will trigger an automatic deferred table resizing if residency in the
table grows beyond 70%.

Returns zero on success.

.. _`rhashtable_lookup_get_insert_key`:

rhashtable_lookup_get_insert_key
================================

.. c:function:: void *rhashtable_lookup_get_insert_key(struct rhashtable *ht, const void *key, struct rhash_head *obj, const struct rhashtable_params params)

    lookup and insert object into hash table

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param key:
        *undescribed*
    :type key: const void \*

    :param obj:
        pointer to hash head inside object
    :type obj: struct rhash_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_lookup_get_insert_key.description`:

Description
-----------

Just like \ :c:func:`rhashtable_lookup_insert_key`\ , but this function returns the
object if it exists, NULL if it does not and the insertion was successful,
and an ERR_PTR otherwise.

.. _`rhashtable_remove_fast`:

rhashtable_remove_fast
======================

.. c:function:: int rhashtable_remove_fast(struct rhashtable *ht, struct rhash_head *obj, const struct rhashtable_params params)

    remove object from hash table

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param obj:
        pointer to hash head inside object
    :type obj: struct rhash_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_remove_fast.description`:

Description
-----------

Since the hash chain is single linked, the removal operation needs to
walk the bucket chain upon removal. The removal operation is thus
considerable slow if the hash table is not correctly sized.

Will automatically shrink the table if permitted when residency drops
below 30%.

Returns zero on success, -ENOENT if the entry could not be found.

.. _`rhltable_remove`:

rhltable_remove
===============

.. c:function:: int rhltable_remove(struct rhltable *hlt, struct rhlist_head *list, const struct rhashtable_params params)

    remove object from hash list table

    :param hlt:
        hash list table
    :type hlt: struct rhltable \*

    :param list:
        pointer to hash list head inside object
    :type list: struct rhlist_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhltable_remove.description`:

Description
-----------

Since the hash chain is single linked, the removal operation needs to
walk the bucket chain upon removal. The removal operation is thus
considerable slow if the hash table is not correctly sized.

Will automatically shrink the table if permitted when residency drops
below 30%

Returns zero on success, -ENOENT if the entry could not be found.

.. _`rhashtable_replace_fast`:

rhashtable_replace_fast
=======================

.. c:function:: int rhashtable_replace_fast(struct rhashtable *ht, struct rhash_head *obj_old, struct rhash_head *obj_new, const struct rhashtable_params params)

    replace an object in hash table

    :param ht:
        hash table
    :type ht: struct rhashtable \*

    :param obj_old:
        pointer to hash head inside object being replaced
    :type obj_old: struct rhash_head \*

    :param obj_new:
        pointer to hash head inside object which is new
    :type obj_new: struct rhash_head \*

    :param params:
        hash table parameters
    :type params: const struct rhashtable_params

.. _`rhashtable_replace_fast.description`:

Description
-----------

Replacing an object doesn't affect the number of elements in the hash table
or bucket, so we don't need to worry about shrinking or expanding the
table here.

Returns zero on success, -ENOENT if the entry could not be found,
-EINVAL if hash is not the same for the old and new objects.

.. _`rhltable_walk_enter`:

rhltable_walk_enter
===================

.. c:function:: void rhltable_walk_enter(struct rhltable *hlt, struct rhashtable_iter *iter)

    Initialise an iterator

    :param hlt:
        Table to walk over
    :type hlt: struct rhltable \*

    :param iter:
        Hash table Iterator
    :type iter: struct rhashtable_iter \*

.. _`rhltable_walk_enter.description`:

Description
-----------

This function prepares a hash table walk.

Note that if you restart a walk after rhashtable_walk_stop you
may see the same object twice.  Also, you may miss objects if
there are removals in between rhashtable_walk_stop and the next
call to rhashtable_walk_start.

For a completely stable walk you should construct your own data
structure outside the hash table.

This function may be called from any process context, including
non-preemptable context, but cannot be called from softirq or
hardirq context.

You must call rhashtable_walk_exit after this function returns.

.. _`rhltable_free_and_destroy`:

rhltable_free_and_destroy
=========================

.. c:function:: void rhltable_free_and_destroy(struct rhltable *hlt, void (*free_fn)(void *ptr, void *arg), void *arg)

    free elements and destroy hash list table

    :param hlt:
        the hash list table to destroy
    :type hlt: struct rhltable \*

    :param void (\*free_fn)(void \*ptr, void \*arg):
        callback to release resources of element

    :param arg:
        pointer passed to free_fn
    :type arg: void \*

.. _`rhltable_free_and_destroy.description`:

Description
-----------

See documentation for rhashtable_free_and_destroy.

.. This file was automatic generated / don't edit.

