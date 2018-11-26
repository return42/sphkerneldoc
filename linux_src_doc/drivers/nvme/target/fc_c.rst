.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/target/fc.c

.. _`nvmet_fc_register_targetport`:

nvmet_fc_register_targetport
============================

.. c:function:: int nvmet_fc_register_targetport(struct nvmet_fc_port_info *pinfo, struct nvmet_fc_target_template *template, struct device *dev, struct nvmet_fc_target_port **portptr)

    transport entry point called by an LLDD to register the existence of a local NVME subystem FC port.

    :param pinfo:
        pointer to information about the port to be registered
    :type pinfo: struct nvmet_fc_port_info \*

    :param template:
        LLDD entrypoints and operational parameters for the port
    :type template: struct nvmet_fc_target_template \*

    :param dev:
        physical hardware device node port corresponds to. Will be
        used for DMA mappings
    :type dev: struct device \*

    :param portptr:
        pointer to a local port pointer. Upon success, the routine
        will allocate a nvme_fc_local_port structure and place its
        address in the local port pointer. Upon failure, local port
        pointer will be set to NULL.
    :type portptr: struct nvmet_fc_target_port \*\*

.. _`nvmet_fc_register_targetport.return`:

Return
------

a completion status. Must be 0 upon success; a negative errno
(ex: -ENXIO) upon failure.

.. _`nvmet_fc_unregister_targetport`:

nvmet_fc_unregister_targetport
==============================

.. c:function:: int nvmet_fc_unregister_targetport(struct nvmet_fc_target_port *target_port)

    transport entry point called by an LLDD to deregister/remove a previously registered a local NVME subsystem FC port.

    :param target_port:
        pointer to the (registered) target port that is to be
        deregistered.
    :type target_port: struct nvmet_fc_target_port \*

.. _`nvmet_fc_unregister_targetport.return`:

Return
------

a completion status. Must be 0 upon success; a negative errno
(ex: -ENXIO) upon failure.

.. _`nvmet_fc_rcv_ls_req`:

nvmet_fc_rcv_ls_req
===================

.. c:function:: int nvmet_fc_rcv_ls_req(struct nvmet_fc_target_port *target_port, struct nvmefc_tgt_ls_req *lsreq, void *lsreqbuf, u32 lsreqbuf_len)

    transport entry point called by an LLDD upon the reception of a NVME LS request.

    :param target_port:
        pointer to the (registered) target port the LS was
        received on.
    :type target_port: struct nvmet_fc_target_port \*

    :param lsreq:
        pointer to a lsreq request structure to be used to reference
        the exchange corresponding to the LS.
    :type lsreq: struct nvmefc_tgt_ls_req \*

    :param lsreqbuf:
        pointer to the buffer containing the LS Request
    :type lsreqbuf: void \*

    :param lsreqbuf_len:
        length, in bytes, of the received LS request
    :type lsreqbuf_len: u32

.. _`nvmet_fc_rcv_ls_req.description`:

Description
-----------

The nvmet-fc layer will copy payload to an internal structure for
processing.  As such, upon completion of the routine, the LLDD may
immediately free/reuse the LS request buffer passed in the call.

If this routine returns error, the LLDD should abort the exchange.

.. _`nvmet_fc_rcv_fcp_req`:

nvmet_fc_rcv_fcp_req
====================

.. c:function:: int nvmet_fc_rcv_fcp_req(struct nvmet_fc_target_port *target_port, struct nvmefc_tgt_fcp_req *fcpreq, void *cmdiubuf, u32 cmdiubuf_len)

    transport entry point called by an LLDD upon the reception of a NVME FCP CMD IU.

    :param target_port:
        pointer to the (registered) target port the FCP CMD IU
        was received on.
    :type target_port: struct nvmet_fc_target_port \*

    :param fcpreq:
        pointer to a fcpreq request structure to be used to reference
        the exchange corresponding to the FCP Exchange.
    :type fcpreq: struct nvmefc_tgt_fcp_req \*

    :param cmdiubuf:
        pointer to the buffer containing the FCP CMD IU
    :type cmdiubuf: void \*

    :param cmdiubuf_len:
        length, in bytes, of the received FCP CMD IU
    :type cmdiubuf_len: u32

.. _`nvmet_fc_rcv_fcp_req.description`:

Description
-----------

Pass a FC-NVME FCP CMD IU received from the FC link to the nvmet-fc
layer for processing.

The nvmet_fc layer allocates a local job structure (struct
nvmet_fc_fcp_iod) from the queue for the io and copies the
CMD IU buffer to the job structure. As such, on a successful
completion (returns 0), the LLDD may immediately free/reuse
the CMD IU buffer passed in the call.

However, in some circumstances, due to the packetized nature of FC
and the api of the FC LLDD which may issue a hw command to send the
response, but the LLDD may not get the hw completion for that command
and upcall the nvmet_fc layer before a new command may be
asynchronously received - its possible for a command to be received
before the LLDD and nvmet_fc have recycled the job structure. It gives
the appearance of more commands received than fits in the sq.
To alleviate this scenario, a temporary queue is maintained in the
transport for pending LLDD requests waiting for a queue job structure.
In these "overrun" cases, a temporary queue element is allocated
the LLDD request and CMD iu buffer information remembered, and the
routine returns a -EOVERFLOW status. Subsequently, when a queue job
structure is freed, it is immediately reallocated for anything on the
pending request list. The LLDDs \ :c:func:`defer_rcv`\  callback is called,
informing the LLDD that it may reuse the CMD IU buffer, and the io
is then started normally with the transport.

The LLDD, when receiving an -EOVERFLOW completion status, is to treat
the completion as successful but must not reuse the CMD IU buffer
until the LLDD's \ :c:func:`defer_rcv`\  callback has been called for the
corresponding struct nvmefc_tgt_fcp_req pointer.

If there is any other condition in which an error occurs, the
transport will return a non-zero status indicating the error.
In all cases other than -EOVERFLOW, the transport has not accepted the
request and the LLDD should abort the exchange.

.. _`nvmet_fc_rcv_fcp_abort`:

nvmet_fc_rcv_fcp_abort
======================

.. c:function:: void nvmet_fc_rcv_fcp_abort(struct nvmet_fc_target_port *target_port, struct nvmefc_tgt_fcp_req *fcpreq)

    transport entry point called by an LLDD upon the reception of an ABTS for a FCP command

    :param target_port:
        pointer to the (registered) target port the FCP CMD IU
        was received on.
    :type target_port: struct nvmet_fc_target_port \*

    :param fcpreq:
        pointer to the fcpreq request structure that corresponds
        to the exchange that received the ABTS.
    :type fcpreq: struct nvmefc_tgt_fcp_req \*

.. _`nvmet_fc_rcv_fcp_abort.description`:

Description
-----------

Notify the transport that an ABTS has been received for a FCP command
that had been given to the transport via \ :c:func:`nvmet_fc_rcv_fcp_req`\ . The
LLDD believes the command is still being worked on
(template_ops->fcp_req_release() has not been called).

The transport will wait for any outstanding work (an op to the LLDD,
which the lldd should complete with error due to the ABTS; or the
completion from the nvmet layer of the nvme command), then will
stop processing and call the \ :c:func:`nvmet_fc_rcv_fcp_req`\  callback to
return the i/o context to the LLDD.  The LLDD may send the BA_ACC
to the ABTS either after return from this function (assuming any
outstanding op work has been terminated) or upon the callback being
called.

.. This file was automatic generated / don't edit.

