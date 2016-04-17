.. -*- coding: utf-8; mode: rst -*-

============
read_write.c
============


.. _`vfs_setpos`:

vfs_setpos
==========

.. c:function:: loff_t vfs_setpos (struct file *file, loff_t offset, loff_t maxsize)

    update the file offset for lseek

    :param struct file \*file:
        file structure in question

    :param loff_t offset:
        file offset to seek to

    :param loff_t maxsize:
        maximum file size



.. _`vfs_setpos.description`:

Description
-----------

This is a low-level filesystem helper for updating the file offset to
the value specified by ``offset`` if the given offset is valid and it is
not equal to the current file offset.

Return the specified offset on success and -EINVAL on invalid offset.



.. _`generic_file_llseek_size`:

generic_file_llseek_size
========================

.. c:function:: loff_t generic_file_llseek_size (struct file *file, loff_t offset, int whence, loff_t maxsize, loff_t eof)

    generic llseek implementation for regular files

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

    :param loff_t maxsize:

        *undescribed*

    :param loff_t eof:
        offset used for SEEK_END position



.. _`generic_file_llseek_size.description`:

Description
-----------

This is a variant of generic_file_llseek that allows passing in a custom
maximum file size and a custom EOF position, for e.g. hashed directories



.. _`generic_file_llseek_size.synchronization`:

Synchronization
---------------

SEEK_SET and SEEK_END are unsynchronized (but atomic on 64bit platforms)
SEEK_CUR is synchronized against other SEEK_CURs, but not read/writes.
read/writes behave like SEEK_SET against seeks.



.. _`generic_file_llseek`:

generic_file_llseek
===================

.. c:function:: loff_t generic_file_llseek (struct file *file, loff_t offset, int whence)

    generic llseek implementation for regular files

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek



.. _`generic_file_llseek.description`:

Description
-----------

This is a generic implemenation of ->llseek useable for all normal local
filesystems.  It just updates the file offset to the value specified by
``offset`` and ``whence``\ .



.. _`fixed_size_llseek`:

fixed_size_llseek
=================

.. c:function:: loff_t fixed_size_llseek (struct file *file, loff_t offset, int whence, loff_t size)

    llseek implementation for fixed-sized devices

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

    :param loff_t size:
        size of the file



.. _`no_seek_end_llseek`:

no_seek_end_llseek
==================

.. c:function:: loff_t no_seek_end_llseek (struct file *file, loff_t offset, int whence)

    llseek implementation for fixed-sized devices

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek



.. _`no_seek_end_llseek_size`:

no_seek_end_llseek_size
=======================

.. c:function:: loff_t no_seek_end_llseek_size (struct file *file, loff_t offset, int whence, loff_t size)

    llseek implementation for fixed-sized devices

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

    :param loff_t size:
        maximal offset allowed



.. _`noop_llseek`:

noop_llseek
===========

.. c:function:: loff_t noop_llseek (struct file *file, loff_t offset, int whence)

    No Operation Performed llseek implementation

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek



.. _`noop_llseek.description`:

Description
-----------

This is an implementation of ->llseek useable for the rare special case when
userspace expects the seek to succeed but the (device) file is actually not
able to perform the seek. In this case you use :c:func:`noop_llseek` instead of
falling back to the default implementation of ->llseek.

