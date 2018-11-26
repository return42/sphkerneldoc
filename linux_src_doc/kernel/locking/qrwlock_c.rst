.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/locking/qrwlock.c

.. _`queued_read_lock_slowpath`:

queued_read_lock_slowpath
=========================

.. c:function:: void queued_read_lock_slowpath(struct qrwlock *lock)

    acquire read lock of a queue rwlock

    :param lock:
        Pointer to queue rwlock structure
    :type lock: struct qrwlock \*

.. _`queued_write_lock_slowpath`:

queued_write_lock_slowpath
==========================

.. c:function:: void queued_write_lock_slowpath(struct qrwlock *lock)

    acquire write lock of a queue rwlock

    :param lock:
        Pointer to queue rwlock structure
    :type lock: struct qrwlock \*

.. This file was automatic generated / don't edit.

