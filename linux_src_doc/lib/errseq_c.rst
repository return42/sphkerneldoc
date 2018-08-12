.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/errseq.c

.. _`errseq_set`:

errseq_set
==========

.. c:function:: errseq_t errseq_set(errseq_t *eseq, int err)

    set a errseq_t for later reporting

    :param errseq_t \*eseq:
        errseq_t field that should be set

    :param int err:
        error to set (must be between -1 and -MAX_ERRNO)

.. _`errseq_set.description`:

Description
-----------

This function sets the error in \ ``eseq``\ , and increments the sequence counter
if the last sequence was sampled at some point in the past.

Any error set will always overwrite an existing error.

.. _`errseq_set.return`:

Return
------

The previous value, primarily for debugging purposes. The
return value should not be used as a previously sampled value in later
calls as it will not have the SEEN flag set.

.. _`errseq_sample`:

errseq_sample
=============

.. c:function:: errseq_t errseq_sample(errseq_t *eseq)

    Grab current errseq_t value.

    :param errseq_t \*eseq:
        Pointer to errseq_t to be sampled.

.. _`errseq_sample.description`:

Description
-----------

This function allows callers to initialise their errseq_t variable.
If the error has been "seen", new callers will not see an old error.
If there is an unseen error in \ ``eseq``\ , the caller of this function will
see it the next time it checks for an error.

.. _`errseq_sample.context`:

Context
-------

Any context.

.. _`errseq_sample.return`:

Return
------

The current errseq value.

.. _`errseq_check`:

errseq_check
============

.. c:function:: int errseq_check(errseq_t *eseq, errseq_t since)

    Has an error occurred since a particular sample point?

    :param errseq_t \*eseq:
        Pointer to errseq_t value to be checked.

    :param errseq_t since:
        Previously-sampled errseq_t from which to check.

.. _`errseq_check.description`:

Description
-----------

Grab the value that eseq points to, and see if it has changed \ ``since``\ 
the given value was sampled. The \ ``since``\  value is not advanced, so there
is no need to mark the value as seen.

.. _`errseq_check.return`:

Return
------

The latest error set in the errseq_t or 0 if it hasn't changed.

.. _`errseq_check_and_advance`:

errseq_check_and_advance
========================

.. c:function:: int errseq_check_and_advance(errseq_t *eseq, errseq_t *since)

    Check an errseq_t and advance to current value.

    :param errseq_t \*eseq:
        Pointer to value being checked and reported.

    :param errseq_t \*since:
        Pointer to previously-sampled errseq_t to check against and advance.

.. _`errseq_check_and_advance.description`:

Description
-----------

Grab the eseq value, and see whether it matches the value that \ ``since``\ 
points to. If it does, then just return 0.

If it doesn't, then the value has changed. Set the "seen" flag, and try to
swap it into place as the new eseq value. Then, set that value as the new
"since" value, and return whatever the error portion is set to.

Note that no locking is provided here for concurrent updates to the "since"
value. The caller must provide that if necessary. Because of this, callers
may want to do a lockless errseq_check before taking the lock and calling
this.

.. _`errseq_check_and_advance.return`:

Return
------

Negative errno if one has been stored, or 0 if no new error has
occurred.

.. This file was automatic generated / don't edit.

