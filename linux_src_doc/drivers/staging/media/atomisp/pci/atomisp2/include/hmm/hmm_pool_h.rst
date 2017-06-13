.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/atomisp/pci/atomisp2/include/hmm/hmm_pool.h

.. _`hmm_pool_ops`:

struct hmm_pool_ops
===================

.. c:type:: struct hmm_pool_ops

    memory pool callbacks.

.. _`hmm_pool_ops.definition`:

Definition
----------

.. code-block:: c

    struct hmm_pool_ops {
        int (*pool_init)(void **pool, unsigned int pool_size);
        void (*pool_exit)(void **pool);
        unsigned int (*pool_alloc_pages)(void *pool,struct hmm_page_object *page_obj, unsigned int size, bool cached);
        void (*pool_free_pages)(void *pool, struct hmm_page_object *page_obj);
        int (*pool_inited)(void *pool);
    }

.. _`hmm_pool_ops.members`:

Members
-------

pool_init
    initialize the memory pool.

pool_exit
    uninitialize the memory pool.

pool_alloc_pages
    allocate pages from memory pool.

pool_free_pages
    free pages to memory pool.

pool_inited
    check whether memory pool is initialized.

.. _`hmm_reserved_pool_info`:

struct hmm_reserved_pool_info
=============================

.. c:type:: struct hmm_reserved_pool_info

    represents reserved pool private data.

.. _`hmm_reserved_pool_info.definition`:

Definition
----------

.. code-block:: c

    struct hmm_reserved_pool_info {
        struct page **pages;
        unsigned int index;
        unsigned int pgnr;
        spinlock_t list_lock;
        bool initialized;
    }

.. _`hmm_reserved_pool_info.members`:

Members
-------

pages
    a array that store physical pages.
    The array is as reserved memory pool.

index
    to indicate the first blank page number
    in reserved memory pool(pages array).

pgnr
    the valid page amount in reserved memory
    pool.

list_lock
    list lock is used to protect the operation
    to reserved memory pool.

initialized
    *undescribed*

.. _`hmm_dynamic_pool_info`:

struct hmm_dynamic_pool_info
============================

.. c:type:: struct hmm_dynamic_pool_info

    represents dynamic pool private data.

.. _`hmm_dynamic_pool_info.definition`:

Definition
----------

.. code-block:: c

    struct hmm_dynamic_pool_info {
        struct list_head pages_list;
        spinlock_t list_lock;
        struct kmem_cache *pgptr_cache;
        bool initialized;
        unsigned int pool_size;
        unsigned int pgnr;
    }

.. _`hmm_dynamic_pool_info.members`:

Members
-------

pages_list
    a list that store physical pages.
    The pages list is as dynamic memory pool.

list_lock
    list lock is used to protect the operation
    to dynamic memory pool.

pgptr_cache
    struct kmem_cache, manages a cache.

initialized
    *undescribed*

pool_size
    *undescribed*

pgnr
    *undescribed*

.. This file was automatic generated / don't edit.

