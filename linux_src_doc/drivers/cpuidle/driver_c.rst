.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/driver.c

.. _`__cpuidle_get_cpu_driver`:

__cpuidle_get_cpu_driver
========================

.. c:function:: struct cpuidle_driver *__cpuidle_get_cpu_driver(int cpu)

    return the cpuidle driver tied to a CPU.

    :param int cpu:
        the CPU handled by the driver

.. _`__cpuidle_get_cpu_driver.description`:

Description
-----------

Returns a pointer to struct cpuidle_driver or NULL if no driver has been
registered for \ ``cpu``\ .

.. _`__cpuidle_unset_driver`:

__cpuidle_unset_driver
======================

.. c:function:: void __cpuidle_unset_driver(struct cpuidle_driver *drv)

    unset per CPU driver variables.

    :param struct cpuidle_driver \*drv:
        a valid pointer to a struct cpuidle_driver

.. _`__cpuidle_unset_driver.description`:

Description
-----------

For each CPU in the driver's CPU mask, unset the registered driver per CPU
variable. If \ ``drv``\  is different from the registered driver, the corresponding
variable is not cleared.

.. _`__cpuidle_set_driver`:

__cpuidle_set_driver
====================

.. c:function:: int __cpuidle_set_driver(struct cpuidle_driver *drv)

    set per CPU driver variables for the given driver.

    :param struct cpuidle_driver \*drv:
        a valid pointer to a struct cpuidle_driver

.. _`__cpuidle_set_driver.description`:

Description
-----------

For each CPU in the driver's cpumask, unset the registered driver per CPU
to \ ``drv``\ .

Returns 0 on success, -EBUSY if the CPUs have driver(s) already.

.. _`__cpuidle_get_cpu_driver`:

__cpuidle_get_cpu_driver
========================

.. c:function:: struct cpuidle_driver *__cpuidle_get_cpu_driver(int cpu)

    return the global cpuidle driver pointer.

    :param int cpu:
        ignored without the multiple driver support

.. _`__cpuidle_get_cpu_driver.description`:

Description
-----------

Return a pointer to a struct cpuidle_driver object or NULL if no driver was
previously registered.

.. _`__cpuidle_set_driver`:

__cpuidle_set_driver
====================

.. c:function:: int __cpuidle_set_driver(struct cpuidle_driver *drv)

    assign the global cpuidle driver variable.

    :param struct cpuidle_driver \*drv:
        pointer to a struct cpuidle_driver object

.. _`__cpuidle_set_driver.description`:

Description
-----------

Returns 0 on success, -EBUSY if the driver is already registered.

.. _`__cpuidle_unset_driver`:

__cpuidle_unset_driver
======================

.. c:function:: void __cpuidle_unset_driver(struct cpuidle_driver *drv)

    unset the global cpuidle driver variable.

    :param struct cpuidle_driver \*drv:
        a pointer to a struct cpuidle_driver

.. _`__cpuidle_unset_driver.description`:

Description
-----------

Reset the global cpuidle variable to NULL.  If \ ``drv``\  does not match the
registered driver, do nothing.

.. _`cpuidle_setup_broadcast_timer`:

cpuidle_setup_broadcast_timer
=============================

.. c:function:: void cpuidle_setup_broadcast_timer(void *arg)

    enable/disable the broadcast timer on a cpu

    :param void \*arg:
        a void pointer used to match the SMP cross call API

.. _`cpuidle_setup_broadcast_timer.description`:

Description
-----------

If \ ``arg``\  is NULL broadcast is disabled otherwise enabled

This function is executed per CPU by an SMP cross call.  It's not
supposed to be called directly.

.. _`__cpuidle_driver_init`:

__cpuidle_driver_init
=====================

.. c:function:: void __cpuidle_driver_init(struct cpuidle_driver *drv)

    initialize the driver's internal data

    :param struct cpuidle_driver \*drv:
        a valid pointer to a struct cpuidle_driver

.. _`__cpuidle_register_driver`:

__cpuidle_register_driver
=========================

