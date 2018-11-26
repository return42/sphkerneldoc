.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/logfile.c

.. _`ntfs_check_restart_page_header`:

ntfs_check_restart_page_header
==============================

.. c:function:: bool ntfs_check_restart_page_header(struct inode *vi, RESTART_PAGE_HEADER *rp, s64 pos)

    check the page header for consistency

    :param vi:
        \ ``$LogFile``\  inode to which the restart page header belongs
    :type vi: struct inode \*

    :param rp:
        restart page header to check
    :type rp: RESTART_PAGE_HEADER \*

    :param pos:
        position in \ ``vi``\  at which the restart page header resides
    :type pos: s64

.. _`ntfs_check_restart_page_header.description`:

Description
-----------

Check the restart page header \ ``rp``\  for consistency and return 'true' if it is
consistent and 'false' otherwise.

This function only needs NTFS_BLOCK_SIZE bytes in \ ``rp``\ , i.e. it does not
require the full restart page.

.. _`ntfs_check_restart_area`:

ntfs_check_restart_area
=======================

.. c:function:: bool ntfs_check_restart_area(struct inode *vi, RESTART_PAGE_HEADER *rp)

    check the restart area for consistency

    :param vi:
        \ ``$LogFile``\  inode to which the restart page belongs
    :type vi: struct inode \*

    :param rp:
        restart page whose restart area to check
    :type rp: RESTART_PAGE_HEADER \*

.. _`ntfs_check_restart_area.description`:

Description
-----------

Check the restart area of the restart page \ ``rp``\  for consistency and return
'true' if it is consistent and 'false' otherwise.

This function assumes that the restart page header has already been
consistency checked.

This function only needs NTFS_BLOCK_SIZE bytes in \ ``rp``\ , i.e. it does not
require the full restart page.

.. _`ntfs_check_log_client_array`:

ntfs_check_log_client_array
===========================

.. c:function:: bool ntfs_check_log_client_array(struct inode *vi, RESTART_PAGE_HEADER *rp)

    check the log client array for consistency

    :param vi:
        \ ``$LogFile``\  inode to which the restart page belongs
    :type vi: struct inode \*

    :param rp:
        restart page whose log client array to check
    :type rp: RESTART_PAGE_HEADER \*

.. _`ntfs_check_log_client_array.description`:

Description
-----------

Check the log client array of the restart page \ ``rp``\  for consistency and
return 'true' if it is consistent and 'false' otherwise.

This function assumes that the restart page header and the restart area have
already been consistency checked.

Unlike \ :c:func:`ntfs_check_restart_page_header`\  and \ :c:func:`ntfs_check_restart_area`\ , this
function needs \ ``rp->system_page_size``\  bytes in \ ``rp``\ , i.e. it requires the full
restart page and the page must be multi sector transfer deprotected.

.. _`ntfs_check_and_load_restart_page`:

ntfs_check_and_load_restart_page
================================

.. c:function:: int ntfs_check_and_load_restart_page(struct inode *vi, RESTART_PAGE_HEADER *rp, s64 pos, RESTART_PAGE_HEADER **wrp, LSN *lsn)

    check the restart page for consistency

    :param vi:
        \ ``$LogFile``\  inode to which the restart page belongs
    :type vi: struct inode \*

    :param rp:
        restart page to check
    :type rp: RESTART_PAGE_HEADER \*

    :param pos:
        position in \ ``vi``\  at which the restart page resides
    :type pos: s64

    :param wrp:
        [OUT] copy of the multi sector transfer deprotected restart page
    :type wrp: RESTART_PAGE_HEADER \*\*

    :param lsn:
        [OUT] set to the current logfile lsn on success
    :type lsn: LSN \*

.. _`ntfs_check_and_load_restart_page.description`:

Description
-----------

Check the restart page \ ``rp``\  for consistency and return 0 if it is consistent
and -errno otherwise.  The restart page may have been modified by chkdsk in
which case its magic is CHKD instead of RSTR.

This function only needs NTFS_BLOCK_SIZE bytes in \ ``rp``\ , i.e. it does not
require the full restart page.

