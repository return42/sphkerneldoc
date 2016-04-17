.. -*- coding: utf-8; mode: rst -*-

======
rw26.c
======


.. _`ll_invalidatepage`:

ll_invalidatepage
=================

.. c:function:: void ll_invalidatepage (struct page *vmpage, unsigned int offset, unsigned int length)

    :param struct page \*vmpage:

        *undescribed*

    :param unsigned int offset:

        *undescribed*

    :param unsigned int length:

        *undescribed*



.. _`ll_invalidatepage.description`:

Description
-----------

called when the page is truncate from a file, either as a result of
explicit truncate, or when inode is removed from memory (as a result of
final :c:func:`iput`, umount, or memory pressure induced icache shrinking).

[0, offset] bytes of the page remain valid (this is for a case of not-page
aligned truncate). Lustre leaves partially truncated page in the cache,



.. _`ll_invalidatepage.relying-on-struct-inode`:

relying on struct inode
-----------------------

:i_size to limit further accesses.

