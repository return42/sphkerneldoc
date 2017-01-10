.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/file.c

.. _`ll_prepare_close`:

ll_prepare_close
================

.. c:function:: void ll_prepare_close(struct inode *inode, struct md_op_data *op_data, struct obd_client_handle *och)

    :param struct inode \*inode:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param struct obd_client_handle \*och:
        *undescribed*

.. _`ll_close_inode_openhandle`:

ll_close_inode_openhandle
=========================

.. c:function:: int ll_close_inode_openhandle(struct obd_export *md_exp, struct obd_client_handle *och, struct inode *inode, enum mds_op_bias bias, void *data)

    The meaning of "data" depends on the value of "bias".

    :param struct obd_export \*md_exp:
        *undescribed*

    :param struct obd_client_handle \*och:
        *undescribed*

    :param struct inode \*inode:
        *undescribed*

    :param enum mds_op_bias bias:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ll_close_inode_openhandle.description`:

Description
-----------

If \a bias is MDS_HSM_RELEASE then \a data is a pointer to the data version.
If \a bias is MDS_CLOSE_LAYOUT_SWAP then \a data is a pointer to the inode to
swap layouts with.

.. _`ll_lease_open`:

ll_lease_open
=============

.. c:function:: struct obd_client_handle *ll_lease_open(struct inode *inode, struct file *file, fmode_t fmode, __u64 open_flags)

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

    :param fmode_t fmode:
        *undescribed*

    :param __u64 open_flags:
        *undescribed*

.. _`ll_check_swap_layouts_validity`:

ll_check_swap_layouts_validity
==============================

.. c:function:: int ll_check_swap_layouts_validity(struct inode *inode1, struct inode *inode2)

    :param struct inode \*inode1:
        *undescribed*

    :param struct inode \*inode2:
        *undescribed*

.. _`ll_check_swap_layouts_validity.description`:

Description
-----------

\param[in] inode1  First inode to check
\param[in] inode2  Second inode to check

\retval 0 on success, layout swap can be performed between both inodes
\retval negative error code if requirements are not met

.. _`ll_lease_close`:

ll_lease_close
==============

.. c:function:: int ll_lease_close(struct obd_client_handle *och, struct inode *inode, bool *lease_broken)

    It will check if the lease has ever broken.

    :param struct obd_client_handle \*och:
        *undescribed*

    :param struct inode \*inode:
        *undescribed*

    :param bool \*lease_broken:
        *undescribed*

.. _`ll_release_openhandle`:

ll_release_openhandle
=====================

.. c:function:: int ll_release_openhandle(struct inode *inode, struct lookup_intent *it)

    :param struct inode \*inode:
        *undescribed*

    :param struct lookup_intent \*it:
        *undescribed*

.. _`ll_release_openhandle.description`:

Description
-----------

\param inode  [in]     inode in question
\param it     [in,out] intent which contains open info and result

\retval 0     success
\retval <0    failure

.. _`ll_do_fiemap`:

ll_do_fiemap
============

.. c:function:: int ll_do_fiemap(struct inode *inode, struct fiemap *fiemap, size_t num_bytes)

    Make the FIEMAP get_info call and returns the result.

    :param struct inode \*inode:
        *undescribed*

    :param struct fiemap \*fiemap:
        *undescribed*

    :param size_t num_bytes:
        *undescribed*

.. _`ll_do_fiemap.description`:

Description
-----------

\param fiemap        kernel buffer to hold extens
\param num_bytes     kernel buffer size

.. _`cl_sync_file_range`:

cl_sync_file_range
==================

.. c:function:: int cl_sync_file_range(struct inode *inode, loff_t start, loff_t end, enum cl_fsync_mode mode, int ignore_layout)

    if \ ``mode``\  is not CL_FSYNC_LOCAL, it will send OST_SYNC RPCs to OST.

    :param struct inode \*inode:
        *undescribed*

    :param loff_t start:
        *undescribed*

    :param loff_t end:
        *undescribed*

    :param enum cl_fsync_mode mode:
        *undescribed*

    :param int ignore_layout:
        *undescribed*

.. _`cl_sync_file_range.description`:

Description
-----------

Return how many pages have been written.

.. _`ll_have_md_lock`:

ll_have_md_lock
===============

.. c:function:: int ll_have_md_lock(struct inode *inode, __u64 *bits, enum ldlm_mode l_req_mode)

    - bits can be in different locks - if found clear the common lock bits in \*bits - the bits not found, are kept in \*bits \param inode [IN] \param bits [IN] searched lock bits [IN] \param l_req_mode [IN] searched lock mode \retval boolean, true iff all bits are found

    :param struct inode \*inode:
        *undescribed*

    :param __u64 \*bits:
        *undescribed*

    :param enum ldlm_mode l_req_mode:
        *undescribed*

.. _`ll_layout_lock_set`:

ll_layout_lock_set
==================

.. c:function:: int ll_layout_lock_set(struct lustre_handle *lockh, enum ldlm_mode mode, struct inode *inode)

    in this function.

    :param struct lustre_handle \*lockh:
        *undescribed*

    :param enum ldlm_mode mode:
        *undescribed*

    :param struct inode \*inode:
        *undescribed*

.. _`ll_layout_refresh`:

ll_layout_refresh
=================

.. c:function:: int ll_layout_refresh(struct inode *inode, __u32 *gen)

    or enqueues it if it doesn't have one in cache.

    :param struct inode \*inode:
        *undescribed*

    :param __u32 \*gen:
        *undescribed*

.. _`ll_layout_refresh.description`:

Description
-----------

This function will not hold layout lock so it may be revoked any time after
this function returns. Any operations depend on layout should be redone
in that case.

This function should be called before \ :c:func:`lov_io_init`\  to get an uptodate
layout version, the caller should save the version number and after IO
is finished, this function should be called again to verify that layout
is not changed during IO time.

.. _`ll_layout_restore`:

ll_layout_restore
=================

.. c:function:: int ll_layout_restore(struct inode *inode, loff_t offset, __u64 length)

    :param struct inode \*inode:
        *undescribed*

    :param loff_t offset:
        *undescribed*

    :param __u64 length:
        *undescribed*

.. This file was automatic generated / don't edit.

