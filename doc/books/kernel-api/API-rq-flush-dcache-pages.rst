.. -*- coding: utf-8; mode: rst -*-

.. _API-rq-flush-dcache-pages:

=====================
rq_flush_dcache_pages
=====================

*man rq_flush_dcache_pages(9)*

*4.6.0-rc5*

Helper function to flush all pages in a request


Synopsis
========

.. c:function:: void rq_flush_dcache_pages( struct request * rq )

Arguments
=========

``rq``
    the request to be flushed


Description
===========

Flush all pages in ``rq``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
