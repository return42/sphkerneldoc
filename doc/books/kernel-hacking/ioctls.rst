.. -*- coding: utf-8; mode: rst -*-

.. _ioctls:

=====================================
ioctls: Not writing a new system call
=====================================

A system call generally looks like this


.. code-block:: c

    asmlinkage long sys_mycall(int arg)
    {
            return 0;
    }

First, in most cases you don't want to create a new system call. You
create a character device and implement an appropriate ioctl for it.
This is much more flexible than system calls, doesn't have to be entered
in every architecture's ``include/asm/unistd.h`` and
``arch/kernel/entry.S`` file, and is much more likely to be accepted by
Linus.

If all your routine does is read or write some parameter, consider
implementing a ``sysfs`` interface instead.

Inside the ioctl you're in user context to a process. When a error
occurs you return a negated errno (see ``include/linux/errno.h``),
otherwise you return 0.

After you slept you should check if a signal occurred: the Unix/Linux
way of handling signals is to temporarily exit the system call with the
``-ERESTARTSYS`` error. The system call entry code will switch back to
user context, process the signal handler and then your system call will
be restarted (unless the user disabled that). So you should be prepared
to process the restart, e.g. if you're in the middle of manipulating
some data structure.


.. code-block:: c

    if (signal_pending(current))
            return -ERESTARTSYS;

If you're doing longer computations: first think userspace. If you
*really* want to do it in kernel you should regularly check if you need
to give up the CPU (remember there is cooperative multitasking per CPU).
Idiom:


.. code-block:: c

    cond_resched(); /* Will sleep */

A short note on interface design: the UNIX system call motto is "Provide
mechanism not policy".


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
