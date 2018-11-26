.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/list_lru.h

.. _`list_lru_add`:

list_lru_add
============

.. c:function:: bool list_lru_add(struct list_lru *lru, struct list_head *item)

    add an element to the lru list's tail

    :param lru:
        *undescribed*
    :type lru: struct list_lru \*

    :param item:
        the item to be added.
    :type item: struct list_head \*

.. _`list_lru_add.description`:

Description
-----------

If the element is already part of a list, this function returns doing
nothing. Therefore the caller does not need to keep state about whether or
not the element already belongs in the list and is allowed to lazy update
it. Note however that this is valid for \*a\* list, not \*this\* list. If
the caller organize itself in a way that elements can be in more than
one type of list, it is up to the caller to fully remove the item from
the previous list (with \ :c:func:`list_lru_del`\  for instance) before moving it
to \ ``list_lru``\ 

.. _`list_lru_add.return-value`:

Return value
------------

true if the list was updated, false otherwise

.. _`list_lru_del`:

list_lru_del
============

.. c:function:: bool list_lru_del(struct list_lru *lru, struct list_head *item)

    delete an element to the lru list

    :param lru:
        *undescribed*
    :type lru: struct list_lru \*

    :param item:
        the item to be deleted.
    :type item: struct list_head \*

.. _`list_lru_del.description`:

Description
-----------

This function works analogously as list_lru_add in terms of list
manipulation. The comments about an element already pertaining to
a list are also valid for list_lru_del.

.. _`list_lru_del.return-value`:

Return value
------------

true if the list was updated, false otherwise

.. _`list_lru_count_one`:

list_lru_count_one
==================

.. c:function:: unsigned long list_lru_count_one(struct list_lru *lru, int nid, struct mem_cgroup *memcg)

    return the number of objects currently held by \ ``lru``\ 

    :param lru:
        the lru pointer.
    :type lru: struct list_lru \*

    :param nid:
        the node id to count from.
    :type nid: int

    :param memcg:
        the cgroup to count from.
    :type memcg: struct mem_cgroup \*

.. _`list_lru_count_one.description`:

Description
-----------

Always return a non-negative number, 0 for empty lists. There is no
guarantee that the list is not updated while the count is being computed.
Callers that want such a guarantee need to provide an outer lock.

.. _`list_lru_walk_one`:

list_lru_walk_one
=================

.. c:function:: unsigned long list_lru_walk_one(struct list_lru *lru, int nid, struct mem_cgroup *memcg, list_lru_walk_cb isolate, void *cb_arg, unsigned long *nr_to_walk)

    walk a list_lru, isolating and disposing freeable items.

    :param lru:
        the lru pointer.
    :type lru: struct list_lru \*

    :param nid:
        the node id to scan from.
    :type nid: int

    :param memcg:
        the cgroup to scan from.
    :type memcg: struct mem_cgroup \*

    :param isolate:
        callback function that is resposible for deciding what to do with
        the item currently being scanned
    :type isolate: list_lru_walk_cb

    :param cb_arg:
        opaque type that will be passed to \ ``isolate``\ 
    :type cb_arg: void \*

    :param nr_to_walk:
        how many items to scan.
    :type nr_to_walk: unsigned long \*

.. _`list_lru_walk_one.description`:

Description
-----------

This function will scan all elements in a particular list_lru, calling the
\ ``isolate``\  callback for each of those items, along with the current list
spinlock and a caller-provided opaque. The \ ``isolate``\  callback can choose to
drop the lock internally, but \*must\* return with the lock held. The callback
will return an enum lru_status telling the list_lru infrastructure what to
do with the object being scanned.

Please note that nr_to_walk does not mean how many objects will be freed,
just how many objects will be scanned.

.. _`list_lru_walk_one.return-value`:

Return value
------------

the number of objects effectively removed from the LRU.

.. _`list_lru_walk_one_irq`:

list_lru_walk_one_irq
=====================

.. c:function:: unsigned long list_lru_walk_one_irq(struct list_lru *lru, int nid, struct mem_cgroup *memcg, list_lru_walk_cb isolate, void *cb_arg, unsigned long *nr_to_walk)

    walk a list_lru, isolating and disposing freeable items.

    :param lru:
        the lru pointer.
    :type lru: struct list_lru \*

    :param nid:
        the node id to scan from.
    :type nid: int

    :param memcg:
        the cgroup to scan from.
    :type memcg: struct mem_cgroup \*

    :param isolate:
        callback function that is resposible for deciding what to do with
        the item currently being scanned
    :type isolate: list_lru_walk_cb

    :param cb_arg:
        opaque type that will be passed to \ ``isolate``\ 
    :type cb_arg: void \*

    :param nr_to_walk:
        how many items to scan.
    :type nr_to_walk: unsigned long \*

.. _`list_lru_walk_one_irq.description`:

Description
-----------

Same as \ ``list_lru_walk_one``\  except that the spinlock is acquired with
\ :c:func:`spin_lock_irq`\ .

.. This file was automatic generated / don't edit.

