.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/notifier.c

.. _`notifier_call_chain`:

notifier_call_chain
===================

.. c:function:: int notifier_call_chain(struct notifier_block **nl, unsigned long val, void *v, int nr_to_call, int *nr_calls)

    Informs the registered notifiers about an event.

    :param struct notifier_block \*\*nl:
        Pointer to head of the blocking notifier chain

    :param unsigned long val:
        Value passed unmodified to notifier function

    :param void \*v:
        Pointer passed unmodified to notifier function

    :param int nr_to_call:
        Number of notifier functions to be called. Don't care
        value of this parameter is -1.

    :param int \*nr_calls:
        Records the number of notifications sent. Don't care
        value of this field is NULL.

.. _`atomic_notifier_chain_register`:

atomic_notifier_chain_register
==============================

.. c:function:: int atomic_notifier_chain_register(struct atomic_notifier_head *nh, struct notifier_block *n)

    Add notifier to an atomic notifier chain

    :param struct atomic_notifier_head \*nh:
        Pointer to head of the atomic notifier chain

    :param struct notifier_block \*n:
        New entry in notifier chain

.. _`atomic_notifier_chain_register.description`:

Description
-----------

Adds a notifier to an atomic notifier chain.

Currently always returns zero.

.. _`atomic_notifier_chain_unregister`:

atomic_notifier_chain_unregister
================================

.. c:function:: int atomic_notifier_chain_unregister(struct atomic_notifier_head *nh, struct notifier_block *n)

    Remove notifier from an atomic notifier chain

    :param struct atomic_notifier_head \*nh:
        Pointer to head of the atomic notifier chain

    :param struct notifier_block \*n:
        Entry to remove from notifier chain

.. _`atomic_notifier_chain_unregister.description`:

Description
-----------

Removes a notifier from an atomic notifier chain.

Returns zero on success or \ ``-ENOENT``\  on failure.

.. _`__atomic_notifier_call_chain`:

\__atomic_notifier_call_chain
=============================

.. c:function:: int __atomic_notifier_call_chain(struct atomic_notifier_head *nh, unsigned long val, void *v, int nr_to_call, int *nr_calls)

    Call functions in an atomic notifier chain

    :param struct atomic_notifier_head \*nh:
        Pointer to head of the atomic notifier chain

    :param unsigned long val:
        Value passed unmodified to notifier function

    :param void \*v:
        Pointer passed unmodified to notifier function

    :param int nr_to_call:
        See the comment for notifier_call_chain.

    :param int \*nr_calls:
        See the comment for notifier_call_chain.

.. _`__atomic_notifier_call_chain.description`:

Description
-----------

Calls each function in a notifier chain in turn.  The functions
run in an atomic context, so they must not block.
This routine uses RCU to synchronize with changes to the chain.

If the return value of the notifier can be and'ed
with \ ``NOTIFY_STOP_MASK``\  then \ :c:func:`atomic_notifier_call_chain`\ 
will return immediately, with the return value of
the notifier function which halted execution.
Otherwise the return value is the return value
of the last notifier function called.

.. _`blocking_notifier_chain_register`:

blocking_notifier_chain_register
================================

.. c:function:: int blocking_notifier_chain_register(struct blocking_notifier_head *nh, struct notifier_block *n)

    Add notifier to a blocking notifier chain

    :param struct blocking_notifier_head \*nh:
        Pointer to head of the blocking notifier chain

    :param struct notifier_block \*n:
        New entry in notifier chain

.. _`blocking_notifier_chain_register.description`:

Description
-----------

Adds a notifier to a blocking notifier chain.
Must be called in process context.

Currently always returns zero.

.. _`blocking_notifier_chain_cond_register`:

blocking_notifier_chain_cond_register
=====================================

.. c:function:: int blocking_notifier_chain_cond_register(struct blocking_notifier_head *nh, struct notifier_block *n)

    Cond add notifier to a blocking notifier chain

    :param struct blocking_notifier_head \*nh:
        Pointer to head of the blocking notifier chain

    :param struct notifier_block \*n:
        New entry in notifier chain

.. _`blocking_notifier_chain_cond_register.description`:

Description
-----------

Adds a notifier to a blocking notifier chain, only if not already
present in the chain.
Must be called in process context.

Currently always returns zero.

.. _`blocking_notifier_chain_unregister`:

blocking_notifier_chain_unregister
==================================

.. c:function:: int blocking_notifier_chain_unregister(struct blocking_notifier_head *nh, struct notifier_block *n)

    Remove notifier from a blocking notifier chain

    :param struct blocking_notifier_head \*nh:
        Pointer to head of the blocking notifier chain

    :param struct notifier_block \*n:
        Entry to remove from notifier chain

.. _`blocking_notifier_chain_unregister.description`:

Description
-----------

Removes a notifier from a blocking notifier chain.
Must be called from process context.

Returns zero on success or \ ``-ENOENT``\  on failure.

.. _`__blocking_notifier_call_chain`:

\__blocking_notifier_call_chain
===============================

.. c:function:: int __blocking_notifier_call_chain(struct blocking_notifier_head *nh, unsigned long val, void *v, int nr_to_call, int *nr_calls)

    Call functions in a blocking notifier chain

    :param struct blocking_notifier_head \*nh:
        Pointer to head of the blocking notifier chain

    :param unsigned long val:
        Value passed unmodified to notifier function

    :param void \*v:
        Pointer passed unmodified to notifier function

    :param int nr_to_call:
        See comment for notifier_call_chain.

    :param int \*nr_calls:
        See comment for notifier_call_chain.

.. _`__blocking_notifier_call_chain.description`:

Description
-----------

Calls each function in a notifier chain in turn.  The functions
run in a process context, so they are allowed to block.

