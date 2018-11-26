.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/file.c

.. _`release_new_page_budget`:

release_new_page_budget
=======================

.. c:function:: void release_new_page_budget(struct ubifs_info *c)

    release budget of a new page.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`release_new_page_budget.description`:

Description
-----------

This is a helper function which releases budget corresponding to the budget
of one new page of data.

.. _`release_existing_page_budget`:

release_existing_page_budget
============================

.. c:function:: void release_existing_page_budget(struct ubifs_info *c)

    release budget of an existing page.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`release_existing_page_budget.description`:

Description
-----------

This is a helper function which releases budget corresponding to the budget
of changing one one page of data which already exists on the flash media.

.. _`allocate_budget`:

allocate_budget
===============

.. c:function:: int allocate_budget(struct ubifs_info *c, struct page *page, struct ubifs_inode *ui, int appending)

    allocate budget for 'ubifs_write_begin()'.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param page:
        page to allocate budget for
    :type page: struct page \*

    :param ui:
        UBIFS inode object the page belongs to
    :type ui: struct ubifs_inode \*

    :param appending:
        non-zero if the page is appended
    :type appending: int

.. _`allocate_budget.description`:

Description
-----------

This is a helper function for 'ubifs_write_begin()' which allocates budget
for the operation. The budget is allocated differently depending on whether
this is appending, whether the page is dirty or not, and so on. This
function leaves the \ ``ui->ui_mutex``\  locked in case of appending. Returns zero
in case of success and \ ``-ENOSPC``\  in case of failure.

.. _`cancel_budget`:

cancel_budget
=============

.. c:function:: void cancel_budget(struct ubifs_info *c, struct page *page, struct ubifs_inode *ui, int appending)

    cancel budget.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param page:
        page to cancel budget for
    :type page: struct page \*

    :param ui:
        UBIFS inode object the page belongs to
    :type ui: struct ubifs_inode \*

    :param appending:
        non-zero if the page is appended
    :type appending: int

.. _`cancel_budget.description`:

Description
-----------

This is a helper function for a page write operation. It unlocks the
\ ``ui->ui_mutex``\  in case of appending.

.. _`populate_page`:

populate_page
=============

.. c:function:: int populate_page(struct ubifs_info *c, struct page *page, struct bu_info *bu, int *n)

    copy data nodes into a page for bulk-read.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param page:
        page
    :type page: struct page \*

    :param bu:
        bulk-read information
    :type bu: struct bu_info \*

    :param n:
        next zbranch slot
    :type n: int \*

.. _`populate_page.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_do_bulk_read`:

ubifs_do_bulk_read
==================

.. c:function:: int ubifs_do_bulk_read(struct ubifs_info *c, struct bu_info *bu, struct page *page1)

    do bulk-read.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param bu:
        bulk-read information
    :type bu: struct bu_info \*

    :param page1:
        first page to read
    :type page1: struct page \*

.. _`ubifs_do_bulk_read.description`:

Description
-----------

This function returns \ ``1``\  if the bulk-read is done, otherwise \ ``0``\  is returned.

.. _`ubifs_bulk_read`:

ubifs_bulk_read
===============

.. c:function:: int ubifs_bulk_read(struct page *page)

    determine whether to bulk-read and, if so, do it.

    :param page:
        page from which to start bulk-read.
    :type page: struct page \*

.. _`ubifs_bulk_read.description`:

Description
-----------

Some flash media are capable of reading sequentially at faster rates. UBIFS
bulk-read facility is designed to take advantage of that, by reading in one
go consecutive data nodes that are also located consecutively in the same
LEB. This function returns \ ``1``\  if a bulk-read is done and \ ``0``\  otherwise.

.. _`do_attr_changes`:

do_attr_changes
===============

.. c:function:: void do_attr_changes(struct inode *inode, const struct iattr *attr)

    change inode attributes.

    :param inode:
        inode to change attributes for
    :type inode: struct inode \*

    :param attr:
        describes attributes to change
    :type attr: const struct iattr \*

.. _`do_truncation`:

do_truncation
=============

.. c:function:: int do_truncation(struct ubifs_info *c, struct inode *inode, const struct iattr *attr)

    truncate an inode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        inode to truncate
    :type inode: struct inode \*

    :param attr:
        inode attribute changes description
    :type attr: const struct iattr \*

.. _`do_truncation.description`:

Description
-----------

This function implements VFS '->setattr()' call when the inode is truncated
to a smaller size. Returns zero in case of success and a negative error code
in case of failure.

.. _`do_setattr`:

do_setattr
==========

.. c:function:: int do_setattr(struct ubifs_info *c, struct inode *inode, const struct iattr *attr)

    change inode attributes.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        inode to change attributes for
    :type inode: struct inode \*

    :param attr:
        inode attribute changes description
    :type attr: const struct iattr \*

.. _`do_setattr.description`:

Description
-----------

This function implements VFS '->setattr()' call for all cases except
truncations to smaller size. Returns zero in case of success and a negative
error code in case of failure.

.. _`mctime_update_needed`:

mctime_update_needed
====================

.. c:function:: int mctime_update_needed(const struct inode *inode, const struct timespec64 *now)

    check if mtime or ctime update is needed.

    :param inode:
        the inode to do the check for
    :type inode: const struct inode \*

    :param now:
        current time
    :type now: const struct timespec64 \*

.. _`mctime_update_needed.description`:

Description
-----------

This helper function checks if the inode mtime/ctime should be updated or
not. If current values of the time-stamps are within the UBIFS inode time
granularity, they are not updated. This is an optimization.

.. _`ubifs_update_time`:

ubifs_update_time
=================

.. c:function:: int ubifs_update_time(struct inode *inode, struct timespec64 *time, int flags)

    update time of inode.

    :param inode:
        inode to update
    :type inode: struct inode \*

    :param time:
        *undescribed*
    :type time: struct timespec64 \*

    :param flags:
        *undescribed*
    :type flags: int

.. _`ubifs_update_time.description`:

Description
-----------

This function updates time of the inode.

.. _`update_mctime`:

update_mctime
=============

.. c:function:: int update_mctime(struct inode *inode)

    update mtime and ctime of an inode.

    :param inode:
        inode to update
    :type inode: struct inode \*

.. _`update_mctime.description`:

Description
-----------

This function updates mtime and ctime of the inode if it is not equivalent to
current time. Returns zero in case of success and a negative error code in
case of failure.

.. This file was automatic generated / don't edit.

