.. -*- coding: utf-8; mode: rst -*-

.. _API-svc-print-addr:

==============
svc_print_addr
==============

*man svc_print_addr(9)*

*4.6.0-rc5*

Format rq_addr field for printing


Synopsis
========

.. c:function:: char * svc_print_addr( struct svc_rqst * rqstp, char * buf, size_t len )

Arguments
=========

``rqstp``
    svc_rqst struct containing address to print

``buf``
    target buffer for formatted address

``len``
    length of target buffer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
