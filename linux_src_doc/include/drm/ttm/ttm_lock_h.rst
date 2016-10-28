.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_lock.h

.. _`ttm_lock`:

struct ttm_lock
===============

.. c:type:: struct ttm_lock


.. _`ttm_lock.definition`:

Definition
----------

.. code-block:: c

    struct ttm_lock {
        struct ttm_base_object base;
        wait_queue_head_t queue;
        spinlock_t lock;
        int32_t rw;
        uint32_t flags;
        bool kill_takers;
        int signal;
        struct ttm_object_file *vt_holder;
    }

.. _`ttm_lock.members`:

Members
-------

base
    ttm base object used solely to release the lock if the client
    holding the lock dies.

queue
    Queue for processes waiting for lock change-of-status.

lock
    Spinlock protecting some lock members.

rw
    Read-write lock counter. Protected by \ ``lock``\ .

flags
    Lock state. Protected by \ ``lock``\ .

kill_takers
    Boolean whether to kill takers of the lock.

signal
    Signal to send when kill_takers is true.

vt_holder
    *undescribed*

.. _`ttm_lock_init`:

ttm_lock_init
=============

.. c:function:: void ttm_lock_init(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock
        Initializes the lock.

.. _`ttm_read_unlock`:

ttm_read_unlock
===============

.. c:function:: void ttm_read_unlock(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

.. _`ttm_read_unlock.description`:

Description
-----------

Releases a read lock.

.. _`ttm_read_lock`:

ttm_read_lock
=============

.. c:function:: int ttm_read_lock(struct ttm_lock *lock, bool interruptible)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

    :param bool interruptible:
        Interruptible sleeping while waiting for a lock.

.. _`ttm_read_lock.description`:

Description
-----------

Takes the lock in read mode.

.. _`ttm_read_lock.return`:

Return
------

-ERESTARTSYS If interrupted by a signal and interruptible is true.

.. _`ttm_read_trylock`:

ttm_read_trylock
================

.. c:function:: int ttm_read_trylock(struct ttm_lock *lock, bool interruptible)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

    :param bool interruptible:
        Interruptible sleeping while waiting for a lock.

.. _`ttm_read_trylock.description`:

Description
-----------

Tries to take the lock in read mode. If the lock is already held
in write mode, the function will return -EBUSY. If the lock is held
in vt or suspend mode, the function will sleep until these modes
are unlocked.

.. _`ttm_read_trylock.return`:

Return
------

-EBUSY The lock was already held in write mode.
-ERESTARTSYS If interrupted by a signal and interruptible is true.

.. _`ttm_write_unlock`:

ttm_write_unlock
================

.. c:function:: void ttm_write_unlock(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

.. _`ttm_write_unlock.description`:

Description
-----------

Releases a write lock.

.. _`ttm_write_lock`:

ttm_write_lock
==============

.. c:function:: int ttm_write_lock(struct ttm_lock *lock, bool interruptible)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

    :param bool interruptible:
        Interruptible sleeping while waiting for a lock.

.. _`ttm_write_lock.description`:

Description
-----------

Takes the lock in write mode.

.. _`ttm_write_lock.return`:

Return
------

-ERESTARTSYS If interrupted by a signal and interruptible is true.

.. _`ttm_lock_downgrade`:

ttm_lock_downgrade
==================

.. c:function:: void ttm_lock_downgrade(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

.. _`ttm_lock_downgrade.description`:

Description
-----------

Downgrades a write lock to a read lock.

.. _`ttm_suspend_lock`:

ttm_suspend_lock
================

.. c:function:: void ttm_suspend_lock(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

.. _`ttm_suspend_lock.description`:

Description
-----------

Takes the lock in suspend mode. Excludes read and write mode.

.. _`ttm_suspend_unlock`:

ttm_suspend_unlock
==================

.. c:function:: void ttm_suspend_unlock(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

.. _`ttm_suspend_unlock.description`:

Description
-----------

Releases a suspend lock

.. _`ttm_vt_lock`:

ttm_vt_lock
===========

.. c:function:: int ttm_vt_lock(struct ttm_lock *lock, bool interruptible, struct ttm_object_file *tfile)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

    :param bool interruptible:
        Interruptible sleeping while waiting for a lock.

    :param struct ttm_object_file \*tfile:
        Pointer to a struct ttm_object_file to register the lock with.

.. _`ttm_vt_lock.description`:

Description
-----------

Takes the lock in vt mode.

.. _`ttm_vt_lock.return`:

Return
------

-ERESTARTSYS If interrupted by a signal and interruptible is true.
-ENOMEM: Out of memory when locking.

.. _`ttm_vt_unlock`:

ttm_vt_unlock
=============

.. c:function:: int ttm_vt_unlock(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

.. _`ttm_vt_unlock.description`:

Description
-----------

Releases a vt lock.

.. _`ttm_vt_unlock.return`:

Return
------

-EINVAL If the lock was not held.

.. _`ttm_write_unlock`:

ttm_write_unlock
================

.. c:function:: void ttm_write_unlock(struct ttm_lock *lock)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

.. _`ttm_write_unlock.description`:

Description
-----------

Releases a write lock.

.. _`ttm_write_lock`:

ttm_write_lock
==============

.. c:function:: int ttm_write_lock(struct ttm_lock *lock, bool interruptible)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

    :param bool interruptible:
        Interruptible sleeping while waiting for a lock.

.. _`ttm_write_lock.description`:

Description
-----------

Takes the lock in write mode.

.. _`ttm_write_lock.return`:

Return
------

-ERESTARTSYS If interrupted by a signal and interruptible is true.

.. _`ttm_lock_set_kill`:

ttm_lock_set_kill
=================

.. c:function:: void ttm_lock_set_kill(struct ttm_lock *lock, bool val, int signal)

    :param struct ttm_lock \*lock:
        Pointer to a struct ttm_lock

    :param bool val:
        Boolean whether to kill processes taking the lock.

    :param int signal:
        Signal to send to the process taking the lock.

.. _`ttm_lock_set_kill.description`:

Description
-----------

The kill-when-taking-lock functionality is used to kill processes that keep
on using the TTM functionality when its resources has been taken down, for
example when the X server exits. A typical sequence would look like this:
- X server takes lock in write mode.
- \ :c:func:`ttm_lock_set_kill`\  is called with \ ``val``\  set to true.
- As part of X server exit, TTM resources are taken down.
- X server releases the lock on file release.
- Another dri client wants to render, takes the lock and is killed.

.. This file was automatic generated / don't edit.

