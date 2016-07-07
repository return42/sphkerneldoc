.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rcu_sync.h

.. _`rcu_sync_is_idle`:

rcu_sync_is_idle
================

.. c:function:: bool rcu_sync_is_idle(struct rcu_sync *rsp)

    Are readers permitted to use their fastpaths?

    :param struct rcu_sync \*rsp:
        Pointer to rcu_sync structure to use for synchronization

.. _`rcu_sync_is_idle.description`:

Description
-----------

Returns true if readers are permitted to use their fastpaths.
Must be invoked within an RCU read-side critical section whose
flavor matches that of the rcu_sync struture.

.. This file was automatic generated / don't edit.

