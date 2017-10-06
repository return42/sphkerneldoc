.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nvme-fc-driver.h

.. _`nvme_fc_port_info`:

struct nvme_fc_port_info
========================

.. c:type:: struct nvme_fc_port_info

    port-specific ids and FC connection-specific data element used during NVME Host role registrations

.. _`nvme_fc_port_info.definition`:

Definition
----------

.. code-block:: c

    struct nvme_fc_port_info {
        u64 node_name;
        u64 port_name;
        u32 port_role;
        u32 port_id;
    }

.. _`nvme_fc_port_info.members`:

Members
-------

node_name
    FC WWNN for the port

port_name
    FC WWPN for the port

port_role
    What NVME roles are supported (see FC_PORT_ROLE_xxx)

port_id
    FC N_Port_ID currently assigned the port. Upper 8 bits must
    be set to 0.

.. _`nvmefc_ls_req`:

struct nvmefc_ls_req
====================

.. c:type:: struct nvmefc_ls_req

    Request structure passed from NVME-FC transport to LLDD in order to perform a NVME FC-4 LS request and obtain a response.

.. _`nvmefc_ls_req.definition`:

Definition
----------

.. code-block:: c

    struct nvmefc_ls_req {
        void *rqstaddr;
        dma_addr_t rqstdma;
        u32 rqstlen;
        void *rspaddr;
        dma_addr_t rspdma;
        u32 rsplen;
        u32 timeout;
        void *private;
        void (*done)(struct nvmefc_ls_req *req, int status);
    }

.. _`nvmefc_ls_req.members`:

Members
-------

rqstaddr
    pointer to request buffer

rqstdma
    PCI DMA address of request buffer

rqstlen
    Length, in bytes, of request buffer

rspaddr
    pointer to response buffer

rspdma
    PCI DMA address of response buffer

rsplen
    Length, in bytes, of response buffer

timeout
    Maximum amount of time, in seconds, to wait for the LS response.
    If timeout exceeded, LLDD to abort LS exchange and complete
    LS request with error status.

private
    pointer to memory allocated alongside the ls request structure
    that is specifically for the LLDD to use while processing the
    request. The length of the buffer corresponds to the
    lsrqst_priv_sz value specified in the nvme_fc_port_template
    supplied by the LLDD.

done
    The callback routine the LLDD is to invoke upon completion of
    the LS request. req argument is the pointer to the original LS
    request structure. Status argument must be 0 upon success, a
    negative errno on failure (example: -ENXIO).

.. _`nvmefc_ls_req.description`:

Description
-----------

Values set by the NVME-FC layer prior to calling the LLDD ls_req
entrypoint.

.. _`nvmefc_fcp_req`:

struct nvmefc_fcp_req
=====================

.. c:type:: struct nvmefc_fcp_req

    Request structure passed from NVME-FC transport to LLDD in order to perform a NVME FCP IO operation.

.. _`nvmefc_fcp_req.definition`:

Definition
----------

.. code-block:: c

    struct nvmefc_fcp_req {
        void *cmdaddr;
        void *rspaddr;
        dma_addr_t cmddma;
        dma_addr_t rspdma;
        u16 cmdlen;
        u16 rsplen;
        u32 payload_length;
        struct sg_table sg_table;
        struct scatterlist *first_sgl;
        int sg_cnt;
        enum nvmefc_fcp_datadir io_dir;
        __le16 sqid;
        void (*done)(struct nvmefc_fcp_req *req);
        void *private;
        u32 transferred_length;
        u16 rcv_rsplen;
        u32 status;
    }

.. _`nvmefc_fcp_req.members`:

Members
-------

cmdaddr
    pointer to the FCP CMD IU buffer

rspaddr
    pointer to the FCP RSP IU buffer

cmddma
    PCI DMA address of the FCP CMD IU buffer

rspdma
    PCI DMA address of the FCP RSP IU buffer

cmdlen
    Length, in bytes, of the FCP CMD IU buffer

rsplen
    Length, in bytes, of the FCP RSP IU buffer

payload_length
    Length of DATA_IN or DATA_OUT payload data to transfer

sg_table
    scatter/gather structure for payload data

first_sgl
    memory for 1st scatter/gather list segment for payload data

sg_cnt
    number of elements in the scatter/gather list

