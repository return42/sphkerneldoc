.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rtmutex.h

.. _`rt_mutex_is_locked`:

rt_mutex_is_locked
==================

.. c:function:: int rt_mutex_is_locked(struct rt_mutex *lock)

    is the mutex locked

    :param lock:
        the mutex to be queried
    :type lock: struct rt_mutex \*

.. _`rt_mutex_is_locked.description`:

Description
-----------

Returns 1 if the mutex is locked, 0 if unlocked.

.. This file was automatic generated / don't edit.

