.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/smpboot.c

.. _`idle_init`:

idle_init
=========

.. c:function:: void idle_init(unsigned int cpu)

    Initialize the idle thread for a cpu

    :param unsigned int cpu:
        The cpu for which the idle thread should be initialized

.. _`idle_init.description`:

Description
-----------

Creates the thread if it does not exist.

.. _`idle_threads_init`:

idle_threads_init
=================

.. c:function:: void idle_threads_init( void)

    Initialize idle threads for all cpus

    :param  void:
        no arguments

.. _`smpboot_thread_fn`:

smpboot_thread_fn
=================

.. c:function:: int smpboot_thread_fn(void *data)

    percpu hotplug thread loop function

    :param void \*data:
        thread data pointer

.. _`smpboot_thread_fn.description`:

Description
-----------

Checks for thread stop and park conditions. Calls the necessary
setup, cleanup, park and unpark functions for the registered
thread.

Returns 1 when the thread should exit, 0 otherwise.

.. _`smpboot_register_percpu_thread_cpumask`:

smpboot_register_percpu_thread_cpumask
======================================

.. c:function:: int smpboot_register_percpu_thread_cpumask(struct smp_hotplug_thread *plug_thread, const struct cpumask *cpumask)

    Register a per_cpu thread related to hotplug

    :param struct smp_hotplug_thread \*plug_thread:
        Hotplug thread descriptor

    :param const struct cpumask \*cpumask:
        The cpumask where threads run

.. _`smpboot_register_percpu_thread_cpumask.description`:

Description
-----------

Creates and starts the threads on all online cpus.

.. _`smpboot_unregister_percpu_thread`:

smpboot_unregister_percpu_thread
================================

.. c:function:: void smpboot_unregister_percpu_thread(struct smp_hotplug_thread *plug_thread)

    Unregister a per_cpu thread related to hotplug

    :param struct smp_hotplug_thread \*plug_thread:
        Hotplug thread descriptor

.. _`smpboot_unregister_percpu_thread.description`:

Description
-----------

Stops all threads on all possible cpus.

.. _`smpboot_update_cpumask_percpu_thread`:

smpboot_update_cpumask_percpu_thread
====================================

.. c:function:: void smpboot_update_cpumask_percpu_thread(struct smp_hotplug_thread *plug_thread, const struct cpumask *new)

    Adjust which per_cpu hotplug threads stay parked

    :param struct smp_hotplug_thread \*plug_thread:
        Hotplug thread descriptor

    :param const struct cpumask \*new:
        Revised mask to use

.. _`smpboot_update_cpumask_percpu_thread.description`:

Description
-----------

The cpumask field in the smp_hotplug_thread must not be updated directly
by the client, but only by calling this function.
This function can only be called on a registered smp_hotplug_thread.

.. This file was automatic generated / don't edit.

