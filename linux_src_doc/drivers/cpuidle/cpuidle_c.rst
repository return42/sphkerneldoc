.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/cpuidle.c

.. _`cpuidle_play_dead`:

cpuidle_play_dead
=================

.. c:function:: int cpuidle_play_dead( void)

    cpu off-lining

    :param  void:
        no arguments

.. _`cpuidle_play_dead.description`:

Description
-----------

Returns in case of an error or no driver

.. _`cpuidle_use_deepest_state`:

cpuidle_use_deepest_state
=========================

.. c:function:: void cpuidle_use_deepest_state(bool enable)

    Set/clear governor override flag.

    :param bool enable:
        New value of the flag.

.. _`cpuidle_use_deepest_state.description`:

Description
-----------

Set/unset the current CPU to use the deepest idle state (override governors
going forward if set).

.. _`cpuidle_find_deepest_state`:

cpuidle_find_deepest_state
==========================

.. c:function:: int cpuidle_find_deepest_state(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    Find the deepest available idle state.

    :param struct cpuidle_driver \*drv:
        cpuidle driver for the given CPU.

    :param struct cpuidle_device \*dev:
        cpuidle device for the given CPU.

.. _`cpuidle_enter_freeze`:

cpuidle_enter_freeze
====================

.. c:function:: int cpuidle_enter_freeze(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    Enter an idle state suitable for suspend-to-idle.

    :param struct cpuidle_driver \*drv:
        cpuidle driver for the given CPU.

    :param struct cpuidle_device \*dev:
        cpuidle device for the given CPU.

.. _`cpuidle_enter_freeze.description`:

Description
-----------

If there are states with the ->enter_freeze callback, find the deepest of
them and enter it with frozen tick.

.. _`cpuidle_enter_state`:

cpuidle_enter_state
===================

.. c:function:: int cpuidle_enter_state(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    enter the state and update stats

    :param struct cpuidle_device \*dev:
        cpuidle device for this cpu

    :param struct cpuidle_driver \*drv:
        cpuidle driver for this cpu

    :param int index:
        index into the states table in \ ``drv``\  of the state to enter

.. _`cpuidle_select`:

cpuidle_select
==============

.. c:function:: int cpuidle_select(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    ask the cpuidle framework to choose an idle state

    :param struct cpuidle_driver \*drv:
        the cpuidle driver

    :param struct cpuidle_device \*dev:
        the cpuidle device

.. _`cpuidle_select.description`:

Description
-----------

Returns the index of the idle state.  The return value must not be negative.

.. _`cpuidle_enter`:

cpuidle_enter
=============

.. c:function:: int cpuidle_enter(struct cpuidle_driver *drv, struct cpuidle_device *dev, int index)

    enter into the specified idle state

    :param struct cpuidle_driver \*drv:
        the cpuidle driver tied with the cpu

    :param struct cpuidle_device \*dev:
        the cpuidle device

    :param int index:
        the index in the idle state table

.. _`cpuidle_enter.description`:

Description
-----------

Returns the index in the idle state, < 0 in case of error.
The error code depends on the backend driver

.. _`cpuidle_reflect`:

cpuidle_reflect
===============

.. c:function:: void cpuidle_reflect(struct cpuidle_device *dev, int index)

    tell the underlying governor what was the state we were in

    :param struct cpuidle_device \*dev:
        the cpuidle device

    :param int index:
        the index in the idle state table

.. _`cpuidle_install_idle_handler`:

cpuidle_install_idle_handler
============================

.. c:function:: void cpuidle_install_idle_handler( void)

    installs the cpuidle idle loop handler

    :param  void:
        no arguments

.. _`cpuidle_uninstall_idle_handler`:

cpuidle_uninstall_idle_handler
==============================

.. c:function:: void cpuidle_uninstall_idle_handler( void)

    uninstalls the cpuidle idle loop handler

    :param  void:
        no arguments

.. _`cpuidle_pause_and_lock`:

cpuidle_pause_and_lock
======================

.. c:function:: void cpuidle_pause_and_lock( void)

    temporarily disables CPUIDLE

    :param  void:
        no arguments

.. _`cpuidle_resume_and_unlock`:

cpuidle_resume_and_unlock
=========================

.. c:function:: void cpuidle_resume_and_unlock( void)

    resumes CPUIDLE operation

    :param  void:
        no arguments

.. _`cpuidle_enable_device`:

cpuidle_enable_device
=====================

.. c:function:: int cpuidle_enable_device(struct cpuidle_device *dev)

    enables idle PM for a CPU

    :param struct cpuidle_device \*dev:
        the CPU

.. _`cpuidle_enable_device.description`:

Description
-----------

This function must be called between cpuidle_pause_and_lock and
cpuidle_resume_and_unlock when used externally.

.. _`cpuidle_disable_device`:

cpuidle_disable_device
======================

.. c:function:: void cpuidle_disable_device(struct cpuidle_device *dev)

    disables idle PM for a CPU

    :param struct cpuidle_device \*dev:
        the CPU

.. _`cpuidle_disable_device.description`:

Description
-----------

This function must be called between cpuidle_pause_and_lock and
cpuidle_resume_and_unlock when used externally.

.. _`__cpuidle_register_device`:

__cpuidle_register_device
=========================

.. c:function:: int __cpuidle_register_device(struct cpuidle_device *dev)

    internal register function called before register and enable routines

    :param struct cpuidle_device \*dev:
        the cpu

.. _`__cpuidle_register_device.description`:

Description
-----------

cpuidle_lock mutex must be held before this is called

.. _`cpuidle_register_device`:

cpuidle_register_device
=======================

.. c:function:: int cpuidle_register_device(struct cpuidle_device *dev)

    registers a CPU's idle PM feature

    :param struct cpuidle_device \*dev:
        the cpu

.. _`cpuidle_unregister_device`:

cpuidle_unregister_device
=========================

.. c:function:: void cpuidle_unregister_device(struct cpuidle_device *dev)

    unregisters a CPU's idle PM feature

    :param struct cpuidle_device \*dev:
        the cpu

.. _`cpuidle_unregister`:

cpuidle_unregister
==================

.. c:function:: void cpuidle_unregister(struct cpuidle_driver *drv)

    unregister a driver and the devices. This function can be used only if the driver has been previously registered through the cpuidle_register function.

    :param struct cpuidle_driver \*drv:
        a valid pointer to a struct cpuidle_driver

.. _`cpuidle_register`:

cpuidle_register
================

.. c:function:: int cpuidle_register(struct cpuidle_driver *drv, const struct cpumask *const coupled_cpus)

    registers the driver and the cpu devices with the coupled_cpus passed as parameter. This function is used for all common initialization pattern there are in the arch specific drivers. The devices is globally defined in this file.

    :param struct cpuidle_driver \*drv:
        a valid pointer to a struct cpuidle_driver

    :param const struct cpumask \*const coupled_cpus:
        a cpumask for the coupled states

.. _`cpuidle_register.description`:

Description
-----------

Returns 0 on success, < 0 otherwise

.. _`cpuidle_init`:

cpuidle_init
============

.. c:function:: int cpuidle_init( void)

    core initializer

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

