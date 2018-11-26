.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/ti/knav_qmss_queue.c

.. _`knav_queue_notify`:

knav_queue_notify
=================

.. c:function:: void knav_queue_notify(struct knav_queue_inst *inst)

    qmss queue notfier call

    :param inst:
        qmss queue instance like accumulator
    :type inst: struct knav_queue_inst \*

.. _`knav_queue_open`:

knav_queue_open
===============

.. c:function:: void *knav_queue_open(const char *name, unsigned id, unsigned flags)

    open a hardware queue \ ``name``\                 - name to give the queue handle \ ``id``\                   - desired queue number if any or specifes the type of queue

    :param name:
        *undescribed*
    :type name: const char \*

    :param id:
        *undescribed*
    :type id: unsigned

    :param flags:
        KNAV_QUEUE_SHARED - allow the queue to be shared. Queues are
        exclusive by default.
        Subsequent attempts to open a shared queue should
        also have this flag.
    :type flags: unsigned

.. _`knav_queue_open.description`:

Description
-----------

Returns a handle to the open hardware queue if successful. Use \ :c:func:`IS_ERR`\ 
to check the returned value for error codes.

.. _`knav_queue_close`:

knav_queue_close
================

.. c:function:: void knav_queue_close(void *qhandle)

    close a hardware queue handle \ ``qh``\                   - handle to close

    :param qhandle:
        *undescribed*
    :type qhandle: void \*

.. _`knav_queue_device_control`:

knav_queue_device_control
=========================

.. c:function:: int knav_queue_device_control(void *qhandle, enum knav_queue_ctrl_cmd cmd, unsigned long arg)

    Perform control operations on a queue \ ``qh``\                           - queue handle \ ``cmd``\                          - control commands \ ``arg``\                          - command argument

    :param qhandle:
        *undescribed*
    :type qhandle: void \*

    :param cmd:
        *undescribed*
    :type cmd: enum knav_queue_ctrl_cmd

    :param arg:
        *undescribed*
    :type arg: unsigned long

.. _`knav_queue_device_control.description`:

Description
-----------

Returns 0 on success, errno otherwise.

.. _`knav_queue_push`:

knav_queue_push
===============

.. c:function:: int knav_queue_push(void *qhandle, dma_addr_t dma, unsigned size, unsigned flags)

    push data (or descriptor) to the tail of a queue \ ``qh``\                   - hardware queue handle \ ``data``\                 - data to push \ ``size``\                 - size of data to push \ ``flags``\                - can be used to pass additional information

    :param qhandle:
        *undescribed*
    :type qhandle: void \*

    :param dma:
        *undescribed*
    :type dma: dma_addr_t

    :param size:
        *undescribed*
    :type size: unsigned

    :param flags:
        *undescribed*
    :type flags: unsigned

.. _`knav_queue_push.description`:

Description
-----------

Returns 0 on success, errno otherwise.

.. _`knav_queue_pop`:

knav_queue_pop
==============

.. c:function:: dma_addr_t knav_queue_pop(void *qhandle, unsigned *size)

    pop data (or descriptor) from the head of a queue \ ``qh``\                   - hardware queue handle \ ``size``\                 - (optional) size of the data pop'ed.

    :param qhandle:
        *undescribed*
    :type qhandle: void \*

    :param size:
        *undescribed*
    :type size: unsigned \*

.. _`knav_queue_pop.description`:

Description
-----------

Returns a DMA address on success, 0 on failure.

.. _`knav_pool_create`:

knav_pool_create
================

.. c:function:: void *knav_pool_create(const char *name, int num_desc, int region_id)

    Create a pool of descriptors \ ``name``\                 - name to give the pool handle \ ``num_desc``\             - numbers of descriptors in the pool \ ``region_id``\            - QMSS region id from which the descriptors are to be allocated.

    :param name:
        *undescribed*
    :type name: const char \*

    :param num_desc:
        *undescribed*
    :type num_desc: int

    :param region_id:
        *undescribed*
    :type region_id: int

.. _`knav_pool_create.description`:

Description
-----------

Returns a pool handle on success.
Use \ :c:func:`IS_ERR_OR_NULL`\  to identify error values on return.

.. _`knav_pool_destroy`:

knav_pool_destroy
=================

.. c:function:: void knav_pool_destroy(void *ph)

    Free a pool of descriptors \ ``pool``\                 - pool handle

    :param ph:
        *undescribed*
    :type ph: void \*

.. _`knav_pool_desc_get`:

knav_pool_desc_get
==================

.. c:function:: void *knav_pool_desc_get(void *ph)

    Get a descriptor from the pool \ ``pool``\                         - pool handle

    :param ph:
        *undescribed*
    :type ph: void \*

.. _`knav_pool_desc_get.description`:

Description
-----------

Returns descriptor from the pool.

.. _`knav_pool_desc_put`:

knav_pool_desc_put
==================

.. c:function:: void knav_pool_desc_put(void *ph, void *desc)

    return a descriptor to the pool \ ``pool``\                         - pool handle

    :param ph:
        *undescribed*
    :type ph: void \*

    :param desc:
        *undescribed*
    :type desc: void \*

.. _`knav_pool_desc_map`:

knav_pool_desc_map
==================

.. c:function:: int knav_pool_desc_map(void *ph, void *desc, unsigned size, dma_addr_t *dma, unsigned *dma_sz)

    Map descriptor for DMA transfer \ ``pool``\                         - pool handle \ ``desc``\                         - address of descriptor to map \ ``size``\                         - size of descriptor to map \ ``dma``\                          - DMA address return pointer \ ``dma_sz``\                       - adjusted return pointer

    :param ph:
        *undescribed*
    :type ph: void \*

    :param desc:
        *undescribed*
    :type desc: void \*

    :param size:
        *undescribed*
    :type size: unsigned

    :param dma:
        *undescribed*
    :type dma: dma_addr_t \*

    :param dma_sz:
        *undescribed*
    :type dma_sz: unsigned \*

.. _`knav_pool_desc_map.description`:

Description
-----------

Returns 0 on success, errno otherwise.

.. _`knav_pool_desc_unmap`:

knav_pool_desc_unmap
====================

.. c:function:: void *knav_pool_desc_unmap(void *ph, dma_addr_t dma, unsigned dma_sz)

    Unmap descriptor after DMA transfer \ ``pool``\                         - pool handle \ ``dma``\                          - DMA address of descriptor to unmap \ ``dma_sz``\                       - size of descriptor to unmap

    :param ph:
        *undescribed*
    :type ph: void \*

    :param dma:
        *undescribed*
    :type dma: dma_addr_t

    :param dma_sz:
        *undescribed*
    :type dma_sz: unsigned

.. _`knav_pool_desc_unmap.description`:

Description
-----------

Returns descriptor address on success, Use \ :c:func:`IS_ERR_OR_NULL`\  to identify
error values on return.

.. _`knav_pool_count`:

knav_pool_count
===============

.. c:function:: int knav_pool_count(void *ph)

    Get the number of descriptors in pool. \ ``pool``\                 - pool handle Returns number of elements in the pool.

    :param ph:
        *undescribed*
    :type ph: void \*

.. This file was automatic generated / don't edit.

