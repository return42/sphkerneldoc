
.. _API-struct-thread-group-cputimer:

============================
struct thread_group_cputimer
============================

*man struct thread_group_cputimer(9)*

*4.6.0-rc1*

thread group interval timer counts


Synopsis
========

.. code-block:: c

    struct thread_group_cputimer {
      struct task_cputime_atomic cputime_atomic;
      bool running;
      bool checking_timer;
    };


Members
=======

cputime_atomic
    atomic thread group interval timers.

running
    true when there are timers running and ``cputime_atomic`` receives updates.

checking_timer
    true when a thread in the group is in the process of checking for thread group timers.


Description
===========

This structure contains the version of task_cputime, above, that is used for thread group CPU timer calculations.
