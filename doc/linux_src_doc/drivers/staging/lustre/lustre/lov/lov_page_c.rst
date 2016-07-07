.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lov/lov_page.c

.. _`lov_raid0_page_is_under_lock`:

lov_raid0_page_is_under_lock
============================

.. c:function:: int lov_raid0_page_is_under_lock(const struct lu_env *env, const struct cl_page_slice *slice, struct cl_io *unused, pgoff_t *max_index)

    page index covered by an underlying DLM lock. This function converts max_index from stripe level to file level, and make sure it's not beyond one stripe.

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_page_slice \*slice:
        *undescribed*

    :param struct cl_io \*unused:
        *undescribed*

    :param pgoff_t \*max_index:
        *undescribed*

.. This file was automatic generated / don't edit.

