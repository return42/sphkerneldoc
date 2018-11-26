.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/dat.c

.. _`nilfs_dat_info`:

struct nilfs_dat_info
=====================

.. c:type:: struct nilfs_dat_info

    on-memory private data of DAT file

.. _`nilfs_dat_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_dat_info {
        struct nilfs_mdt_info mi;
        struct nilfs_palloc_cache palloc_cache;
        struct nilfs_shadow_map shadow;
    }

.. _`nilfs_dat_info.members`:

Members
-------

mi
    on-memory private data of metadata file

palloc_cache
    persistent object allocator cache of DAT file

shadow
    shadow map of DAT file

.. _`nilfs_dat_mark_dirty`:

nilfs_dat_mark_dirty
====================

.. c:function:: int nilfs_dat_mark_dirty(struct inode *dat, __u64 vblocknr)

    :param dat:
        DAT file inode
    :type dat: struct inode \*

    :param vblocknr:
        virtual block number
    :type vblocknr: __u64

.. _`nilfs_dat_mark_dirty.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_dat_freev`:

nilfs_dat_freev
===============

.. c:function:: int nilfs_dat_freev(struct inode *dat, __u64 *vblocknrs, size_t nitems)

    free virtual block numbers

    :param dat:
        DAT file inode
    :type dat: struct inode \*

    :param vblocknrs:
        array of virtual block numbers
    :type vblocknrs: __u64 \*

    :param nitems:
        number of virtual block numbers
    :type nitems: size_t

.. _`nilfs_dat_freev.description`:

Description
-----------

\ :c:func:`nilfs_dat_freev`\  frees the virtual block numbers specified by
\ ``vblocknrs``\  and \ ``nitems``\ .

.. _`nilfs_dat_freev.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - The virtual block number have not been allocated.

.. _`nilfs_dat_move`:

nilfs_dat_move
==============

.. c:function:: int nilfs_dat_move(struct inode *dat, __u64 vblocknr, sector_t blocknr)

    change a block number

    :param dat:
        DAT file inode
    :type dat: struct inode \*

    :param vblocknr:
        virtual block number
    :type vblocknr: __u64

    :param blocknr:
        block number
    :type blocknr: sector_t

.. _`nilfs_dat_move.description`:

Description
-----------

\ :c:func:`nilfs_dat_move`\  changes the block number associated with
\ ``vblocknr``\  to \ ``blocknr``\ .

.. _`nilfs_dat_move.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_dat_translate`:

nilfs_dat_translate
===================

.. c:function:: int nilfs_dat_translate(struct inode *dat, __u64 vblocknr, sector_t *blocknrp)

    translate a virtual block number to a block number

    :param dat:
        DAT file inode
    :type dat: struct inode \*

    :param vblocknr:
        virtual block number
    :type vblocknr: __u64

    :param blocknrp:
        pointer to a block number
    :type blocknrp: sector_t \*

.. _`nilfs_dat_translate.description`:

Description
-----------

\ :c:func:`nilfs_dat_translate`\  maps the virtual block number \ ``vblocknr``\ 
to the corresponding block number.

.. _`nilfs_dat_translate.return-value`:

Return Value
------------

On success, 0 is returned and the block number associated
with \ ``vblocknr``\  is stored in the place pointed by \ ``blocknrp``\ . On error, one
of the following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - A block number associated with \ ``vblocknr``\  does not exist.

.. _`nilfs_dat_read`:

nilfs_dat_read
==============

.. c:function:: int nilfs_dat_read(struct super_block *sb, size_t entry_size, struct nilfs_inode *raw_inode, struct inode **inodep)

    read or get dat inode

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param entry_size:
        size of a dat entry
    :type entry_size: size_t

    :param raw_inode:
        on-disk dat inode
    :type raw_inode: struct nilfs_inode \*

    :param inodep:
        buffer to store the inode
    :type inodep: struct inode \*\*

.. This file was automatic generated / don't edit.

