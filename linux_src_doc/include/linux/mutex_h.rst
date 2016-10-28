.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mutex.h

.. _`mutex_init`:

mutex_init
==========

.. c:function::  mutex_init( mutex)

    initialize the mutex

    :param  mutex:
        the mutex to be initialized

.. _`mutex_init.description`:

Description
-----------

Initialize the mutex to unlocked state.

It is not allowed to initialize an already locked mutex.

.. _`mutex_is_locked`:

mutex_is_locked
===============

.. c:function:: int mutex_is_locked(struct mutex *lock)

    is the mutex locked

    :param struct mutex \*lock:
        the mutex to be queried

.. _`mutex_is_locked.description`:

Description
-----------

Returns 1 if the mutex is locked, 0 if unlocked.

.. This file was automatic generated / don't edit.

