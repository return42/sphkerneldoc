.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_page_alloc.h

.. _`ttm_page_alloc_init`:

ttm_page_alloc_init
===================

.. c:function:: int ttm_page_alloc_init(struct ttm_mem_global *glob, unsigned max_pages)

    :param glob:
        *undescribed*
    :type glob: struct ttm_mem_global \*

    :param max_pages:
        *undescribed*
    :type max_pages: unsigned

.. _`ttm_page_alloc_fini`:

ttm_page_alloc_fini
===================

.. c:function:: void ttm_page_alloc_fini( void)

    :param void:
        no arguments
    :type void: 

.. _`ttm_pool_populate`:

ttm_pool_populate
=================

.. c:function:: int ttm_pool_populate(struct ttm_tt *ttm, struct ttm_operation_ctx *ctx)

    :param ttm:
        The struct ttm_tt to contain the backing pages.
    :type ttm: struct ttm_tt \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

.. _`ttm_pool_populate.description`:

Description
-----------

Add backing pages to all of \ ``ttm``\ 

.. _`ttm_pool_unpopulate`:

ttm_pool_unpopulate
===================

.. c:function:: void ttm_pool_unpopulate(struct ttm_tt *ttm)

    :param ttm:
        The struct ttm_tt which to free backing pages.
    :type ttm: struct ttm_tt \*

.. _`ttm_pool_unpopulate.description`:

Description
-----------

Free all pages of \ ``ttm``\ 

.. _`ttm_populate_and_map_pages`:

ttm_populate_and_map_pages
==========================

.. c:function:: int ttm_populate_and_map_pages(struct device *dev, struct ttm_dma_tt *tt, struct ttm_operation_ctx *ctx)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param tt:
        *undescribed*
    :type tt: struct ttm_dma_tt \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

.. _`ttm_unmap_and_unpopulate_pages`:

ttm_unmap_and_unpopulate_pages
==============================

.. c:function:: void ttm_unmap_and_unpopulate_pages(struct device *dev, struct ttm_dma_tt *tt)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param tt:
        *undescribed*
    :type tt: struct ttm_dma_tt \*

.. _`ttm_page_alloc_debugfs`:

ttm_page_alloc_debugfs
======================

.. c:function:: int ttm_page_alloc_debugfs(struct seq_file *m, void *data)

    :param m:
        *undescribed*
    :type m: struct seq_file \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`ttm_dma_page_alloc_init`:

ttm_dma_page_alloc_init
=======================

.. c:function:: int ttm_dma_page_alloc_init(struct ttm_mem_global *glob, unsigned max_pages)

    :param glob:
        *undescribed*
    :type glob: struct ttm_mem_global \*

    :param max_pages:
        *undescribed*
    :type max_pages: unsigned

.. _`ttm_dma_page_alloc_fini`:

ttm_dma_page_alloc_fini
=======================

.. c:function:: void ttm_dma_page_alloc_fini( void)

    :param void:
        no arguments
    :type void: 

.. _`ttm_dma_page_alloc_debugfs`:

ttm_dma_page_alloc_debugfs
==========================

.. c:function:: int ttm_dma_page_alloc_debugfs(struct seq_file *m, void *data)

    :param m:
        *undescribed*
    :type m: struct seq_file \*

    :param data:
        *undescribed*
    :type data: void \*

.. This file was automatic generated / don't edit.

