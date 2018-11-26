.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/powercap/idle_inject.c

.. _`idle_inject_thread`:

struct idle_inject_thread
=========================

.. c:type:: struct idle_inject_thread

    task on/off switch structure

.. _`idle_inject_thread.definition`:

Definition
----------

.. code-block:: c

    struct idle_inject_thread {
        struct task_struct *tsk;
        int should_run;
    }

.. _`idle_inject_thread.members`:

Members
-------

tsk
    task injecting the idle cycles

should_run
    whether or not to run the task (for the smpboot kthread API)

.. _`idle_inject_device`:

struct idle_inject_device
=========================

.. c:type:: struct idle_inject_device

    idle injection data

.. _`idle_inject_device.definition`:

Definition
----------

.. code-block:: c

    struct idle_inject_device {
        struct hrtimer timer;
        unsigned int idle_duration_ms;
        unsigned int run_duration_ms;
        unsigned long int cpumask[0];
    }

.. _`idle_inject_device.members`:

Members
-------

timer
    idle injection period timer

idle_duration_ms
    duration of CPU idle time to inject

run_duration_ms
    duration of CPU run time to allow

cpumask
    mask of CPUs affected by idle injection

.. _`idle_inject_wakeup`:

idle_inject_wakeup
==================

.. c:function:: void idle_inject_wakeup(struct idle_inject_device *ii_dev)

    Wake up idle injection threads

    :param ii_dev:
        target idle injection device
    :type ii_dev: struct idle_inject_device \*

.. _`idle_inject_wakeup.description`:

Description
-----------

Every idle injection task associated with the given idle injection device
and running on an online CPU will be woken up.

.. _`idle_inject_timer_fn`:

idle_inject_timer_fn
====================

.. c:function:: enum hrtimer_restart idle_inject_timer_fn(struct hrtimer *timer)

    idle injection timer function

    :param timer:
        idle injection hrtimer
    :type timer: struct hrtimer \*

.. _`idle_inject_timer_fn.description`:

Description
-----------

This function is called when the idle injection timer expires.  It wakes up
idle injection tasks associated with the timer and they, in turn, invoke
\ :c:func:`play_idle`\  to inject a specified amount of CPU idle time.

.. _`idle_inject_timer_fn.return`:

Return
------

HRTIMER_RESTART.

.. _`idle_inject_fn`:

idle_inject_fn
==============

.. c:function:: void idle_inject_fn(unsigned int cpu)

    idle injection work function

    :param cpu:
        the CPU owning the task
    :type cpu: unsigned int

.. _`idle_inject_fn.description`:

Description
-----------

This function calls \ :c:func:`play_idle`\  to inject a specified amount of CPU idle
time.

.. _`idle_inject_set_duration`:

idle_inject_set_duration
========================

.. c:function:: void idle_inject_set_duration(struct idle_inject_device *ii_dev, unsigned int run_duration_ms, unsigned int idle_duration_ms)

    idle and run duration update helper

    :param ii_dev:
        *undescribed*
    :type ii_dev: struct idle_inject_device \*

    :param run_duration_ms:
        CPU run time to allow in milliseconds
    :type run_duration_ms: unsigned int

    :param idle_duration_ms:
        CPU idle time to inject in milliseconds
    :type idle_duration_ms: unsigned int

.. _`idle_inject_get_duration`:

idle_inject_get_duration
========================

.. c:function:: void idle_inject_get_duration(struct idle_inject_device *ii_dev, unsigned int *run_duration_ms, unsigned int *idle_duration_ms)

    idle and run duration retrieval helper

    :param ii_dev:
        *undescribed*
    :type ii_dev: struct idle_inject_device \*

    :param run_duration_ms:
        memory location to store the current CPU run time
    :type run_duration_ms: unsigned int \*

    :param idle_duration_ms:
        memory location to store the current CPU idle time
    :type idle_duration_ms: unsigned int \*

.. _`idle_inject_start`:

idle_inject_start
=================

.. c:function:: int idle_inject_start(struct idle_inject_device *ii_dev)

    start idle injections

    :param ii_dev:
        idle injection control device structure
    :type ii_dev: struct idle_inject_device \*

.. _`idle_inject_start.description`:

Description
-----------

The function starts idle injection by first waking up all of the idle
injection kthreads associated with \ ``ii_dev``\  to let them inject CPU idle time
sets up a timer to start the next idle injection period.

.. _`idle_inject_start.return`:

Return
------

-EINVAL if the CPU idle or CPU run time is not set or 0 on success.

.. _`idle_inject_stop`:

idle_inject_stop
================

.. c:function:: void idle_inject_stop(struct idle_inject_device *ii_dev)

    stops idle injections

    :param ii_dev:
        idle injection control device structure
    :type ii_dev: struct idle_inject_device \*

.. _`idle_inject_stop.description`:

Description
-----------

The function stops idle injection and waits for the threads to finish work.
If CPU idle time is being injected when this function runs, then it will
wait until the end of the cycle.

When it returns, there is no more idle injection kthread activity.  The
kthreads are scheduled out and the periodic timer is off.

.. _`idle_inject_setup`:

idle_inject_setup
=================

.. c:function:: void idle_inject_setup(unsigned int cpu)

    prepare the current task for idle injection

    :param cpu:
        not used
    :type cpu: unsigned int

.. _`idle_inject_setup.description`:

Description
-----------

Called once, this function is in charge of setting the current task's
scheduler parameters to make it an RT task.

.. _`idle_inject_should_run`:

idle_inject_should_run
======================

.. c:function:: int idle_inject_should_run(unsigned int cpu)

    function helper for the smpboot API

    :param cpu:
        CPU the kthread is running on
    :type cpu: unsigned int

.. _`idle_inject_should_run.return`:

Return
------

whether or not the thread can run.

.. _`idle_inject_register`:

idle_inject_register
====================

.. c:function:: struct idle_inject_device *idle_inject_register(struct cpumask *cpumask)

    initialize idle injection on a set of CPUs

    :param cpumask:
        CPUs to be affected by idle injection
    :type cpumask: struct cpumask \*

.. _`idle_inject_register.description`:

Description
-----------

This function creates an idle injection control device structure for the
given set of CPUs and initializes the timer associated with it.  It does not
start any injection cycles.

.. _`idle_inject_register.return`:

Return
------

NULL if memory allocation fails, idle injection control device
pointer on success.

.. _`idle_inject_unregister`:

idle_inject_unregister
======================

.. c:function:: void idle_inject_unregister(struct idle_inject_device *ii_dev)

    unregister idle injection control device

    :param ii_dev:
        idle injection control device to unregister
    :type ii_dev: struct idle_inject_device \*

.. _`idle_inject_unregister.description`:

Description
-----------

The function stops idle injection for the given control device,
unregisters its kthreads and frees memory allocated when that device was
created.

.. This file was automatic generated / don't edit.

