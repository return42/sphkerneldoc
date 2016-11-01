.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/vvp_page.c

.. _`vvp_vmpage_error`:

vvp_vmpage_error
================

.. c:function:: void vvp_vmpage_error(struct inode *inode, struct page *vmpage, int ioret)

    :param struct inode \*inode:
        *undescribed*

    :param struct page \*vmpage:
        *undescribed*

    :param int ioret:
        *undescribed*

.. _`vvp_vmpage_error.description`:

Description
-----------

This takes inode as a separate argument, because inode on which error is to
be set can be different from \a vmpage inode in case of direct-io.

.. _`vvp_page_make_ready`:

vvp_page_make_ready
===================

.. c:function:: int vvp_page_make_ready(const struct lu_env *env, const struct cl_page_slice *slice)

    :cpo_make_ready() method.

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_page_slice \*slice:
        *undescribed*

.. _`vvp_page_make_ready.description`:

Description
-----------

This is called to yank a page from the transfer cache and to send it out as
a part of transfer. This function try-locks the page. If try-lock failed,
page is owned by some concurrent IO, and should be skipped (this is bad,
but hopefully rare situation, as it usually results in transfer being
shorter than possible).

\retval 0      success, page can be placed into transfer

\retval -EAGAIN page is either used by concurrent IO has been
truncated. Skip it.

.. This file was automatic generated / don't edit.

