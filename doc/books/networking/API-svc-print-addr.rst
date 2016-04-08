
.. _API-svc-print-addr:

==============
svc_print_addr
==============

*man svc_print_addr(9)*

*4.6.0-rc1*

Format rq_addr field for printing


Synopsis
========

.. c:function:: char ⋆ svc_print_addr( struct svc_rqst * rqstp, char * buf, size_t len )

Arguments
=========

``rqstp``
    svc_rqst struct containing address to print

``buf``
    target buffer for formatted address

``len``
    length of target buffer
