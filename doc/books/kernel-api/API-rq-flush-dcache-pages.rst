
.. _API-rq-flush-dcache-pages:

=====================
rq_flush_dcache_pages
=====================

*man rq_flush_dcache_pages(9)*

*4.6.0-rc1*

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
