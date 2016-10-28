.. -*- coding: utf-8; mode: rst -*-

.. _vfs:

*************
The Linux VFS
*************


.. _the_filesystem_types:

The Filesystem types
====================


.. kernel-doc:: include/linux/fs.h
    :man-sect: 9
    :internal:


.. _the_directory_cache:

The Directory Cache
===================


.. kernel-doc:: fs/dcache.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/dcache.h
    :man-sect: 9
    :internal:


.. _inode_handling:

Inode Handling
==============


.. kernel-doc:: fs/inode.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/bad_inode.c
    :man-sect: 9
    :export:


.. _registration_and_superblocks:

Registration and Superblocks
============================


.. kernel-doc:: fs/super.c
    :man-sect: 9
    :export:


.. _file_locks:

File Locks
==========


.. kernel-doc:: fs/locks.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/locks.c
    :man-sect: 9
    :internal:


.. _other_functions:

Other Functions
===============


.. kernel-doc:: fs/mpage.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/namei.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/buffer.c
    :man-sect: 9
    :export:


.. kernel-doc:: block/bio.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/seq_file.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/filesystems.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/fs-writeback.c
    :man-sect: 9
    :export:


.. kernel-doc:: fs/block_dev.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
