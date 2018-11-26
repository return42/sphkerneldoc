.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ceph/locks.c

.. _`ceph_lock_message`:

ceph_lock_message
=================

.. c:function:: int ceph_lock_message(u8 lock_type, u16 operation, struct inode *inode, int cmd, u8 wait, struct file_lock *fl)

    :param lock_type:
        *undescribed*
    :type lock_type: u8

    :param operation:
        *undescribed*
    :type operation: u16

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param cmd:
        *undescribed*
    :type cmd: int

    :param wait:
        *undescribed*
    :type wait: u8

    :param fl:
        *undescribed*
    :type fl: struct file_lock \*

.. _`ceph_lock`:

ceph_lock
=========

.. c:function:: int ceph_lock(struct file *file, int cmd, struct file_lock *fl)

    For now, this just goes away to the server. Later it may be more awesome.

    :param file:
        *undescribed*
    :type file: struct file \*

    :param cmd:
        *undescribed*
    :type cmd: int

    :param fl:
        *undescribed*
    :type fl: struct file_lock \*

.. _`ceph_encode_locks_to_buffer`:

ceph_encode_locks_to_buffer
===========================

.. c:function:: int ceph_encode_locks_to_buffer(struct inode *inode, struct ceph_filelock *flocks, int num_fcntl_locks, int num_flock_locks)

    array. Must be called with inode->i_lock already held. If we encounter more of a specific lock type than expected, return -ENOSPC.

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param flocks:
        *undescribed*
    :type flocks: struct ceph_filelock \*

    :param num_fcntl_locks:
        *undescribed*
    :type num_fcntl_locks: int

    :param num_flock_locks:
        *undescribed*
    :type num_flock_locks: int

.. _`ceph_locks_to_pagelist`:

ceph_locks_to_pagelist
======================

.. c:function:: int ceph_locks_to_pagelist(struct ceph_filelock *flocks, struct ceph_pagelist *pagelist, int num_fcntl_locks, int num_flock_locks)

    :param flocks:
        *undescribed*
    :type flocks: struct ceph_filelock \*

    :param pagelist:
        *undescribed*
    :type pagelist: struct ceph_pagelist \*

    :param num_fcntl_locks:
        *undescribed*
    :type num_fcntl_locks: int

    :param num_flock_locks:
        *undescribed*
    :type num_flock_locks: int

.. _`ceph_locks_to_pagelist.format-is`:

Format is
---------

#fcntl locks, sequential fcntl locks, #flock locks,
sequential flock locks.
Returns zero on success.

.. This file was automatic generated / don't edit.

