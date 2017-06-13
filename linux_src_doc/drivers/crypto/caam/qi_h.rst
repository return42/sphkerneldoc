.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/qi.h

.. _`caam_drv_ctx_init`:

caam_drv_ctx_init
=================

.. c:function:: struct caam_drv_ctx *caam_drv_ctx_init(struct device *qidev, int *cpu, u32 *sh_desc)

    Initialise a CAAM/QI driver context

    :param struct device \*qidev:
        *undescribed*

    :param int \*cpu:
        CPU where the application prefers to the driver to receive CAAM
        responses. The request completion callback would be issued from this
        CPU.

    :param u32 \*sh_desc:
        shared descriptor pointer to be attached with CAAM/QI driver
        context.

.. _`caam_drv_ctx_init.description`:

Description
-----------

A CAAM/QI driver context must be attached with each cryptographic context.
This function allocates memory for CAAM/QI context and returns a handle to
the application. This handle must be submitted along with each enqueue
request to the driver by the application.

Returns a driver context on success or negative error code on failure.

.. _`caam_qi_enqueue`:

caam_qi_enqueue
===============

.. c:function:: int caam_qi_enqueue(struct device *qidev, struct caam_drv_req *req)

    Submit a request to QI backend driver.

    :param struct device \*qidev:
        device pointer for QI backend

    :param struct caam_drv_req \*req:
        CAAM QI request structure

.. _`caam_qi_enqueue.description`:

Description
-----------

The request structure must be properly filled as described above.

Returns 0 on success or negative error code on failure.

.. _`caam_drv_ctx_busy`:

caam_drv_ctx_busy
=================

.. c:function:: bool caam_drv_ctx_busy(struct caam_drv_ctx *drv_ctx)

    Check if there are too many jobs pending with CAAM or too many CAAM responses are pending to be processed.

    :param struct caam_drv_ctx \*drv_ctx:
        driver context for which job is to be submitted

.. _`caam_drv_ctx_busy.description`:

Description
-----------

Returns caam congestion status 'true/false'

.. _`caam_drv_ctx_update`:

caam_drv_ctx_update
===================

.. c:function:: int caam_drv_ctx_update(struct caam_drv_ctx *drv_ctx, u32 *sh_desc)

    Update QI driver context

    :param struct caam_drv_ctx \*drv_ctx:
        driver context to be updated

    :param u32 \*sh_desc:
        new shared descriptor pointer to be updated in QI driver context

.. _`caam_drv_ctx_update.description`:

Description
-----------

Invoked when shared descriptor is required to be change in driver context.

Returns 0 on success or negative error code on failure.

.. _`caam_drv_ctx_rel`:

caam_drv_ctx_rel
================

.. c:function:: void caam_drv_ctx_rel(struct caam_drv_ctx *drv_ctx)

    Release a QI driver context

    :param struct caam_drv_ctx \*drv_ctx:
        context to be released

.. _`qi_cache_alloc`:

qi_cache_alloc
==============

.. c:function:: void *qi_cache_alloc(gfp_t flags)

    Allocate buffers from CAAM-QI cache

    :param gfp_t flags:
        flags that would be used for the equivalent malloc(..) call

.. _`qi_cache_alloc.description`:

Description
-----------

Invoked when a user of the CAAM-QI (i.e. caamalg-qi) needs data which has
to be allocated on the hotpath. Instead of using malloc, one can use the
services of the CAAM QI memory cache (backed by kmem_cache). The buffers
will have a size of 256B, which is sufficient for hosting 16 SG entries.

Returns a pointer to a retrieved buffer on success or NULL on failure.

.. _`qi_cache_free`:

qi_cache_free
=============

.. c:function:: void qi_cache_free(void *obj)

    Frees buffers allocated from CAAM-QI cache

    :param void \*obj:
        object previously allocated using \ :c:func:`qi_cache_alloc`\ 

.. _`qi_cache_free.description`:

Description
-----------

Invoked when a user of the CAAM-QI (i.e. caamalg-qi) no longer needs
the buffer previously allocated by a qi_cache_alloc call.
No checking is being done, the call is a passthrough call to
kmem_cache_free(...)

.. This file was automatic generated / don't edit.

