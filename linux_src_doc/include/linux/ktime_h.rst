.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ktime.h

.. _`ktime_set`:

ktime_set
=========

.. c:function:: ktime_t ktime_set(const s64 secs, const unsigned long nsecs)

    Set a ktime_t variable from a seconds/nanoseconds value

    :param secs:
        seconds to set
    :type secs: const s64

    :param nsecs:
        nanoseconds to set
    :type nsecs: const unsigned long

.. _`ktime_set.return`:

Return
------

The ktime_t representation of the value.

.. _`ktime_compare`:

ktime_compare
=============

.. c:function:: int ktime_compare(const ktime_t cmp1, const ktime_t cmp2)

    Compares two ktime_t variables for less, greater or equal

    :param cmp1:
        comparable1
    :type cmp1: const ktime_t

    :param cmp2:
        comparable2
    :type cmp2: const ktime_t

.. _`ktime_compare.return`:

Return
------

...
  cmp1  < cmp2: return <0
  cmp1 == cmp2: return 0
  cmp1  > cmp2: return >0

.. _`ktime_after`:

ktime_after
===========

.. c:function:: bool ktime_after(const ktime_t cmp1, const ktime_t cmp2)

    Compare if a ktime_t value is bigger than another one.

    :param cmp1:
        comparable1
    :type cmp1: const ktime_t

    :param cmp2:
        comparable2
    :type cmp2: const ktime_t

.. _`ktime_after.return`:

Return
------

true if cmp1 happened after cmp2.

.. _`ktime_before`:

ktime_before
============

.. c:function:: bool ktime_before(const ktime_t cmp1, const ktime_t cmp2)

    Compare if a ktime_t value is smaller than another one.

    :param cmp1:
        comparable1
    :type cmp1: const ktime_t

    :param cmp2:
        comparable2
    :type cmp2: const ktime_t

.. _`ktime_before.return`:

Return
------

true if cmp1 happened before cmp2.

.. _`ktime_to_timespec_cond`:

ktime_to_timespec_cond
======================

.. c:function:: bool ktime_to_timespec_cond(const ktime_t kt, struct timespec *ts)

    convert a ktime_t variable to timespec format only if the variable contains data

    :param kt:
        the ktime_t variable to convert
    :type kt: const ktime_t

    :param ts:
        the timespec variable to store the result in
    :type ts: struct timespec \*

.. _`ktime_to_timespec_cond.return`:

Return
------

\ ``true``\  if there was a successful conversion, \ ``false``\  if kt was 0.

.. _`ktime_to_timespec64_cond`:

ktime_to_timespec64_cond
========================

.. c:function:: bool ktime_to_timespec64_cond(const ktime_t kt, struct timespec64 *ts)

    convert a ktime_t variable to timespec64 format only if the variable contains data

    :param kt:
        the ktime_t variable to convert
    :type kt: const ktime_t

    :param ts:
        the timespec variable to store the result in
    :type ts: struct timespec64 \*

.. _`ktime_to_timespec64_cond.return`:

Return
------

\ ``true``\  if there was a successful conversion, \ ``false``\  if kt was 0.

.. This file was automatic generated / don't edit.

