.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/smpboot.c

.. _`idle_init`:

idle_init
=========

.. c:function:: void idle_init(unsigned int cpu)

    Initialize the idle thread for a cpu

    :param cpu:
        The cpu for which the idle thread should be initialized
    :type cpu: unsigned int

.. _`idle_init.description`:

Description
-----------

Creates the thread if it does not exist.

.. _`idle_threads_init`:

idle_threads_init
=================

.. c:function:: void idle_threads_init( void)

    Initialize idle threads for all cpus

    :param void:
        no arguments
    :type void: 

.. _`smpboot_thread_fn`:

smpboot_thread_fn
=================

.. c:function:: int smpboot_thread_fn(void *data)

    percpu hotplug thread loop function

    :param data:
        thread data pointer
    :type data: void \*

.. _`smpboot_thread_fn.description`:

Description
-----------

Checks for thread stop and park conditions. Calls the necessary
setup, cleanup, park and unpark functions for the registered
thread.

Returns 1 when the thread should exit, 0 otherwise.

.. _`smpboot_register_percpu_thread`:

smpboot_register_percpu_thread
==============================

.. c:function:: int smpboot_register_percpu_thread(struct smp_hotplug_thread *plug_thread)

    Register a per_cpu thread related to hotplug

    :param plug_thread:
        Hotplug thread descriptor
    :type plug_thread: struct smp_hotplug_thread \*

.. _`smpboot_register_percpu_thread.description`:

Description
-----------

Creates and starts the threads on all online cpus.

.. _`smpboot_unregister_percpu_thread`:

smpboot_unregister_percpu_thread
================================

.. c:function:: void smpboot_unregister_percpu_thread(struct smp_hotplug_thread *plug_thread)

    Unregister a per_cpu thread related to hotplug

    :param plug_thread:
        Hotplug thread descriptor
    :type plug_thread: struct smp_hotplug_thread \*

.. _`smpboot_unregister_percpu_thread.description`:

Description
-----------

Stops all threads on all possible cpus.

.. This file was automatic generated / don't edit.