io_dir
    direction of the FCP request (see NVMEFC_FCP_xxx)

sqid
    The nvme SQID the command is being issued on

done
    The callback routine the LLDD is to invoke upon completion of
    the FCP operation. req argument is the pointer to the original
    FCP IO operation.

private
    pointer to memory allocated alongside the FCP operation
    request structure that is specifically for the LLDD to use
    while processing the operation. The length of the buffer
    corresponds to the fcprqst_priv_sz value specified in the
    nvme_fc_port_template supplied by the LLDD.

transferred_length
    amount of payload data, in bytes, that were
    transferred. Should equal payload_length on success.

rcv_rsplen
    length, in bytes, of the FCP RSP IU received.

status
    Completion status of the FCP operation. must be 0 upon success,
    negative errno value upon failure (ex: -EIO). Note: this is
    NOT a reflection of the NVME CQE completion status. Only the
    status of the FCP operation at the NVME-FC level.

.. _`nvmefc_fcp_req.description`:

Description
-----------

Values set by the NVME-FC layer prior to calling the LLDD fcp_io
entrypoint.

Values set by the LLDD indicating completion status of the FCP operation.
Must be set prior to calling the \ :c:func:`done`\  callback.

.. _`nvme_fc_local_port`:

struct nvme_fc_local_port
=========================

.. c:type:: struct nvme_fc_local_port

    structure used between NVME-FC transport and a LLDD to reference a local NVME host port. Allocated/created by the \ :c:func:`nvme_fc_register_localport`\  transport interface.

.. _`nvme_fc_local_port.definition`:

Definition
----------

.. code-block:: c

    struct nvme_fc_local_port {
        u32 port_num;
        u32 port_role;
        u64 node_name;
        u64 port_name;
        void *private;
        u32 port_id;
        enum nvme_fc_obj_state port_state;
    }

.. _`nvme_fc_local_port.members`:

Members
-------

port_num
    NVME-FC transport host port number

port_role
    NVME roles are supported on the port (see FC_PORT_ROLE_xxx)

node_name
    FC WWNN for the port

port_name
    FC WWPN for the port

private
    pointer to memory allocated alongside the local port
    structure that is specifically for the LLDD to use.
    The length of the buffer corresponds to the local_priv_sz
    value specified in the nvme_fc_port_template supplied by
    the LLDD.

port_id
    FC N_Port_ID currently assigned the port. Upper 8 bits must
    be set to 0.

port_state
    Operational state of the port.

.. _`nvme_fc_local_port.description`:

Description
-----------

Fields with static values for the port. Initialized by the
port_info struct supplied to the registration call.

Fields with dynamic values. Values may change base on link state. LLDD
may reference fields directly to change them. Initialized by the
port_info struct supplied to the registration call.

.. _`nvme_fc_remote_port`:

struct nvme_fc_remote_port
==========================

.. c:type:: struct nvme_fc_remote_port

    structure used between NVME-FC transport and a LLDD to reference a remote NVME subsystem port. Allocated/created by the \ :c:func:`nvme_fc_register_remoteport`\  transport interface.

.. _`nvme_fc_remote_port.definition`:

Definition
----------

.. code-block:: c

    struct nvme_fc_remote_port {
        u32 port_num;
        u32 port_role;
        u64 node_name;
        u64 port_name;
        struct nvme_fc_local_port *localport;
        void *private;
        u32 port_id;
        enum nvme_fc_obj_state port_state;
    }

.. _`nvme_fc_remote_port.members`:

Members
-------

port_num
    NVME-FC transport remote subsystem port number

port_role
    NVME roles are supported on the port (see FC_PORT_ROLE_xxx)

node_name
    FC WWNN for the port

port_name
    FC WWPN for the port

localport
    pointer to the NVME-FC local host port the subsystem is
    connected to.

private
    pointer to memory allocated alongside the remote port
    structure that is specifically for the LLDD to use.
    The length of the buffer corresponds to the remote_priv_sz
    value specified in the nvme_fc_port_template supplied by
    the LLDD.

port_id
    FC N_Port_ID currently assigned the port. Upper 8 bits must
    be set to 0.

port_state
    Operational state of the remote port. Valid values are
    ONLINE or UNKNOWN.

.. _`nvme_fc_remote_port.description`:

Description
-----------

