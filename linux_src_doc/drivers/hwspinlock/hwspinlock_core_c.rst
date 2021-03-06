.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwspinlock/hwspinlock_core.c

.. _`__hwspin_trylock`:

\__hwspin_trylock
=================

.. c:function:: int __hwspin_trylock(struct hwspinlock *hwlock, int mode, unsigned long *flags)

    attempt to lock a specific hwspinlock

    :param hwlock:
        an hwspinlock which we want to trylock
    :type hwlock: struct hwspinlock \*

    :param mode:
        controls whether local interrupts are disabled or not
    :type mode: int

    :param flags:
        a pointer where the caller's interrupt state will be saved at (if
        requested)
    :type flags: unsigned long \*

.. _`__hwspin_trylock.description`:

Description
-----------

This function attempts to lock an hwspinlock, and will immediately
fail if the hwspinlock is already taken.

.. _`__hwspin_trylock.caution`:

Caution
-------

If the mode is HWLOCK_RAW, that means user must protect the routine
of getting hardware lock with mutex or spinlock. Since in some scenarios,
user need some time-consuming or sleepable operations under the hardware
lock, they need one sleepable lock (like mutex) to protect the operations.

If the mode is not HWLOCK_RAW, upon a successful return from this function,
preemption (and possibly interrupts) is disabled, so the caller must not
sleep, and is advised to release the hwspinlock as soon as possible. This is
required in order to minimize remote cores polling on the hardware
interconnect.

The user decides whether local interrupts are disabled or not, and if yes,
whether he wants their previous state to be saved. It is up to the user
to choose the appropriate \ ``mode``\  of operation, exactly the same way users
should decide between spin_trylock, spin_trylock_irq and
spin_trylock_irqsave.

Returns 0 if we successfully locked the hwspinlock or -EBUSY if
the hwspinlock was already taken.
This function will never sleep.

.. _`__hwspin_lock_timeout`:

\__hwspin_lock_timeout
======================

.. c:function:: int __hwspin_lock_timeout(struct hwspinlock *hwlock, unsigned int to, int mode, unsigned long *flags)

    lock an hwspinlock with timeout limit

    :param hwlock:
        the hwspinlock to be locked
    :type hwlock: struct hwspinlock \*

    :param to:
        *undescribed*
    :type to: unsigned int

    :param mode:
        mode which controls whether local interrupts are disabled or not
    :type mode: int

    :param flags:
        a pointer to where the caller's interrupt state will be saved at (if
        requested)
    :type flags: unsigned long \*

.. _`__hwspin_lock_timeout.description`:

Description
-----------

This function locks the given \ ``hwlock``\ . If the \ ``hwlock``\ 
is already taken, the function will busy loop waiting for it to
be released, but give up after \ ``timeout``\  msecs have elapsed.

.. _`__hwspin_lock_timeout.caution`:

Caution
-------

If the mode is HWLOCK_RAW, that means user must protect the routine
of getting hardware lock with mutex or spinlock. Since in some scenarios,
user need some time-consuming or sleepable operations under the hardware
lock, they need one sleepable lock (like mutex) to protect the operations.

If the mode is not HWLOCK_RAW, upon a successful return from this function,
preemption is disabled (and possibly local interrupts, too), so the caller
must not sleep, and is advised to release the hwspinlock as soon as possible.
This is required in order to minimize remote cores polling on the
hardware interconnect.

The user decides whether local interrupts are disabled or not, and if yes,
whether he wants their previous state to be saved. It is up to the user
to choose the appropriate \ ``mode``\  of operation, exactly the same way users
should decide between spin_lock, spin_lock_irq and spin_lock_irqsave.

Returns 0 when the \ ``hwlock``\  was successfully taken, and an appropriate
error code otherwise (most notably -ETIMEDOUT if the \ ``hwlock``\  is still
busy after \ ``timeout``\  msecs). The function will never sleep.

.. _`__hwspin_unlock`:

\__hwspin_unlock
================

