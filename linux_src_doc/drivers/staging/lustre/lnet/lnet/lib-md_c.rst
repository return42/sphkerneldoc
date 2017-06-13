.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/lnet/lib-md.c

.. _`lnetmdattach`:

LNetMDAttach
============

.. c:function:: int LNetMDAttach(struct lnet_handle_me meh, struct lnet_md umd, enum lnet_unlink unlink, struct lnet_handle_md *handle)

    :param struct lnet_handle_me meh:
        *undescribed*

    :param struct lnet_md umd:
        *undescribed*

    :param enum lnet_unlink unlink:
        *undescribed*

    :param struct lnet_handle_md \*handle:
        *undescribed*

.. _`lnetmdattach.description`:

Description
-----------

\param meh A handle for a ME to associate the new MD with.
\param umd Provides initial values for the user-visible parts of a MD.
Other than its use for initialization, there is no linkage between this
structure and the MD maintained by the LNet.
\param unlink A flag to indicate whether the MD is automatically unlinked
when it becomes inactive, either because the operation threshold drops to
zero or because the available memory becomes less than \a umd.max_size.
(Note that the check for unlinking a MD only occurs after the completion
of a successful operation on the MD.) The value LNET_UNLINK enables auto
unlinking; the value LNET_RETAIN disables it.
\param handle On successful returns, a handle to the newly created MD is
saved here. This handle can be used later in \ :c:func:`LNetMDUnlink`\ .

\retval 0       On success.
\retval -EINVAL If \a umd is not valid.
\retval -ENOMEM If new MD cannot be allocated.
\retval -ENOENT Either \a meh or \a umd.eq_handle does not point to a
valid object. Note that it's OK to supply a NULL \a umd.eq_handle by
calling \ :c:func:`LNetInvalidateHandle`\  on it.
\retval -EBUSY  If the ME pointed to by \a meh is already associated with
a MD.

.. _`lnetmdbind`:

LNetMDBind
==========

.. c:function:: int LNetMDBind(struct lnet_md umd, enum lnet_unlink unlink, struct lnet_handle_md *handle)

    a MD that is not associated with a ME. Such MDs are usually used in \ :c:func:`LNetPut`\  and \ :c:func:`LNetGet`\  operations.

    :param struct lnet_md umd:
        *undescribed*

    :param enum lnet_unlink unlink:
        *undescribed*

    :param struct lnet_handle_md \*handle:
        *undescribed*

.. _`lnetmdbind.description`:

Description
-----------

\param umd,unlink See the discussion for \ :c:func:`LNetMDAttach`\ .
\param handle On successful returns, a handle to the newly created MD is
saved here. This handle can be used later in \ :c:func:`LNetMDUnlink`\ , \ :c:func:`LNetPut`\ ,
and \ :c:func:`LNetGet`\  operations.

\retval 0       On success.
\retval -EINVAL If \a umd is not valid.
\retval -ENOMEM If new MD cannot be allocated.
\retval -ENOENT \a umd.eq_handle does not point to a valid EQ. Note that
it's OK to supply a NULL \a umd.eq_handle by calling
\ :c:func:`LNetInvalidateHandle`\  on it.

.. _`lnetmdunlink`:

LNetMDUnlink
============

.. c:function:: int LNetMDUnlink(struct lnet_handle_md mdh)

    the internal resources associated with it. As a result, active messages associated with the MD may get aborted.

    :param struct lnet_handle_md mdh:
        *undescribed*

.. _`lnetmdunlink.description`:

Description
-----------

This function does not free the memory region associated with the MD;
i.e., the memory the user allocated for this MD. If the ME associated with
this MD is not NULL and was created with auto unlink enabled, the ME is
unlinked as well (see \ :c:func:`LNetMEAttach`\ ).

Explicitly unlinking a MD via this function call has the same behavior as
a MD that has been automatically unlinked, except that no LNET_EVENT_UNLINK
is generated in the latter case.

.. _`lnetmdunlink.an-unlinked-event-can-be-reported-in-two-ways`:

An unlinked event can be reported in two ways
---------------------------------------------

- If there's no pending operations on the MD, it's unlinked immediately
and an LNET_EVENT_UNLINK event is logged before this function returns.
- Otherwise, the MD is only marked for deletion when this function
returns, and the unlinked event will be piggybacked on the event of
the completion of the last operation by setting the unlinked field of
the event. No dedicated LNET_EVENT_UNLINK event is generated.

Note that in both cases the unlinked field of the event is always set; no
more event will happen on the MD after such an event is logged.

\param mdh A handle for the MD to be unlinked.

\retval 0       On success.
\retval -ENOENT If \a mdh does not point to a valid MD object.

.. This file was automatic generated / don't edit.

