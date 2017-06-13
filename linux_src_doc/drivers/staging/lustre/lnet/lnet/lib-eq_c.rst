.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/lnet/lib-eq.c

.. _`lneteqalloc`:

LNetEQAlloc
===========

.. c:function:: int LNetEQAlloc(unsigned int count, lnet_eq_handler_t callback, struct lnet_handle_eq *handle)

    :param unsigned int count:
        *undescribed*

    :param lnet_eq_handler_t callback:
        *undescribed*

    :param struct lnet_handle_eq \*handle:
        *undescribed*

.. _`lneteqalloc.description`:

Description
-----------

The event queue is circular and older events will be overwritten by new
ones if they are not removed in time by the user using the functions
\ :c:func:`LNetEQGet`\ , \ :c:func:`LNetEQWait`\ , or \ :c:func:`LNetEQPoll`\ . It is up to the user to
determine the appropriate size of the event queue to prevent this loss
of events. Note that when EQ handler is specified in \a callback, no
event loss can happen, since the handler is run for each event deposited
into the EQ.

\param count The number of events to be stored in the event queue. It
will be rounded up to the next power of two.
\param callback A handler function that runs when an event is deposited
into the EQ. The constant value LNET_EQ_HANDLER_NONE can be used to
indicate that no event handler is desired.
\param handle On successful return, this location will hold a handle for
the newly created EQ.

\retval 0       On success.
\retval -EINVAL If an parameter is not valid.
\retval -ENOMEM If memory for the EQ can't be allocated.

\see lnet_eq_handler_t for the discussion on EQ handler semantics.

.. _`lneteqfree`:

LNetEQFree
==========

.. c:function:: int LNetEQFree(struct lnet_handle_eq eqh)

    otherwise do nothing and it's up to the user to try again.

    :param struct lnet_handle_eq eqh:
        *undescribed*

.. _`lneteqfree.description`:

Description
-----------

\param eqh A handle for the event queue to be released.

\retval 0 If the EQ is not in use and freed.
\retval -ENOENT If \a eqh does not point to a valid EQ.
\retval -EBUSY  If the EQ is still in use by some MDs.

.. _`lnet_eq_wait_locked`:

lnet_eq_wait_locked
===================

.. c:function:: int lnet_eq_wait_locked(int *timeout_ms)

    If an event handler is associated with the EQ, the handler will run before this function returns successfully. The event is removed from the queue.

    :param int \*timeout_ms:
        *undescribed*

.. _`lnet_eq_wait_locked.description`:

Description
-----------

\param eventq A handle for the event queue.
\param event On successful return (1 or -EOVERFLOW), this location will
hold the next event in the EQ.

\retval 0      No pending event in the EQ.
\retval 1      Indicates success.
\retval -ENOENT    If \a eventq does not point to a valid EQ.
\retval -EOVERFLOW Indicates success (i.e., an event is returned) and that
at least one event between this event and the last event obtained from the
EQ has been dropped due to limited space in the EQ.

.. _`lneteqpoll`:

LNetEQPoll
==========

.. c:function:: int LNetEQPoll(struct lnet_handle_eq *eventqs, int neq, int timeout_ms, struct lnet_event *event, int *which)

    timeout happens.

    :param struct lnet_handle_eq \*eventqs:
        *undescribed*

    :param int neq:
        *undescribed*

    :param int timeout_ms:
        *undescribed*

    :param struct lnet_event \*event:
        *undescribed*

    :param int \*which:
        *undescribed*

.. _`lneteqpoll.description`:

Description
-----------

If an event handler is associated with the EQ, the handler will run before
this function returns successfully, in which case the corresponding event
is consumed.

\ :c:func:`LNetEQPoll`\  provides a timeout to allow applications to poll, block for a
fixed period, or block indefinitely.

\param eventqs,neq An array of EQ handles, and size of the array.
\param timeout_ms Time in milliseconds to wait for an event to occur on
one of the EQs. The constant LNET_TIME_FOREVER can be used to indicate an
infinite timeout.
\param event,which On successful return (1 or -EOVERFLOW), \a event will
hold the next event in the EQs, and \a which will contain the index of the
EQ from which the event was taken.

\retval 0      No pending event in the EQs after timeout.
\retval 1      Indicates success.
\retval -EOVERFLOW Indicates success (i.e., an event is returned) and that
at least one event between this event and the last event obtained from the
EQ indicated by \a which has been dropped due to limited space in the EQ.
\retval -ENOENT    If there's an invalid handle in \a eventqs.

.. This file was automatic generated / don't edit.

