.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_elsct.c

.. _`fc_elsct_send`:

fc_elsct_send
=============

.. c:function:: struct fc_seq *fc_elsct_send(struct fc_lport *lport, u32 did, struct fc_frame *fp, unsigned int op, void (*resp)(struct fc_seq *, struct fc_frame *, void *), void *arg, u32 timer_msec)

    Send an ELS or CT frame

    :param lport:
        The local port to send the frame on
    :type lport: struct fc_lport \*

    :param did:
        The destination ID for the frame
    :type did: u32

    :param fp:
        The frame to be sent
    :type fp: struct fc_frame \*

    :param op:
        The operational code
    :type op: unsigned int

    :param void (\*resp)(struct fc_seq \*, struct fc_frame \*, void \*):
        The callback routine when the response is received

    :param arg:
        The argument to pass to the response callback routine
    :type arg: void \*

    :param timer_msec:
        The timeout period for the frame (in msecs)
    :type timer_msec: u32

.. _`fc_elsct_init`:

fc_elsct_init
=============

.. c:function:: int fc_elsct_init(struct fc_lport *lport)

    Initialize the ELS/CT layer

    :param lport:
        The local port to initialize the ELS/CT layer for
    :type lport: struct fc_lport \*

.. _`fc_els_resp_type`:

fc_els_resp_type
================

.. c:function:: const char *fc_els_resp_type(struct fc_frame *fp)

    Return a string describing the ELS response

    :param fp:
        The frame pointer or possible error code
    :type fp: struct fc_frame \*

.. This file was automatic generated / don't edit.