Fields with static values for the port. Initialized by the
port_info struct supplied to the registration call.

Fields with dynamic values. Values may change base on link or login
state. LLDD may reference fields directly to change them. Initialized by
the port_info struct supplied to the registration call.

.. _`nvme_fc_port_template`:

struct nvme_fc_port_template
============================

.. c:type:: struct nvme_fc_port_template

    structure containing static entrypoints and operational parameters for an LLDD that supports NVME host behavior. Passed by reference in port registrations. NVME-FC transport remembers template reference and may access it during runtime operation.

.. _`nvme_fc_port_template.definition`:

Definition
----------

.. code-block:: c

    struct nvme_fc_port_template {
        void (*localport_delete)(struct nvme_fc_local_port *);
        void (*remoteport_delete)(struct nvme_fc_remote_port *);
        int (*create_queue)(struct nvme_fc_local_port *,unsigned int qidx, u16 qsize, void **handle);
        void (*delete_queue)(struct nvme_fc_local_port *, unsigned int qidx, void *handle);
        void (*poll_queue)(struct nvme_fc_local_port *, void *handle);
        int (*ls_req)(struct nvme_fc_local_port *,struct nvme_fc_remote_port *, struct nvmefc_ls_req *);
        int (*fcp_io)(struct nvme_fc_local_port *,struct nvme_fc_remote_port *,void *hw_queue_handle, struct nvmefc_fcp_req *);
        void (*ls_abort)(struct nvme_fc_local_port *,struct nvme_fc_remote_port *, struct nvmefc_ls_req *);
        void (*fcp_abort)(struct nvme_fc_local_port *,struct nvme_fc_remote_port *,void *hw_queue_handle, struct nvmefc_fcp_req *);
        u32 max_hw_queues;
        u16 max_sgl_segments;
        u16 max_dif_sgl_segments;
        u64 dma_boundary;
        u32 local_priv_sz;
        u32 remote_priv_sz;
        u32 lsrqst_priv_sz;
        u32 fcprqst_priv_sz;
    }

.. _`nvme_fc_port_template.members`:

Members
-------

localport_delete
    The LLDD initiates deletion of a localport via
    \ :c:func:`nvme_fc_deregister_localport`\ . However, the teardown is
    asynchronous. This routine is called upon the completion of the
    teardown to inform the LLDD that the localport has been deleted.
    Entrypoint is Mandatory.

remoteport_delete
    The LLDD initiates deletion of a remoteport via
    \ :c:func:`nvme_fc_deregister_remoteport`\ . However, the teardown is
    asynchronous. This routine is called upon the completion of the
    teardown to inform the LLDD that the remoteport has been deleted.
    Entrypoint is Mandatory.

create_queue
    Upon creating a host<->controller association, queues are
    created such that they can be affinitized to cpus/cores. This
    callback into the LLDD to notify that a controller queue is being
    created.  The LLDD may choose to allocate an associated hw queue
    or map it onto a shared hw queue. Upon return from the call, the
    LLDD specifies a handle that will be given back to it for any
    command that is posted to the controller queue.  The handle can
    be used by the LLDD to map quickly to the proper hw queue for
    command execution.  The mask of cpu's that will map to this queue
    at the block-level is also passed in. The LLDD should use the
    queue id and/or cpu masks to ensure proper affinitization of the
    controller queue to the hw queue.
    Entrypoint is Optional.

delete_queue
    This is the inverse of the crete_queue. During
    host<->controller association teardown, this routine is called
    when a controller queue is being terminated. Any association with
    a hw queue should be termined. If there is a unique hw queue, the
    hw queue should be torn down.
    Entrypoint is Optional.

poll_queue
    Called to poll for the completion of an io on a blk queue.
    Entrypoint is Optional.

ls_req
    Called to issue a FC-NVME FC-4 LS service request.
    The nvme_fc_ls_req structure will fully describe the buffers for
    the request payload and where to place the response payload. The
    LLDD is to allocate an exchange, issue the LS request, obtain the
    LS response, and call the "done" routine specified in the request
    structure (argument to done is the ls request structure itself).
    Entrypoint is Mandatory.

fcp_io
    called to issue a FC-NVME I/O request.  The I/O may be for
    an admin queue or an i/o queue.  The nvmefc_fcp_req structure will

