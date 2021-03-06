.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/backing-dev.h

.. _`writeback_in_progress`:

writeback_in_progress
=====================

.. c:function:: bool writeback_in_progress(struct bdi_writeback *wb)

    determine whether there is writeback in progress

    :param wb:
        bdi_writeback of interest
    :type wb: struct bdi_writeback \*

.. _`writeback_in_progress.description`:

Description
-----------

Determine whether there is writeback waiting to be handled against a
bdi_writeback.

.. _`inode_cgwb_enabled`:

inode_cgwb_enabled
==================

.. c:function:: bool inode_cgwb_enabled(struct inode *inode)

    test whether cgroup writeback is enabled on an inode

    :param inode:
        inode of interest
    :type inode: struct inode \*

.. _`inode_cgwb_enabled.description`:

Description
-----------

cgroup writeback requires support from both the bdi and filesystem.
Also, both memcg and iocg have to be on the default hierarchy.  Test
whether all conditions are met.

Note that the test result may change dynamically on the same inode
depending on how memcg and iocg are configured.

.. _`wb_find_current`:

wb_find_current
===============

.. c:function:: struct bdi_writeback *wb_find_current(struct backing_dev_info *bdi)

    find wb for \ ``current``\  on a bdi

    :param bdi:
        bdi of interest
    :type bdi: struct backing_dev_info \*

.. _`wb_find_current.description`:

Description
-----------

Find the wb of \ ``bdi``\  which matches both the memcg and blkcg of \ ``current``\ .
Must be called under \ :c:func:`rcu_read_lock`\  which protects the returend wb.
NULL if not found.

.. _`wb_get_create_current`:

wb_get_create_current
=====================

.. c:function:: struct bdi_writeback *wb_get_create_current(struct backing_dev_info *bdi, gfp_t gfp)

    get or create wb for \ ``current``\  on a bdi

    :param bdi:
        bdi of interest
    :type bdi: struct backing_dev_info \*

    :param gfp:
        allocation mask
    :type gfp: gfp_t

.. _`wb_get_create_current.description`:

Description
-----------

Equivalent to \ :c:func:`wb_get_create`\  on \ ``current``\ 's memcg.  This function is
called from a relatively hot path and optimizes the common cases using
\ :c:func:`wb_find_current`\ .

.. _`inode_to_wb_is_valid`:

inode_to_wb_is_valid
====================

.. c:function:: bool inode_to_wb_is_valid(struct inode *inode)

    test whether an inode has a wb associated

    :param inode:
        inode of interest
    :type inode: struct inode \*

.. _`inode_to_wb_is_valid.description`:

Description
-----------

Returns \ ``true``\  if \ ``inode``\  has a wb associated.  May be called without any
locking.

.. _`inode_to_wb`:

inode_to_wb
===========

.. c:function:: struct bdi_writeback *inode_to_wb(const struct inode *inode)

    determine the wb of an inode

    :param inode:
        inode of interest
    :type inode: const struct inode \*

.. _`inode_to_wb.description`:

Description
-----------

Returns the wb \ ``inode``\  is currently associated with.  The caller must be
holding either \ ``inode->i_lock``\ , the i_pages lock, or the
associated wb's list_lock.

.. _`unlocked_inode_to_wb_begin`:

unlocked_inode_to_wb_begin
==========================

.. c:function:: struct bdi_writeback *unlocked_inode_to_wb_begin(struct inode *inode, struct wb_lock_cookie *cookie)

    begin unlocked inode wb access transaction

    :param inode:
        target inode
    :type inode: struct inode \*

    :param cookie:
        output param, to be passed to the end function
    :type cookie: struct wb_lock_cookie \*

.. _`unlocked_inode_to_wb_begin.description`:

Description
-----------

The caller wants to access the wb associated with \ ``inode``\  but isn't
holding inode->i_lock, the i_pages lock or wb->list_lock.  This
function determines the wb associated with \ ``inode``\  and ensures that the
association doesn't change until the transaction is finished with
\ :c:func:`unlocked_inode_to_wb_end`\ .

The caller must call \ :c:func:`unlocked_inode_to_wb_end`\  with \*@cookie afterwards and
can't sleep during the transaction.  IRQs may or may not be disabled on
return.

.. _`unlocked_inode_to_wb_end`:

unlocked_inode_to_wb_end
========================

.. c:function:: void unlocked_inode_to_wb_end(struct inode *inode, struct wb_lock_cookie *cookie)

    end inode wb access transaction

    :param inode:
        target inode
    :type inode: struct inode \*

    :param cookie:
        \ ``cookie``\  from \ :c:func:`unlocked_inode_to_wb_begin`\ 
    :type cookie: struct wb_lock_cookie \*

.. This file was automatic generated / don't edit.