If \ ``wrp``\  is not NULL, on success, \*@wrp will point to a buffer containing a
copy of the complete multi sector transfer deprotected page.  On failure,
\*@wrp is undefined.

Simillarly, if \ ``lsn``\  is not NULL, on success \*@lsn will be set to the current
logfile lsn according to this restart page.  On failure, \*@lsn is undefined.

.. _`ntfs_check_and_load_restart_page.the-following-error-codes-are-defined`:

The following error codes are defined
-------------------------------------

-EINVAL - The restart page is inconsistent.
-ENOMEM - Not enough memory to load the restart page.
-EIO    - Failed to reading from \ ``$LogFile``\ .

.. _`ntfs_check_logfile`:

ntfs_check_logfile
==================

.. c:function:: bool ntfs_check_logfile(struct inode *log_vi, RESTART_PAGE_HEADER **rp)

    check the journal for consistency

    :param log_vi:
        struct inode of loaded journal \ ``$LogFile``\  to check
    :type log_vi: struct inode \*

    :param rp:
        [OUT] on success this is a copy of the current restart page
    :type rp: RESTART_PAGE_HEADER \*\*

.. _`ntfs_check_logfile.description`:

Description
-----------

Check the \ ``$LogFile``\  journal for consistency and return 'true' if it is
consistent and 'false' if not.  On success, the current restart page is
returned in \*@rp.  Caller must call ntfs_free(\*@rp) when finished with it.

At present we only check the two restart pages and ignore the log record
pages.

Note that the MstProtected flag is not set on the \ ``$LogFile``\  inode and hence
when reading pages they are not deprotected.  This is because we do not know
if the \ ``$LogFile``\  was created on a system with a different page size to ours
yet and mst deprotection would fail if our page size is smaller.

.. _`ntfs_is_logfile_clean`:

ntfs_is_logfile_clean
=====================

.. c:function:: bool ntfs_is_logfile_clean(struct inode *log_vi, const RESTART_PAGE_HEADER *rp)

    check in the journal if the volume is clean

    :param log_vi:
        struct inode of loaded journal \ ``$LogFile``\  to check
    :type log_vi: struct inode \*

    :param rp:
        copy of the current restart page
    :type rp: const RESTART_PAGE_HEADER \*

.. _`ntfs_is_logfile_clean.description`:

Description
-----------

Analyze the \ ``$LogFile``\  journal and return 'true' if it indicates the volume was
shutdown cleanly and 'false' if not.

At present we only look at the two restart pages and ignore the log record
pages.  This is a little bit crude in that there will be a very small number
of cases where we think that a volume is dirty when in fact it is clean.
This should only affect volumes that have not been shutdown cleanly but did
not have any pending, non-check-pointed i/o, i.e. they were completely idle
at least for the five seconds preceding the unclean shutdown.

This function assumes that the \ ``$LogFile``\  journal has already been consistency
checked by a call to \ :c:func:`ntfs_check_logfile`\  and in particular if the \ ``$LogFile``\ 
is empty this function requires that \ :c:func:`NVolLogFileEmpty`\  is true otherwise an
empty volume will be reported as dirty.

.. _`ntfs_empty_logfile`:

ntfs_empty_logfile
==================

.. c:function:: bool ntfs_empty_logfile(struct inode *log_vi)

    empty the contents of the \ ``$LogFile``\  journal

    :param log_vi:
        struct inode of loaded journal \ ``$LogFile``\  to empty
    :type log_vi: struct inode \*

.. _`ntfs_empty_logfile.description`:

Description
-----------

Empty the contents of the \ ``$LogFile``\  journal \ ``log_vi``\  and return 'true' on
success and 'false' on error.

This function assumes that the \ ``$LogFile``\  journal has already been consistency
checked by a call to \ :c:func:`ntfs_check_logfile`\  and that \ :c:func:`ntfs_is_logfile_clean`\ 
has been used to ensure that the \ ``$LogFile``\  is clean.

.. This file was automatic generated / don't edit.

