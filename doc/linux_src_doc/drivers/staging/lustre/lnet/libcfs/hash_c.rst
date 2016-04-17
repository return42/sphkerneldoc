.. -*- coding: utf-8; mode: rst -*-

======
hash.c
======


.. _`cfs_hash_rehash_worker`:

cfs_hash_rehash_worker
======================

.. c:function:: int cfs_hash_rehash_worker (cfs_workitem_t *wi)

    :param cfs_workitem_t \*wi:

        *undescribed*



.. _`cfs_hash_rehash_worker.description`:

Description
-----------

``name``     - Descriptive hash name
``cur_bits`` - Initial hash table size, in bits
``max_bits`` - Maximum allowed hash table resize, in bits
``ops``      - Registered hash table operations
``flags``    - CFS_HASH_REHASH enable synamic hash resizing

             - CFS_HASH_SORT enable chained hash sort



.. _`cfs_hash_destroy`:

cfs_hash_destroy
================

.. c:function:: void cfs_hash_destroy (struct cfs_hash *hs)

    :param struct cfs_hash \*hs:

        *undescribed*



.. _`cfs_hash_rehash_inline`:

cfs_hash_rehash_inline
======================

.. c:function:: int cfs_hash_rehash_inline (struct cfs_hash *hs)

    :param struct cfs_hash \*hs:

        *undescribed*



.. _`cfs_hash_rehash_inline.description`:

Description
-----------

- user wants non-blocking change (add/del) on hash table
- too many elements



.. _`cfs_hash_add`:

cfs_hash_add
============

.. c:function:: void cfs_hash_add (struct cfs_hash *hs, const void *key, struct hlist_node *hnode)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param const void \*key:

        *undescribed*

    :param struct hlist_node \*hnode:

        *undescribed*



.. _`cfs_hash_add.description`:

Description
-----------

ops->hs_get function will be called when the item is added.



.. _`cfs_hash_add_unique`:

cfs_hash_add_unique
===================

.. c:function:: int cfs_hash_add_unique (struct cfs_hash *hs, const void *key, struct hlist_node *hnode)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param const void \*key:

        *undescribed*

    :param struct hlist_node \*hnode:

        *undescribed*



.. _`cfs_hash_add_unique.description`:

Description
-----------

ops->hs_get function will be called if the item was added.
Returns 0 on success or -EALREADY on key collisions.



.. _`cfs_hash_findadd_unique`:

cfs_hash_findadd_unique
=======================

.. c:function:: void *cfs_hash_findadd_unique (struct cfs_hash *hs, const void *key, struct hlist_node *hnode)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param const void \*key:

        *undescribed*

    :param struct hlist_node \*hnode:

        *undescribed*



.. _`cfs_hash_findadd_unique.description`:

Description
-----------

already exists in the hash then ops->hs_get will be called on the
conflicting entry and that entry will be returned to the caller.
Otherwise ops->hs_get is called on the item which was added.



.. _`cfs_hash_del`:

cfs_hash_del
============

.. c:function:: void *cfs_hash_del (struct cfs_hash *hs, const void *key, struct hlist_node *hnode)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param const void \*key:

        *undescribed*

    :param struct hlist_node \*hnode:

        *undescribed*



.. _`cfs_hash_del.description`:

Description
-----------

is required to ensure the correct hash bucket is locked since there
is no direct linkage from the item to the bucket.  The object
removed from the hash will be returned and obs->hs_put is called
on the removed object.



.. _`cfs_hash_del_key`:

cfs_hash_del_key
================

.. c:function:: void *cfs_hash_del_key (struct cfs_hash *hs, const void *key)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param const void \*key:

        *undescribed*



.. _`cfs_hash_del_key.description`:

Description
-----------

the hash will be removed, if the key exists multiple times in the hash
``hs`` this function must be called once per key.  The removed object
will be returned and ops->hs_put is called on the removed object.



.. _`cfs_hash_lookup`:

cfs_hash_lookup
===============

.. c:function:: void *cfs_hash_lookup (struct cfs_hash *hs, const void *key)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param const void \*key:

        *undescribed*



