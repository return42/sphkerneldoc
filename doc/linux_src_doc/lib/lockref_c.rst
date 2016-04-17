.. -*- coding: utf-8; mode: rst -*-

=========
lockref.c
=========


.. _`lockref_get`:

lockref_get
===========

.. c:function:: void lockref_get (struct lockref *lockref)

    Increments reference count unconditionally

    :param struct lockref \*lockref:
        pointer to lockref structure



.. _`lockref_get.description`:

Description
-----------

This operation is only valid if you already hold a reference
to the object, so you know the count cannot be zero.



.. _`lockref_get_not_zero`:

lockref_get_not_zero
====================

.. c:function:: int lockref_get_not_zero (struct lockref *lockref)

    Increments count unless the count is 0 or dead

    :param struct lockref \*lockref:
        pointer to lockref structure



.. _`lockref_get_not_zero.return`:

Return
------

1 if count updated successfully or 0 if count was zero



.. _`lockref_get_or_lock`:

lockref_get_or_lock
===================

.. c:function:: int lockref_get_or_lock (struct lockref *lockref)

    Increments count unless the count is 0 or dead

    :param struct lockref \*lockref:
        pointer to lockref structure



.. _`lockref_get_or_lock.return`:

Return
------

1 if count updated successfully or 0 if count was zero
and we got the lock instead.



.. _`lockref_put_return`:

lockref_put_return
==================

.. c:function:: int lockref_put_return (struct lockref *lockref)

    Decrement reference count if possible

    :param struct lockref \*lockref:
        pointer to lockref structure



.. _`lockref_put_return.description`:

Description
-----------

Decrement the reference count and return the new value.
If the lockref was dead or locked, return an error.



.. _`lockref_put_or_lock`:

lockref_put_or_lock
===================

.. c:function:: int lockref_put_or_lock (struct lockref *lockref)

    decrements count unless count <= 1 before decrement

    :param struct lockref \*lockref:
        pointer to lockref structure



.. _`lockref_put_or_lock.return`:

Return
------

1 if count updated successfully or 0 if count <= 1 and lock taken



.. _`lockref_mark_dead`:

lockref_mark_dead
=================

.. c:function:: void lockref_mark_dead (struct lockref *lockref)

    mark lockref dead

    :param struct lockref \*lockref:
        pointer to lockref structure



.. _`lockref_get_not_dead`:

lockref_get_not_dead
====================

.. c:function:: int lockref_get_not_dead (struct lockref *lockref)

    Increments count unless the ref is dead

    :param struct lockref \*lockref:
        pointer to lockref structure



.. _`lockref_get_not_dead.return`:

Return
------

1 if count updated successfully or 0 if lockref was dead

