.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fuse/fuse_i.h

.. _`fuse_inode_eq`:

fuse_inode_eq
=============

.. c:function:: int fuse_inode_eq(struct inode *inode, void *_nodeidp)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param _nodeidp:
        *undescribed*
    :type _nodeidp: void \*

.. _`fuse_iget`:

fuse_iget
=========

.. c:function:: struct inode *fuse_iget(struct super_block *sb, u64 nodeid, int generation, struct fuse_attr *attr, u64 attr_valid, u64 attr_version)

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param nodeid:
        *undescribed*
    :type nodeid: u64

    :param generation:
        *undescribed*
    :type generation: int

    :param attr:
        *undescribed*
    :type attr: struct fuse_attr \*

    :param attr_valid:
        *undescribed*
    :type attr_valid: u64

    :param attr_version:
        *undescribed*
    :type attr_version: u64

.. _`fuse_queue_forget`:

fuse_queue_forget
=================

.. c:function:: void fuse_queue_forget(struct fuse_conn *fc, struct fuse_forget_link *forget, u64 nodeid, u64 nlookup)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param forget:
        *undescribed*
    :type forget: struct fuse_forget_link \*

    :param nodeid:
        *undescribed*
    :type nodeid: u64

    :param nlookup:
        *undescribed*
    :type nlookup: u64

.. _`fuse_read_fill`:

fuse_read_fill
==============

.. c:function:: void fuse_read_fill(struct fuse_req *req, struct file *file, loff_t pos, size_t count, int opcode)

    :param req:
        *undescribed*
    :type req: struct fuse_req \*

    :param file:
        *undescribed*
    :type file: struct file \*

    :param pos:
        *undescribed*
    :type pos: loff_t

    :param count:
        *undescribed*
    :type count: size_t

    :param opcode:
        *undescribed*
    :type opcode: int

.. _`fuse_open_common`:

fuse_open_common
================

.. c:function:: int fuse_open_common(struct inode *inode, struct file *file, bool isdir)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param file:
        *undescribed*
    :type file: struct file \*

    :param isdir:
        *undescribed*
    :type isdir: bool

.. _`fuse_release_common`:

fuse_release_common
===================

.. c:function:: void fuse_release_common(struct file *file, int opcode)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param opcode:
        *undescribed*
    :type opcode: int

.. _`fuse_fsync_common`:

fuse_fsync_common
=================

.. c:function:: int fuse_fsync_common(struct file *file, loff_t start, loff_t end, int datasync, int isdir)

    :param file:
        *undescribed*
    :type file: struct file \*

    :param start:
        *undescribed*
    :type start: loff_t

    :param end:
        *undescribed*
    :type end: loff_t

    :param datasync:
        *undescribed*
    :type datasync: int

    :param isdir:
        *undescribed*
    :type isdir: int

.. _`fuse_notify_poll_wakeup`:

fuse_notify_poll_wakeup
=======================

.. c:function:: int fuse_notify_poll_wakeup(struct fuse_conn *fc, struct fuse_notify_poll_wakeup_out *outarg)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param outarg:
        *undescribed*
    :type outarg: struct fuse_notify_poll_wakeup_out \*

.. _`fuse_init_file_inode`:

fuse_init_file_inode
====================

.. c:function:: void fuse_init_file_inode(struct inode *inode)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`fuse_init_common`:

fuse_init_common
================

.. c:function:: void fuse_init_common(struct inode *inode)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`fuse_init_dir`:

fuse_init_dir
=============

.. c:function:: void fuse_init_dir(struct inode *inode)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`fuse_init_symlink`:

fuse_init_symlink
=================

.. c:function:: void fuse_init_symlink(struct inode *inode)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`fuse_change_attributes`:

fuse_change_attributes
======================

.. c:function:: void fuse_change_attributes(struct inode *inode, struct fuse_attr *attr, u64 attr_valid, u64 attr_version)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param attr:
        *undescribed*
    :type attr: struct fuse_attr \*

    :param attr_valid:
        *undescribed*
    :type attr_valid: u64

    :param attr_version:
        *undescribed*
    :type attr_version: u64

.. _`fuse_dev_init`:

fuse_dev_init
=============

.. c:function:: int fuse_dev_init( void)

    :param void:
        no arguments
    :type void: 

.. _`fuse_dev_cleanup`:

fuse_dev_cleanup
================

.. c:function:: void fuse_dev_cleanup( void)

    :param void:
        no arguments
    :type void: 

.. _`fuse_request_alloc`:

fuse_request_alloc
==================

