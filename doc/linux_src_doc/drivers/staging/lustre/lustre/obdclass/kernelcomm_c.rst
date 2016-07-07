.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/kernelcomm.c

.. _`libcfs_kkuc_msg_put`:

libcfs_kkuc_msg_put
===================

.. c:function:: int libcfs_kkuc_msg_put(struct file *filp, void *payload)

    send an message from kernel to userspace \ ``param``\  fp to send the message to \ ``param``\  payload Payload data.  First field of payload is always struct kuc_hdr

    :param struct file \*filp:
        *undescribed*

    :param void \*payload:
        *undescribed*

.. _`libcfs_kkuc_group_foreach`:

libcfs_kkuc_group_foreach
=========================

.. c:function:: int libcfs_kkuc_group_foreach(unsigned int group, libcfs_kkuc_cb_t cb_func, void *cb_arg)

    \ ``param``\  group the group to call the function on. \ ``param``\  cb_func the function to be called. \ ``param``\  cb_arg extra argument to be passed to the callback function.

    :param unsigned int group:
        *undescribed*

    :param libcfs_kkuc_cb_t cb_func:
        *undescribed*

    :param void \*cb_arg:
        *undescribed*

.. This file was automatic generated / don't edit.

