.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/wait_bit.h

.. _`wait_on_bit`:

wait_on_bit
===========

.. c:function:: int wait_on_bit(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared

    :param word:
        the word being waited on, a kernel virtual address
    :type word: unsigned long \*

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param mode:
        the task state to sleep in
    :type mode: unsigned

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

    :param word:
        the word being waited on, a kernel virtual address
    :type word: unsigned long \*

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param mode:
        the task state to sleep in
    :type mode: unsigned

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

    :param word:
        the word being waited on, a kernel virtual address
    :type word: unsigned long \*

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param mode:
        the task state to sleep in
    :type mode: unsigned

    :param timeout:
        timeout, in jiffies
    :type timeout: unsigned long

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

    :param word:
        the word being waited on, a kernel virtual address
    :type word: unsigned long \*

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param action:
        the function used to sleep, which may take special actions
    :type action: wait_bit_action_f \*

    :param mode:
        the task state to sleep in
    :type mode: unsigned

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

    :param word:
        the word being waited on, a kernel virtual address
    :type word: unsigned long \*

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param mode:
        the task state to sleep in
    :type mode: unsigned

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

    :param word:
        the word being waited on, a kernel virtual address
    :type word: unsigned long \*

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param mode:
        the task state to sleep in
    :type mode: unsigned

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

    :param word:
        the word being waited on, a kernel virtual address
    :type word: unsigned long \*

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param action:
        the function used to sleep, which may take special actions
    :type action: wait_bit_action_f \*

    :param mode:
        the task state to sleep in
    :type mode: unsigned

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

.. _`clear_and_wake_up_bit`:

clear_and_wake_up_bit
=====================

.. c:function:: void clear_and_wake_up_bit(int bit, void *word)

    clear a bit and wake up anyone waiting on that bit

    :param bit:
        the bit of the word being waited on
    :type bit: int

    :param word:
        the word being waited on, a kernel virtual address
    :type word: void \*

.. _`clear_and_wake_up_bit.description`:

Description
-----------

You can use this helper if bitflags are manipulated atomically rather than
non-atomically under a lock.

.. This file was automatic generated / don't edit.

