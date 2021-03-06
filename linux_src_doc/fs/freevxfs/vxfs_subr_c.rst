.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_subr.c

.. _`vxfs_get_page`:

vxfs_get_page
=============

.. c:function:: struct page *vxfs_get_page(struct address_space *mapping, u_long n)

    read a page into memory.

    :param mapping:
        *undescribed*
    :type mapping: struct address_space \*

    :param n:
        page number
    :type n: u_long

.. _`vxfs_get_page.description`:

Description
-----------

vxfs_get_page reads the \ ``n``\  th page of \ ``ip``\  into the pagecache.

.. _`vxfs_get_page.return`:

Return
------

The wanted page on success, else a NULL pointer.

.. _`vxfs_bread`:

vxfs_bread
==========

.. c:function:: struct buffer_head *vxfs_bread(struct inode *ip, int block)

    read buffer for a give inode,block tuple

    :param ip:
        inode
    :type ip: struct inode \*

    :param block:
        logical block
    :type block: int

.. _`vxfs_bread.description`:

Description
-----------

The vxfs_bread function reads block no \ ``block``\   of
\ ``ip``\  into the buffercache.

.. _`vxfs_bread.return`:

Return
------

The resulting \ :c:type:`struct buffer_head <buffer_head>`\ .

.. _`vxfs_getblk`:

vxfs_getblk
===========

.. c:function:: int vxfs_getblk(struct inode *ip, sector_t iblock, struct buffer_head *bp, int create)

    locate buffer for given inode,block tuple

    :param ip:
        inode
    :type ip: struct inode \*

    :param iblock:
        logical block
    :type iblock: sector_t

    :param bp:
        buffer skeleton
    :type bp: struct buffer_head \*

    :param create:
        \ ``TRUE``\  if blocks may be newly allocated.
    :type create: int

.. _`vxfs_getblk.description`:

Description
-----------

The vxfs_get_block function fills \ ``bp``\  with the right physical
block and device number to perform a lowlevel read/write on
it.

.. _`vxfs_getblk.return`:

Return
------

Zero on success, else a negativ error code (-EIO).

.. _`vxfs_readpage`:

vxfs_readpage
=============

.. c:function:: int vxfs_readpage(struct file *file, struct page *page)

    read one page synchronously into the pagecache

    :param file:
        file context (unused)
    :type file: struct file \*

    :param page:
        page frame to fill in.
    :type page: struct page \*

.. _`vxfs_readpage.description`:

Description
-----------

The vxfs_readpage routine reads \ ``page``\  synchronously into the
pagecache.

.. _`vxfs_readpage.return`:

Return
------

Zero on success, else a negative error code.

.. _`vxfs_readpage.locking-status`:

Locking status
--------------

\ ``page``\  is locked and will be unlocked.

.. _`vxfs_bmap`:

vxfs_bmap
=========

.. c:function:: sector_t vxfs_bmap(struct address_space *mapping, sector_t block)

    perform logical to physical block mapping

    :param mapping:
        logical to physical mapping to use
    :type mapping: struct address_space \*

    :param block:
        logical block (relative to \ ``mapping``\ ).
    :type block: sector_t

.. _`vxfs_bmap.description`:

Description
-----------

Vxfs_bmap find out the corresponding phsical block to the
\ ``mapping``\ , \ ``block``\  pair.

.. _`vxfs_bmap.return`:

Return
------

Physical block number on success, else Zero.

.. _`vxfs_bmap.locking-status`:

Locking status
--------------

We are under the bkl.

.. This file was automatic generated / don't edit.

