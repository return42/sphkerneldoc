.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/io.c

.. _`nfs_start_io_read`:

nfs_start_io_read
=================

.. c:function:: void nfs_start_io_read(struct inode *inode)

    declare the file is being used for buffered reads \ ``inode``\  - file inode

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`nfs_start_io_read.description`:

Description
-----------

Declare that a buffered read operation is about to start, and ensure
that we block all direct I/O.
On exit, the function ensures that the NFS_INO_ODIRECT flag is unset,
and holds a shared lock on inode->i_rwsem to ensure that the flag
cannot be changed.
In practice, this means that buffered read operations are allowed to
execute in parallel, thanks to the shared lock, whereas direct I/O
operations need to wait to grab an exclusive lock in order to set
NFS_INO_ODIRECT.
Note that buffered writes and truncates both take a write lock on
inode->i_rwsem, meaning that those are serialised w.r.t. the reads.

.. _`nfs_end_io_read`:

nfs_end_io_read
===============

.. c:function:: void nfs_end_io_read(struct inode *inode)

    declare that the buffered read operation is done \ ``inode``\  - file inode

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`nfs_end_io_read.description`:

Description
-----------

Declare that a buffered read operation is done, and release the shared
lock on inode->i_rwsem.

.. _`nfs_start_io_write`:

nfs_start_io_write
==================

.. c:function:: void nfs_start_io_write(struct inode *inode)

    declare the file is being used for buffered writes \ ``inode``\  - file inode

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`nfs_start_io_write.description`:

Description
-----------

Declare that a buffered read operation is about to start, and ensure
that we block all direct I/O.

.. _`nfs_end_io_write`:

nfs_end_io_write
================

.. c:function:: void nfs_end_io_write(struct inode *inode)

    declare that the buffered write operation is done \ ``inode``\  - file inode

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`nfs_end_io_write.description`:

Description
-----------

Declare that a buffered write operation is done, and release the
lock on inode->i_rwsem.

.. _`nfs_start_io_direct`:

nfs_start_io_direct
===================

.. c:function:: void nfs_start_io_direct(struct inode *inode)

    declare the file is being used for direct i/o \ ``inode``\  - file inode

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`nfs_start_io_direct.description`:

Description
-----------

Declare that a direct I/O operation is about to start, and ensure
that we block all buffered I/O.
On exit, the function ensures that the NFS_INO_ODIRECT flag is set,
and holds a shared lock on inode->i_rwsem to ensure that the flag
cannot be changed.
In practice, this means that direct I/O operations are allowed to
execute in parallel, thanks to the shared lock, whereas buffered I/O
operations need to wait to grab an exclusive lock in order to clear
NFS_INO_ODIRECT.
Note that buffered writes and truncates both take a write lock on
inode->i_rwsem, meaning that those are serialised w.r.t. O_DIRECT.

.. _`nfs_end_io_direct`:

nfs_end_io_direct
=================

.. c:function:: void nfs_end_io_direct(struct inode *inode)

    declare that the direct i/o operation is done \ ``inode``\  - file inode

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`nfs_end_io_direct.description`:

Description
-----------

Declare that a direct I/O operation is done, and release the shared
lock on inode->i_rwsem.

.. This file was automatic generated / don't edit.

