.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/wait_bit.h

.. _`wait_on_bit`:

wait_on_bit
===========

.. c:function:: int wait_on_bit(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit.description`:

Description
-----------

There is a standard hashed waitqueue table for generic use. This
is the part of the hashtable's accessor API that waits on a bit.
For instance, if one were to have waiters on a bitflag, one would
call \ :c:func:`wait_on_bit`\  in threads waiting for the bit to clear.
One uses \ :c:func:`wait_on_bit`\  where one is waiting for the bit to clear,
but has no intention of setting it.
Returned value will be zero if the bit was cleared, or non-zero
if the process received a signal and the mode permitted wakeup
on that signal.

.. _`wait_on_bit_io`:

wait_on_bit_io
==============

.. c:function:: int wait_on_bit_io(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_io.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared.  This is similar to \ :c:func:`wait_on_bit`\ , but calls
\ :c:func:`io_schedule`\  instead of \ :c:func:`schedule`\  for the actual waiting.

Returned value will be zero if the bit was cleared, or non-zero
if the process received a signal and the mode permitted wakeup
on that signal.

.. _`wait_on_bit_timeout`:

wait_on_bit_timeout
===================

.. c:function:: int wait_on_bit_timeout(unsigned long *word, int bit, unsigned mode, unsigned long timeout)

    wait for a bit to be cleared or a timeout elapses

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

    :param unsigned long timeout:
        timeout, in jiffies

.. _`wait_on_bit_timeout.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared. This is similar to \ :c:func:`wait_on_bit`\ , except also takes a
timeout parameter.

Returned value will be zero if the bit was cleared before the
\ ``timeout``\  elapsed, or non-zero if the \ ``timeout``\  elapsed or process
received a signal and the mode permitted wakeup on that signal.

.. _`wait_on_bit_action`:

wait_on_bit_action
==================

.. c:function:: int wait_on_bit_action(unsigned long *word, int bit, wait_bit_action_f *action, unsigned mode)

    wait for a bit to be cleared

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param wait_bit_action_f \*action:
        the function used to sleep, which may take special actions

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_action.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared, and allow the waiting action to be specified.
This is like \ :c:func:`wait_on_bit`\  but allows fine control of how the waiting
is done.

Returned value will be zero if the bit was cleared, or non-zero
if the process received a signal and the mode permitted wakeup
on that signal.

.. _`wait_on_bit_lock`:

wait_on_bit_lock
================

.. c:function:: int wait_on_bit_lock(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared, when wanting to set it

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_lock.description`:

Description
-----------

There is a standard hashed waitqueue table for generic use. This
is the part of the hashtable's accessor API that waits on a bit
when one intends to set it, for instance, trying to lock bitflags.
For instance, if one were to have waiters trying to set bitflag
and waiting for it to clear before setting it, one would call
\ :c:func:`wait_on_bit`\  in threads waiting to be able to set the bit.
One uses \ :c:func:`wait_on_bit_lock`\  where one is waiting for the bit to
clear with the intention of setting it, and when done, clearing it.

Returns zero if the bit was (eventually) found to be clear and was
set.  Returns non-zero if a signal was delivered to the process and
the \ ``mode``\  allows that signal to wake the process.

.. _`wait_on_bit_lock_io`:

wait_on_bit_lock_io
===================

.. c:function:: int wait_on_bit_lock_io(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared, when wanting to set it

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_lock_io.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared and then to atomically set it.  This is similar
to \ :c:func:`wait_on_bit`\ , but calls \ :c:func:`io_schedule`\  instead of \ :c:func:`schedule`\ 
for the actual waiting.

Returns zero if the bit was (eventually) found to be clear and was
set.  Returns non-zero if a signal was delivered to the process and
the \ ``mode``\  allows that signal to wake the process.

.. _`wait_on_bit_lock_action`:

wait_on_bit_lock_action
=======================

.. c:function:: int wait_on_bit_lock_action(unsigned long *word, int bit, wait_bit_action_f *action, unsigned mode)

    wait for a bit to be cleared, when wanting to set it

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param wait_bit_action_f \*action:
        the function used to sleep, which may take special actions

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_lock_action.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared and then to set it, and allow the waiting action
to be specified.
This is like \ :c:func:`wait_on_bit`\  but allows fine control of how the waiting
is done.

Returns zero if the bit was (eventually) found to be clear and was
set.  Returns non-zero if a signal was delivered to the process and
the \ ``mode``\  allows that signal to wake the process.

.. _`wait_on_atomic_t`:

wait_on_atomic_t
================

.. c:function:: int wait_on_atomic_t(atomic_t *val, wait_atomic_t_action_f action, unsigned mode)

    Wait for an atomic_t to become 0

    :param atomic_t \*val:
        The atomic value being waited on, a kernel virtual address

    :param wait_atomic_t_action_f action:
        the function used to sleep, which may take special actions

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_atomic_t.description`:

Description
-----------

Wait for an atomic_t to become 0.  We abuse the bit-wait waitqueue table for
the purpose of getting a waitqueue, but we set the key to a bit number
outside of the target 'word'.

.. This file was automatic generated / don't edit.

