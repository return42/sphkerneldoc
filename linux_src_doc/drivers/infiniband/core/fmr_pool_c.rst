.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/fmr_pool.c

.. _`ib_create_fmr_pool`:

ib_create_fmr_pool
==================

.. c:function:: struct ib_fmr_pool *ib_create_fmr_pool(struct ib_pd *pd, struct ib_fmr_pool_param *params)

    Create an FMR pool

    :param struct ib_pd \*pd:
        Protection domain for FMRs

    :param struct ib_fmr_pool_param \*params:
        FMR pool parameters

.. _`ib_create_fmr_pool.description`:

Description
-----------

Create a pool of FMRs.  Return value is pointer to new pool or
error code if creation failed.

.. _`ib_destroy_fmr_pool`:

ib_destroy_fmr_pool
===================

.. c:function:: void ib_destroy_fmr_pool(struct ib_fmr_pool *pool)

    Free FMR pool

    :param struct ib_fmr_pool \*pool:
        FMR pool to free

.. _`ib_destroy_fmr_pool.description`:

Description
-----------

Destroy an FMR pool and free all associated resources.

.. _`ib_flush_fmr_pool`:

ib_flush_fmr_pool
=================

.. c:function:: int ib_flush_fmr_pool(struct ib_fmr_pool *pool)

    Invalidate all unmapped FMRs

    :param struct ib_fmr_pool \*pool:
        FMR pool to flush

.. _`ib_flush_fmr_pool.description`:

Description
-----------

Ensure that all unmapped FMRs are fully invalidated.

.. _`ib_fmr_pool_map_phys`:

ib_fmr_pool_map_phys
====================

.. c:function:: struct ib_pool_fmr *ib_fmr_pool_map_phys(struct ib_fmr_pool *pool_handle, u64 *page_list, int list_len, u64 io_virtual_address)

    Map an FMR from an FMR pool.

    :param struct ib_fmr_pool \*pool_handle:
        FMR pool to allocate FMR from

    :param u64 \*page_list:
        List of pages to map

    :param int list_len:
        Number of pages in \ ``page_list``\ 

    :param u64 io_virtual_address:
        I/O virtual address for new FMR

.. _`ib_fmr_pool_unmap`:

ib_fmr_pool_unmap
=================

.. c:function:: int ib_fmr_pool_unmap(struct ib_pool_fmr *fmr)

    Unmap FMR

    :param struct ib_pool_fmr \*fmr:
        FMR to unmap

.. _`ib_fmr_pool_unmap.description`:

Description
-----------

Unmap an FMR.  The FMR mapping may remain valid until the FMR is
reused (or until \ :c:func:`ib_flush_fmr_pool`\  is called).

.. This file was automatic generated / don't edit.

