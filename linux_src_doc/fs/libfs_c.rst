.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/libfs.c

.. _`simple_setattr`:

simple_setattr
==============

.. c:function:: int simple_setattr(struct dentry *dentry, struct iattr *iattr)

    setattr for simple filesystem

    :param struct dentry \*dentry:
        dentry

    :param struct iattr \*iattr:
        iattr structure

.. _`simple_setattr.description`:

Description
-----------

Returns 0 on success, -error on failure.

simple_setattr is a simple ->setattr implementation without a proper
implementation of size changes.

It can either be used for in-memory filesystems or special files
on simple regular filesystems.  Anything that needs to change on-disk
or wire state on size changes needs its own setattr method.

.. _`simple_write_end`:

simple_write_end
================

.. c:function:: int simple_write_end(struct file *file, struct address_space *mapping, loff_t pos, unsigned len, unsigned copied, struct page *page, void *fsdata)

    .write_end helper for non-block-device FSes

    :param struct file \*file:
        "

    :param struct address_space \*mapping:
        "

    :param loff_t pos:
        "

    :param unsigned len:
        "

    :param unsigned copied:
        "

    :param struct page \*page:
        "

    :param void \*fsdata:
        "

.. _`simple_write_end.description`:

Description
-----------

simple_write_end does the minimum needed for updating a page after writing is
done. It has the same API signature as the .write_end of
address_space_operations vector. So it can just be set onto .write_end for
FSes that don't need any other processing. i_mutex is assumed to be held.
Block based filesystems should use \ :c:func:`generic_write_end`\ .

.. _`simple_write_end.note`:

NOTE
----

Even though i_size might get updated by this function, mark_inode_dirty
is not called, so a filesystem that actually does store data in .write_inode
should extend on what's done here with a call to \ :c:func:`mark_inode_dirty`\  in the
case that i_size has changed.

Use \*ONLY\* with \ :c:func:`simple_readpage`\ 

.. _`simple_read_from_buffer`:

simple_read_from_buffer
=======================

.. c:function:: ssize_t simple_read_from_buffer(void __user *to, size_t count, loff_t *ppos, const void *from, size_t available)

    copy data from the buffer to user space

    :param void __user \*to:
        the user space buffer to read to

    :param size_t count:
        the maximum number of bytes to read

    :param loff_t \*ppos:
        the current position in the buffer

    :param const void \*from:
        the buffer to read from

    :param size_t available:
        the size of the buffer

.. _`simple_read_from_buffer.description`:

Description
-----------

The \ :c:func:`simple_read_from_buffer`\  function reads up to \ ``count``\  bytes from the
buffer \ ``from``\  at offset \ ``ppos``\  into the user space address starting at \ ``to``\ .

On success, the number of bytes read is returned and the offset \ ``ppos``\  is
advanced by this number, or negative value is returned on error.

.. _`simple_write_to_buffer`:

simple_write_to_buffer
======================

.. c:function:: ssize_t simple_write_to_buffer(void *to, size_t available, loff_t *ppos, const void __user *from, size_t count)

    copy data from user space to the buffer

    :param void \*to:
        the buffer to write to

    :param size_t available:
        the size of the buffer

    :param loff_t \*ppos:
        the current position in the buffer

    :param const void __user \*from:
        the user space buffer to read from

    :param size_t count:
        the maximum number of bytes to read

.. _`simple_write_to_buffer.description`:

Description
-----------

The \ :c:func:`simple_write_to_buffer`\  function reads up to \ ``count``\  bytes from the user
space address starting at \ ``from``\  into the buffer \ ``to``\  at offset \ ``ppos``\ .

On success, the number of bytes written is returned and the offset \ ``ppos``\  is
advanced by this number, or negative value is returned on error.

.. _`memory_read_from_buffer`:

memory_read_from_buffer
=======================

.. c:function:: ssize_t memory_read_from_buffer(void *to, size_t count, loff_t *ppos, const void *from, size_t available)

    copy data from the buffer

    :param void \*to:
        the kernel space buffer to read to

    :param size_t count:
        the maximum number of bytes to read

    :param loff_t \*ppos:
        the current position in the buffer

    :param const void \*from:
        the buffer to read from

    :param size_t available:
        the size of the buffer

.. _`memory_read_from_buffer.description`:

Description
-----------

The \ :c:func:`memory_read_from_buffer`\  function reads up to \ ``count``\  bytes from the
buffer \ ``from``\  at offset \ ``ppos``\  into the kernel space address starting at \ ``to``\ .

