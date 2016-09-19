.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_fsf.h

.. _`zfcp_fsf_ct_els`:

struct zfcp_fsf_ct_els
======================

.. c:type:: struct zfcp_fsf_ct_els

    zfcp data for ct or els request

.. _`zfcp_fsf_ct_els.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_fsf_ct_els {
        struct scatterlist *req;
        struct scatterlist *resp;
        void (*handler)(void *);
        void *handler_data;
        struct zfcp_port *port;
        int status;
    }

.. _`zfcp_fsf_ct_els.members`:

Members
-------

req
    scatter-gather list for request

resp
    scatter-gather list for response

handler
    handler function (called for response to the request)

handler_data
    data passed to handler function

port
    Optional pointer to port for zfcp internal ELS (only test link ADISC)

status
    used to pass error status to calling function

.. This file was automatic generated / don't edit.

