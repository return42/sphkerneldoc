.. -*- coding: utf-8; mode: rst -*-

=========
qrwlock.c
=========


.. _`rspin_until_writer_unlock`:

rspin_until_writer_unlock
=========================

.. c:function:: void rspin_until_writer_unlock (struct qrwlock *lock, u32 cnts)

    inc reader count & spin until writer is gone

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure

    :param u32 cnts:

        *undescribed*



.. _`rspin_until_writer_unlock.description`:

Description
-----------

In interrupt context or at the head of the queue, the reader will just
increment the reader count & wait until the writer releases the lock.



.. _`queued_read_lock_slowpath`:

queued_read_lock_slowpath
=========================

.. c:function:: void queued_read_lock_slowpath (struct qrwlock *lock, u32 cnts)

    acquire read lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure

    :param u32 cnts:
        Current qrwlock lock value



.. _`queued_write_lock_slowpath`:

queued_write_lock_slowpath
==========================

.. c:function:: void queued_write_lock_slowpath (struct qrwlock *lock)

    acquire write lock of a queue rwlock

    :param struct qrwlock \*lock:
        Pointer to queue rwlock structure