On success, the number of bytes read is returned and the offset \ ``ppos``\  is
advanced by this number, or negative value is returned on error.

.. _`generic_fh_to_dentry`:

generic_fh_to_dentry
====================

.. c:function:: struct dentry *generic_fh_to_dentry(struct super_block *sb, struct fid *fid, int fh_len, int fh_type, struct inode *(*get_inode)(struct super_block *sb, u64 ino, u32 gen))

    generic helper for the fh_to_dentry export operation

    :param struct super_block \*sb:
        filesystem to do the file handle conversion on

    :param struct fid \*fid:
        file handle to convert

    :param int fh_len:
        length of the file handle in bytes

    :param int fh_type:
        type of file handle

    :param struct inode \*(\*get_inode)(struct super_block \*sb, u64 ino, u32 gen):
        filesystem callback to retrieve inode

.. _`generic_fh_to_dentry.description`:

Description
-----------

This function decodes \ ``fid``\  as long as it has one of the well-known
Linux filehandle types and calls \ ``get_inode``\  on it to retrieve the
inode for the object specified in the file handle.

.. _`generic_fh_to_parent`:

generic_fh_to_parent
====================

.. c:function:: struct dentry *generic_fh_to_parent(struct super_block *sb, struct fid *fid, int fh_len, int fh_type, struct inode *(*get_inode)(struct super_block *sb, u64 ino, u32 gen))

    generic helper for the fh_to_parent export operation

    :param struct super_block \*sb:
        filesystem to do the file handle conversion on

    :param struct fid \*fid:
        file handle to convert

    :param int fh_len:
        length of the file handle in bytes

    :param int fh_type:
        type of file handle

    :param struct inode \*(\*get_inode)(struct super_block \*sb, u64 ino, u32 gen):
        filesystem callback to retrieve inode

.. _`generic_fh_to_parent.description`:

Description
-----------

This function decodes \ ``fid``\  as long as it has one of the well-known
Linux filehandle types and calls \ ``get_inode``\  on it to retrieve the
inode for the \_parent\_ object specified in the file handle if it
is specified in the file handle, or NULL otherwise.

.. _`__generic_file_fsync`:

__generic_file_fsync
====================

.. c:function:: int __generic_file_fsync(struct file *file, loff_t start, loff_t end, int datasync)

    generic fsync implementation for simple filesystems

    :param struct file \*file:
        file to synchronize

    :param loff_t start:
        start offset in bytes

    :param loff_t end:
        end offset in bytes (inclusive)

    :param int datasync:
        only synchronize essential metadata if true

.. _`__generic_file_fsync.description`:

Description
-----------

This is a generic implementation of the fsync method for simple
filesystems which track all non-inode metadata in the buffers list
hanging off the address_space structure.

.. _`generic_file_fsync`:

generic_file_fsync
==================

.. c:function:: int generic_file_fsync(struct file *file, loff_t start, loff_t end, int datasync)

    generic fsync implementation for simple filesystems with flush

    :param struct file \*file:
        file to synchronize

    :param loff_t start:
        start offset in bytes

    :param loff_t end:
        end offset in bytes (inclusive)

    :param int datasync:
        only synchronize essential metadata if true

.. _`generic_check_addressable`:

generic_check_addressable
=========================

.. c:function:: int generic_check_addressable(unsigned blocksize_bits, u64 num_blocks)

    Check addressability of file system

    :param unsigned blocksize_bits:
        log of file system block size

    :param u64 num_blocks:
        number of blocks in file system

.. _`generic_check_addressable.description`:

Description
-----------

Determine whether a file system with \ ``num_blocks``\  blocks (and a
block size of 2\*\*@blocksize_bits) is addressable by the sector_t
and page cache of the system.  Return 0 if so and -EFBIG otherwise.

.. _`simple_nosetlease`:

simple_nosetlease
=================

.. c:function:: int simple_nosetlease(struct file *filp, long arg, struct file_lock **flp, void **priv)

    generic helper for prohibiting leases

    :param struct file \*filp:
        file pointer

    :param long arg:
        type of lease to obtain

    :param struct file_lock \*\*flp:
        new lease supplied for insertion

    :param void \*\*priv:
        private data for lm_setup operation

.. _`simple_nosetlease.description`:

Description
-----------

Generic helper for filesystems that do not wish to allow leases to be set.
All arguments are ignored and it just returns -EINVAL.

.. This file was automatic generated / don't edit.

