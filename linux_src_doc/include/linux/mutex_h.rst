.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mutex.h

.. _`mutex_init`:

mutex_init
==========

.. c:function::  mutex_init( mutex)

    initialize the mutex

    :param mutex:
        the mutex to be initialized
    :type mutex: 

.. _`mutex_init.description`:

Description
-----------

Initialize the mutex to unlocked state.

It is not allowed to initialize an already locked mutex.

.. _`mutex_is_locked`:

mutex_is_locked
===============

.. c:function:: bool mutex_is_locked(struct mutex *lock)

    is the mutex locked

    :param lock:
        the mutex to be queried
    :type lock: struct mutex \*

.. _`mutex_is_locked.description`:

Description
-----------

Returns true if the mutex is locked, false if unlocked.

.. _`mutex_trylock_recursive`:

mutex_trylock_recursive
=======================

.. c:function:: enum mutex_trylock_recursive_enum mutex_trylock_recursive(struct mutex *lock)

    trylock variant that allows recursive locking

    :param lock:
        mutex to be locked
    :type lock: struct mutex \*

.. _`mutex_trylock_recursive.description`:

Description
-----------

This function should not be used, _ever_. It is purely for hysterical GEM
raisins, and once those are gone this will be removed.

.. _`mutex_trylock_recursive.return`:

Return
------

 - MUTEX_TRYLOCK_FAILED    - trylock failed,
 - MUTEX_TRYLOCK_SUCCESS   - lock acquired,
 - MUTEX_TRYLOCK_RECURSIVE - we already owned the lock.

.. This file was automatic generated / don't edit.

