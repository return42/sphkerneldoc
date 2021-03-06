.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/posix-timers.h

.. _`k_itimer`:

struct k_itimer
===============

.. c:type:: struct k_itimer

    POSIX.1b interval timer structure.

.. _`k_itimer.definition`:

Definition
----------

.. code-block:: c

    struct k_itimer {
        struct list_head list;
        struct hlist_node t_hash;
        spinlock_t it_lock;
        const struct k_clock *kclock;
        clockid_t it_clock;
        timer_t it_id;
        int it_active;
        s64 it_overrun;
        s64 it_overrun_last;
        int it_requeue_pending;
        int it_sigev_notify;
        ktime_t it_interval;
        struct signal_struct *it_signal;
        union {
            struct pid *it_pid;
            struct task_struct *it_process;
        } ;
        struct sigqueue *sigq;
        union {
            struct {
                struct hrtimer timer;
            } real;
            struct cpu_timer_list cpu;
            struct {
                struct alarm alarmtimer;
            } alarm;
            struct rcu_head rcu;
        } it;
    }

.. _`k_itimer.members`:

Members
-------

list
    List head for binding the timer to signals->posix_timers

t_hash
    Entry in the posix timer hash table

it_lock
    Lock protecting the timer

kclock
    Pointer to the k_clock struct handling this timer

it_clock
    The posix timer clock id

it_id
    The posix timer id for identifying the timer

it_active
    Marker that timer is active

it_overrun
    The overrun counter for pending signals

it_overrun_last
    The overrun at the time of the last delivered signal

it_requeue_pending
    Indicator that timer waits for being requeued on
    signal delivery

it_sigev_notify
    The notify word of sigevent struct for signal delivery

it_interval
    The interval for periodic timers

it_signal
    Pointer to the creators signal struct

{unnamed_union}
    anonymous

it_pid
    The pid of the process/task targeted by the signal

it_process
    The task to wakeup on clock_nanosleep (CPU timers)

sigq
    Pointer to preallocated sigqueue

it
    Union representing the various posix timer type
    internals. Also used for rcu freeing the timer.

.. This file was automatic generated / don't edit.

