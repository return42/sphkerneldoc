
.. _API-struct-task-cputime:

===================
struct task_cputime
===================

*man struct task_cputime(9)*

*4.6.0-rc1*

collected CPU time counts


Synopsis
========

.. code-block:: c

    struct task_cputime {
      cputime_t utime;
      cputime_t stime;
      unsigned long long sum_exec_runtime;
    };


Members
=======

utime
    time spent in user mode, in ``cputime_t`` units

stime
    time spent in kernel mode, in ``cputime_t`` units

sum_exec_runtime
    total time spent on the CPU, in nanoseconds


Description
===========

This structure groups together three kinds of CPU time that are tracked for threads and thread groups. Most things considering CPU time want to group these counts together and
treat all three of them in parallel.
