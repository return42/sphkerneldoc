.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ceph/locks.c

.. _`ceph_lock_message`:

ceph_lock_message
=================

.. c:function:: int ceph_lock_message(u8 lock_type, u16 operation, struct file *file, int cmd, u8 wait, struct file_lock *fl)

    :param u8 lock_type:
        *undescribed*

    :param u16 operation:
        *undescribed*

    :param struct file \*file:
        *undescribed*

    :param int cmd:
        *undescribed*

    :param u8 wait:
        *undescribed*

    :param struct file_lock \*fl:
        *undescribed*

.. _`ceph_lock`:

ceph_lock
=========

.. c:function:: int ceph_lock(struct file *file, int cmd, struct file_lock *fl)

    For now, this just goes away to the server. Later it may be more awesome.

    :param struct file \*file:
        *undescribed*

    :param int cmd:
        *undescribed*

    :param struct file_lock \*fl:
        *undescribed*

.. _`ceph_encode_locks_to_buffer`:

ceph_encode_locks_to_buffer
===========================

.. c:function:: int ceph_encode_locks_to_buffer(struct inode *inode, struct ceph_filelock *flocks, int num_fcntl_locks, int num_flock_locks)

    array. Must be called with inode->i_lock already held. If we encounter more of a specific lock type than expected, return -ENOSPC.

    :param struct inode \*inode:
        *undescribed*

    :param struct ceph_filelock \*flocks:
        *undescribed*

    :param int num_fcntl_locks:
        *undescribed*

    :param int num_flock_locks:
        *undescribed*

.. _`ceph_locks_to_pagelist`:

ceph_locks_to_pagelist
======================

.. c:function:: int ceph_locks_to_pagelist(struct ceph_filelock *flocks, struct ceph_pagelist *pagelist, int num_fcntl_locks, int num_flock_locks)

    :param struct ceph_filelock \*flocks:
        *undescribed*

    :param struct ceph_pagelist \*pagelist:
        *undescribed*

    :param int num_fcntl_locks:
        *undescribed*

    :param int num_flock_locks:
        *undescribed*

.. _`ceph_locks_to_pagelist.format-is`:

Format is
---------

#fcntl locks, sequential fcntl locks, #flock locks,
sequential flock locks.
Returns zero on success.

.. This file was automatic generated / don't edit.