ls_abort
    called to request the LLDD to abort the indicated ls request.
    The call may return before the abort has completed. After aborting
    the request, the LLDD must still call the ls request done routine
    indicating an FC transport Aborted status.
    Entrypoint is Mandatory.

fcp_abort
    called to request the LLDD to abort the indicated fcp request.
    The call may return before the abort has completed. After aborting
    the request, the LLDD must still call the fcp request done routine
    indicating an FC transport Aborted status.
    Entrypoint is Mandatory.

max_hw_queues
    indicates the maximum number of hw queues the LLDD
    supports for cpu affinitization.
    Value is Mandatory. Must be at least 1.

max_sgl_segments
    indicates the maximum number of sgl segments supported
    by the LLDD
    Value is Mandatory. Must be at least 1. Recommend at least 256.

max_dif_sgl_segments
    indicates the maximum number of sgl segments
    supported by the LLDD for DIF operations.
    Value is Mandatory. Must be at least 1. Recommend at least 256.

dma_boundary
    indicates the dma address boundary where dma mappings
    will be split across.
    Value is Mandatory. Typical value is 0xFFFFFFFF to split across
    4Gig address boundarys

local_priv_sz
    The LLDD sets this field to the amount of additional
    memory that it would like fc nvme layer to allocate on the LLDD's
    behalf whenever a localport is allocated.  The additional memory
    area solely for the of the LLDD and its location is specified by
    the localport->private pointer.
    Value is Mandatory. Allowed to be zero.

remote_priv_sz
    The LLDD sets this field to the amount of additional
    memory that it would like fc nvme layer to allocate on the LLDD's
    behalf whenever a remoteport is allocated.  The additional memory
    area solely for the of the LLDD and its location is specified by
    the remoteport->private pointer.
    Value is Mandatory. Allowed to be zero.

lsrqst_priv_sz
    The LLDD sets this field to the amount of additional
    memory that it would like fc nvme layer to allocate on the LLDD's
    behalf whenever a ls request structure is allocated. The additional
    memory area solely for the of the LLDD and its location is
    specified by the ls_request->private pointer.
    Value is Mandatory. Allowed to be zero.

fcprqst_priv_sz
    The LLDD sets this field to the amount of additional
    memory that it would like fc nvme layer to allocate on the LLDD's
    behalf whenever a fcp request structure is allocated. The additional
    memory area solely for the of the LLDD and its location is
    specified by the fcp_request->private pointer.
    Value is Mandatory. Allowed to be zero.

.. _`nvme_fc_port_template.description`:

Description
-----------

Host/Initiator Transport Entrypoints/Parameters:

.. _`nvme_fc_port_template.fully-describe-the-io`:

fully describe the io
---------------------

the buffer containing the FC-NVME CMD IU
(which contains the SQE), the sg list for the payload if applicable,
and the buffer to place the FC-NVME RSP IU into.  The LLDD will
complete the i/o, indicating the amount of data transferred or
any transport error, and call the "done" routine specified in the
request structure (argument to done is the fcp request structure
itself).
Entrypoint is Mandatory.

.. _`nvmet_fc_port_info`:

struct nvmet_fc_port_info
=========================

.. c:type:: struct nvmet_fc_port_info

    port-specific ids and FC connection-specific data element used during NVME Subsystem role registrations

.. _`nvmet_fc_port_info.definition`:

Definition
----------

.. code-block:: c

    struct nvmet_fc_port_info {
        u64 node_name;
        u64 port_name;
        u32 port_id;
    }

.. _`nvmet_fc_port_info.members`:

Members
-------

node_name
    FC WWNN for the port

port_name
    FC WWPN for the port

port_id
    FC N_Port_ID currently assigned the port. Upper 8 bits must
    be set to 0.

.. _`nvmefc_tgt_ls_req`:

struct nvmefc_tgt_ls_req
========================

.. c:type:: struct nvmefc_tgt_ls_req

    Structure used between LLDD and NVMET-FC layer to represent the exchange context for a FC-NVME Link Service (LS).

.. _`nvmefc_tgt_ls_req.definition`:

Definition
----------

.. code-block:: c

    struct nvmefc_tgt_ls_req {
        void *rspbuf;
        dma_addr_t rspdma;
        u16 rsplen;
        void (*done)(struct nvmefc_tgt_ls_req *req);
        void *nvmet_fc_private;
    }

