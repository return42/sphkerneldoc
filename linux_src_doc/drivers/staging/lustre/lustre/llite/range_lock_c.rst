.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/range_lock.c

.. _`range_lock_tree_init`:

range_lock_tree_init
====================

.. c:function:: void range_lock_tree_init(struct range_lock_tree *tree)

    :param struct range_lock_tree \*tree:
        *undescribed*

.. _`range_lock_tree_init.description`:

Description
-----------

\param tree [in]     an empty range lock tree

.. _`range_lock_tree_init.pre`:

Pre
---

Caller should have allocated the range lock tree.

.. _`range_lock_tree_init.post`:

Post
----

The range lock tree is ready to function.

.. _`range_lock_init`:

range_lock_init
===============

.. c:function:: void range_lock_init(struct range_lock *lock, __u64 start, __u64 end)

    :param struct range_lock \*lock:
        *undescribed*

    :param __u64 start:
        *undescribed*

    :param __u64 end:
        *undescribed*

.. _`range_lock_init.description`:

Description
-----------

\param lock  [in]    an empty range lock node
\param start [in]    start of the covering region
\param end   [in]    end of the covering region

.. _`range_lock_init.pre`:

Pre
---

Caller should have allocated the range lock node.

.. _`range_lock_init.post`:

Post
----

The range lock node is meant to cover [start, end] region

.. _`range_unlock_cb`:

range_unlock_cb
===============

.. c:function:: enum interval_iter range_unlock_cb(struct interval_node *node, void *arg)

    :param struct interval_node \*node:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`range_unlock_cb.description`:

Description
-----------

\param node [in]     a range lock found overlapped during interval node
search
\param arg [in]      the range lock to be tested

\retval INTERVAL_ITER_CONT   indicate to continue the search for next
overlapping range node
\retval INTERVAL_ITER_STOP   indicate to stop the search

.. _`range_unlock`:

range_unlock
============

.. c:function:: void range_unlock(struct range_lock_tree *tree, struct range_lock *lock)

    :param struct range_lock_tree \*tree:
        *undescribed*

    :param struct range_lock \*lock:
        *undescribed*

.. _`range_unlock.description`:

Description
-----------

\param tree [in]     range lock tree
\param lock [in]     range lock to be deleted

If this lock has been granted, relase it; if not, just delete it from
the tree or the same region lock list. Wake up those locks only blocked
by this lock through \ :c:func:`range_unlock_cb`\ .

.. _`range_lock_cb`:

range_lock_cb
=============

.. c:function:: enum interval_iter range_lock_cb(struct interval_node *node, void *arg)

    :param struct interval_node \*node:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`range_lock_cb.description`:

Description
-----------

\param node [in]     a range lock found overlapped during interval node
search
\param arg [in]      the range lock to be tested

\retval INTERVAL_ITER_CONT   indicate to continue the search for next
overlapping range node
\retval INTERVAL_ITER_STOP   indicate to stop the search

.. _`range_lock`:

range_lock
==========

.. c:function:: int range_lock(struct range_lock_tree *tree, struct range_lock *lock)

    :param struct range_lock_tree \*tree:
        *undescribed*

    :param struct range_lock \*lock:
        *undescribed*

.. _`range_lock.description`:

Description
-----------

\param tree [in]     range lock tree
\param lock [in]     range lock node containing the region span

\retval 0    get the range lock
\retval <0   error code while not getting the range lock

If there exists overlapping range lock, the new lock will wait and
retry, if later it find that it is not the chosen one to wake up,
it wait again.

.. This file was automatic generated / don't edit.

