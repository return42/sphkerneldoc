.. -*- coding: utf-8; mode: rst -*-

.. _API-rq-ioc:

======
rq_ioc
======

*man rq_ioc(9)*

*4.6.0-rc5*

determine io_context for request allocation


Synopsis
========

.. c:function:: struct io_context * rq_ioc( struct bio * bio )

Arguments
=========

``bio``
    request being allocated is for this bio (can be ``NULL``)


Description
===========

Determine io_context to use for request allocation for ``bio``. May
return ``NULL`` if ``current-``>io_context doesn't exist.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
