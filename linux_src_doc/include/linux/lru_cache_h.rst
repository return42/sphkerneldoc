.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/lru_cache.h

.. _`lc_try_lock_for_transaction`:

lc_try_lock_for_transaction
===========================

.. c:function:: int lc_try_lock_for_transaction(struct lru_cache *lc)

    can be used to stop \ :c:func:`lc_get`\  from changing the tracked set

    :param struct lru_cache \*lc:
        the lru cache to operate on

.. _`lc_try_lock_for_transaction.description`:

Description
-----------

Allows (expects) the set to be "dirty".  Note that the reference counts and
order on the active and lru lists may still change.  Used to serialize
changing transactions.  Returns true if we aquired the lock.

.. _`lc_try_lock`:

lc_try_lock
===========

.. c:function:: int lc_try_lock(struct lru_cache *lc)

    variant to stop \ :c:func:`lc_get`\  from changing the tracked set

    :param struct lru_cache \*lc:
        the lru cache to operate on

.. _`lc_try_lock.description`:

Description
-----------

Note that the reference counts and order on the active and lru lists may
still change.  Only works on a "clean" set.  Returns true if we aquired the
lock, which means there are no pending changes, and any further attempt to
change the set will not succeed until the next \ :c:func:`lc_unlock`\ .

.. _`lc_unlock`:

lc_unlock
=========

.. c:function:: void lc_unlock(struct lru_cache *lc)

    unlock \ ``lc``\ , allow \ :c:func:`lc_get`\  to change the set again

    :param struct lru_cache \*lc:
        the lru cache to operate on

.. This file was automatic generated / don't edit.

