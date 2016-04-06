
.. _API-rq-ioc:

======
rq_ioc
======

*man rq_ioc(9)*

*4.6.0-rc1*

determine io_context for request allocation


Synopsis
========

.. c:function:: struct io_context ⋆ rq_ioc( struct bio * bio )

Arguments
=========

``bio``
    request being allocated is for this bio (can be ``NULL``)


Description
===========

Determine io_context to use for request allocation for ``bio``. May return ``NULL`` if ``current-``>io_context doesn't exist.
