.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/rw.c

.. _`ll_ra_count_get`:

ll_ra_count_get
===============

.. c:function:: unsigned long ll_ra_count_get(struct ll_sb_info *sbi, struct ra_io_arg *ria, unsigned long pages, unsigned long min)

    thread.

    :param struct ll_sb_info \*sbi:
        *undescribed*

    :param struct ra_io_arg \*ria:
        *undescribed*

    :param unsigned long pages:
        *undescribed*

    :param unsigned long min:
        *undescribed*

.. _`ll_ra_count_get.description`:

Description
-----------

/param sbi superblock for filesystem readahead state ll_ra_info
/param ria per-thread readahead state
/param pages number of pages requested for readahead for the thread.

.. _`ll_ra_count_get.warning`:

WARNING
-------

This algorithm is used to reduce contention on sbi->ll_lock.
It should work well if the ra_max_pages is much greater than the single
file's read-ahead window, and not too many threads contending for
these readahead pages.

.. _`ll_ra_count_get.todo`:

TODO
----

There may be a 'global sync problem' if many threads are trying
to get an ra budget that is larger than the remaining readahead pages
and reach here at exactly the same time. They will compute /a ret to
consume the remaining pages, but will fail at \ :c:func:`atomic_add_return`\  and
get a zero ra window, although there is still ra space remaining. - Jay

.. _`ll_read_ahead_page`:

ll_read_ahead_page
==================

.. c:function:: int ll_read_ahead_page(const struct lu_env *env, struct cl_io *io, struct cl_page_list *queue, pgoff_t index)

    ahead of a page with given index.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct cl_page_list \*queue:
        *undescribed*

    :param pgoff_t index:
        *undescribed*

.. _`ll_read_ahead_page.description`:

Description
-----------

\retval +ve: page was already uptodate so it will be skipped
from being added;
\retval -ve: page wasn't added to \a queue for error;
\retval   0: page was added into \a queue for read ahead.

.. This file was automatic generated / don't edit.

