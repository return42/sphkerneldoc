.. -*- coding: utf-8; mode: rst -*-

=============
ib_fmr_pool.h
=============


.. _`ib_fmr_pool_param`:

struct ib_fmr_pool_param
========================

.. c:type:: ib_fmr_pool_param

    Parameters for creating FMR pool


.. _`ib_fmr_pool_param.definition`:

Definition
----------

.. code-block:: c

  struct ib_fmr_pool_param {
    int max_pages_per_fmr;
    int page_shift;
    enum ib_access_flags access;
    int pool_size;
    int dirty_watermark;
    void (* flush_function) (struct ib_fmr_pool *pool,void               *arg);
    void * flush_arg;
    unsigned cache:1;
  };


.. _`ib_fmr_pool_param.members`:

Members
-------

:``max_pages_per_fmr``:
    Maximum number of pages per map request.

:``page_shift``:
    Log2 of sizeof "pages" mapped by this fmr

:``access``:
    Access flags for FMRs in pool.

:``pool_size``:
    Number of FMRs to allocate for pool.

:``dirty_watermark``:
    Flush is triggered when ``dirty_watermark`` dirty
    FMRs are present.

:``flush_function``:
    Callback called when unmapped FMRs are flushed and
    more FMRs are possibly available for mapping

:``flush_arg``:
    Context passed to user's flush function.

:``cache``:
    If set, FMRs may be reused after unmapping for identical map
    requests.


