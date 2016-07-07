.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_qdio.c

.. _`zfcp_qdio_sbals_from_sg`:

zfcp_qdio_sbals_from_sg
=======================

.. c:function:: int zfcp_qdio_sbals_from_sg(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req, struct scatterlist *sg)

    fill SBALs from scatter-gather list

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        pointer to struct zfcp_qdio_req

    :param struct scatterlist \*sg:
        scatter-gather list

.. _`zfcp_qdio_sbals_from_sg.return`:

Return
------

zero or -EINVAL on error

.. _`zfcp_qdio_sbal_get`:

zfcp_qdio_sbal_get
==================

.. c:function:: int zfcp_qdio_sbal_get(struct zfcp_qdio *qdio)

    get free sbal in request queue, wait if necessary

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

.. _`zfcp_qdio_sbal_get.description`:

Description
-----------

The req_q_lock must be held by the caller of this function, and
this function may only be called from process context; it will
sleep when waiting for a free sbal.

.. _`zfcp_qdio_sbal_get.return`:

Return
------

0 on success, -EIO if there is no free sbal after waiting.

.. _`zfcp_qdio_send`:

zfcp_qdio_send
==============

.. c:function:: int zfcp_qdio_send(struct zfcp_qdio *qdio, struct zfcp_qdio_req *q_req)

    set PCI flag in first SBALE and send req to QDIO

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

    :param struct zfcp_qdio_req \*q_req:
        pointer to struct zfcp_qdio_req

.. _`zfcp_qdio_send.return`:

Return
------

0 on success, error otherwise

.. _`zfcp_qdio_allocate`:

zfcp_qdio_allocate
==================

.. c:function:: int zfcp_qdio_allocate(struct zfcp_qdio *qdio)

    allocate queue memory and initialize QDIO data

    :param struct zfcp_qdio \*qdio:
        *undescribed*

.. _`zfcp_qdio_allocate.return`:

Return
------

-ENOMEM on memory allocation error or return value from
qdio_allocate

.. _`zfcp_qdio_close`:

zfcp_qdio_close
===============

.. c:function:: void zfcp_qdio_close(struct zfcp_qdio *qdio)

    close qdio queues for an adapter

    :param struct zfcp_qdio \*qdio:
        pointer to structure zfcp_qdio

.. _`zfcp_qdio_open`:

zfcp_qdio_open
==============

.. c:function:: int zfcp_qdio_open(struct zfcp_qdio *qdio)

    prepare and initialize response queue

    :param struct zfcp_qdio \*qdio:
        pointer to struct zfcp_qdio

.. _`zfcp_qdio_open.return`:

Return
------

0 on success, otherwise -EIO

.. _`zfcp_qdio_siosl`:

zfcp_qdio_siosl
===============

.. c:function:: void zfcp_qdio_siosl(struct zfcp_adapter *adapter)

    Trigger logging in FCP channel

    :param struct zfcp_adapter \*adapter:
        The zfcp_adapter where to trigger logging

.. _`zfcp_qdio_siosl.description`:

Description
-----------

Call the cio siosl function to trigger hardware logging.  This
wrapper function sets a flag to ensure hardware logging is only
triggered once before going through qdio shutdown.

The triggers are always run from qdio tasklet context, so no
additional synchronization is necessary.

.. This file was automatic generated / don't edit.