.. c:function:: int __cpuidle_register_driver(struct cpuidle_driver *drv)

    register the driver

    :param struct cpuidle_driver \*drv:
        a valid pointer to a struct cpuidle_driver

.. _`__cpuidle_register_driver.description`:

Description
-----------

Do some sanity checks, initialize the driver, assign the driver to the
global cpuidle driver variable(s) and set up the broadcast timer if the
cpuidle driver has some states that shut down the local timer.

Returns 0 on success, a negative error code otherwise:
\* -EINVAL if the driver pointer is NULL or no idle states are available
\* -ENODEV if the cpuidle framework is disabled
\* -EBUSY if the driver is already assigned to the global variable(s)

.. _`__cpuidle_unregister_driver`:

__cpuidle_unregister_driver
===========================

.. c:function:: void __cpuidle_unregister_driver(struct cpuidle_driver *drv)

    unregister the driver

    :param struct cpuidle_driver \*drv:
        a valid pointer to a struct cpuidle_driver

.. _`__cpuidle_unregister_driver.description`:

Description
-----------

Check if the driver is no longer in use, reset the global cpuidle driver
variable(s) and disable the timer broadcast notification mechanism if it was
in use.

.. _`cpuidle_register_driver`:

cpuidle_register_driver
=======================

.. c:function:: int cpuidle_register_driver(struct cpuidle_driver *drv)

    registers a driver

    :param struct cpuidle_driver \*drv:
        a pointer to a valid struct cpuidle_driver

.. _`cpuidle_register_driver.description`:

Description
-----------

Register the driver under a lock to prevent concurrent attempts to
[un]register the driver from occuring at the same time.

Returns 0 on success, a negative error code (returned by
\__cpuidle_register_driver()) otherwise.

.. _`cpuidle_unregister_driver`:

cpuidle_unregister_driver
=========================

.. c:function:: void cpuidle_unregister_driver(struct cpuidle_driver *drv)

    unregisters a driver

    :param struct cpuidle_driver \*drv:
        a pointer to a valid struct cpuidle_driver

.. _`cpuidle_unregister_driver.description`:

Description
-----------

Unregisters the cpuidle driver under a lock to prevent concurrent attempts
to [un]register the driver from occuring at the same time.  \ ``drv``\  has to
match the currently registered driver.

.. _`cpuidle_get_driver`:

cpuidle_get_driver
==================

.. c:function:: struct cpuidle_driver *cpuidle_get_driver( void)

    return the driver tied to the current CPU.

    :param  void:
        no arguments

.. _`cpuidle_get_driver.description`:

Description
-----------

Returns a struct cpuidle_driver pointer, or NULL if no driver is registered.

.. _`cpuidle_get_cpu_driver`:

cpuidle_get_cpu_driver
======================

.. c:function:: struct cpuidle_driver *cpuidle_get_cpu_driver(struct cpuidle_device *dev)

    return the driver registered for a CPU.

    :param struct cpuidle_device \*dev:
        a valid pointer to a struct cpuidle_device

.. _`cpuidle_get_cpu_driver.description`:

Description
-----------

Returns a struct cpuidle_driver pointer, or NULL if no driver is registered
for the CPU associated with \ ``dev``\ .

.. _`cpuidle_driver_ref`:

cpuidle_driver_ref
==================

.. c:function:: struct cpuidle_driver *cpuidle_driver_ref( void)

    get a reference to the driver.

    :param  void:
        no arguments

.. _`cpuidle_driver_ref.description`:

Description
-----------

Increment the reference counter of the cpuidle driver associated with
the current CPU.

Returns a pointer to the driver, or NULL if the current CPU has no driver.

.. _`cpuidle_driver_unref`:

cpuidle_driver_unref
====================

.. c:function:: void cpuidle_driver_unref( void)

    puts down the refcount for the driver

    :param  void:
        no arguments

.. _`cpuidle_driver_unref.description`:

Description
-----------

Decrement the reference counter of the cpuidle driver associated with
the current CPU.

.. This file was automatic generated / don't edit.

