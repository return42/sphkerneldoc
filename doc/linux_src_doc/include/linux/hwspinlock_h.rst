.. -*- coding: utf-8; mode: rst -*-

============
hwspinlock.h
============


.. _`hwspinlock_pdata`:

struct hwspinlock_pdata
=======================

.. c:type:: hwspinlock_pdata

    platform data for hwspinlock drivers


.. _`hwspinlock_pdata.definition`:

Definition
----------

.. code-block:: c

  struct hwspinlock_pdata {
    int base_id;
  };


.. _`hwspinlock_pdata.members`:

Members
-------

:``base_id``:
    base id for this hwspinlock device




.. _`hwspinlock_pdata.description`:

Description
-----------

hwspinlock devices provide system-wide hardware locks that are used
by remote processors that have no other way to achieve synchronization.

To achieve that, each physical lock must have a system-wide id number
that is agreed upon, otherwise remote processors can't possibly assume
they're using the same hardware lock.

Usually boards have a single hwspinlock device, which provides several
hwspinlocks, and in this case, they can be trivially numbered 0 to
(num-of-locks - 1).

In case boards have several hwspinlocks devices, a different base id
should be used for each hwspinlock device (they can't all use 0 as
a starting id!).

This platform data structure should be used to provide the base id
for each device (which is trivially 0 when only a single hwspinlock
device exists). It can be shared between different platforms, hence
its location.



.. _`hwspin_trylock_irqsave`:

hwspin_trylock_irqsave
======================

.. c:function:: int hwspin_trylock_irqsave (struct hwspinlock *hwlock, unsigned long *flags)

    try to lock an hwspinlock, disable interrupts

    :param struct hwspinlock \*hwlock:
        an hwspinlock which we want to trylock

    :param unsigned long \*flags:
        a pointer to where the caller's interrupt state will be saved at



.. _`hwspin_trylock_irqsave.description`:

Description
-----------

This function attempts to lock the underlying hwspinlock, and will
immediately fail if the hwspinlock is already locked.

Upon a successful return from this function, preemption and local
interrupts are disabled (previous interrupts state is saved at ``flags``\ ),
so the caller must not sleep, and is advised to release the hwspinlock
as soon as possible.

Returns 0 if we successfully locked the hwspinlock, -EBUSY if
the hwspinlock was already taken, and -EINVAL if ``hwlock`` is invalid.



.. _`hwspin_trylock_irq`:

hwspin_trylock_irq
==================

.. c:function:: int hwspin_trylock_irq (struct hwspinlock *hwlock)

    try to lock an hwspinlock, disable interrupts

    :param struct hwspinlock \*hwlock:
        an hwspinlock which we want to trylock



.. _`hwspin_trylock_irq.description`:

Description
-----------

This function attempts to lock the underlying hwspinlock, and will
immediately fail if the hwspinlock is already locked.

Upon a successful return from this function, preemption and local
interrupts are disabled, so the caller must not sleep, and is advised
to release the hwspinlock as soon as possible.

Returns 0 if we successfully locked the hwspinlock, -EBUSY if
the hwspinlock was already taken, and -EINVAL if ``hwlock`` is invalid.



.. _`hwspin_trylock`:

hwspin_trylock
==============

.. c:function:: int hwspin_trylock (struct hwspinlock *hwlock)

    attempt to lock a specific hwspinlock

    :param struct hwspinlock \*hwlock:
        an hwspinlock which we want to trylock



.. _`hwspin_trylock.description`:

Description
-----------

This function attempts to lock an hwspinlock, and will immediately fail
if the hwspinlock is already taken.

Upon a successful return from this function, preemption is disabled,
so the caller must not sleep, and is advised to release the hwspinlock
as soon as possible. This is required in order to minimize remote cores
polling on the hardware interconnect.

Returns 0 if we successfully locked the hwspinlock, -EBUSY if
the hwspinlock was already taken, and -EINVAL if ``hwlock`` is invalid.



.. _`hwspin_lock_timeout_irqsave`:

hwspin_lock_timeout_irqsave
===========================

.. c:function:: int hwspin_lock_timeout_irqsave (struct hwspinlock *hwlock, unsigned int to, unsigned long *flags)

    lock hwspinlock, with timeout, disable irqs

    :param struct hwspinlock \*hwlock:
        the hwspinlock to be locked

    :param unsigned int to:
        timeout value in msecs

    :param unsigned long \*flags:
        a pointer to where the caller's interrupt state will be saved at



.. _`hwspin_lock_timeout_irqsave.description`:

Description
-----------

This function locks the underlying ``hwlock``\ . If the ``hwlock``
is already taken, the function will busy loop waiting for it to
be released, but give up when ``timeout`` msecs have elapsed.

