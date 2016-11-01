.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fuse/fuse_i.h

.. _`fuse_inode_eq`:

fuse_inode_eq
=============

.. c:function:: int fuse_inode_eq(struct inode *inode, void *_nodeidp)

    :param struct inode \*inode:
        *undescribed*

    :param void \*_nodeidp:
        *undescribed*

.. _`fuse_iget`:

fuse_iget
=========

.. c:function:: struct inode *fuse_iget(struct super_block *sb, u64 nodeid, int generation, struct fuse_attr *attr, u64 attr_valid, u64 attr_version)

    :param struct super_block \*sb:
        *undescribed*

    :param u64 nodeid:
        *undescribed*

    :param int generation:
        *undescribed*

    :param struct fuse_attr \*attr:
        *undescribed*

    :param u64 attr_valid:
        *undescribed*

    :param u64 attr_version:
        *undescribed*

.. _`fuse_queue_forget`:

fuse_queue_forget
=================

.. c:function:: void fuse_queue_forget(struct fuse_conn *fc, struct fuse_forget_link *forget, u64 nodeid, u64 nlookup)

    :param struct fuse_conn \*fc:
        *undescribed*

    :param struct fuse_forget_link \*forget:
        *undescribed*

    :param u64 nodeid:
        *undescribed*

    :param u64 nlookup:
        *undescribed*

.. _`fuse_read_fill`:

fuse_read_fill
==============

.. c:function:: void fuse_read_fill(struct fuse_req *req, struct file *file, loff_t pos, size_t count, int opcode)

    :param struct fuse_req \*req:
        *undescribed*

    :param struct file \*file:
        *undescribed*

    :param loff_t pos:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param int opcode:
        *undescribed*

.. _`fuse_open_common`:

fuse_open_common
================

.. c:function:: int fuse_open_common(struct inode *inode, struct file *file, bool isdir)

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

    :param bool isdir:
        *undescribed*

.. _`fuse_release_common`:

fuse_release_common
===================

.. c:function:: void fuse_release_common(struct file *file, int opcode)

    :param struct file \*file:
        *undescribed*

    :param int opcode:
        *undescribed*

.. _`fuse_fsync_common`:

fuse_fsync_common
=================

.. c:function:: int fuse_fsync_common(struct file *file, loff_t start, loff_t end, int datasync, int isdir)

    :param struct file \*file:
        *undescribed*

    :param loff_t start:
        *undescribed*

    :param loff_t end:
        *undescribed*

    :param int datasync:
        *undescribed*

    :param int isdir:
        *undescribed*

.. _`fuse_notify_poll_wakeup`:

fuse_notify_poll_wakeup
=======================

.. c:function:: int fuse_notify_poll_wakeup(struct fuse_conn *fc, struct fuse_notify_poll_wakeup_out *outarg)

    :param struct fuse_conn \*fc:
        *undescribed*

    :param struct fuse_notify_poll_wakeup_out \*outarg:
        *undescribed*

.. _`fuse_init_file_inode`:

fuse_init_file_inode
====================

.. c:function:: void fuse_init_file_inode(struct inode *inode)

    :param struct inode \*inode:
        *undescribed*

.. _`fuse_init_common`:

fuse_init_common
================

.. c:function:: void fuse_init_common(struct inode *inode)

    :param struct inode \*inode:
        *undescribed*

.. _`fuse_init_dir`:

fuse_init_dir
=============

.. c:function:: void fuse_init_dir(struct inode *inode)

    :param struct inode \*inode:
        *undescribed*

.. _`fuse_init_symlink`:

fuse_init_symlink
=================

.. c:function:: void fuse_init_symlink(struct inode *inode)

    :param struct inode \*inode:
        *undescribed*

.. _`fuse_change_attributes`:

fuse_change_attributes
======================

.. c:function:: void fuse_change_attributes(struct inode *inode, struct fuse_attr *attr, u64 attr_valid, u64 attr_version)

    :param struct inode \*inode:
        *undescribed*

    :param struct fuse_attr \*attr:
        *undescribed*

    :param u64 attr_valid:
        *undescribed*

    :param u64 attr_version:
        *undescribed*

.. _`fuse_dev_init`:

fuse_dev_init
=============

.. c:function:: int fuse_dev_init( void)

    :param  void:
        no arguments

.. _`fuse_dev_cleanup`:

fuse_dev_cleanup
================

.. c:function:: void fuse_dev_cleanup( void)

    :param  void:
        no arguments

.. _`fuse_request_alloc`:

fuse_request_alloc
==================

.. c:function:: struct fuse_req *fuse_request_alloc(unsigned npages)

    :param unsigned npages:
        *undescribed*

.. _`fuse_request_free`:

fuse_request_free
=================

.. c:function:: void fuse_request_free(struct fuse_req *req)

    :param struct fuse_req \*req:
        *undescribed*

