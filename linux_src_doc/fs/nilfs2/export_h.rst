.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/export.h

.. _`nilfs_fid`:

struct nilfs_fid
================

.. c:type:: struct nilfs_fid

    NILFS file id type

.. _`nilfs_fid.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_fid {
        u64 cno;
        u64 ino;
        u32 gen;
        u32 parent_gen;
        u64 parent_ino;
    }

.. _`nilfs_fid.members`:

Members
-------

cno
    checkpoint number

ino
    inode number

gen
    file generation (version) for NFS

parent_gen
    parent generation (version) for NFS

parent_ino
    parent inode number

.. This file was automatic generated / don't edit.

