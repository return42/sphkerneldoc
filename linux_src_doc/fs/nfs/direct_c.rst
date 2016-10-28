.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/direct.c

.. _`nfs_direct_io`:

nfs_direct_IO
=============

.. c:function:: ssize_t nfs_direct_IO(struct kiocb *iocb, struct iov_iter *iter)

    NFS address space operation for direct I/O

    :param struct kiocb \*iocb:
        target I/O control block

    :param struct iov_iter \*iter:
        *undescribed*

.. _`nfs_direct_io.description`:

Description
-----------

The presence of this routine in the address space ops vector means
the NFS client supports direct I/O. However, for most direct IO, we
shunt off direct read and write requests before the VFS gets them,
so this method is only ever called for swap.

.. _`nfs_file_direct_read`:

nfs_file_direct_read
====================

.. c:function:: ssize_t nfs_file_direct_read(struct kiocb *iocb, struct iov_iter *iter)

    file direct read operation for NFS files

    :param struct kiocb \*iocb:
        target I/O control block

    :param struct iov_iter \*iter:
        vector of user buffers into which to read data

.. _`nfs_file_direct_read.description`:

Description
-----------

We use this function for direct reads instead of calling
\ :c:func:`generic_file_aio_read`\  in order to avoid gfar's check to see if
the request starts before the end of the file.  For that check
to work, we must generate a GETATTR before each direct read, and
even then there is a window between the GETATTR and the subsequent
READ where the file size could change.  Our preference is simply
to do all reads the application wants, and the server will take
care of managing the end of file boundary.

This function also eliminates unnecessarily updating the file's
atime locally, as the NFS server sets the file's atime, and this
client must read the updated atime from the server back into its
cache.

.. _`nfs_file_direct_write`:

nfs_file_direct_write
=====================

.. c:function:: ssize_t nfs_file_direct_write(struct kiocb *iocb, struct iov_iter *iter)

    file direct write operation for NFS files

    :param struct kiocb \*iocb:
        target I/O control block

    :param struct iov_iter \*iter:
        vector of user buffers from which to write data

.. _`nfs_file_direct_write.description`:

Description
-----------

We use this function for direct writes instead of calling
\ :c:func:`generic_file_aio_write`\  in order to avoid taking the inode
semaphore and updating the i_size.  The NFS server will set
the new i_size and this client must read the updated size
back into its cache.  We let the server do generic write
parameter checking and report problems.

We eliminate local atime updates, see direct read above.

We avoid unnecessary page cache invalidations for normal cached
readers of this file.

Note that O_APPEND is not supported for NFS direct writes, as there
is no atomic O_APPEND write facility in the NFS protocol.

.. _`nfs_init_directcache`:

nfs_init_directcache
====================

.. c:function:: int nfs_init_directcache( void)

    create a slab cache for nfs_direct_req structures

    :param  void:
        no arguments

.. _`nfs_destroy_directcache`:

nfs_destroy_directcache
=======================

.. c:function:: void nfs_destroy_directcache( void)

    destroy the slab cache for nfs_direct_req structures

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

