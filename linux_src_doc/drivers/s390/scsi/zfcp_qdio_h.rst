.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_qdio.h

.. _`zfcp_qdio`:

struct zfcp_qdio
================

.. c:type:: struct zfcp_qdio

    basic qdio data structure

.. _`zfcp_qdio.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_qdio {
        struct qdio_buffer  *res_q;
        struct qdio_buffer  *req_q;
        u8 req_q_idx;
        atomic_t req_q_free;
        spinlock_t stat_lock;
        spinlock_t req_q_lock;
        unsigned long long req_q_time;
        u64 req_q_util;
        atomic_t req_q_full;
        wait_queue_head_t req_q_wq;
        struct zfcp_adapter *adapter;
        u16 max_sbale_per_sbal;
        u16 max_sbale_per_req;
    }

.. _`zfcp_qdio.members`:

Members
-------

res_q
    response queue

req_q
    request queue

req_q_idx
    index of next free buffer

req_q_free
    number of free buffers in queue

stat_lock
    lock to protect req_q_util and req_q_time

req_q_lock
    lock to serialize access to request queue

req_q_time
    time of last fill level change

req_q_util
    used for accounting

req_q_full
    queue full incidents

req_q_wq
    used to wait for SBAL availability

adapter
    adapter used in conjunction with this qdio structure

max_sbale_per_sbal
    *undescribed*

max_sbale_per_req
    *undescribed*

.. _`zfcp_qdio_req`:

struct zfcp_qdio_req
====================

.. c:type:: struct zfcp_qdio_req

    qdio queue related values for a request

.. _`zfcp_qdio_req.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_qdio_req {
        u8 sbtype;
        u8 sbal_number;
        u8 sbal_first;
        u8 sbal_last;
        u8 sbal_limit;
        u8 sbale_curr;
        u8 sbal_response;
        u16 qdio_outb_usage;
    }

.. _`zfcp_qdio_req.members`:

Members
-------

sbtype
    sbal type flags for sbale 0

sbal_number
    number of free sbals

sbal_first
    first sbal for this request

sbal_last
    last sbal for this request

sbal_limit
    last possible sbal for this request

sbale_curr
    current sbale at creation of this request

sbal_response
    sbal used in interrupt

qdio_outb_usage
    usage of outbound queue

.. _`zfcp_qdio_sbale_req`:

zfcp_qdio_sbale_req
===================

.. c:function:: struct qdio_buffer_element *zfcp_qdio_sbale_req(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req)

    return pointer to sbale on req_q for a request

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        *undescribed*

.. _`zfcp_qdio_sbale_req.return`:

Return
------

pointer to qdio_buffer_element (sbale) structure

.. _`zfcp_qdio_sbale_curr`:

zfcp_qdio_sbale_curr
====================

.. c:function:: struct qdio_buffer_element *zfcp_qdio_sbale_curr(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req)

    return current sbale on req_q for a request

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        *undescribed*

.. _`zfcp_qdio_sbale_curr.return`:

Return
------

pointer to qdio_buffer_element (sbale) structure

.. _`zfcp_qdio_req_init`:

zfcp_qdio_req_init
==================

.. c:function:: void zfcp_qdio_req_init(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req, unsigned long req_id, u8 sbtype, void *data, u32 len)

    initialize qdio request

    :param struct zfcp_qdio \*qdio:
        request queue where to start putting the request

    :param struct zfcp_qdio_req \*q_req:
        the qdio request to start

    :param unsigned long req_id:
        The request id

    :param u8 sbtype:
        type flags to set for all sbals

    :param void \*data:
        First data block

    :param u32 len:
        Length of first data block

.. _`zfcp_qdio_req_init.description`:

Description
-----------

This is the start of putting the request into the queue, the last
step is passing the request to zfcp_qdio_send. The request queue
lock must be held during the whole process from init to send.

.. _`zfcp_qdio_fill_next`:

zfcp_qdio_fill_next
===================

.. c:function:: void zfcp_qdio_fill_next(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req, void *data, u32 len)

    Fill next sbale, only for single sbal requests

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        pointer to struct zfcp_queue_req

    :param void \*data:
        *undescribed*

    :param u32 len:
        *undescribed*

.. _`zfcp_qdio_fill_next.description`:

Description
-----------

This is only required for single sbal requests, calling it when
wrapping around to the next sbal is a bug.

.. _`zfcp_qdio_set_sbale_last`:

zfcp_qdio_set_sbale_last
========================

.. c:function:: void zfcp_qdio_set_sbale_last(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req)

    set last entry flag in current sbale

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        pointer to struct zfcp_queue_req

.. _`zfcp_qdio_sg_one_sbale`:

zfcp_qdio_sg_one_sbale
======================

.. c:function:: int zfcp_qdio_sg_one_sbale(struct scatterlist *sg)

    check if one sbale is enough for sg data

    :param struct scatterlist \*sg:
        The scatterlist where to check the data size

.. _`zfcp_qdio_sg_one_sbale.return`:

Return
------

1 when one sbale is enough for the data in the scatterlist,
0 if not.

.. _`zfcp_qdio_skip_to_last_sbale`:

zfcp_qdio_skip_to_last_sbale
============================

.. c:function:: void zfcp_qdio_skip_to_last_sbale(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req)

    skip to last sbale in sbal

    :param struct zfcp_qdio \*qdio:
        *undescribed*

    :param struct zfcp_qdio_req \*q_req:
        The current zfcp_qdio_req

.. _`zfcp_qdio_sbal_limit`:

zfcp_qdio_sbal_limit
====================

.. c:function:: void zfcp_qdio_sbal_limit(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req, int max_sbals)

    set the sbal limit for a request in q_req

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        The current zfcp_qdio_req

    :param int max_sbals:
        maximum number of SBALs allowed

.. _`zfcp_qdio_set_data_div`:

zfcp_qdio_set_data_div
======================

.. c:function:: void zfcp_qdio_set_data_div(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req, u32 count)

    set data division count

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        The current zfcp_qdio_req

    :param u32 count:
        The data division count

.. _`zfcp_qdio_sbale_count`:

zfcp_qdio_sbale_count
=====================

.. c:function:: unsigned int zfcp_qdio_sbale_count(struct scatterlist *sg)

    count sbale used

    :param struct scatterlist \*sg:
        pointer to struct scatterlist

.. _`zfcp_qdio_real_bytes`:

zfcp_qdio_real_bytes
====================

.. c:function:: unsigned int zfcp_qdio_real_bytes(struct scatterlist *sg)

    count bytes used

    :param struct scatterlist \*sg:
        pointer to struct scatterlist

.. _`zfcp_qdio_set_scount`:

zfcp_qdio_set_scount
====================

.. c:function:: void zfcp_qdio_set_scount(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req)

    set SBAL count value

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        The current zfcp_qdio_req

.. This file was automatic generated / don't edit.

