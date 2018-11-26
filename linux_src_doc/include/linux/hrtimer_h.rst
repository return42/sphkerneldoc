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
        u8 is_soft;
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

is_soft
    Set if hrtimer will be expired in soft interrupt context.

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
        unsigned int index;
        clockid_t clockid;
        seqcount_t seq;
        struct hrtimer *running;
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

seq
    seqcount around __run_hrtimer

running
    pointer to the currently running hrtimer

active
    red black tree root node for the active timers

get_time
    function to retrieve the current time of the clock

offset
    offset of this clock to the monotonic base

.. _`hrtimer_cpu_base`:

struct hrtimer_cpu_base
=======================

.. c:type:: struct hrtimer_cpu_base

    the per cpu clock bases

.. _`hrtimer_cpu_base.definition`:

Definition
----------

.. code-block:: c

    struct hrtimer_cpu_base {
        raw_spinlock_t lock;
        unsigned int cpu;
        unsigned int active_bases;
        unsigned int clock_was_set_seq;
        unsigned int hres_active : 1,in_hrtirq : 1,hang_detected : 1, softirq_activated : 1;
    #ifdef CONFIG_HIGH_RES_TIMERS
        unsigned int nr_events;
        unsigned short nr_retries;
        unsigned short nr_hangs;
        unsigned int max_hang_time;
    #endif
        ktime_t expires_next;
        struct hrtimer *next_timer;
        ktime_t softirq_expires_next;
        struct hrtimer *softirq_next_timer;
        struct hrtimer_clock_base clock_base[HRTIMER_MAX_CLOCK_BASES];
    }

.. _`hrtimer_cpu_base.members`:

Members
-------

lock
    lock protecting the base and associated clock bases
    and timers

cpu
    cpu number

active_bases
    Bitfield to mark bases with active timers

clock_was_set_seq
    Sequence counter of clock was set events

hres_active
    State of high resolution mode

in_hrtirq
    \ :c:func:`hrtimer_interrupt`\  is currently executing

hang_detected
    The last hrtimer interrupt detected a hang

softirq_activated
    displays, if the softirq is raised - update of softirq
    related settings is not required then.

nr_events
    Total number of hrtimer interrupt events

nr_retries
    Total number of hrtimer interrupt retries

nr_hangs
    Total number of hrtimer interrupt hangs

max_hang_time
    Maximum time spent in hrtimer_interrupt

expires_next
    absolute time of the next event, is required for remote
    hrtimer enqueue; it is the total first expiry time (hard
    and soft hrtimer are taken into account)

next_timer
    Pointer to the first expiring timer

softirq_expires_next
    Time to check, if soft queues needs also to be expired

softirq_next_timer
    Pointer to the first expiring softirq based timer

clock_base
    array of clock bases for this cpu

.. _`hrtimer_cpu_base.note`:

Note
----

next_timer is just an optimization for \ :c:func:`__remove_hrtimer`\ .
      Do not dereference the pointer because it is not reliable on
      cross cpu removals.

.. _`hrtimer_start`:

hrtimer_start
=============

.. c:function:: void hrtimer_start(struct hrtimer *timer, ktime_t tim, const enum hrtimer_mode mode)

    (re)start an hrtimer

    :param timer:
        the timer to be added
    :type timer: struct hrtimer \*

    :param tim:
        expiry time
    :type tim: ktime_t

    :param mode:
        timer mode: absolute (HRTIMER_MODE_ABS) or
        relative (HRTIMER_MODE_REL), and pinned (HRTIMER_MODE_PINNED);
        softirq based mode is considered for debug purpose only!
    :type mode: const enum hrtimer_mode

.. _`hrtimer_forward_now`:

hrtimer_forward_now
===================

.. c:function:: u64 hrtimer_forward_now(struct hrtimer *timer, ktime_t interval)

    forward the timer expiry so it expires after now

    :param timer:
        hrtimer to forward
    :type timer: struct hrtimer \*

    :param interval:
        the interval to forward
    :type interval: ktime_t

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

