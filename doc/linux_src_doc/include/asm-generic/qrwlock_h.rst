.. -*- coding: utf-8; mode: rst -*-

=========
qrwlock.h
=========


.. _`queued_read_can_lock`:

queued_read_can_lock
====================

.. c:function:: int queued_read_can_lock (struct qrwlock *lock)

    would read_trylock() succeed?

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure



.. _`queued_write_can_lock`:

queued_write_can_lock
=====================

.. c:function:: int queued_write_can_lock (struct qrwlock *lock)

    would write_trylock() succeed?

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure



.. _`queued_read_trylock`:

queued_read_trylock
===================

.. c:function:: int queued_read_trylock (struct qrwlock *lock)

    try to acquire read lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure



.. _`queued_read_trylock.return`:

Return
------

1 if lock acquired, 0 if failed



.. _`queued_write_trylock`:

queued_write_trylock
====================

.. c:function:: int queued_write_trylock (struct qrwlock *lock)

    try to acquire write lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure



.. _`queued_write_trylock.return`:

Return
------

1 if lock acquired, 0 if failed



.. _`queued_read_lock`:

queued_read_lock
================

.. c:function:: void queued_read_lock (struct qrwlock *lock)

    acquire read lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure



.. _`queued_write_lock`:

queued_write_lock
=================

.. c:function:: void queued_write_lock (struct qrwlock *lock)

    acquire write lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure



.. _`queued_read_unlock`:

queued_read_unlock
==================

.. c:function:: void queued_read_unlock (struct qrwlock *lock)

    release read lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure



.. _`queued_write_unlock`:

queued_write_unlock
===================

.. c:function:: void queued_write_unlock (struct qrwlock *lock)

    release write lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure

