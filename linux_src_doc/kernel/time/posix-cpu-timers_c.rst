.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/posix-cpu-timers.c

.. _`task_cputime_zero`:

task_cputime_zero
=================

.. c:function:: int task_cputime_zero(const struct task_cputime *cputime)

    Check a task_cputime struct for all zero fields.

    :param cputime:
        The struct to compare.
    :type cputime: const struct task_cputime \*

.. _`task_cputime_zero.description`:

Description
-----------

Checks \ ``cputime``\  to see if all fields are zero.  Returns true if all fields
are zero, false if any field is nonzero.

.. _`task_cputime_expired`:

task_cputime_expired
====================

.. c:function:: int task_cputime_expired(const struct task_cputime *sample, const struct task_cputime *expires)

    Compare two task_cputime entities.

    :param sample:
        The task_cputime structure to be checked for expiration.
    :type sample: const struct task_cputime \*

    :param expires:
        Expiration times, against which \ ``sample``\  will be checked.
    :type expires: const struct task_cputime \*

.. _`task_cputime_expired.description`:

Description
-----------

Checks \ ``sample``\  against \ ``expires``\  to see if any field of \ ``sample``\  has expired.
Returns true if any field of the former is greater than the corresponding
field of the latter if the latter field is set.  Otherwise returns false.

.. _`fastpath_timer_check`:

fastpath_timer_check
====================

.. c:function:: int fastpath_timer_check(struct task_struct *tsk)

    POSIX CPU timers fast path.

    :param tsk:
        The task (thread) being checked.
    :type tsk: struct task_struct \*

.. _`fastpath_timer_check.description`:

Description
-----------

Check the task and thread group timers.  If both are zero (there are no
timers set) return false.  Otherwise snapshot the task and thread group
timers and compare them with the corresponding expiration times.  Return
true if a timer has expired, else return false.

.. This file was automatic generated / don't edit.

