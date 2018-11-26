.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/process.c

.. _`freeze_processes`:

freeze_processes
================

.. c:function:: int freeze_processes( void)

    Signal user space processes to enter the refrigerator. The current thread will not be frozen.  The same process that calls freeze_processes must later call thaw_processes.

    :param void:
        no arguments
    :type void: 

.. _`freeze_processes.description`:

Description
-----------

On success, returns 0.  On failure, -errno and system is fully thawed.

.. _`freeze_kernel_threads`:

freeze_kernel_threads
=====================

.. c:function:: int freeze_kernel_threads( void)

    Make freezable kernel threads go to the refrigerator.

    :param void:
        no arguments
    :type void: 

.. _`freeze_kernel_threads.description`:

Description
-----------

On success, returns 0.  On failure, -errno and only the kernel threads are
thawed, so as to give a chance to the caller to do additional cleanups
(if any) before thawing the userspace tasks. So, it is the responsibility
of the caller to thaw the userspace tasks, when the time is right.

.. This file was automatic generated / don't edit.

