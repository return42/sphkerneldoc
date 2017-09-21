.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_recvfrom.c

.. _`svc_rdma_recvfrom`:

svc_rdma_recvfrom
=================

.. c:function:: int svc_rdma_recvfrom(struct svc_rqst *rqstp)

    Receive an RPC call

    :param struct svc_rqst \*rqstp:
        request structure into which to receive an RPC Call

.. _`svc_rdma_recvfrom.return`:

Return
------

The positive number of bytes in the RPC Call message,
\ ``0``\  if there were no Calls ready to return,
\ ``-EINVAL``\  if the Read chunk data is too large,
\ ``-ENOMEM``\  if rdma_rw context pool was exhausted,
\ ``-ENOTCONN``\  if posting failed (connection is lost),
\ ``-EIO``\  if rdma_rw initialization failed (DMA mapping, etc).

Called in a loop when XPT_DATA is set. XPT_DATA is cleared only
when there are no remaining ctxt's to process.

The next ctxt is removed from the "receive" lists.

- If the ctxt completes a Read, then finish assembling the Call
message and return the number of bytes in the message.

- If the ctxt completes a Receive, then construct the Call
message from the contents of the Receive buffer.

- If there are no Read chunks in this message, then finish
assembling the Call message and return the number of bytes
in the message.

- If there are Read chunks in this message, post Read WRs to
pull that payload and return 0.

.. This file was automatic generated / don't edit.

