.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwspinlock/hwspinlock_internal.h

.. _`hwspinlock_ops`:

struct hwspinlock_ops
=====================

.. c:type:: struct hwspinlock_ops

    platform-specific hwspinlock handlers

.. _`hwspinlock_ops.definition`:

Definition
----------

.. code-block:: c

    struct hwspinlock_ops {
        int (* trylock) (struct hwspinlock *lock);
        void (* unlock) (struct hwspinlock *lock);
        void (* relax) (struct hwspinlock *lock);
    }

.. _`hwspinlock_ops.members`:

Members
-------

trylock
    make a single attempt to take the lock. returns 0 on
    failure and true on success. may \_not\_ sleep.

unlock
    release the lock. always succeed. may \_not\_ sleep.

relax
    optional, platform-specific relax handler, called by hwspinlock
    core while spinning on a lock, between two successive
    invocations of \ ``trylock``\ . may \_not\_ sleep.

.. _`hwspinlock`:

struct hwspinlock
=================

.. c:type:: struct hwspinlock

    this struct represents a single hwspinlock instance

.. _`hwspinlock.definition`:

Definition
----------

.. code-block:: c

    struct hwspinlock {
        struct hwspinlock_device *bank;
        spinlock_t lock;
        void *priv;
    }

.. _`hwspinlock.members`:

Members
-------

bank
    the hwspinlock_device structure which owns this lock

lock
    initialized and used by hwspinlock core

priv
    private data, owned by the underlying platform-specific hwspinlock drv

.. _`hwspinlock_device`:

struct hwspinlock_device
========================

.. c:type:: struct hwspinlock_device

    a device which usually spans numerous hwspinlocks

.. _`hwspinlock_device.definition`:

Definition
----------

.. code-block:: c

    struct hwspinlock_device {
        struct device *dev;
        const struct hwspinlock_ops *ops;
        int base_id;
        int num_locks;
        struct hwspinlock lock[0];
    }

.. _`hwspinlock_device.members`:

Members
-------

dev
    underlying device, will be used to invoke runtime PM api

ops
    platform-specific hwspinlock handlers

base_id
    id index of the first lock in this device

num_locks
    number of locks in this device

lock
    dynamically allocated array of 'struct hwspinlock'

.. This file was automatic generated / don't edit.

