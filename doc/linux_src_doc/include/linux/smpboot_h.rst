.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/smpboot.h

.. _`smp_hotplug_thread`:

struct smp_hotplug_thread
=========================

.. c:type:: struct smp_hotplug_thread

    CPU hotplug related thread descriptor

.. _`smp_hotplug_thread.definition`:

Definition
----------

.. code-block:: c

    struct smp_hotplug_thread {
        struct task_struct __percpu **store;
        struct list_head list;
        int (*thread_should_run)(unsigned int cpu);
        void (*thread_fn)(unsigned int cpu);
        void (*create)(unsigned int cpu);
        void (*setup)(unsigned int cpu);
        void (*cleanup)(unsigned int cpu, bool online);
        void (*park)(unsigned int cpu);
        void (*unpark)(unsigned int cpu);
        cpumask_var_t cpumask;
        bool selfparking;
        const char *thread_comm;
    }

.. _`smp_hotplug_thread.members`:

Members
-------

store
    Pointer to per cpu storage for the task pointers

list
    List head for core management

thread_should_run
    Check whether the thread should run or not. Called with
    preemption disabled.

thread_fn
    The associated thread function

create
    Optional setup function, called when the thread gets
    created (Not called from the thread context)

setup
    Optional setup function, called when the thread gets
    operational the first time

cleanup
    Optional cleanup function, called when the thread
    should stop (module exit)

park
    Optional park function, called when the thread is
    parked (cpu offline)

unpark
    Optional unpark function, called when the thread is
    unparked (cpu online)

cpumask
    Internal state.  To update which threads are unparked,
    call \ :c:func:`smpboot_update_cpumask_percpu_thread`\ .

selfparking
    Thread is not parked by the park function.

thread_comm
    The base name of the thread

.. This file was automatic generated / don't edit.

