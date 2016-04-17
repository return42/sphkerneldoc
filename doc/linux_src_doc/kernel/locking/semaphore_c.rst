.. -*- coding: utf-8; mode: rst -*-

===========
semaphore.c
===========


.. _`down`:

down
====

.. c:function:: void down (struct semaphore *sem)

    acquire the semaphore

    :param struct semaphore \*sem:
        the semaphore to be acquired



.. _`down.description`:

Description
-----------

Acquires the semaphore.  If no more tasks are allowed to acquire the
semaphore, calling this function will put the task to sleep until the
semaphore is released.

Use of this function is deprecated, please use :c:func:`down_interruptible` or
:c:func:`down_killable` instead.



.. _`down_interruptible`:

down_interruptible
==================

.. c:function:: int down_interruptible (struct semaphore *sem)

    acquire the semaphore unless interrupted

    :param struct semaphore \*sem:
        the semaphore to be acquired



.. _`down_interruptible.description`:

Description
-----------

Attempts to acquire the semaphore.  If no more tasks are allowed to
acquire the semaphore, calling this function will put the task to sleep.
If the sleep is interrupted by a signal, this function will return -EINTR.
If the semaphore is successfully acquired, this function returns 0.



.. _`down_killable`:

down_killable
=============

.. c:function:: int down_killable (struct semaphore *sem)

    acquire the semaphore unless killed

    :param struct semaphore \*sem:
        the semaphore to be acquired



.. _`down_killable.description`:

Description
-----------

Attempts to acquire the semaphore.  If no more tasks are allowed to
acquire the semaphore, calling this function will put the task to sleep.
If the sleep is interrupted by a fatal signal, this function will return
-EINTR.  If the semaphore is successfully acquired, this function returns
0.



.. _`down_trylock`:

down_trylock
============

.. c:function:: int down_trylock (struct semaphore *sem)

    try to acquire the semaphore, without waiting

    :param struct semaphore \*sem:
        the semaphore to be acquired



.. _`down_trylock.description`:

Description
-----------

Try to acquire the semaphore atomically.  Returns 0 if the semaphore has
been acquired successfully or 1 if it it cannot be acquired.



.. _`down_trylock.note`:

NOTE
----

This return value is inverted from both spin_trylock and
mutex_trylock!  Be careful about this when converting code.

Unlike mutex_trylock, this function can be used from interrupt context,
and the semaphore can be released by any task or interrupt.



.. _`down_timeout`:

down_timeout
============

.. c:function:: int down_timeout (struct semaphore *sem, long timeout)

    acquire the semaphore within a specified time

    :param struct semaphore \*sem:
        the semaphore to be acquired

    :param long timeout:
        how long to wait before failing



.. _`down_timeout.description`:

Description
-----------

Attempts to acquire the semaphore.  If no more tasks are allowed to
acquire the semaphore, calling this function will put the task to sleep.
If the semaphore is not released within the specified number of jiffies,
this function returns -ETIME.  It returns 0 if the semaphore was acquired.



.. _`up`:

up
==

.. c:function:: void up (struct semaphore *sem)

    release the semaphore

    :param struct semaphore \*sem:
        the semaphore to release



.. _`up.description`:

Description
-----------

Release the semaphore.  Unlike mutexes, :c:func:`up` may be called from any
context and even by tasks which have never called :c:func:`down`.

