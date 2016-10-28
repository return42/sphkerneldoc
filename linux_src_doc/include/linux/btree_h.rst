.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/btree.h

.. _`btree_head`:

struct btree_head
=================

.. c:type:: struct btree_head

    btree head

.. _`btree_head.definition`:

Definition
----------

.. code-block:: c

    struct btree_head {
        unsigned long *node;
        mempool_t *mempool;
        int height;
    }

.. _`btree_head.members`:

Members
-------

node
    the first node in the tree

mempool
    mempool used for node allocations

height
    current of the tree

.. _`btree_alloc`:

btree_alloc
===========

.. c:function:: void *btree_alloc(gfp_t gfp_mask, void *pool_data)

    allocate function for the mempool

    :param gfp_t gfp_mask:
        gfp mask for the allocation

    :param void \*pool_data:
        unused

.. _`btree_free`:

btree_free
==========

.. c:function:: void btree_free(void *element, void *pool_data)

    free function for the mempool

    :param void \*element:
        the element to free

    :param void \*pool_data:
        unused

.. _`btree_init_mempool`:

btree_init_mempool
==================

.. c:function:: void btree_init_mempool(struct btree_head *head, mempool_t *mempool)

    initialise a btree with given mempool

    :param struct btree_head \*head:
        the btree head to initialise

    :param mempool_t \*mempool:
        the mempool to use

.. _`btree_init_mempool.description`:

Description
-----------

When this function is used, there is no need to destroy
the mempool.

.. _`btree_init`:

btree_init
==========

.. c:function:: int btree_init(struct btree_head *head)

    initialise a btree

    :param struct btree_head \*head:
        the btree head to initialise

.. _`btree_init.description`:

Description
-----------

This function allocates the memory pool that the
btree needs. Returns zero or a negative error code
(-\ ``ENOMEM``\ ) when memory allocation fails.

.. _`btree_destroy`:

btree_destroy
=============

.. c:function:: void btree_destroy(struct btree_head *head)

    destroy mempool

    :param struct btree_head \*head:
        the btree head to destroy

.. _`btree_destroy.description`:

Description
-----------

This function destroys the internal memory pool, use only
when using \ :c:func:`btree_init`\ , not with \ :c:func:`btree_init_mempool`\ .

.. _`btree_lookup`:

btree_lookup
============

.. c:function:: void *btree_lookup(struct btree_head *head, struct btree_geo *geo, unsigned long *key)

    look up a key in the btree

    :param struct btree_head \*head:
        the btree to look in

    :param struct btree_geo \*geo:
        the btree geometry

    :param unsigned long \*key:
        the key to look up

.. _`btree_lookup.description`:

Description
-----------

This function returns the value for the given key, or \ ``NULL``\ .

.. _`btree_insert`:

btree_insert
============

.. c:function:: int btree_insert(struct btree_head *head, struct btree_geo *geo, unsigned long *key, void *val, gfp_t gfp)

    insert an entry into the btree

    :param struct btree_head \*head:
        the btree to add to

    :param struct btree_geo \*geo:
        the btree geometry

    :param unsigned long \*key:
        the key to add (must not already be present)

    :param void \*val:
        the value to add (must not be \ ``NULL``\ )

    :param gfp_t gfp:
        allocation flags for node allocations

.. _`btree_insert.description`:

Description
-----------

This function returns 0 if the item could be added, or an
error code if it failed (may fail due to memory pressure).

.. _`btree_update`:

btree_update
============

.. c:function:: int btree_update(struct btree_head *head, struct btree_geo *geo, unsigned long *key, void *val)

    update an entry in the btree

    :param struct btree_head \*head:
        the btree to update

    :param struct btree_geo \*geo:
        the btree geometry

    :param unsigned long \*key:
        the key to update

    :param void \*val:
        the value to change it to (must not be \ ``NULL``\ )

.. _`btree_update.description`:

Description
-----------

This function returns 0 if the update was successful, or
-\ ``ENOENT``\  if the key could not be found.

.. _`btree_remove`:

btree_remove
============

.. c:function:: void *btree_remove(struct btree_head *head, struct btree_geo *geo, unsigned long *key)

    remove an entry from the btree

    :param struct btree_head \*head:
        the btree to update

    :param struct btree_geo \*geo:
        the btree geometry

    :param unsigned long \*key:
        the key to remove

.. _`btree_remove.description`:

Description
-----------

This function returns the removed entry, or \ ``NULL``\  if the key
could not be found.

.. _`btree_merge`:

btree_merge
===========

.. c:function:: int btree_merge(struct btree_head *target, struct btree_head *victim, struct btree_geo *geo, gfp_t gfp)

    merge two btrees

    :param struct btree_head \*target:
        the tree that gets all the entries

    :param struct btree_head \*victim:
        the tree that gets merged into \ ``target``\ 

    :param struct btree_geo \*geo:
        the btree geometry

    :param gfp_t gfp:
        allocation flags

.. _`btree_merge.description`:

Description
-----------

The two trees \ ``target``\  and \ ``victim``\  may not contain the same keys,
that is a bug and triggers a \ :c:func:`BUG`\ . This function returns zero
if the trees were merged successfully, and may return a failure
when memory allocation fails, in which case both trees might have
been partially merged, i.e. some entries have been moved from
\ ``victim``\  to \ ``target``\ .

.. _`btree_last`:

btree_last
==========

.. c:function:: void *btree_last(struct btree_head *head, struct btree_geo *geo, unsigned long *key)

    get last entry in btree

    :param struct btree_head \*head:
        btree head

    :param struct btree_geo \*geo:
        btree geometry

    :param unsigned long \*key:
        last key

.. _`btree_last.description`:

Description
-----------

Returns the last entry in the btree, and sets \ ``key``\  to the key
of that entry; returns NULL if the tree is empty, in that case
key is not changed.

.. _`btree_get_prev`:

btree_get_prev
==============

.. c:function:: void *btree_get_prev(struct btree_head *head, struct btree_geo *geo, unsigned long *key)

    get previous entry

    :param struct btree_head \*head:
        btree head

    :param struct btree_geo \*geo:
        btree geometry

    :param unsigned long \*key:
        pointer to key

.. _`btree_get_prev.description`:

Description
-----------

The function returns the next item right before the value pointed to by
\ ``key``\ , and updates \ ``key``\  with its key, or returns \ ``NULL``\  when there is no
entry with a key smaller than the given key.

.. This file was automatic generated / don't edit.

