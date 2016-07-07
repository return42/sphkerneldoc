.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ufs/inode.c

.. _`ufs_inode_getfrag`:

ufs_inode_getfrag
=================

.. c:function:: u64 ufs_inode_getfrag(struct inode *inode, unsigned index, sector_t new_fragment, int *err, int *new, struct page *locked_page)

    allocate new fragment(s)

    :param struct inode \*inode:
        pointer to inode

    :param unsigned index:
        number of block pointer within the inode's array.

    :param sector_t new_fragment:
        number of new allocated fragment(s)

    :param int \*err:
        we set it if something wrong

    :param int \*new:
        we set it if we allocate new block

    :param struct page \*locked_page:
        for \ :c:func:`ufs_new_fragments`\ 

.. _`ufs_inode_getblock`:

ufs_inode_getblock
==================

.. c:function:: u64 ufs_inode_getblock(struct inode *inode, u64 ind_block, unsigned index, sector_t new_fragment, int *err, int *new, struct page *locked_page)

    allocate new block

    :param struct inode \*inode:
        pointer to inode

    :param u64 ind_block:
        block number of the indirect block

    :param unsigned index:
        number of pointer within the indirect block

    :param sector_t new_fragment:
        number of new allocated fragment
        (block will hold this fragment and also uspi->s_fpb-1)

    :param int \*err:
        see \ :c:func:`ufs_inode_getfrag`\ 

    :param int \*new:
        see \ :c:func:`ufs_inode_getfrag`\ 

    :param struct page \*locked_page:
        see \ :c:func:`ufs_inode_getfrag`\ 

.. _`ufs_getfrag_block`:

ufs_getfrag_block
=================

.. c:function:: int ufs_getfrag_block(struct inode *inode, sector_t fragment, struct buffer_head *bh_result, int create)

    \`get_block_t' function, interface between UFS and readpage, writepage and so on

    :param struct inode \*inode:
        *undescribed*

    :param sector_t fragment:
        *undescribed*

    :param struct buffer_head \*bh_result:
        *undescribed*

    :param int create:
        *undescribed*

.. This file was automatic generated / don't edit.

