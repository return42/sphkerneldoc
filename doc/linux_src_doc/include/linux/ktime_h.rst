.. -*- coding: utf-8; mode: rst -*-

=======
ktime.h
=======

.. _`ktime_set`:

ktime_set
=========

.. c:function:: ktime_t ktime_set (const s64 secs, const unsigned long nsecs)

    Set a ktime_t variable from a seconds/nanoseconds value

    :param const s64 secs:
        seconds to set

    :param const unsigned long nsecs:
        nanoseconds to set


.. _`ktime_set.description`:

Description
-----------

Return: The ktime_t representation of the value.


.. _`ktime_equal`:

ktime_equal
===========

.. c:function:: int ktime_equal (const ktime_t cmp1, const ktime_t cmp2)

    Compares two ktime_t variables to see if they are equal

    :param const ktime_t cmp1:
        comparable1

    :param const ktime_t cmp2:
        comparable2


.. _`ktime_equal.description`:

Description
-----------

Compare two ktime_t variables.

Return: 1 if equal.


.. _`ktime_compare`:

ktime_compare
=============

.. c:function:: int ktime_compare (const ktime_t cmp1, const ktime_t cmp2)

    Compares two ktime_t variables for less, greater or equal

    :param const ktime_t cmp1:
        comparable1

    :param const ktime_t cmp2:
        comparable2


.. _`ktime_compare.description`:

Description
-----------

Return: ...::

  cmp1  < cmp2: return <0
  cmp1 == cmp2: return 0
  cmp1  > cmp2: return >0


.. _`ktime_after`:

ktime_after
===========

.. c:function:: bool ktime_after (const ktime_t cmp1, const ktime_t cmp2)

    Compare if a ktime_t value is bigger than another one.

    :param const ktime_t cmp1:
        comparable1

    :param const ktime_t cmp2:
        comparable2


.. _`ktime_after.description`:

Description
-----------

Return: true if cmp1 happened after cmp2.


.. _`ktime_before`:

ktime_before
============

.. c:function:: bool ktime_before (const ktime_t cmp1, const ktime_t cmp2)

    Compare if a ktime_t value is smaller than another one.

    :param const ktime_t cmp1:
        comparable1

    :param const ktime_t cmp2:
        comparable2


.. _`ktime_before.description`:

Description
-----------

Return: true if cmp1 happened before cmp2.


.. _`ktime_to_timespec_cond`:

ktime_to_timespec_cond
======================

.. c:function:: bool ktime_to_timespec_cond (const ktime_t kt, struct timespec *ts)

    convert a ktime_t variable to timespec format only if the variable contains data

    :param const ktime_t kt:
        the ktime_t variable to convert

    :param struct timespec \*ts:
        the timespec variable to store the result in


.. _`ktime_to_timespec_cond.description`:

Description
-----------

Return: ``true`` if there was a successful conversion, ``false`` if kt was 0.


.. _`ktime_to_timespec64_cond`:

ktime_to_timespec64_cond
========================

.. c:function:: bool ktime_to_timespec64_cond (const ktime_t kt, struct timespec64 *ts)

    convert a ktime_t variable to timespec64 format only if the variable contains data

    :param const ktime_t kt:
        the ktime_t variable to convert

    :param struct timespec64 \*ts:
        the timespec variable to store the result in


.. _`ktime_to_timespec64_cond.description`:

Description
-----------

Return: ``true`` if there was a successful conversion, ``false`` if kt was 0.