.. c:function:: void __hwspin_unlock(struct hwspinlock *hwlock, int mode, unsigned long *flags)

    unlock a specific hwspinlock

    :param hwlock:
        it is a bug
        to call unlock on a \ ``hwlock``\  that is already unlocked.
    :type hwlock: struct hwspinlock \*

    :param mode:
        controls whether local interrupts needs to be restored or not
    :type mode: int

    :param flags:
        previous caller's interrupt state to restore (if requested)
    :type flags: unsigned long \*

.. _`__hwspin_unlock.description`:

Description
-----------

This function will unlock a specific hwspinlock, enable preemption and
(possibly) enable interrupts or restore their previous state.

The user decides whether local interrupts should be enabled or not, and
if yes, whether he wants their previous state to be restored. It is up
to the user to choose the appropriate \ ``mode``\  of operation, exactly the
same way users decide between spin_unlock, spin_unlock_irq and
spin_unlock_irqrestore.

The function will never sleep.

.. _`of_hwspin_lock_simple_xlate`:

of_hwspin_lock_simple_xlate
===========================

.. c:function:: int of_hwspin_lock_simple_xlate(const struct of_phandle_args *hwlock_spec)

    translate hwlock_spec to return a lock id

    :param hwlock_spec:
        hwlock specifier as found in the device tree
    :type hwlock_spec: const struct of_phandle_args \*

.. _`of_hwspin_lock_simple_xlate.description`:

Description
-----------

This is a simple translation function, suitable for hwspinlock platform
drivers that only has a lock specifier length of 1.

Returns a relative index of the lock within a specified bank on success,
or -EINVAL on invalid specifier cell count.

.. _`of_hwspin_lock_get_id`:

of_hwspin_lock_get_id
=====================

.. c:function:: int of_hwspin_lock_get_id(struct device_node *np, int index)

    get lock id for an OF phandle-based specific lock

    :param np:
        device node from which to request the specific hwlock
    :type np: struct device_node \*

    :param index:
        index of the hwlock in the list of values
    :type index: int

.. _`of_hwspin_lock_get_id.description`:

Description
-----------

This function provides a means for DT users of the hwspinlock module to
get the global lock id of a specific hwspinlock using the phandle of the
hwspinlock device, so that it can be requested using the normal
\ :c:func:`hwspin_lock_request_specific`\  API.

Returns the global lock id number on success, -EPROBE_DEFER if the hwspinlock
device is not yet registered, -EINVAL on invalid args specifier value or an
appropriate error as returned from the OF parsing of the DT client node.

.. _`of_hwspin_lock_get_id_byname`:

of_hwspin_lock_get_id_byname
============================

.. c:function:: int of_hwspin_lock_get_id_byname(struct device_node *np, const char *name)

    get lock id for an specified hwlock name

    :param np:
        device node from which to request the specific hwlock
    :type np: struct device_node \*

    :param name:
        hwlock name
    :type name: const char \*

.. _`of_hwspin_lock_get_id_byname.description`:

Description
-----------

This function provides a means for DT users of the hwspinlock module to
get the global lock id of a specific hwspinlock using the specified name of
the hwspinlock device, so that it can be requested using the normal
\ :c:func:`hwspin_lock_request_specific`\  API.

Returns the global lock id number on success, -EPROBE_DEFER if the hwspinlock
device is not yet registered, -EINVAL on invalid args specifier value or an
appropriate error as returned from the OF parsing of the DT client node.

.. _`hwspin_lock_register`:

hwspin_lock_register
====================

.. c:function:: int hwspin_lock_register(struct hwspinlock_device *bank, struct device *dev, const struct hwspinlock_ops *ops, int base_id, int num_locks)

    register a new hw spinlock device

    :param bank:
        the hwspinlock device, which usually provides numerous hw locks
    :type bank: struct hwspinlock_device \*

    :param dev:
        the backing device
    :type dev: struct device \*

    :param ops:
        hwspinlock handlers for this device
    :type ops: const struct hwspinlock_ops \*

    :param base_id:
        id of the first hardware spinlock in this bank
    :type base_id: int

    :param num_locks:
        number of hwspinlocks provided by this device
    :type num_locks: int

