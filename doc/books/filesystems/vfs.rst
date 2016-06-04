.. -*- coding: utf-8; mode: rst -*-

.. _vfs:

=============
The Linux VFS
=============


.. _the_filesystem_types:

The Filesystem types
====================


.. kernel-doc:: include/linux/fs.h
    :internal:

.. _the_directory_cache:

The Directory Cache
===================


.. kernel-doc:: fs/dcache.c
    :export:

.. kernel-doc:: include/linux/dcache.h
    :internal:

.. _inode_handling:

Inode Handling
==============


.. kernel-doc:: fs/inode.c
    :export:

.. kernel-doc:: fs/bad_inode.c
    :export:

.. _registration_and_superblocks:

Registration and Superblocks
============================


.. kernel-doc:: fs/super.c
    :export:

.. _file_locks:

File Locks
==========


.. kernel-doc:: fs/locks.c
    :export:

.. kernel-doc:: fs/locks.c
    :internal:

.. _other_functions:

Other Functions
===============


.. kernel-doc:: fs/mpage.c
    :export:

.. kernel-doc:: fs/namei.c
    :export:

.. kernel-doc:: fs/buffer.c
    :export:

.. kernel-doc:: block/bio.c
    :export:

.. kernel-doc:: fs/seq_file.c
    :export:

.. kernel-doc:: fs/filesystems.c
    :export:

.. kernel-doc:: fs/fs-writeback.c
    :export:

.. kernel-doc:: fs/block_dev.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
