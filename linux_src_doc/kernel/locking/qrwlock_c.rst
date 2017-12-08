.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/locking/qrwlock.c

.. _`queued_read_lock_slowpath`:

queued_read_lock_slowpath
=========================

.. c:function:: void queued_read_lock_slowpath(struct qrwlock *lock)

    acquire read lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure

.. _`queued_write_lock_slowpath`:

queued_write_lock_slowpath
==========================

.. c:function:: void queued_write_lock_slowpath(struct qrwlock *lock)

    acquire write lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure

.. This file was automatic generated / don't edit.

