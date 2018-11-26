.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_aux.c

.. _`zfcp_get_port_by_wwpn`:

zfcp_get_port_by_wwpn
=====================

.. c:function:: struct zfcp_port *zfcp_get_port_by_wwpn(struct zfcp_adapter *adapter, u64 wwpn)

    find port in port list of adapter by wwpn

    :param adapter:
        pointer to adapter to search for port
    :type adapter: struct zfcp_adapter \*

    :param wwpn:
        wwpn to search for
    :type wwpn: u64

.. _`zfcp_get_port_by_wwpn.return`:

Return
------

pointer to zfcp_port or NULL

.. _`zfcp_status_read_refill`:

zfcp_status_read_refill
=======================

.. c:function:: int zfcp_status_read_refill(struct zfcp_adapter *adapter)

    refill the long running status_read_requests

    :param adapter:
        ptr to struct zfcp_adapter for which the buffers should be refilled
    :type adapter: struct zfcp_adapter \*

.. _`zfcp_status_read_refill.return`:

Return
------

0 on success, 1 otherwise

if there are 16 or more status_read requests missing an adapter_reopen
is triggered

.. _`zfcp_adapter_enqueue`:

zfcp_adapter_enqueue
====================

.. c:function:: struct zfcp_adapter *zfcp_adapter_enqueue(struct ccw_device *ccw_device)

    enqueue a new adapter to the list

    :param ccw_device:
        pointer to the struct cc_device
    :type ccw_device: struct ccw_device \*

.. _`zfcp_adapter_enqueue.return`:

Return
------

struct zfcp_adapter\*
Enqueues an adapter at the end of the adapter list in the driver data.
All adapter internal structures are set up.
Proc-fs entries are also created.

.. _`zfcp_adapter_release`:

zfcp_adapter_release
====================

.. c:function:: void zfcp_adapter_release(struct kref *ref)

    remove the adapter from the resource list

    :param ref:
        pointer to struct kref
    :type ref: struct kref \*

.. _`zfcp_adapter_release.locks`:

locks
-----

adapter list write lock is assumed to be held by caller

.. _`zfcp_port_enqueue`:

zfcp_port_enqueue
=================

.. c:function:: struct zfcp_port *zfcp_port_enqueue(struct zfcp_adapter *adapter, u64 wwpn, u32 status, u32 d_id)

    enqueue port to port list of adapter

    :param adapter:
        adapter where remote port is added
    :type adapter: struct zfcp_adapter \*

    :param wwpn:
        WWPN of the remote port to be enqueued
    :type wwpn: u64

    :param status:
        initial status for the port
    :type status: u32

    :param d_id:
        destination id of the remote port to be enqueued
    :type d_id: u32

.. _`zfcp_port_enqueue.return`:

Return
------

pointer to enqueued port on success, ERR_PTR on error

All port internal structures are set up and the sysfs entry is generated.
d_id is used to enqueue ports with a well known address like the Directory
Service for nameserver lookup.

.. _`zfcp_sg_free_table`:

zfcp_sg_free_table
==================

.. c:function:: void zfcp_sg_free_table(struct scatterlist *sg, int count)

    free memory used by scatterlists

    :param sg:
        pointer to scatterlist
    :type sg: struct scatterlist \*

    :param count:
        number of scatterlist which are to be free'ed
        the scatterlist are expected to reference pages always
    :type count: int

.. _`zfcp_sg_setup_table`:

zfcp_sg_setup_table
===================

.. c:function:: int zfcp_sg_setup_table(struct scatterlist *sg, int count)

    init scatterlist and allocate, assign buffers

    :param sg:
        pointer to struct scatterlist
    :type sg: struct scatterlist \*

    :param count:
        number of scatterlists which should be assigned with buffers
        of size page
    :type count: int

.. _`zfcp_sg_setup_table.return`:

Return
------

0 on success, -ENOMEM otherwise

.. This file was automatic generated / don't edit.

