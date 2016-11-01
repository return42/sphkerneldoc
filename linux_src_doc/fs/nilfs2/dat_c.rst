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

    :param struct inode \*dat:
        DAT file inode

    :param __u64 vblocknr:
        virtual block number

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

    :param struct inode \*dat:
        DAT file inode

    :param __u64 \*vblocknrs:
        array of virtual block numbers

    :param size_t nitems:
        number of virtual block numbers

.. _`nilfs_dat_freev.description`:

Description
-----------

nilfs_dat_freev() frees the virtual block numbers specified by
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

    :param struct inode \*dat:
        DAT file inode

    :param __u64 vblocknr:
        virtual block number

    :param sector_t blocknr:
        block number

.. _`nilfs_dat_move.description`:

Description
-----------

nilfs_dat_move() changes the block number associated with
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

    :param struct inode \*dat:
        DAT file inode

    :param __u64 vblocknr:
        virtual block number

    :param sector_t \*blocknrp:
        pointer to a block number

.. _`nilfs_dat_translate.description`:

Description
-----------

nilfs_dat_translate() maps the virtual block number \ ``vblocknr``\ 
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

    :param struct super_block \*sb:
        super block instance

    :param size_t entry_size:
        size of a dat entry

    :param struct nilfs_inode \*raw_inode:
        on-disk dat inode

    :param struct inode \*\*inodep:
        buffer to store the inode

.. This file was automatic generated / don't edit.

