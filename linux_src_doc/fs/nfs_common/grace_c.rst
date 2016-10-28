.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs_common/grace.c

.. _`locks_start_grace`:

locks_start_grace
=================

.. c:function:: void locks_start_grace(struct net *net, struct lock_manager *lm)

    :param struct net \*net:
        net namespace that this lock manager belongs to

    :param struct lock_manager \*lm:
        who this grace period is for

.. _`locks_start_grace.description`:

Description
-----------

A grace period is a period during which locks should not be given
out.  Currently grace periods are only enforced by the two lock
managers (lockd and nfsd), using the \ :c:func:`locks_in_grace`\  function to
check when they are in a grace period.

This function is called to start a grace period.

.. _`locks_end_grace`:

locks_end_grace
===============

.. c:function:: void locks_end_grace(struct lock_manager *lm)

    :param struct lock_manager \*lm:
        who this grace period is for

.. _`locks_end_grace.description`:

Description
-----------

Call this function to state that the given lock manager is ready to
resume regular locking.  The grace period will not end until all lock
managers that called \ :c:func:`locks_start_grace`\  also call \ :c:func:`locks_end_grace`\ .
Note that callers count on it being safe to call this more than once,
and the second call should be a no-op.

.. _`__state_in_grace`:

__state_in_grace
================

.. c:function:: int __state_in_grace(struct net *net, bool open)

    :param struct net \*net:
        *undescribed*

    :param bool open:
        *undescribed*

.. _`__state_in_grace.description`:

Description
-----------

Lock managers call this function to determine when it is OK for them
to answer ordinary lock requests, and when they should accept only
lock reclaims.

.. This file was automatic generated / don't edit.

