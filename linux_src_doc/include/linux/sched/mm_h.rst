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

See also <Documentation/vm/active_mm.rst> for an in-depth explanation
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

See also <Documentation/vm/active_mm.rst> for an in-depth explanation
of \ :c:type:`mm_struct.mm_count <mm_struct>`\  vs \ :c:type:`mm_struct.mm_users <mm_struct>`\ .

.. _`memalloc_noio_save`:

memalloc_noio_save
==================

.. c:function:: unsigned int memalloc_noio_save( void)

    Marks implicit GFP_NOIO allocation scope.

    :param  void:
        no arguments

.. _`memalloc_noio_save.description`:

Description
-----------

This functions marks the beginning of the GFP_NOIO allocation scope.
All further allocations will implicitly drop __GFP_IO flag and so
they are safe for the IO critical section from the allocation recursion
point of view. Use memalloc_noio_restore to end the scope with flags
returned by this function.

This function is safe to be used from any context.

.. _`memalloc_noio_restore`:

memalloc_noio_restore
=====================

.. c:function:: void memalloc_noio_restore(unsigned int flags)

    Ends the implicit GFP_NOIO scope.

    :param unsigned int flags:
        Flags to restore.

.. _`memalloc_noio_restore.description`:

Description
-----------

Ends the implicit GFP_NOIO scope started by memalloc_noio_save function.
Always make sure that that the given flags is the return value from the
pairing memalloc_noio_save call.

.. _`memalloc_nofs_save`:

memalloc_nofs_save
==================

.. c:function:: unsigned int memalloc_nofs_save( void)

    Marks implicit GFP_NOFS allocation scope.

    :param  void:
        no arguments

.. _`memalloc_nofs_save.description`:

Description
-----------

This functions marks the beginning of the GFP_NOFS allocation scope.
All further allocations will implicitly drop __GFP_FS flag and so
they are safe for the FS critical section from the allocation recursion
point of view. Use memalloc_nofs_restore to end the scope with flags
returned by this function.

This function is safe to be used from any context.

.. _`memalloc_nofs_restore`:

memalloc_nofs_restore
=====================

.. c:function:: void memalloc_nofs_restore(unsigned int flags)

    Ends the implicit GFP_NOFS scope.

    :param unsigned int flags:
        Flags to restore.

.. _`memalloc_nofs_restore.description`:

Description
-----------

Ends the implicit GFP_NOFS scope started by memalloc_nofs_save function.
Always make sure that that the given flags is the return value from the
pairing memalloc_nofs_save call.

.. This file was automatic generated / don't edit.