.. _`nvmefc_tgt_ls_req.members`:

Members
-------

rspbuf
    pointer to the LS response buffer

rspdma
    PCI DMA address of the LS response buffer

rsplen
    Length, in bytes, of the LS response buffer

done
    The callback routine the LLDD is to invoke upon completion of
    transmitting the LS response. req argument is the pointer to
    the original ls request.

nvmet_fc_private
    pointer to an internal NVMET-FC layer structure used
    as part of the NVMET-FC processing. The LLDD is not to access
    this pointer.

.. _`nvmefc_tgt_ls_req.description`:

Description
-----------

The structure is allocated by the LLDD whenever a LS Request is received
from the FC link. The address of the structure is passed to the nvmet-fc
layer via the \ :c:func:`nvmet_fc_rcv_ls_req`\  call. The address of the structure
will be passed back to the LLDD when the response is to be transmit.
The LLDD is to use the address to map back to the LLDD exchange structure
which maintains information such as the targetport the LS was received
on, the remote FC NVME initiator that sent the LS, and any FC exchange
context.  Upon completion of the LS response transmit, the address of the
structure will be passed back to the LS rsp \ :c:func:`done`\  routine, allowing the
nvmet-fc layer to release dma resources. Upon completion of the \ :c:func:`done`\ 
routine, no further access will be made by the nvmet-fc layer and the
LLDD can de-allocate the structure.

.. _`nvmefc_tgt_ls_req.field-initialization`:

Field initialization
--------------------

At the time of the \ :c:func:`nvmet_fc_rcv_ls_req`\  call, there is no content that
is valid in the structure.

When the structure is used for the LLDD->xmt_ls_rsp() call, the nvmet-fc
layer will fully set the fields in order to specify the response
payload buffer and its length as well as the done routine to be called
upon compeletion of the transmit.  The nvmet-fc layer will also set a
private pointer for its own use in the done routine.

Values set by the NVMET-FC layer prior to calling the LLDD xmt_ls_rsp
entrypoint.

.. _`nvmefc_tgt_fcp_req`:

struct nvmefc_tgt_fcp_req
=========================

.. c:type:: struct nvmefc_tgt_fcp_req

    Structure used between LLDD and NVMET-FC layer to represent the exchange context and the specific FC-NVME IU operation(s) to perform for a FC-NVME FCP IO.

.. _`nvmefc_tgt_fcp_req.definition`:

Definition
----------

.. code-block:: c

    struct nvmefc_tgt_fcp_req {
        u8 op;
        u16 hwqid;
        u32 offset;
        u32 timeout;
        u32 transfer_length;
        struct fc_ba_rjt ba_rjt;
        struct scatterlist *sg;
        int sg_cnt;
        void *rspaddr;
        dma_addr_t rspdma;
        u16 rsplen;
        void (*done)(struct nvmefc_tgt_fcp_req *);
        void *nvmet_fc_private;
        u32 transferred_length;
        int fcp_error;
    }

.. _`nvmefc_tgt_fcp_req.members`:

Members
-------

op
    Indicates the FCP IU operation to perform (see NVMET_FCOP_xxx)

