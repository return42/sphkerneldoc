.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/hrtimer.h

.. _`hrtimer`:

struct hrtimer
==============

.. c:type:: struct hrtimer

    the basic hrtimer structure

.. _`hrtimer.definition`:

Definition
----------

.. code-block:: c

    struct hrtimer {
        struct timerqueue_node node;
        ktime_t _softexpires;
        enum hrtimer_restart (*function)(struct hrtimer *);
        struct hrtimer_clock_base *base;
        u8 state;
        u8 is_rel;
    }

.. _`hrtimer.members`:

Members
-------

node
    timerqueue node, which also manages node.expires,
    the absolute expiry time in the hrtimers internal
    representation. The time is related to the clock on
    which the timer is based. Is setup by adding
    slack to the _softexpires value. For non range timers
    identical to _softexpires.

_softexpires
    the absolute earliest expiry time of the hrtimer.
    The time which was given as expiry time when the timer
    was armed.

function
    timer expiry callback function

base
    pointer to the timer base (per cpu and per clock)

state
    state information (See bit values above)

is_rel
    Set if the timer was armed relative

.. _`hrtimer.description`:

Description
-----------

The hrtimer structure must be initialized by \ :c:func:`hrtimer_init`\ 

.. _`hrtimer_sleeper`:

struct hrtimer_sleeper
======================

.. c:type:: struct hrtimer_sleeper

    simple sleeper structure

.. _`hrtimer_sleeper.definition`:

Definition
----------

.. code-block:: c

    struct hrtimer_sleeper {
        struct hrtimer timer;
        struct task_struct *task;
    }

.. _`hrtimer_sleeper.members`:

Members
-------

timer
    embedded timer structure

task
    task to wake up

.. _`hrtimer_sleeper.description`:

Description
-----------

task is set to NULL, when the timer expires.

.. _`hrtimer_clock_base`:

struct hrtimer_clock_base
=========================

.. c:type:: struct hrtimer_clock_base

    the timer base for a specific clock

.. _`hrtimer_clock_base.definition`:

Definition
----------

.. code-block:: c

    struct hrtimer_clock_base {
        struct hrtimer_cpu_base *cpu_base;
        int index;
        clockid_t clockid;
        struct timerqueue_head active;
        ktime_t (*get_time)(void);
        ktime_t offset;
    }

.. _`hrtimer_clock_base.members`:

Members
-------

cpu_base
    per cpu clock base

index
    clock type index for per_cpu support when moving a
    timer to a base on another cpu.

clockid
    clock id for per_cpu support

active
    red black tree root node for the active timers

get_time
    function to retrieve the current time of the clock

offset
    offset of this clock to the monotonic base

.. _`hrtimer_start`:

hrtimer_start
=============

.. c:function:: void hrtimer_start(struct hrtimer *timer, ktime_t tim, const enum hrtimer_mode mode)

    (re)start an hrtimer on the current CPU

    :param struct hrtimer \*timer:
        the timer to be added

    :param ktime_t tim:
        expiry time

    :param const enum hrtimer_mode mode:
        expiry mode: absolute (HRTIMER_MODE_ABS) or
        relative (HRTIMER_MODE_REL)

.. _`hrtimer_forward_now`:

hrtimer_forward_now
===================

.. c:function:: u64 hrtimer_forward_now(struct hrtimer *timer, ktime_t interval)

    forward the timer expiry so it expires after now

    :param struct hrtimer \*timer:
        hrtimer to forward

    :param ktime_t interval:
        the interval to forward

.. _`hrtimer_forward_now.description`:

Description
-----------

Forward the timer expiry so it will expire after the current time
of the hrtimer clock base. Returns the number of overruns.

Can be safely called from the callback function of \ ``timer``\ . If
called from other contexts \ ``timer``\  must neither be enqueued nor
running the callback and the caller needs to take care of
serialization.

.. _`hrtimer_forward_now.note`:

Note
----

This only updates the timer expiry value and does not requeue
the timer.

.. This file was automatic generated / don't edit.

