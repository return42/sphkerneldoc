.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/iser/iscsi_iser.c

.. _`iscsi_iser_pdu_alloc`:

iscsi_iser_pdu_alloc
====================

.. c:function:: int iscsi_iser_pdu_alloc(struct iscsi_task *task, uint8_t opcode)

    allocate an iscsi-iser PDU

    :param struct iscsi_task \*task:
        iscsi task

    :param uint8_t opcode:
        iscsi command opcode

.. _`iscsi_iser_pdu_alloc.netes`:

Netes
-----

This routine can't fail, just assign iscsi task
hdr and max hdr size.

.. _`iser_initialize_task_headers`:

iser_initialize_task_headers
============================

.. c:function:: int iser_initialize_task_headers(struct iscsi_task *task, struct iser_tx_desc *tx_desc)

    Initialize task headers

    :param struct iscsi_task \*task:
        iscsi task

    :param struct iser_tx_desc \*tx_desc:
        iser tx descriptor

.. _`iser_initialize_task_headers.notes`:

Notes
-----

This routine may race with iser teardown flow for scsi
error handling TMFs. So for TMF we should acquire the
state mutex to avoid dereferencing the IB device which
may have already been terminated.

.. _`iscsi_iser_task_init`:

iscsi_iser_task_init
====================

.. c:function:: int iscsi_iser_task_init(struct iscsi_task *task)

    Initialize iscsi-iser task

    :param struct iscsi_task \*task:
        iscsi task

.. _`iscsi_iser_task_init.description`:

Description
-----------

Initialize the task for the scsi command or mgmt command.

.. _`iscsi_iser_task_init.return`:

Return
------

Returns zero on success or -ENOMEM when failing
to init task headers (dma mapping error).

.. _`iscsi_iser_mtask_xmit`:

iscsi_iser_mtask_xmit
=====================

.. c:function:: int iscsi_iser_mtask_xmit(struct iscsi_conn *conn, struct iscsi_task *task)

    xmit management (immediate) task

    :param struct iscsi_conn \*conn:
        iscsi connection

    :param struct iscsi_task \*task:
        task management task

.. _`iscsi_iser_mtask_xmit.notes`:

Notes
-----

The function can return -EAGAIN in which case caller must
call it again later, or recover. '0' return code means successful
xmit.

.. _`iscsi_iser_task_xmit`:

iscsi_iser_task_xmit
====================

.. c:function:: int iscsi_iser_task_xmit(struct iscsi_task *task)

    xmit iscsi-iser task

    :param struct iscsi_task \*task:
        iscsi task

.. _`iscsi_iser_task_xmit.return`:

Return
------

zero on success or escalates \ ``$error``\  on failure.

.. _`iscsi_iser_cleanup_task`:

iscsi_iser_cleanup_task
=======================

.. c:function:: void iscsi_iser_cleanup_task(struct iscsi_task *task)

    cleanup an iscsi-iser task

    :param struct iscsi_task \*task:
        iscsi task

.. _`iscsi_iser_cleanup_task.notes`:

Notes
-----