Upon a successful return from this function, preemption and local interrupts
are disabled (plus previous interrupt state is saved), so the caller must
not sleep, and is advised to release the hwspinlock as soon as possible.

Returns 0 when the ``hwlock`` was successfully taken, and an appropriate
error code otherwise (most notably an -ETIMEDOUT if the ``hwlock`` is still
busy after ``timeout`` msecs). The function will never sleep.



.. _`hwspin_lock_timeout_irq`:

hwspin_lock_timeout_irq
=======================

.. c:function:: int hwspin_lock_timeout_irq (struct hwspinlock *hwlock, unsigned int to)

    lock hwspinlock, with timeout, disable irqs

    :param struct hwspinlock \*hwlock:
        the hwspinlock to be locked

    :param unsigned int to:
        timeout value in msecs



.. _`hwspin_lock_timeout_irq.description`:

Description
-----------

This function locks the underlying ``hwlock``\ . If the ``hwlock``
is already taken, the function will busy loop waiting for it to
be released, but give up when ``timeout`` msecs have elapsed.

Upon a successful return from this function, preemption and local interrupts
are disabled so the caller must not sleep, and is advised to release the
hwspinlock as soon as possible.

Returns 0 when the ``hwlock`` was successfully taken, and an appropriate
error code otherwise (most notably an -ETIMEDOUT if the ``hwlock`` is still
busy after ``timeout`` msecs). The function will never sleep.



.. _`hwspin_lock_timeout`:

hwspin_lock_timeout
===================

.. c:function:: int hwspin_lock_timeout (struct hwspinlock *hwlock, unsigned int to)

    lock an hwspinlock with timeout limit

    :param struct hwspinlock \*hwlock:
        the hwspinlock to be locked

    :param unsigned int to:
        timeout value in msecs



.. _`hwspin_lock_timeout.description`:

Description
-----------

This function locks the underlying ``hwlock``\ . If the ``hwlock``
is already taken, the function will busy loop waiting for it to
be released, but give up when ``timeout`` msecs have elapsed.

Upon a successful return from this function, preemption is disabled
so the caller must not sleep, and is advised to release the hwspinlock
as soon as possible.
This is required in order to minimize remote cores polling on the
hardware interconnect.

Returns 0 when the ``hwlock`` was successfully taken, and an appropriate
error code otherwise (most notably an -ETIMEDOUT if the ``hwlock`` is still
busy after ``timeout`` msecs). The function will never sleep.



.. _`hwspin_unlock_irqrestore`:

hwspin_unlock_irqrestore
========================

.. c:function:: void hwspin_unlock_irqrestore (struct hwspinlock *hwlock, unsigned long *flags)

    unlock hwspinlock, restore irq state

    :param struct hwspinlock \*hwlock:
        it is a bug
        to call unlock on a ``hwlock`` that is already unlocked.

    :param unsigned long \*flags:
        previous caller's interrupt state to restore



.. _`hwspin_unlock_irqrestore.description`:

Description
-----------

This function will unlock a specific hwspinlock, enable preemption and
restore the previous state of the local interrupts. It should be used
to undo, e.g., :c:func:`hwspin_trylock_irqsave`.



.. _`hwspin_unlock_irq`:

hwspin_unlock_irq
=================

.. c:function:: void hwspin_unlock_irq (struct hwspinlock *hwlock)

    unlock hwspinlock, enable interrupts

    :param struct hwspinlock \*hwlock:
        a previously-acquired hwspinlock which we want to unlock



.. _`hwspin_unlock_irq.description`:

Description
-----------

This function will unlock a specific hwspinlock, enable preemption and
enable local interrupts. Should be used to undo :c:func:`hwspin_lock_irq`.

``hwlock`` must be already locked (e.g. by :c:func:`hwspin_trylock_irq`) before



.. _`hwspin_unlock_irq.calling-this-function`:

calling this function
---------------------

it is a bug to call unlock on a ``hwlock`` that is
already unlocked.



.. _`hwspin_unlock`:

hwspin_unlock
=============

.. c:function:: void hwspin_unlock (struct hwspinlock *hwlock)

    unlock hwspinlock

    :param struct hwspinlock \*hwlock:
        a previously-acquired hwspinlock which we want to unlock



.. _`hwspin_unlock.description`:

Description
-----------

This function will unlock a specific hwspinlock and enable preemption
back.

``hwlock`` must be already locked (e.g. by :c:func:`hwspin_trylock`) before calling



.. _`hwspin_unlock.this-function`:

this function
-------------

it is a bug to call unlock on a ``hwlock`` that is already
unlocked.