.. _`hwspin_lock_register.description`:

Description
-----------

This function should be called from the underlying platform-specific
implementation, to register a new hwspinlock device instance.

Should be called from a process context (might sleep)

Returns 0 on success, or an appropriate error code on failure

.. _`hwspin_lock_unregister`:

hwspin_lock_unregister
======================

.. c:function:: int hwspin_lock_unregister(struct hwspinlock_device *bank)

    unregister an hw spinlock device

    :param bank:
        the hwspinlock device, which usually provides numerous hw locks
    :type bank: struct hwspinlock_device \*

.. _`hwspin_lock_unregister.description`:

Description
-----------

This function should be called from the underlying platform-specific
implementation, to unregister an existing (and unused) hwspinlock.

Should be called from a process context (might sleep)

Returns 0 on success, or an appropriate error code on failure

.. _`devm_hwspin_lock_unregister`:

devm_hwspin_lock_unregister
===========================

.. c:function:: int devm_hwspin_lock_unregister(struct device *dev, struct hwspinlock_device *bank)

    unregister an hw spinlock device for a managed device

    :param dev:
        the backing device
    :type dev: struct device \*

    :param bank:
        the hwspinlock device, which usually provides numerous hw locks
    :type bank: struct hwspinlock_device \*

.. _`devm_hwspin_lock_unregister.description`:

Description
-----------

This function should be called from the underlying platform-specific
implementation, to unregister an existing (and unused) hwspinlock.

Should be called from a process context (might sleep)

Returns 0 on success, or an appropriate error code on failure

.. _`devm_hwspin_lock_register`:

devm_hwspin_lock_register
=========================

.. c:function:: int devm_hwspin_lock_register(struct device *dev, struct hwspinlock_device *bank, const struct hwspinlock_ops *ops, int base_id, int num_locks)

    register a new hw spinlock device for a managed device

    :param dev:
        the backing device
    :type dev: struct device \*

    :param bank:
        the hwspinlock device, which usually provides numerous hw locks
    :type bank: struct hwspinlock_device \*

    :param ops:
        hwspinlock handlers for this device
    :type ops: const struct hwspinlock_ops \*

    :param base_id:
        id of the first hardware spinlock in this bank
    :type base_id: int

    :param num_locks:
        number of hwspinlocks provided by this device
    :type num_locks: int

.. _`devm_hwspin_lock_register.description`:

Description
-----------

This function should be called from the underlying platform-specific
implementation, to register a new hwspinlock device instance.

Should be called from a process context (might sleep)

Returns 0 on success, or an appropriate error code on failure

.. _`__hwspin_lock_request`:

\__hwspin_lock_request
======================

.. c:function:: int __hwspin_lock_request(struct hwspinlock *hwlock)

    tag an hwspinlock as used and power it up

    :param hwlock:
        *undescribed*
    :type hwlock: struct hwspinlock \*

.. _`__hwspin_lock_request.description`:

Description
-----------

This is an internal function that prepares an hwspinlock instance
before it is given to the user. The function assumes that
hwspinlock_tree_lock is taken.

Returns 0 or positive to indicate success, and a negative value to
indicate an error (with the appropriate error code)

.. _`hwspin_lock_get_id`:

hwspin_lock_get_id
==================

.. c:function:: int hwspin_lock_get_id(struct hwspinlock *hwlock)

    retrieve id number of a given hwspinlock

    :param hwlock:
        a valid hwspinlock instance
    :type hwlock: struct hwspinlock \*

.. _`hwspin_lock_get_id.description`:

Description
-----------

Returns the id number of a given \ ``hwlock``\ , or -EINVAL if \ ``hwlock``\  is invalid.

.. _`hwspin_lock_request`:

hwspin_lock_request
===================

.. c:function:: struct hwspinlock *hwspin_lock_request( void)

    request an hwspinlock

    :param void:
        no arguments
    :type void: 

.. _`hwspin_lock_request.description`:

Description
-----------

