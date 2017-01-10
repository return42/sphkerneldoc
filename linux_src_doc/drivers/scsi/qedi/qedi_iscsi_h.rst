.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qedi/qedi_iscsi.h

.. _`generic_pdu_resc`:

struct generic_pdu_resc
=======================

.. c:type:: struct generic_pdu_resc

    login pdu resource structure

.. _`generic_pdu_resc.definition`:

Definition
----------

.. code-block:: c

    struct generic_pdu_resc {
        char *req_buf;
        dma_addr_t req_dma_addr;
        u32 req_buf_size;
        char *req_wr_ptr;
        struct iscsi_hdr resp_hdr;
        char *resp_buf;
        dma_addr_t resp_dma_addr;
        u32 resp_buf_size;
        char *resp_wr_ptr;
        char *req_bd_tbl;
        dma_addr_t req_bd_dma;
        char *resp_bd_tbl;
        dma_addr_t resp_bd_dma;
    }

.. _`generic_pdu_resc.members`:

Members
-------

req_buf
    driver buffer used to stage payload associated with
    the login request

req_dma_addr
    dma address for iscsi login request payload buffer

req_buf_size
    actual login request payload length

req_wr_ptr
    pointer into login request buffer when next data is
    to be written

resp_hdr
    iscsi header where iscsi login response header is to
    be recreated

resp_buf
    buffer to stage login response payload

resp_dma_addr
    login response payload buffer dma address

resp_buf_size
    login response paylod length

resp_wr_ptr
    pointer into login response buffer when next data is
    to be written

req_bd_tbl
    iscsi login request payload BD table

req_bd_dma
    login request BD table dma address

resp_bd_tbl
    iscsi login response payload BD table

resp_bd_dma
    login request BD table dma address

.. _`generic_pdu_resc.description`:

Description
-----------

following structure defines buffer info for generic pdus such as iSCSI Login,
Logout and NOP

.. This file was automatic generated / don't edit.

