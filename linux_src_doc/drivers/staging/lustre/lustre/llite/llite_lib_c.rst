.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/llite_lib.c

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

.. This file was automatic generated / don't edit.