This function should be called by users of the hwspinlock device,
in order to dynamically assign them an unused hwspinlock.
Usually the user of this lock will then have to communicate the lock's id
to the remote core before it can be used for synchronization (to get the
id of a given hwlock, use \ :c:func:`hwspin_lock_get_id`\ ).

Should be called from a process context (might sleep)

Returns the address of the assigned hwspinlock, or NULL on error

.. _`hwspin_lock_request_specific`:

hwspin_lock_request_specific
============================

.. c:function:: struct hwspinlock *hwspin_lock_request_specific(unsigned int id)

    request for a specific hwspinlock

    :param id:
        index of the specific hwspinlock that is requested
    :type id: unsigned int

.. _`hwspin_lock_request_specific.description`:

Description
-----------

This function should be called by users of the hwspinlock module,
in order to assign them a specific hwspinlock.
Usually early board code will be calling this function in order to
reserve specific hwspinlock ids for predefined purposes.

Should be called from a process context (might sleep)

Returns the address of the assigned hwspinlock, or NULL on error

.. _`hwspin_lock_free`:

hwspin_lock_free
================

.. c:function:: int hwspin_lock_free(struct hwspinlock *hwlock)

    free a specific hwspinlock

    :param hwlock:
        the specific hwspinlock to free
    :type hwlock: struct hwspinlock \*

.. _`hwspin_lock_free.description`:

Description
-----------

This function mark \ ``hwlock``\  as free again.
Should only be called with an \ ``hwlock``\  that was retrieved from
an earlier call to hwspin_lock_request{_specific}.

Should be called from a process context (might sleep)

Returns 0 on success, or an appropriate error code on failure

.. _`devm_hwspin_lock_free`:

devm_hwspin_lock_free
=====================

.. c:function:: int devm_hwspin_lock_free(struct device *dev, struct hwspinlock *hwlock)

    free a specific hwspinlock for a managed device

    :param dev:
        the device to free the specific hwspinlock
    :type dev: struct device \*

    :param hwlock:
        the specific hwspinlock to free
    :type hwlock: struct hwspinlock \*

.. _`devm_hwspin_lock_free.description`:

Description
-----------

This function mark \ ``hwlock``\  as free again.
Should only be called with an \ ``hwlock``\  that was retrieved from
an earlier call to hwspin_lock_request{_specific}.

Should be called from a process context (might sleep)

Returns 0 on success, or an appropriate error code on failure

.. _`devm_hwspin_lock_request`:

devm_hwspin_lock_request
========================

.. c:function:: struct hwspinlock *devm_hwspin_lock_request(struct device *dev)

    request an hwspinlock for a managed device

    :param dev:
        the device to request an hwspinlock
    :type dev: struct device \*

.. _`devm_hwspin_lock_request.description`:

Description
-----------

This function should be called by users of the hwspinlock device,
in order to dynamically assign them an unused hwspinlock.
Usually the user of this lock will then have to communicate the lock's id
to the remote core before it can be used for synchronization (to get the
id of a given hwlock, use \ :c:func:`hwspin_lock_get_id`\ ).

Should be called from a process context (might sleep)

Returns the address of the assigned hwspinlock, or NULL on error

.. _`devm_hwspin_lock_request_specific`:

devm_hwspin_lock_request_specific
=================================

.. c:function:: struct hwspinlock *devm_hwspin_lock_request_specific(struct device *dev, unsigned int id)

    request for a specific hwspinlock for a managed device

    :param dev:
        the device to request the specific hwspinlock
    :type dev: struct device \*

    :param id:
        index of the specific hwspinlock that is requested
    :type id: unsigned int

.. _`devm_hwspin_lock_request_specific.description`:

Description
-----------

This function should be called by users of the hwspinlock module,
in order to assign them a specific hwspinlock.
Usually early board code will be calling this function in order to
reserve specific hwspinlock ids for predefined purposes.

Should be called from a process context (might sleep)

Returns the address of the assigned hwspinlock, or NULL on error

.. This file was automatic generated / don't edit.

