.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/writeback.h

.. _`wb_domain_size_changed`:

wb_domain_size_changed
======================

.. c:function:: void wb_domain_size_changed(struct wb_domain *dom)

    memory available to a wb_domain has changed

    :param dom:
        wb_domain of interest
    :type dom: struct wb_domain \*

.. _`wb_domain_size_changed.description`:

Description
-----------

This function should be called when the amount of memory available to
\ ``dom``\  has changed.  It resets \ ``dom``\ 's dirty limit parameters to prevent
the past values which don't match the current configuration from skewing
dirty throttling.  Without this, when memory size of a wb_domain is
greatly reduced, the dirty throttling logic may allow too many pages to
be dirtied leading to consecutive unnecessary OOMs and may get stuck in
that situation.

.. _`inode_attach_wb`:

inode_attach_wb
===============

.. c:function:: void inode_attach_wb(struct inode *inode, struct page *page)

    associate an inode with its wb

    :param inode:
        inode of interest
    :type inode: struct inode \*

    :param page:
        page being dirtied (may be NULL)
    :type page: struct page \*

.. _`inode_attach_wb.description`:

Description
-----------

If \ ``inode``\  doesn't have its wb, associate it with the wb matching the
memcg of \ ``page``\  or, if \ ``page``\  is NULL, \ ``current``\ .  May be called w/ or w/o
\ ``inode->i_lock``\ .

.. _`inode_detach_wb`:

inode_detach_wb
===============

.. c:function:: void inode_detach_wb(struct inode *inode)

    disassociate an inode from its wb

    :param inode:
        inode of interest
    :type inode: struct inode \*

.. _`inode_detach_wb.description`:

Description
-----------

\ ``inode``\  is being freed.  Detach from its wb.

.. _`wbc_attach_fdatawrite_inode`:

wbc_attach_fdatawrite_inode
===========================

.. c:function:: void wbc_attach_fdatawrite_inode(struct writeback_control *wbc, struct inode *inode)

    associate wbc and inode for fdatawrite

    :param wbc:
        writeback_control of interest
    :type wbc: struct writeback_control \*

    :param inode:
        target inode
    :type inode: struct inode \*

.. _`wbc_attach_fdatawrite_inode.description`:

Description
-----------

This function is to be used by \__filemap_fdatawrite_range(), which is an
alternative entry point into writeback code, and first ensures \ ``inode``\  is
associated with a bdi_writeback and attaches it to \ ``wbc``\ .

.. _`wbc_init_bio`:

wbc_init_bio
============

.. c:function:: void wbc_init_bio(struct writeback_control *wbc, struct bio *bio)

    writeback specific initializtion of bio

    :param wbc:
        writeback_control for the writeback in progress
    :type wbc: struct writeback_control \*

    :param bio:
        bio to be initialized
    :type bio: struct bio \*

.. _`wbc_init_bio.description`:

Description
-----------

\ ``bio``\  is a part of the writeback in progress controlled by \ ``wbc``\ .  Perform
writeback specific initialization.  This is used to apply the cgroup
writeback context.

.. This file was automatic generated / don't edit.

