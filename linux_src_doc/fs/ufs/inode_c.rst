.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ufs/inode.c

.. _`ufs_inode_getfrag`:

ufs_inode_getfrag
=================

.. c:function:: u64 ufs_inode_getfrag(struct inode *inode, unsigned index, sector_t new_fragment, int *err, int *new, struct page *locked_page)

    allocate new fragment(s)

    :param inode:
        pointer to inode
    :type inode: struct inode \*

    :param index:
        number of block pointer within the inode's array.
    :type index: unsigned

    :param new_fragment:
        number of new allocated fragment(s)
    :type new_fragment: sector_t

    :param err:
        we set it if something wrong
    :type err: int \*

    :param new:
        we set it if we allocate new block
    :type new: int \*

    :param locked_page:
        for \ :c:func:`ufs_new_fragments`\ 
    :type locked_page: struct page \*

.. _`ufs_inode_getblock`:

ufs_inode_getblock
==================

.. c:function:: u64 ufs_inode_getblock(struct inode *inode, u64 ind_block, unsigned index, sector_t new_fragment, int *err, int *new, struct page *locked_page)

    allocate new block

    :param inode:
        pointer to inode
    :type inode: struct inode \*

    :param ind_block:
        block number of the indirect block
    :type ind_block: u64

    :param index:
        number of pointer within the indirect block
    :type index: unsigned

    :param new_fragment:
        number of new allocated fragment
        (block will hold this fragment and also uspi->s_fpb-1)
    :type new_fragment: sector_t

    :param err:
        see \ :c:func:`ufs_inode_getfrag`\ 
    :type err: int \*

    :param new:
        see \ :c:func:`ufs_inode_getfrag`\ 
    :type new: int \*

    :param locked_page:
        see \ :c:func:`ufs_inode_getfrag`\ 
    :type locked_page: struct page \*

.. _`ufs_getfrag_block`:

ufs_getfrag_block
=================

.. c:function:: int ufs_getfrag_block(struct inode *inode, sector_t fragment, struct buffer_head *bh_result, int create)

    \`get_block_t' function, interface between UFS and readpage, writepage and so on

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param fragment:
        *undescribed*
    :type fragment: sector_t

    :param bh_result:
        *undescribed*
    :type bh_result: struct buffer_head \*

    :param create:
        *undescribed*
    :type create: int

.. This file was automatic generated / don't edit.