.. c:function:: struct fuse_req *fuse_request_alloc(unsigned npages)

    :param npages:
        *undescribed*
    :type npages: unsigned

.. _`fuse_request_free`:

fuse_request_free
=================

.. c:function:: void fuse_request_free(struct fuse_req *req)

    :param req:
        *undescribed*
    :type req: struct fuse_req \*

.. _`fuse_get_req`:

fuse_get_req
============

.. c:function:: struct fuse_req *fuse_get_req(struct fuse_conn *fc, unsigned npages)

    ENOMEM, caller should specify # elements in req->pages[] explicitly

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param npages:
        *undescribed*
    :type npages: unsigned

.. _`fuse_get_req_nofail_nopages`:

fuse_get_req_nofail_nopages
===========================

.. c:function:: struct fuse_req *fuse_get_req_nofail_nopages(struct fuse_conn *fc, struct file *file)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param file:
        *undescribed*
    :type file: struct file \*

.. _`fuse_put_request`:

fuse_put_request
================

.. c:function:: void fuse_put_request(struct fuse_conn *fc, struct fuse_req *req)

    the request.

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param req:
        *undescribed*
    :type req: struct fuse_req \*

.. _`fuse_request_send`:

fuse_request_send
=================

.. c:function:: void fuse_request_send(struct fuse_conn *fc, struct fuse_req *req)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param req:
        *undescribed*
    :type req: struct fuse_req \*

.. _`fuse_simple_request`:

fuse_simple_request
===================

.. c:function:: ssize_t fuse_simple_request(struct fuse_conn *fc, struct fuse_args *args)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param args:
        *undescribed*
    :type args: struct fuse_args \*

.. _`fuse_request_send_background`:

fuse_request_send_background
============================

.. c:function:: void fuse_request_send_background(struct fuse_conn *fc, struct fuse_req *req)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param req:
        *undescribed*
    :type req: struct fuse_req \*

.. _`fuse_invalidate_attr`:

fuse_invalidate_attr
====================

.. c:function:: void fuse_invalidate_attr(struct inode *inode)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`fuse_conn_get`:

fuse_conn_get
=============

.. c:function:: struct fuse_conn *fuse_conn_get(struct fuse_conn *fc)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

.. _`fuse_conn_init`:

fuse_conn_init
==============

.. c:function:: void fuse_conn_init(struct fuse_conn *fc, struct user_namespace *user_ns)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param user_ns:
        *undescribed*
    :type user_ns: struct user_namespace \*

.. _`fuse_conn_put`:

fuse_conn_put
=============

.. c:function:: void fuse_conn_put(struct fuse_conn *fc)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

.. _`fuse_ctl_add_conn`:

fuse_ctl_add_conn
=================

.. c:function:: int fuse_ctl_add_conn(struct fuse_conn *fc)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

.. _`fuse_ctl_remove_conn`:

fuse_ctl_remove_conn
====================

.. c:function:: void fuse_ctl_remove_conn(struct fuse_conn *fc)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

.. _`fuse_valid_type`:

fuse_valid_type
===============

.. c:function:: int fuse_valid_type(int m)

    :param m:
        *undescribed*
    :type m: int

.. _`fuse_allow_current_process`:

fuse_allow_current_process
==========================

.. c:function:: int fuse_allow_current_process(struct fuse_conn *fc)

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

.. _`fuse_reverse_inval_inode`:

fuse_reverse_inval_inode
========================

.. c:function:: int fuse_reverse_inval_inode(struct super_block *sb, u64 nodeid, loff_t offset, loff_t len)

    system tells the kernel to invalidate cache for the given node id.

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param nodeid:
        *undescribed*
    :type nodeid: u64

    :param offset:
        *undescribed*
    :type offset: loff_t

    :param len:
        *undescribed*
    :type len: loff_t

.. _`fuse_reverse_inval_entry`:

fuse_reverse_inval_entry
========================

.. c:function:: int fuse_reverse_inval_entry(struct super_block *sb, u64 parent_nodeid, u64 child_nodeid, struct qstr *name)

    system tells the kernel to invalidate parent attributes and the dentry matching parent/name.

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param parent_nodeid:
        *undescribed*
    :type parent_nodeid: u64

    :param child_nodeid:
        *undescribed*
    :type child_nodeid: u64

    :param name:
        *undescribed*
    :type name: struct qstr \*

.. _`fuse_reverse_inval_entry.description`:

Description
-----------

If the child_nodeid is non-zero and:
- matches the inode number for the dentry matching parent/name,
- is not a mount point
- is a file or oan empty directory
then the dentry is unhashed (d_delete()).

.. This file was automatic generated / don't edit.

