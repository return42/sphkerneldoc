
.. _API-proc-flush-task:

===============
proc_flush_task
===============

*man proc_flush_task(9)*

*4.6.0-rc1*

Remove dcache entries for ``task`` from the /proc dcache.


Synopsis
========

.. c:function:: void proc_flush_task( struct task_struct * task )

Arguments
=========

``task``
    task that should be flushed.


Description
===========

When flushing dentries from proc, one needs to flush them from global proc (proc_mnt) and from all the namespaces' procs this task was seen in. This call is supposed to do all of
this job.

Looks in the dcache for /proc/``pid`` /proc/``tgid``/task/``pid`` if either directory is present flushes it and all of it'ts children from the dcache.

It is safe and reasonable to cache /proc entries for a task until that task exits. After that they just clog up the dcache with useless entries, possibly causing useful dcache
entries to be flushed instead. This routine is proved to flush those useless dcache entries at process exit time.


NOTE
====

This routine is just an optimization so it does not guarantee that no dcache entries will exist at process exit time it just makes it very unlikely that any will persist.
