.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/llite_lib.c

.. _`ll_get_default_mdsize`:

ll_get_default_mdsize
=====================

.. c:function:: int ll_get_default_mdsize(struct ll_sb_info *sbi, int *lmmsize)

    :param struct ll_sb_info \*sbi:
        *undescribed*

    :param int \*lmmsize:
        *undescribed*

.. _`ll_get_default_mdsize.description`:

Description
-----------

\see client_obd::cl_default_mds_easize

\param[in]  sbi      superblock info for this filesystem
\param[out] lmmsize  pointer to storage location for value

\retval 0            on success
\retval negative     negated errno on failure

.. _`ll_set_default_mdsize`:

ll_set_default_mdsize
=====================

.. c:function:: int ll_set_default_mdsize(struct ll_sb_info *sbi, int lmmsize)

    :param struct ll_sb_info \*sbi:
        *undescribed*

    :param int lmmsize:
        *undescribed*

.. _`ll_set_default_mdsize.description`:

Description
-----------

\see client_obd::cl_default_mds_easize

\param[in] sbi       superblock info for this filesystem
\param[in] lmmsize   the size to set

\retval 0            on success
\retval negative     negated errno on failure

.. _`ll_open_cleanup`:

ll_open_cleanup
===============

.. c:function:: void ll_open_cleanup(struct super_block *sb, struct ptlrpc_request *open_req)

    side.

    :param struct super_block \*sb:
        *undescribed*

    :param struct ptlrpc_request \*open_req:
        *undescribed*

.. _`ll_open_cleanup.description`:

Description
-----------

For open case, the client side open handling thread may hit error
after the MDT grant the open. Under such case, the client should
send close RPC to the MDT as cleanup; otherwise, the open handle
on the MDT will be leaked there until the client umount or evicted.

In further, if someone unlinked the file, because the open handle
holds the reference on such file/object, then it will block the
subsequent threads that want to locate such object via FID.

\param[in] sb        super block for this file-system
\param[in] open_req  pointer to the original open request

.. _`ll_get_obd_name`:

ll_get_obd_name
===============

.. c:function:: int ll_get_obd_name(struct inode *inode, unsigned int cmd, unsigned long arg)

    :param struct inode \*inode:
        *undescribed*

    :param unsigned int cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. _`ll_get_fsname`:

ll_get_fsname
=============

.. c:function:: char *ll_get_fsname(struct super_block *sb, char *buf, int buflen)

    NULL), the fsname will be returned in this buffer; otherwise, a static buffer will be used to store the fsname and returned to caller.

    :param struct super_block \*sb:
        *undescribed*

    :param char \*buf:
        *undescribed*

    :param int buflen:
        *undescribed*

.. _`ll_linkea_decode`:

ll_linkea_decode
================

.. c:function:: int ll_linkea_decode(struct linkea_data *ldata, unsigned int linkno, struct lu_fid *parent_fid, struct lu_name *ln)

    :param struct linkea_data \*ldata:
        *undescribed*

    :param unsigned int linkno:
        *undescribed*

    :param struct lu_fid \*parent_fid:
        *undescribed*

    :param struct lu_name \*ln:
        *undescribed*

.. _`ll_linkea_decode.description`:

Description
-----------

\param[in]   ldata           - Initialized linkea data
\param[in]   linkno          - Link identifier
\param[out]  parent_fid      - The entry's parent FID
\param[in]   size            - Entry name destination buffer

\retval 0 on success
\retval Appropriate negative error code on failure

.. _`ll_getparent`:

ll_getparent
============

.. c:function:: int ll_getparent(struct file *file, struct getparent __user *arg)

    a given link number, letting the caller iterate over linkno to list one or all links of an entry.

    :param struct file \*file:
        *undescribed*

    :param struct getparent __user \*arg:
        *undescribed*

.. _`ll_getparent.description`:

Description
-----------

\param[in]     file  - File descriptor against which to perform the operation
\param[in,out] arg   - User-filled structure containing the linkno to operate
on and the available size. It is eventually filled with
the requested information or left untouched on error

\retval - 0 on success
\retval - Appropriate negative error code on failure

.. This file was automatic generated / don't edit.

