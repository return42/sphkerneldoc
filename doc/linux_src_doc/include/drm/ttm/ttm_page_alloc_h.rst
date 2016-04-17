.. -*- coding: utf-8; mode: rst -*-

================
ttm_page_alloc.h
================


.. _`ttm_page_alloc_init`:

ttm_page_alloc_init
===================

.. c:function:: int ttm_page_alloc_init (struct ttm_mem_global *glob, unsigned max_pages)

    :param struct ttm_mem_global \*glob:

        *undescribed*

    :param unsigned max_pages:

        *undescribed*



.. _`ttm_page_alloc_fini`:

ttm_page_alloc_fini
===================

.. c:function:: void ttm_page_alloc_fini ( void)

    :param void:
        no arguments



.. _`ttm_pool_populate`:

ttm_pool_populate
=================

.. c:function:: int ttm_pool_populate (struct ttm_tt *ttm)

    :param struct ttm_tt \*ttm:
        The struct ttm_tt to contain the backing pages.



.. _`ttm_pool_populate.description`:

Description
-----------

Add backing pages to all of ``ttm``



.. _`ttm_pool_unpopulate`:

ttm_pool_unpopulate
===================

.. c:function:: void ttm_pool_unpopulate (struct ttm_tt *ttm)

    :param struct ttm_tt \*ttm:
        The struct ttm_tt which to free backing pages.



.. _`ttm_pool_unpopulate.description`:

Description
-----------

Free all pages of ``ttm``



.. _`ttm_page_alloc_debugfs`:

ttm_page_alloc_debugfs
======================

.. c:function:: int ttm_page_alloc_debugfs (struct seq_file *m, void *data)

    :param struct seq_file \*m:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`ttm_dma_page_alloc_init`:

ttm_dma_page_alloc_init
=======================

.. c:function:: int ttm_dma_page_alloc_init (struct ttm_mem_global *glob, unsigned max_pages)

    :param struct ttm_mem_global \*glob:

        *undescribed*

    :param unsigned max_pages:

        *undescribed*



.. _`ttm_dma_page_alloc_fini`:

ttm_dma_page_alloc_fini
=======================

.. c:function:: void ttm_dma_page_alloc_fini ( void)

    :param void:
        no arguments



.. _`ttm_dma_page_alloc_debugfs`:

ttm_dma_page_alloc_debugfs
==========================

.. c:function:: int ttm_dma_page_alloc_debugfs (struct seq_file *m, void *data)

    :param struct seq_file \*m:

        *undescribed*

    :param void \*data:

        *undescribed*

