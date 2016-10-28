.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/rw26.c

.. _`ll_invalidatepage`:

ll_invalidatepage
=================

.. c:function:: void ll_invalidatepage(struct page *vmpage, unsigned int offset, unsigned int length)

    :\ :c:func:`invalidatepage`\  method. This method is called when the page is truncate from a file, either as a result of explicit truncate, or when inode is removed from memory (as a result of final \ :c:func:`iput`\ , umount, or memory pressure induced icache shrinking).

    :param struct page \*vmpage:
        *undescribed*

    :param unsigned int offset:
        *undescribed*

    :param unsigned int length:
        *undescribed*

.. _`ll_invalidatepage.description`:

Description
-----------

[0, offset] bytes of the page remain valid (this is for a case of not-page
aligned truncate). Lustre leaves partially truncated page in the cache,
relying on struct inode::i_size to limit further accesses.

.. _`ll_prepare_partial_page`:

ll_prepare_partial_page
=======================

.. c:function:: int ll_prepare_partial_page(const struct lu_env *env, struct cl_io *io, struct cl_page *pg)

    to page for a write.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page \*pg:
        *undescribed*

.. This file was automatic generated / don't edit.

