.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/completion.c

.. _`complete`:

complete
========

.. c:function:: void complete(struct completion *x)

    - signals a single thread waiting on this completion

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

.. _`complete.description`:

Description
-----------

This will wake up a single thread waiting on this completion. Threads will be
awakened in the same order in which they were queued.

See also \ :c:func:`complete_all`\ , \ :c:func:`wait_for_completion`\  and related routines.

If this function wakes up a task, it executes a full memory barrier before
accessing the task state.

.. _`complete_all`:

complete_all
============

.. c:function:: void complete_all(struct completion *x)

    - signals all threads waiting on this completion

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

.. _`complete_all.description`:

Description
-----------

This will wake up all threads waiting on this particular completion event.

If this function wakes up a task, it executes a full memory barrier before
accessing the task state.

Since \ :c:func:`complete_all`\  sets the completion of \ ``x``\  permanently to done
to allow multiple waiters to finish, a call to \ :c:func:`reinit_completion`\ 
must be used on \ ``x``\  if \ ``x``\  is to be used again. The code must make
sure that all waiters have woken and finished before reinitializing
\ ``x``\ . Also note that the function \ :c:func:`completion_done`\  can not be used
to know if there are still waiters after \ :c:func:`complete_all`\  has been called.

.. _`wait_for_completion`:

wait_for_completion
===================

.. c:function:: void __sched wait_for_completion(struct completion *x)

    - waits for completion of a task

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

.. _`wait_for_completion.description`:

Description
-----------

This waits to be signaled for completion of a specific task. It is NOT
interruptible and there is no timeout.

See also similar routines (i.e. \ :c:func:`wait_for_completion_timeout`\ ) with timeout
and interrupt capability. Also see \ :c:func:`complete`\ .

.. _`wait_for_completion_timeout`:

wait_for_completion_timeout
===========================

.. c:function:: unsigned long __sched wait_for_completion_timeout(struct completion *x, unsigned long timeout)

    - waits for completion of a task (w/timeout)

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

    :param timeout:
        timeout value in jiffies
    :type timeout: unsigned long

.. _`wait_for_completion_timeout.description`:

Description
-----------

This waits for either a completion of a specific task to be signaled or for a
specified timeout to expire. The timeout is in jiffies. It is not
interruptible.

.. _`wait_for_completion_timeout.return`:

Return
------

0 if timed out, and positive (at least 1, or number of jiffies left
till timeout) if completed.

.. _`wait_for_completion_io`:

wait_for_completion_io
======================

.. c:function:: void __sched wait_for_completion_io(struct completion *x)

    - waits for completion of a task

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

.. _`wait_for_completion_io.description`:

Description
-----------

This waits to be signaled for completion of a specific task. It is NOT
interruptible and there is no timeout. The caller is accounted as waiting
for IO (which traditionally means blkio only).

.. _`wait_for_completion_io_timeout`:

wait_for_completion_io_timeout
==============================

.. c:function:: unsigned long __sched wait_for_completion_io_timeout(struct completion *x, unsigned long timeout)

    - waits for completion of a task (w/timeout)

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

    :param timeout:
        timeout value in jiffies
    :type timeout: unsigned long

.. _`wait_for_completion_io_timeout.description`:

Description
-----------

This waits for either a completion of a specific task to be signaled or for a
specified timeout to expire. The timeout is in jiffies. It is not
interruptible. The caller is accounted as waiting for IO (which traditionally
means blkio only).

.. _`wait_for_completion_io_timeout.return`:

Return
------

0 if timed out, and positive (at least 1, or number of jiffies left
till timeout) if completed.

.. _`wait_for_completion_interruptible`:

wait_for_completion_interruptible
=================================

.. c:function:: int __sched wait_for_completion_interruptible(struct completion *x)

    - waits for completion of a task (w/intr)

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

.. _`wait_for_completion_interruptible.description`:

Description
-----------

This waits for completion of a specific task to be signaled. It is
interruptible.

.. _`wait_for_completion_interruptible.return`:

Return
------

-ERESTARTSYS if interrupted, 0 if completed.

.. _`wait_for_completion_interruptible_timeout`:

wait_for_completion_interruptible_timeout
=========================================

.. c:function:: long __sched wait_for_completion_interruptible_timeout(struct completion *x, unsigned long timeout)

    - waits for completion (w/(to,intr))

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

    :param timeout:
        timeout value in jiffies
    :type timeout: unsigned long

.. _`wait_for_completion_interruptible_timeout.description`:

Description
-----------

This waits for either a completion of a specific task to be signaled or for a
specified timeout to expire. It is interruptible. The timeout is in jiffies.

.. _`wait_for_completion_interruptible_timeout.return`:

Return
------

-ERESTARTSYS if interrupted, 0 if timed out, positive (at least 1,
or number of jiffies left till timeout) if completed.

.. _`wait_for_completion_killable`:

wait_for_completion_killable
============================

.. c:function:: int __sched wait_for_completion_killable(struct completion *x)

    - waits for completion of a task (killable)

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

.. _`wait_for_completion_killable.description`:

Description
-----------

This waits to be signaled for completion of a specific task. It can be
interrupted by a kill signal.

.. _`wait_for_completion_killable.return`:

Return
------

-ERESTARTSYS if interrupted, 0 if completed.

.. _`wait_for_completion_killable_timeout`:

wait_for_completion_killable_timeout
====================================

.. c:function:: long __sched wait_for_completion_killable_timeout(struct completion *x, unsigned long timeout)

    - waits for completion of a task (w/(to,killable))

    :param x:
        holds the state of this particular completion
    :type x: struct completion \*

    :param timeout:
        timeout value in jiffies
    :type timeout: unsigned long

.. _`wait_for_completion_killable_timeout.description`:

Description
-----------

This waits for either a completion of a specific task to be
signaled or for a specified timeout to expire. It can be
interrupted by a kill signal. The timeout is in jiffies.

.. _`wait_for_completion_killable_timeout.return`:

Return
------

-ERESTARTSYS if interrupted, 0 if timed out, positive (at least 1,
or number of jiffies left till timeout) if completed.

.. _`try_wait_for_completion`:

try_wait_for_completion
=======================

.. c:function:: bool try_wait_for_completion(struct completion *x)

    try to decrement a completion without blocking

    :param x:
        completion structure
    :type x: struct completion \*

.. _`try_wait_for_completion.return`:

Return
------

0 if a decrement cannot be done without blocking
1 if a decrement succeeded.

If a completion is being used as a counting completion,
attempt to decrement the counter without blocking. This
enables us to avoid waiting if the resource the completion
is protecting is not available.

.. _`completion_done`:

completion_done
===============

.. c:function:: bool completion_done(struct completion *x)

    Test to see if a completion has any waiters

    :param x:
        completion structure
    :type x: struct completion \*

.. _`completion_done.return`:

Return
------

0 if there are waiters (wait_for_completion() in progress)
1 if there are no waiters.

Note, this will always return true if \ :c:func:`complete_all`\  was called on \ ``X``\ .

.. This file was automatic generated / don't edit.

