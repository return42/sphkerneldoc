.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/mcpm.h

.. _`mcpm_is_available`:

mcpm_is_available
=================

.. c:function:: bool mcpm_is_available( void)

    returns whether MCPM is initialized and available

    :param  void:
        no arguments

.. _`mcpm_is_available.description`:

Description
-----------

This returns true or false accordingly.

.. _`mcpm_cpu_power_up`:

mcpm_cpu_power_up
=================

.. c:function:: int mcpm_cpu_power_up(unsigned int cpu, unsigned int cluster)

    make given CPU in given cluster runable

    :param unsigned int cpu:
        CPU number within given cluster

    :param unsigned int cluster:
        cluster number for the CPU

.. _`mcpm_cpu_power_up.description`:

Description
-----------

The identified CPU is brought out of reset.  If the cluster was powered
down then it is brought up as well, taking care not to let the other CPUs
in the cluster run, and ensuring appropriate cluster setup.

Caller must ensure the appropriate entry vector is initialized with
\ :c:func:`mcpm_set_entry_vector`\  prior to calling this.

This must be called in a sleepable context.  However, the implementation
is strongly encouraged to return early and let the operation happen
asynchronously, especially when significant delays are expected.

If the operation cannot be performed then an error code is returned.

.. _`mcpm_cpu_power_down`:

mcpm_cpu_power_down
===================

.. c:function:: void mcpm_cpu_power_down( void)

    power the calling CPU down

    :param  void:
        no arguments

.. _`mcpm_cpu_power_down.description`:

Description
-----------

The calling CPU is powered down.

If this CPU is found to be the "last man standing" in the cluster
then the cluster is prepared for power-down too.

This must be called with interrupts disabled.

On success this does not return.  Re-entry in the kernel is expected
via mcpm_entry_point.

This will return if \ :c:func:`mcpm_platform_register`\  has not been called
previously in which case the caller should take appropriate action.

On success, the CPU is not guaranteed to be truly halted until
\ :c:func:`mcpm_wait_for_cpu_powerdown`\  subsequently returns non-zero for the
specified cpu.  Until then, other CPUs should make sure they do not
trash memory the target CPU might be executing/accessing.

.. _`mcpm_wait_for_cpu_powerdown`:

mcpm_wait_for_cpu_powerdown
===========================

.. c:function:: int mcpm_wait_for_cpu_powerdown(unsigned int cpu, unsigned int cluster)

    wait for a specified CPU to halt, and make sure it is powered off

    :param unsigned int cpu:
        CPU number within given cluster

    :param unsigned int cluster:
        cluster number for the CPU

.. _`mcpm_wait_for_cpu_powerdown.description`:

Description
-----------

Call this function to ensure that a pending powerdown has taken
effect and the CPU is safely parked before performing non-mcpm
operations that may affect the CPU (such as kexec trashing the
kernel text).

It is \*not\* necessary to call this function if you only need to
serialise a pending powerdown with \ :c:func:`mcpm_cpu_power_up`\  or a wakeup
event.

Do not call this function unless the specified CPU has already
called \ :c:func:`mcpm_cpu_power_down`\  or has committed to doing so.

.. _`mcpm_cpu_suspend`:

mcpm_cpu_suspend
================

.. c:function:: void mcpm_cpu_suspend( void)

    bring the calling CPU in a suspended state

    :param  void:
        no arguments

.. _`mcpm_cpu_suspend.description`:

Description
-----------

The calling CPU is suspended.  This is similar to \ :c:func:`mcpm_cpu_power_down`\ 
except for possible extra platform specific configuration steps to allow
an asynchronous wake-up e.g. with a pending interrupt.

If this CPU is found to be the "last man standing" in the cluster
then the cluster may be prepared for power-down too.

This must be called with interrupts disabled.

On success this does not return.  Re-entry in the kernel is expected
via mcpm_entry_point.

This will return if \ :c:func:`mcpm_platform_register`\  has not been called
previously in which case the caller should take appropriate action.

.. _`mcpm_cpu_powered_up`:

mcpm_cpu_powered_up
===================

.. c:function:: int mcpm_cpu_powered_up( void)

    housekeeping workafter a CPU has been powered up

    :param  void:
        no arguments

.. _`mcpm_cpu_powered_up.description`:

Description
-----------

This lets the platform specific backend code perform needed housekeeping
work.  This must be called by the newly activated CPU as soon as it is
fully operational in kernel space, before it enables interrupts.

If the operation cannot be performed then an error code is returned.

.. _`mcpm_platform_register`:

mcpm_platform_register
======================

.. c:function:: int mcpm_platform_register(const struct mcpm_platform_ops *ops)

    register platform specific power methods

    :param const struct mcpm_platform_ops \*ops:
        mcpm_platform_ops structure to register

.. _`mcpm_platform_register.description`:

Description
-----------

An error is returned if the registration has been done previously.

.. _`mcpm_sync_init`:

mcpm_sync_init
==============

.. c:function:: int mcpm_sync_init(void (*) power_up_setup (unsigned int affinity_level)

    Initialize the cluster synchronization support

    :param (void (\*) power_up_setup (unsigned int affinity_level):
        platform specific function invoked during very
        early CPU/cluster bringup stage.

.. _`mcpm_sync_init.description`:

Description
-----------

This prepares memory used by vlocks and the MCPM state machine used
across CPUs that may have their caches active or inactive. Must be
called only after a successful call to \ :c:func:`mcpm_platform_register`\ .

The power_up_setup argument is a pointer to assembly code called when
the MMU and caches are still disabled during boot  and no stack space is
available. The affinity level passed to that code corresponds to the
resource that needs to be initialized (e.g. 1 for cluster level, 0 for
CPU level).  Proper exclusion mechanisms are already activated at that
point.

.. _`mcpm_loopback`:

mcpm_loopback
=============

.. c:function:: int mcpm_loopback(void (*) cache_disable (void)

    make a run through the MCPM low-level code

    :param (void (\*) cache_disable (void):
        pointer to function performing cache disabling

.. _`mcpm_loopback.description`:

Description
-----------

This exercises the MCPM machinery by soft resetting the CPU and branching
to the MCPM low-level entry code before returning to the caller.
The \ ``cache_disable``\  function must do the necessary cache disabling to
let the regular kernel init code turn it back on as if the CPU was
hotplugged in. The MCPM state machine is set as if the cluster was
initialized meaning the power_up_setup callback passed to \ :c:func:`mcpm_sync_init`\ 
will be invoked for all affinity levels. This may be useful to initialize
some resources such as enabling the CCI that requires the cache to be off, or simply for testing purposes.

.. This file was automatic generated / don't edit.