hwqid
    Specifies the hw queue index (0..N-1, where N is the
    max_hw_queues value from the LLD's nvmet_fc_target_template)
    that the operation is to use.

offset
    Indicates the DATA_OUT/DATA_IN payload offset to be tranferred.
    Field is only valid on WRITEDATA, READDATA, or READDATA_RSP ops.

timeout
    amount of time, in seconds, to wait for a response from the NVME
    host. A value of 0 is an infinite wait.
    Valid only for the following ops:
    WRITEDATA: caps the wait for data reception
    READDATA_RSP & RSP: caps wait for FCP_CONF reception (if used)

transfer_length
    the length, in bytes, of the DATA_OUT or DATA_IN payload
    that is to be transferred.
    Valid only for the WRITEDATA, READDATA, or READDATA_RSP ops.

ba_rjt
    Contains the BA_RJT payload that is to be transferred.
    Valid only for the NVMET_FCOP_BA_RJT op.

sg
    Scatter/gather list for the DATA_OUT/DATA_IN payload data.
    Valid only for the WRITEDATA, READDATA, or READDATA_RSP ops.

sg_cnt
    Number of valid entries in the scatter/gather list.
    Valid only for the WRITEDATA, READDATA, or READDATA_RSP ops.

rspaddr
    pointer to the FCP RSP IU buffer to be transmit
    Used by RSP and READDATA_RSP ops

rspdma
    PCI DMA address of the FCP RSP IU buffer
    Used by RSP and READDATA_RSP ops

rsplen
    Length, in bytes, of the FCP RSP IU buffer
    Used by RSP and READDATA_RSP ops

done
    The callback routine the LLDD is to invoke upon completion of
    the operation. req argument is the pointer to the original
    FCP subsystem op request.

nvmet_fc_private
    pointer to an internal NVMET-FC layer structure used
    as part of the NVMET-FC processing. The LLDD is not to
    reference this field.

transferred_length
    amount of DATA_OUT payload data received by a
    a WRITEDATA operation. If not a WRITEDATA operation, value must
    be set to 0. Should equal transfer_length on success.

fcp_error
    status of the FCP operation. Must be 0 on success; on failure
    must be a NVME_SC_FC_xxxx value.

.. _`nvmefc_tgt_fcp_req.description`:

Description
-----------

Structure used between LLDD and nvmet-fc layer to represent the exchange
context for a FC-NVME FCP I/O operation (e.g. a nvme sqe, the sqe-related
memory transfers, and its assocated cqe transfer).

The structure is allocated by the LLDD whenever a FCP CMD IU is received
from the FC link. The address of the structure is passed to the nvmet-fc
layer via the \ :c:func:`nvmet_fc_rcv_fcp_req`\  call. The address of the structure
will be passed back to the LLDD for the data operations and transmit of
the response. The LLDD is to use the address to map back to the LLDD
exchange structure which maintains information such as the targetport
the FCP I/O was received on, the remote FC NVME initiator that sent the
FCP I/O, and any FC exchange context.  Upon completion of the FCP target
operation, the address of the structure will be passed back to the FCP
op \ :c:func:`done`\  routine, allowing the nvmet-fc layer to release dma resources.
Upon completion of the \ :c:func:`done`\  routine for either RSP or ABORT ops, no
further access will be made by the nvmet-fc layer and the LLDD can
de-allocate the structure.

Values set by the LLDD indicating completion status of the FCP operation.
Must be set prior to calling the \ :c:func:`done`\  callback.

.. _`nvmefc_tgt_fcp_req.field-initialization`:

Field initialization
--------------------

At the time of the \ :c:func:`nvmet_fc_rcv_fcp_req`\  call, there is no content that
is valid in the structure.

When the structure is used for an FCP target operation, the nvmet-fc
layer will fully set the fields in order to specify the scattergather
list, the transfer length, as well as the done routine to be called
upon compeletion of the operation.  The nvmet-fc layer will also set a
private pointer for its own use in the done routine.

Values set by the NVMET-FC layer prior to calling the LLDD fcp_op
entrypoint.

.. _`nvmet_fc_target_port`:

struct nvmet_fc_target_port
===========================

.. c:type:: struct nvmet_fc_target_port

    structure used between NVME-FC transport and a LLDD to reference a local NVME subsystem port. Allocated/created by the \ :c:func:`nvme_fc_register_targetport`\  transport interface.

.. _`nvmet_fc_target_port.definition`:

Definition
----------

.. code-block:: c

    struct nvmet_fc_target_port {
        u32 port_num;
        u64 node_name;
        u64 port_name;
        void *private;
        u32 port_id;
        enum nvme_fc_obj_state port_state;
    }

.. _`nvmet_fc_target_port.members`:

Members
-------

port_num
    NVME-FC transport subsytem port number

node_name
    FC WWNN for the port

port_name
    FC WWPN for the port

private
    pointer to memory allocated alongside the local port
    structure that is specifically for the LLDD to use.
    The length of the buffer corresponds to the target_priv_sz
    value specified in the nvme_fc_target_template supplied by
    the LLDD.

port_id
    FC N_Port_ID currently assigned the port. Upper 8 bits must
    be set to 0.

port_state
    Operational state of the port.

.. _`nvmet_fc_target_port.description`:

Description
-----------

Fields with static values for the port. Initialized by the
port_info struct supplied to the registration call.

Fields with dynamic values. Values may change base on link state. LLDD
may reference fields directly to change them. Initialized by the
port_info struct supplied to the registration call.

.. _`nvmet_fc_target_template`:

struct nvmet_fc_target_template
===============================

.. c:type:: struct nvmet_fc_target_template

    structure containing static entrypoints and operational parameters for an LLDD that supports NVME subsystem behavior. Passed by reference in port registrations. NVME-FC transport remembers template reference and may access it during runtime operation.

.. _`nvmet_fc_target_template.definition`:

Definition
----------

.. code-block:: c

    struct nvmet_fc_target_template {
        void (*targetport_delete)(struct nvmet_fc_target_port *tgtport);
        int (*xmt_ls_rsp)(struct nvmet_fc_target_port *tgtport, struct nvmefc_tgt_ls_req *tls_req);
        int (*fcp_op)(struct nvmet_fc_target_port *tgtport, struct nvmefc_tgt_fcp_req *fcpreq);
        void (*fcp_abort)(struct nvmet_fc_target_port *tgtport, struct nvmefc_tgt_fcp_req *fcpreq);
        void (*fcp_req_release)(struct nvmet_fc_target_port *tgtport, struct nvmefc_tgt_fcp_req *fcpreq);
        void (*defer_rcv)(struct nvmet_fc_target_port *tgtport, struct nvmefc_tgt_fcp_req *fcpreq);
        u32 max_hw_queues;
        u16 max_sgl_segments;
        u16 max_dif_sgl_segments;
        u64 dma_boundary;
        u32 target_features;
        u32 target_priv_sz;
    }

.. _`nvmet_fc_target_template.members`:

Members
-------

targetport_delete
    The LLDD initiates deletion of a targetport via
    \ :c:func:`nvmet_fc_unregister_targetport`\ . However, the teardown is
    asynchronous. This routine is called upon the completion of the
    teardown to inform the LLDD that the targetport has been deleted.
    Entrypoint is Mandatory.

xmt_ls_rsp
    Called to transmit the response to a FC-NVME FC-4 LS service.
    The nvmefc_tgt_ls_req structure is the same LLDD-supplied exchange
    structure specified in the \ :c:func:`nvmet_fc_rcv_ls_req`\  call made when
    the LS request was received.  The structure will fully describe
    the buffers for the response payload and the dma address of the
    payload. The LLDD is to transmit the response (or return a non-zero
    errno status), and upon completion of the transmit, call the
    "done" routine specified in the nvmefc_tgt_ls_req structure
    (argument to done is the ls reqwuest structure itself).
    After calling the done routine, the LLDD shall consider the
    LS handling complete and the nvmefc_tgt_ls_req structure may
    be freed/released.
    Entrypoint is Mandatory.

fcp_op
    Called to perform a data transfer or transmit a response.
    The nvmefc_tgt_fcp_req structure is the same LLDD-supplied
    exchange structure specified in the \ :c:func:`nvmet_fc_rcv_fcp_req`\  call
    made when the FCP CMD IU was received. The op field in the
    structure shall indicate the operation for the LLDD to perform
    relative to the io.
    NVMET_FCOP_READDATA operation: the LLDD is to send the
    payload data (described by sglist) to the host in 1 or
    more FC sequences (preferrably 1).  Note: the fc-nvme layer
    may call the READDATA operation multiple times for longer
    payloads.
    NVMET_FCOP_WRITEDATA operation: the LLDD is to receive the
    payload data (described by sglist) from the host via 1 or
    more FC sequences (preferrably 1). The LLDD is to generate
    the XFER_RDY IU(s) corresponding to the data being requested.
    Note: the FC-NVME layer may call the WRITEDATA operation
    multiple times for longer payloads.
    NVMET_FCOP_READDATA_RSP operation: the LLDD is to send the
    payload data (described by sglist) to the host in 1 or
    more FC sequences (preferrably 1). If an error occurs during
    payload data transmission, the LLDD is to set the
    nvmefc_tgt_fcp_req fcp_error and transferred_length field, then
    consider the operation complete. On error, the LLDD is to not
    transmit the FCP_RSP iu. If all payload data is transferred
    successfully, the LLDD is to update the nvmefc_tgt_fcp_req
    transferred_length field and may subsequently transmit the
    FCP_RSP iu payload (described by rspbuf, rspdma, rsplen).
    If FCP_CONF is supported, the LLDD is to await FCP_CONF
    reception to confirm the RSP reception by the host. The LLDD
    may retramsit the FCP_RSP iu if necessary per FC-NVME. Upon
    transmission of the FCP_RSP iu if FCP_CONF is not supported,
    or upon success/failure of FCP_CONF if it is supported, the
    LLDD is to set the nvmefc_tgt_fcp_req fcp_error field and
    consider the operation complete.
    NVMET_FCOP_RSP: the LLDD is to transmit the FCP_RSP iu payload
    (described by rspbuf, rspdma, rsplen). If FCP_CONF is
    supported, the LLDD is to await FCP_CONF reception to confirm
    the RSP reception by the host. The LLDD may retramsit the
    FCP_RSP iu if FCP_CONF is not received per FC-NVME. Upon
    transmission of the FCP_RSP iu if FCP_CONF is not supported,
    or upon success/failure of FCP_CONF if it is supported, the
    LLDD is to set the nvmefc_tgt_fcp_req fcp_error field and
    consider the operation complete.
    Upon completing the indicated operation, the LLDD is to set the
    status fields for the operation (tranferred_length and fcp_error
    status) in the request, then call the "done" routine
    indicated in the fcp request. After the operation completes,
    regardless of whether the FCP_RSP iu was successfully transmit,
    the LLDD-supplied exchange structure must remain valid until the
    transport calls the \ :c:func:`fcp_req_release`\  callback to return ownership
    of the exchange structure back to the LLDD so that it may be used
    for another fcp command.

fcp_abort
    Called by the transport to abort an active command.
    The command may be in-between operations (nothing active in LLDD)
    or may have an active WRITEDATA operation pending. The LLDD is to
    initiate the ABTS process for the command and return from the
    callback. The ABTS does not need to be complete on the command.
    The fcp_abort callback inherently cannot fail. After the
    \ :c:func:`fcp_abort`\  callback completes, the transport will wait for any
    outstanding operation (if there was one) to complete, then will
    call the \ :c:func:`fcp_req_release`\  callback to return the command's
    exchange context back to the LLDD.

fcp_req_release
    Called by the transport to return a nvmefc_tgt_fcp_req
    to the LLDD after all operations on the fcp operation are complete.
    This may be due to the command completing or upon completion of
    abort cleanup.

defer_rcv
    *undescribed*

max_hw_queues
    indicates the maximum number of hw queues the LLDD
    supports for cpu affinitization.
    Value is Mandatory. Must be at least 1.

max_sgl_segments
    indicates the maximum number of sgl segments supported
    by the LLDD
    Value is Mandatory. Must be at least 1. Recommend at least 256.

max_dif_sgl_segments
    indicates the maximum number of sgl segments
    supported by the LLDD for DIF operations.
    Value is Mandatory. Must be at least 1. Recommend at least 256.

dma_boundary
    indicates the dma address boundary where dma mappings
    will be split across.
    Value is Mandatory. Typical value is 0xFFFFFFFF to split across
    4Gig address boundarys

target_features
    The LLDD sets bits in this field to correspond to
    optional features that are supported by the LLDD.
    Refer to the NVMET_FCTGTFEAT_xxx values.
    Value is Mandatory. Allowed to be zero.

target_priv_sz
    The LLDD sets this field to the amount of additional
    memory that it would like fc nvme layer to allocate on the LLDD's
    behalf whenever a targetport is allocated.  The additional memory
    area solely for the of the LLDD and its location is specified by
    the targetport->private pointer.
    Value is Mandatory. Allowed to be zero.

.. _`nvmet_fc_target_template.description`:

Description
-----------

Subsystem/Target Transport Entrypoints/Parameters:

.. _`nvmet_fc_target_template.note`:

Note
----

when calling the done routine for READDATA or WRITEDATA
operations, the fc-nvme layer may immediate convert, in the same
thread and before returning to the LLDD, the fcp operation to
the next operation for the fcp io and call the LLDDs fcp_op
call again. If fields in the fcp request are to be accessed post
the done call, the LLDD should save their values prior to calling
the done routine, and inspect the save values after the done
routine.
Returns 0 on success, -<errno> on failure (Ex: -EIO)
Entrypoint is Mandatory.

.. This file was automatic generated / don't edit.

