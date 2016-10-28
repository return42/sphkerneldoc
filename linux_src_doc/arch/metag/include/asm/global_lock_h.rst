.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/include/asm/global_lock.h

.. _`__global_lock1`:

__global_lock1
==============

.. c:function::  __global_lock1( flags)

    Acquire global voluntary lock (LOCK1).

    :param  flags:
        Variable to store flags into.

.. _`__global_lock1.description`:

Description
-----------

Acquires the Meta global voluntary lock (LOCK1), also taking care to disable
all triggers so we cannot be interrupted, and to enforce a compiler barrier
so that the compiler cannot reorder memory accesses across the lock.

No other hardware thread will be able to acquire the voluntary or exclusive
locks until the voluntary lock is released with \ ``__global_unlock1``\ , but they
may continue to execute as long as they aren't trying to acquire either of
the locks.

.. _`__global_unlock1`:

__global_unlock1
================

.. c:function::  __global_unlock1( flags)

    Release global voluntary lock (LOCK1).

    :param  flags:
        Variable to restore flags from.

.. _`__global_unlock1.description`:

Description
-----------

Releases the Meta global voluntary lock (LOCK1) acquired with
\ ``__global_lock1``\ , also taking care to re-enable triggers, and to enforce a
compiler barrier so that the compiler cannot reorder memory accesses across
the unlock.

This immediately allows another hardware thread to acquire the voluntary or
exclusive locks.

.. _`__global_lock2`:

__global_lock2
==============

.. c:function::  __global_lock2( flags)

    Acquire global exclusive lock (LOCK2).

    :param  flags:
        Variable to store flags into.

.. _`__global_lock2.description`:

Description
-----------

Acquires the Meta global voluntary lock and global exclusive lock (LOCK2),
also taking care to disable all triggers so we cannot be interrupted, to take
the atomic lock (system event) and to enforce a compiler barrier so that the
compiler cannot reorder memory accesses across the lock.

No other hardware thread will be able to execute code until the locks are
released with \ ``__global_unlock2``\ .

.. _`__global_unlock2`:

__global_unlock2
================

.. c:function::  __global_unlock2( flags)

    Release global exclusive lock (LOCK2).

    :param  flags:
        Variable to restore flags from.

.. _`__global_unlock2.description`:

Description
-----------

Releases the Meta global exclusive lock (LOCK2) and global voluntary lock
acquired with \ ``__global_lock2``\ , also taking care to release the atomic lock
(system event), re-enable triggers, and to enforce a compiler barrier so that
the compiler cannot reorder memory accesses across the unlock.

This immediately allows other hardware threads to continue executing and one
of them to acquire locks.

.. This file was automatic generated / don't edit.