In case the RDMA device is already NULL (might have
been removed in DEVICE_REMOVAL CM event it will bail-out
without doing dma unmapping.

.. _`iscsi_iser_check_protection`:

iscsi_iser_check_protection
===========================

.. c:function:: u8 iscsi_iser_check_protection(struct iscsi_task *task, sector_t *sector)

    check protection information status of task.

    :param struct iscsi_task \*task:
        iscsi task

    :param sector_t \*sector:
        error sector if exsists (output)

.. _`iscsi_iser_check_protection.return`:

Return
------

zero if no data-integrity errors have occured
0x1: data-integrity error occured in the guard-block
0x2: data-integrity error occured in the reference tag
0x3: data-integrity error occured in the application tag

In addition the error sector is marked.

.. _`iscsi_iser_conn_create`:

iscsi_iser_conn_create
======================

.. c:function:: struct iscsi_cls_conn *iscsi_iser_conn_create(struct iscsi_cls_session *cls_session, uint32_t conn_idx)

    create a new iscsi-iser connection

    :param struct iscsi_cls_session \*cls_session:
        iscsi class connection

    :param uint32_t conn_idx:
        connection index within the session (for MCS)

.. _`iscsi_iser_conn_create.return`:

Return
------

iscsi_cls_conn when iscsi_conn_setup succeeds or NULL
otherwise.

.. _`iscsi_iser_conn_bind`:

iscsi_iser_conn_bind
====================

.. c:function:: int iscsi_iser_conn_bind(struct iscsi_cls_session *cls_session, struct iscsi_cls_conn *cls_conn, uint64_t transport_eph, int is_leading)

    bind iscsi and iser connection structures

    :param struct iscsi_cls_session \*cls_session:
        iscsi class session

    :param struct iscsi_cls_conn \*cls_conn:
        iscsi class connection

    :param uint64_t transport_eph:
        transport end-point handle

    :param int is_leading:
        indicate if this is the session leading connection (MCS)

.. _`iscsi_iser_conn_bind.return`:

Return
------

zero on success, \ ``$error``\  if iscsi_conn_bind fails and
-EINVAL in case end-point doesn't exsits anymore or iser connection
state is not UP (teardown already started).

.. _`iscsi_iser_conn_start`:

iscsi_iser_conn_start
=====================

.. c:function:: int iscsi_iser_conn_start(struct iscsi_cls_conn *cls_conn)

    start iscsi-iser connection

    :param struct iscsi_cls_conn \*cls_conn:
        iscsi class connection

.. _`iscsi_iser_conn_start.notes`:

Notes
-----

Here iser intialize (or re-initialize) stop_completion as
from this point iscsi must call conn_stop in session/connection
teardown so iser transport must wait for it.

.. _`iscsi_iser_conn_stop`:

iscsi_iser_conn_stop
====================

.. c:function:: void iscsi_iser_conn_stop(struct iscsi_cls_conn *cls_conn, int flag)

    stop iscsi-iser connection

    :param struct iscsi_cls_conn \*cls_conn:
        iscsi class connection

    :param int flag:
        indicate if recover or terminate (passed as is)

.. _`iscsi_iser_conn_stop.notes`:

Notes
-----

Calling iscsi_conn_stop might theoretically race with
DEVICE_REMOVAL event and dereference a previously freed RDMA device
handle, so we call it under iser the state lock to protect against
this kind of race.

.. _`iscsi_iser_session_destroy`:

iscsi_iser_session_destroy
==========================

.. c:function:: void iscsi_iser_session_destroy(struct iscsi_cls_session *cls_session)

    destroy iscsi-iser session

    :param struct iscsi_cls_session \*cls_session:
        iscsi class session

.. _`iscsi_iser_session_destroy.description`:

Description
-----------

Removes and free iscsi host.

.. _`iscsi_iser_session_create`:

iscsi_iser_session_create
=========================

.. c:function:: struct iscsi_cls_session *iscsi_iser_session_create(struct iscsi_endpoint *ep, uint16_t cmds_max, uint16_t qdepth, uint32_t initial_cmdsn)

    create an iscsi-iser session

    :param struct iscsi_endpoint \*ep:
        iscsi end-point handle

    :param uint16_t cmds_max:
        maximum commands in this session

    :param uint16_t qdepth:
        session command queue depth

    :param uint32_t initial_cmdsn:
        initiator command sequnce number

.. _`iscsi_iser_session_create.description`:

Description
-----------

Allocates and adds a scsi host, expose DIF supprot if
exists, and sets up an iscsi session.

.. _`iscsi_iser_conn_get_stats`:

iscsi_iser_conn_get_stats
=========================

.. c:function:: void iscsi_iser_conn_get_stats(struct iscsi_cls_conn *cls_conn, struct iscsi_stats *stats)

    set class connection parameter

    :param struct iscsi_cls_conn \*cls_conn:
        iscsi class connection

    :param struct iscsi_stats \*stats:
        iscsi stats to output

.. _`iscsi_iser_conn_get_stats.description`:

Description
-----------

Output connection statistics.

.. _`iscsi_iser_ep_connect`:

iscsi_iser_ep_connect
=====================

.. c:function:: struct iscsi_endpoint *iscsi_iser_ep_connect(struct Scsi_Host *shost, struct sockaddr *dst_addr, int non_blocking)

    Initiate iSER connection establishment

    :param struct Scsi_Host \*shost:
        scsi_host

    :param struct sockaddr \*dst_addr:
        destination address

    :param int non_blocking:
        *undescribed*

.. _`iscsi_iser_ep_connect.description`:

Description
-----------

Allocate an iscsi endpoint, an iser_conn structure and bind them.
After that start RDMA connection establishment via rdma_cm. We
don't allocate iser_conn embedded in iscsi_endpoint since in teardown
the endpoint will be destroyed at ep_disconnect while iser_conn will
cleanup its resources asynchronuously.

.. _`iscsi_iser_ep_connect.return`:

Return
------

iscsi_endpoint created by iscsi layer or ERR_PTR(error)
if fails.

.. _`iscsi_iser_ep_poll`:

iscsi_iser_ep_poll
==================

.. c:function:: int iscsi_iser_ep_poll(struct iscsi_endpoint *ep, int timeout_ms)

    poll for iser connection establishment to complete

    :param struct iscsi_endpoint \*ep:
        iscsi endpoint (created at ep_connect)

    :param int timeout_ms:
        polling timeout allowed in ms.

.. _`iscsi_iser_ep_poll.description`:

Description
-----------

This routine boils down to waiting for up_completion signaling
that cma_id got CONNECTED event.

.. _`iscsi_iser_ep_poll.return`:

Return
------

1 if succeeded in connection establishment, 0 if timeout expired
(libiscsi will retry will kick in) or -1 if interrupted by signal
or more likely iser connection state transitioned to TEMINATING or
DOWN during the wait period.

.. _`iscsi_iser_ep_disconnect`:

iscsi_iser_ep_disconnect
========================

.. c:function:: void iscsi_iser_ep_disconnect(struct iscsi_endpoint *ep)

    Initiate connection teardown process

    :param struct iscsi_endpoint \*ep:
        iscsi endpoint handle

.. _`iscsi_iser_ep_disconnect.description`:

Description
-----------

This routine is not blocked by iser and RDMA termination process
completion as we queue a deffered work for iser/RDMA destruction
and cleanup or actually call it immediately in case we didn't pass
iscsi conn bind/start stage, thus it is safe.

.. This file was automatic generated / don't edit.

