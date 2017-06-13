.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sched/mm.h

.. _`mmgrab`:

mmgrab
======

.. c:function:: void mmgrab(struct mm_struct *mm)

    Pin a \ :c:type:`struct mm_struct <mm_struct>`\ .

    :param struct mm_struct \*mm:
        The \ :c:type:`struct mm_struct <mm_struct>`\  to pin.

.. _`mmgrab.description`:

Description
-----------

Make sure that \ ``mm``\  will not get freed even after the owning task
exits. This doesn't guarantee that the associated address space
will still exist later on and \ :c:func:`mmget_not_zero`\  has to be used before
accessing it.

This is a preferred way to to pin \ ``mm``\  for a longer/unbounded amount
of time.

Use \ :c:func:`mmdrop`\  to release the reference acquired by \ :c:func:`mmgrab`\ .

See also <Documentation/vm/active_mm.txt> for an in-depth explanation
of \ :c:type:`mm_struct.mm_count <mm_struct>`\  vs \ :c:type:`mm_struct.mm_users <mm_struct>`\ .

.. _`mmget`:

mmget
=====

.. c:function:: void mmget(struct mm_struct *mm)

    Pin the address space associated with a \ :c:type:`struct mm_struct <mm_struct>`\ .

    :param struct mm_struct \*mm:
        The address space to pin.

.. _`mmget.description`:

Description
-----------

Make sure that the address space of the given \ :c:type:`struct mm_struct <mm_struct>`\  doesn't
go away. This does not protect against parts of the address space being
modified or freed, however.

Never use this function to pin this address space for an
unbounded/indefinite amount of time.

Use \ :c:func:`mmput`\  to release the reference acquired by \ :c:func:`mmget`\ .

See also <Documentation/vm/active_mm.txt> for an in-depth explanation
of \ :c:type:`mm_struct.mm_count <mm_struct>`\  vs \ :c:type:`mm_struct.mm_users <mm_struct>`\ .

.. This file was automatic generated / don't edit.