.. _`fuse_get_req`:

fuse_get_req
============

.. c:function:: struct fuse_req *fuse_get_req(struct fuse_conn *fc, unsigned npages)

    ENOMEM, caller should specify # elements in req->pages[] explicitly

    :param struct fuse_conn \*fc:
        *undescribed*

    :param unsigned npages:
        *undescribed*

.. _`fuse_get_req_nofail_nopages`:

fuse_get_req_nofail_nopages
===========================

.. c:function:: struct fuse_req *fuse_get_req_nofail_nopages(struct fuse_conn *fc, struct file *file)

    :param struct fuse_conn \*fc:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`fuse_put_request`:

fuse_put_request
================

.. c:function:: void fuse_put_request(struct fuse_conn *fc, struct fuse_req *req)

    the request.

    :param struct fuse_conn \*fc:
        *undescribed*

    :param struct fuse_req \*req:
        *undescribed*

.. _`fuse_request_send`:

fuse_request_send
=================

.. c:function:: void fuse_request_send(struct fuse_conn *fc, struct fuse_req *req)

    :param struct fuse_conn \*fc:
        *undescribed*

    :param struct fuse_req \*req:
        *undescribed*

.. _`fuse_simple_request`:

fuse_simple_request
===================

.. c:function:: ssize_t fuse_simple_request(struct fuse_conn *fc, struct fuse_args *args)

    :param struct fuse_conn \*fc:
        *undescribed*

    :param struct fuse_args \*args:
        *undescribed*

.. _`fuse_request_send_background`:

fuse_request_send_background
============================

.. c:function:: void fuse_request_send_background(struct fuse_conn *fc, struct fuse_req *req)

    :param struct fuse_conn \*fc:
        *undescribed*

    :param struct fuse_req \*req:
        *undescribed*

.. _`fuse_invalidate_attr`:

fuse_invalidate_attr
====================

.. c:function:: void fuse_invalidate_attr(struct inode *inode)

    :param struct inode \*inode:
        *undescribed*

.. _`fuse_conn_get`:

fuse_conn_get
=============

.. c:function:: struct fuse_conn *fuse_conn_get(struct fuse_conn *fc)

    :param struct fuse_conn \*fc:
        *undescribed*

.. _`fuse_conn_init`:

fuse_conn_init
==============

.. c:function:: void fuse_conn_init(struct fuse_conn *fc)

    :param struct fuse_conn \*fc:
        *undescribed*

.. _`fuse_conn_put`:

fuse_conn_put
=============

.. c:function:: void fuse_conn_put(struct fuse_conn *fc)

    :param struct fuse_conn \*fc:
        *undescribed*

.. _`fuse_ctl_add_conn`:

fuse_ctl_add_conn
=================

.. c:function:: int fuse_ctl_add_conn(struct fuse_conn *fc)

    :param struct fuse_conn \*fc:
        *undescribed*

.. _`fuse_ctl_remove_conn`:

fuse_ctl_remove_conn
====================

.. c:function:: void fuse_ctl_remove_conn(struct fuse_conn *fc)

    :param struct fuse_conn \*fc:
        *undescribed*

.. _`fuse_valid_type`:

fuse_valid_type
===============

.. c:function:: int fuse_valid_type(int m)

    :param int m:
        *undescribed*

.. _`fuse_allow_current_process`:

fuse_allow_current_process
==========================

.. c:function:: int fuse_allow_current_process(struct fuse_conn *fc)

    :param struct fuse_conn \*fc:
        *undescribed*

.. _`fuse_reverse_inval_inode`:

fuse_reverse_inval_inode
========================

.. c:function:: int fuse_reverse_inval_inode(struct super_block *sb, u64 nodeid, loff_t offset, loff_t len)

    system tells the kernel to invalidate cache for the given node id.

    :param struct super_block \*sb:
        *undescribed*

    :param u64 nodeid:
        *undescribed*

    :param loff_t offset:
        *undescribed*

    :param loff_t len:
        *undescribed*

.. _`fuse_reverse_inval_entry`:

fuse_reverse_inval_entry
========================

.. c:function:: int fuse_reverse_inval_entry(struct super_block *sb, u64 parent_nodeid, u64 child_nodeid, struct qstr *name)

    system tells the kernel to invalidate parent attributes and the dentry matching parent/name.

    :param struct super_block \*sb:
        *undescribed*

    :param u64 parent_nodeid:
        *undescribed*

    :param u64 child_nodeid:
        *undescribed*

    :param struct qstr \*name:
        *undescribed*

.. _`fuse_reverse_inval_entry.description`:

Description
-----------

If the child_nodeid is non-zero and:
- matches the inode number for the dentry matching parent/name,
- is not a mount point
- is a file or oan empty directory
then the dentry is unhashed (d_delete()).

.. This file was automatic generated / don't edit.