.. _`cfs_hash_lookup.description`:

Description
-----------

If the ``key`` is found in the hash hs->:c:func:`hs_get` is called and the
matching objects is returned.  It is the callers responsibility
to call the counterpart ops->hs_put using the :c:func:`cfs_hash_put` macro
when when finished with the object.  If the ``key`` was not found
in the hash ``hs`` NULL is returned.



.. _`cfs_hash_for_each_tight`:

cfs_hash_for_each_tight
=======================

.. c:function:: __u64 cfs_hash_for_each_tight (struct cfs_hash *hs, cfs_hash_for_each_cb_t func, void *data, int remove_safe)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param cfs_hash_for_each_cb_t func:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param int remove_safe:

        *undescribed*



.. _`cfs_hash_for_each_tight.description`:

Description
-----------

and pass to it as an argument each hash item and the private ``data``\ .

a) the function may sleep!
b) during the callback::

   . the bucket lock is held so the callback must never sleep.
   . if ``removal_safe`` is true, use can remove current item by
     cfs_hash_bd_del_locked



.. _`cfs_hash_cond_del`:

cfs_hash_cond_del
=================

.. c:function:: void cfs_hash_cond_del (struct cfs_hash *hs, cfs_hash_cond_opt_cb_t func, void *data)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param cfs_hash_cond_opt_cb_t func:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`cfs_hash_cond_del.description`:

Description
-----------

The write lock being hold during loop for each bucket to avoid
any object be reference.



.. _`cfs_hash_for_each_empty`:

cfs_hash_for_each_empty
=======================

.. c:function:: int cfs_hash_for_each_empty (struct cfs_hash *hs, cfs_hash_for_each_cb_t func, void *data)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param cfs_hash_for_each_cb_t func:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`cfs_hash_for_each_empty.description`:

Description
-----------

``func`` until all the hash buckets are empty.  The passed callback ``func``
or the previously registered callback hs->hs_put must remove the item
from the hash.  You may either use the :c:func:`cfs_hash_del` or :c:func:`hlist_del`
functions.  No rwlocks will be held during the callback ``func`` it is
safe to sleep if needed.  This function will not terminate until the
hash is empty.  Note it is still possible to concurrently add new
items in to the hash.  It is the callers responsibility to ensure
the required locking is in place to prevent concurrent insertions.



.. _`cfs_hash_rehash_cancel_locked`:

cfs_hash_rehash_cancel_locked
=============================

.. c:function:: void cfs_hash_rehash_cancel_locked (struct cfs_hash *hs)

    :param struct cfs_hash \*hs:

        *undescribed*



.. _`cfs_hash_rehash_cancel_locked.description`:

Description
-----------

to grow the hash size when excessive chaining is detected, or to
shrink the hash when it is larger than needed.  When the CFS_HASH_REHASH
flag is set in ``hs`` the libcfs hash may be dynamically rehashed
during addition or removal if the hash's theta value exceeds
either the hs->hs_min_theta or hs->max_theta values.  By default
these values are tuned to keep the chained hash depth small, and
this approach assumes a reasonably uniform hashing function.  The
theta thresholds for ``hs`` are tunable via :c:func:`cfs_hash_set_theta`.



.. _`cfs_hash_rehash_key`:

cfs_hash_rehash_key
===================

.. c:function:: void cfs_hash_rehash_key (struct cfs_hash *hs, const void *old_key, void *new_key, struct hlist_node *hnode)

    :param struct cfs_hash \*hs:

        *undescribed*

    :param const void \*old_key:

        *undescribed*

    :param void \*new_key:

        *undescribed*

    :param struct hlist_node \*hnode:

        *undescribed*



.. _`cfs_hash_rehash_key.description`:

Description
-----------

``old_key`` must be provided to locate the objects previous location
in the hash, and the ``new_key`` will be used to reinsert the object.
Use this function instead of a :c:func:`cfs_hash_add` + :c:func:`cfs_hash_del`
combo when it is critical that there is no window in time where the
object is missing from the hash.  When an object is being rehashed
the registered :c:func:`cfs_hash_get` and :c:func:`cfs_hash_put` functions will
not be called.

