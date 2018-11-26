.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sched/signal.h

.. _`thread_group_cputimer`:

struct thread_group_cputimer
============================

.. c:type:: struct thread_group_cputimer

    thread group interval timer counts

.. _`thread_group_cputimer.definition`:

Definition
----------

.. code-block:: c

    struct thread_group_cputimer {
        struct task_cputime_atomic cputime_atomic;
        bool running;
        bool checking_timer;
    }

.. _`thread_group_cputimer.members`:

Members
-------

cputime_atomic
    atomic thread group interval timers.

running
    true when there are timers running and
    \ ``cputime_atomic``\  receives updates.

checking_timer
    true when a thread in the group is in the
    process of checking for thread group timers.

.. _`thread_group_cputimer.description`:

Description
-----------

This structure contains the version of task_cputime, above, that is
used for thread group CPU timer calculations.

.. _`set_restore_sigmask`:

set_restore_sigmask
===================

.. c:function:: void set_restore_sigmask( void)

    make sure saved_sigmask processing gets done

    :param void:
        no arguments
    :type void: 

.. _`set_restore_sigmask.description`:

Description
-----------

This sets TIF_RESTORE_SIGMASK and ensures that the arch signal code
will run before returning to user mode, to process the flag.  For
all callers, TIF_SIGPENDING is already set or it's no harm to set
it.  TIF_RESTORE_SIGMASK need not be in the set of bits that the
arch code will notice on return to user mode, in case those bits
are scarce.  We set TIF_SIGPENDING here to ensure that the arch
signal code always gets run when TIF_RESTORE_SIGMASK is set.

.. This file was automatic generated / don't edit.

