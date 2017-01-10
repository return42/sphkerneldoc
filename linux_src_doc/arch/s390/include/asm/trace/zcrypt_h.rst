.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/trace/zcrypt.h

.. _`trace_s390_zcrypt_req`:

trace_s390_zcrypt_req
=====================

.. c:function:: void trace_s390_zcrypt_req(void *ptr, u32 type)

    zcrypt request tracepoint function

    :param void \*ptr:
        Address of the local buffer where the request from userspace
        is stored. Can be used as a unique id to relate together
        request and reply.

    :param u32 type:
        One of the TP\_ defines above.

.. _`trace_s390_zcrypt_req.description`:

Description
-----------

Called when a request from userspace is recognised within the ioctl
function of the zcrypt device driver and may act as an entry
timestamp.

.. _`trace_s390_zcrypt_rep`:

trace_s390_zcrypt_rep
=====================

.. c:function:: void trace_s390_zcrypt_rep(void *ptr, u32 fc, u32 rc, u16 dev, u16 dom)

    zcrypt reply tracepoint function

    :param void \*ptr:
        Address of the local buffer where the request from userspace
        is stored. Can be used as a unique id to match together
        request and reply.

    :param u32 fc:
        Function code.

    :param u32 rc:
        The bare returncode as returned by the device driver ioctl
        function.

    :param u16 dev:
        The adapter nr where this request was actually processed.

    :param u16 dom:
        Domain id of the device where this request was processed.

.. _`trace_s390_zcrypt_rep.description`:

Description
-----------

Called upon recognising the reply from the crypto adapter. This
message may act as the exit timestamp for the request but also
carries some info about on which adapter the request was processed
and the returncode from the device driver.

.. This file was automatic generated / don't edit.