If the return value of the notifier can be and'ed
with \ ``NOTIFY_STOP_MASK``\  then \ :c:func:`blocking_notifier_call_chain`\ 
will return immediately, with the return value of
the notifier function which halted execution.
Otherwise the return value is the return value
of the last notifier function called.

.. _`raw_notifier_chain_register`:

raw_notifier_chain_register
===========================

.. c:function:: int raw_notifier_chain_register(struct raw_notifier_head *nh, struct notifier_block *n)

    Add notifier to a raw notifier chain

    :param struct raw_notifier_head \*nh:
        Pointer to head of the raw notifier chain

    :param struct notifier_block \*n:
        New entry in notifier chain

.. _`raw_notifier_chain_register.description`:

Description
-----------

Adds a notifier to a raw notifier chain.
All locking must be provided by the caller.

Currently always returns zero.

.. _`raw_notifier_chain_unregister`:

raw_notifier_chain_unregister
=============================

.. c:function:: int raw_notifier_chain_unregister(struct raw_notifier_head *nh, struct notifier_block *n)

    Remove notifier from a raw notifier chain

    :param struct raw_notifier_head \*nh:
        Pointer to head of the raw notifier chain

    :param struct notifier_block \*n:
        Entry to remove from notifier chain

.. _`raw_notifier_chain_unregister.description`:

Description
-----------

Removes a notifier from a raw notifier chain.
All locking must be provided by the caller.

Returns zero on success or \ ``-ENOENT``\  on failure.

.. _`__raw_notifier_call_chain`:

\__raw_notifier_call_chain
==========================

.. c:function:: int __raw_notifier_call_chain(struct raw_notifier_head *nh, unsigned long val, void *v, int nr_to_call, int *nr_calls)

    Call functions in a raw notifier chain

    :param struct raw_notifier_head \*nh:
        Pointer to head of the raw notifier chain

    :param unsigned long val:
        Value passed unmodified to notifier function

    :param void \*v:
        Pointer passed unmodified to notifier function

    :param int nr_to_call:
        See comment for notifier_call_chain.

    :param int \*nr_calls:
        See comment for notifier_call_chain

.. _`__raw_notifier_call_chain.description`:

Description
-----------

Calls each function in a notifier chain in turn.  The functions
run in an undefined context.
All locking must be provided by the caller.

If the return value of the notifier can be and'ed
with \ ``NOTIFY_STOP_MASK``\  then \ :c:func:`raw_notifier_call_chain`\ 
will return immediately, with the return value of
the notifier function which halted execution.
Otherwise the return value is the return value
of the last notifier function called.

.. _`srcu_notifier_chain_register`:

srcu_notifier_chain_register
============================

.. c:function:: int srcu_notifier_chain_register(struct srcu_notifier_head *nh, struct notifier_block *n)

    Add notifier to an SRCU notifier chain

    :param struct srcu_notifier_head \*nh:
        Pointer to head of the SRCU notifier chain

    :param struct notifier_block \*n:
        New entry in notifier chain

.. _`srcu_notifier_chain_register.description`:

Description
-----------

Adds a notifier to an SRCU notifier chain.
Must be called in process context.

Currently always returns zero.

.. _`srcu_notifier_chain_unregister`:

srcu_notifier_chain_unregister
==============================

.. c:function:: int srcu_notifier_chain_unregister(struct srcu_notifier_head *nh, struct notifier_block *n)

    Remove notifier from an SRCU notifier chain

    :param struct srcu_notifier_head \*nh:
        Pointer to head of the SRCU notifier chain

    :param struct notifier_block \*n:
        Entry to remove from notifier chain

.. _`srcu_notifier_chain_unregister.description`:

Description
-----------

Removes a notifier from an SRCU notifier chain.
Must be called from process context.

Returns zero on success or \ ``-ENOENT``\  on failure.

.. _`__srcu_notifier_call_chain`:

\__srcu_notifier_call_chain
===========================

.. c:function:: int __srcu_notifier_call_chain(struct srcu_notifier_head *nh, unsigned long val, void *v, int nr_to_call, int *nr_calls)

    Call functions in an SRCU notifier chain

    :param struct srcu_notifier_head \*nh:
        Pointer to head of the SRCU notifier chain

    :param unsigned long val:
        Value passed unmodified to notifier function

    :param void \*v:
        Pointer passed unmodified to notifier function

    :param int nr_to_call:
        See comment for notifier_call_chain.

    :param int \*nr_calls:
        See comment for notifier_call_chain

.. _`__srcu_notifier_call_chain.description`:

Description
-----------

Calls each function in a notifier chain in turn.  The functions
run in a process context, so they are allowed to block.

If the return value of the notifier can be and'ed
with \ ``NOTIFY_STOP_MASK``\  then \ :c:func:`srcu_notifier_call_chain`\ 
will return immediately, with the return value of
the notifier function which halted execution.
Otherwise the return value is the return value
of the last notifier function called.

.. _`srcu_init_notifier_head`:

srcu_init_notifier_head
=======================

.. c:function:: void srcu_init_notifier_head(struct srcu_notifier_head *nh)

    Initialize an SRCU notifier head

    :param struct srcu_notifier_head \*nh:
        Pointer to head of the srcu notifier chain

.. _`srcu_init_notifier_head.description`:

Description
-----------

Unlike other sorts of notifier heads, SRCU notifier heads require
dynamic initialization.  Be sure to call this routine before
calling any of the other SRCU notifier routines for this head.

If an SRCU notifier head is deallocated, it must first be cleaned
up by calling \ :c:func:`srcu_cleanup_notifier_head`\ .  Otherwise the head's
per-cpu data (used by the SRCU mechanism) will leak.

.. This file was automatic generated / don't edit.

