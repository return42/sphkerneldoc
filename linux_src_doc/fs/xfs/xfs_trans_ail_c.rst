.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/xfs/xfs_trans_ail.c

.. _`xfs_trans_ail_delete`:

xfs_trans_ail_delete
====================

.. c:function:: void xfs_trans_ail_delete(struct xfs_ail *ailp, struct xfs_log_item *lip, int shutdown_type)

    :param ailp:
        *undescribed*
    :type ailp: struct xfs_ail \*

    :param lip:
        *undescribed*
    :type lip: struct xfs_log_item \*

    :param shutdown_type:
        *undescribed*
    :type shutdown_type: int

.. _`xfs_trans_ail_delete.description`:

Description
-----------

\ ``xfs_trans_ail_delete_bulk``\  takes an array of log items that all need to
removed from the AIL. The caller is already holding the AIL lock, and done
all the checks necessary to ensure the items passed in via \ ``log_items``\  are
ready for deletion. This includes checking that the items are in the AIL.

For each log item to be removed, unlink it  from the AIL, clear the IN_AIL
flag from the item and reset the item's lsn to 0. If we remove the first
item in the AIL, update the log tail to match the new minimum LSN in the
AIL.

This function will not drop the AIL lock until all items are removed from
the AIL to minimise the amount of lock traffic on the AIL. This does not
greatly increase the AIL hold time, but does significantly reduce the amount
of traffic on the lock, especially during IO completion.

This function must be called with the AIL lock held.  The lock is dropped
before returning.

.. This file was automatic generated / don't edit.

