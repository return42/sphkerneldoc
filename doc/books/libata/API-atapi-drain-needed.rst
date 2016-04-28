.. -*- coding: utf-8; mode: rst -*-

.. _API-atapi-drain-needed:

==================
atapi_drain_needed
==================

*man atapi_drain_needed(9)*

*4.6.0-rc5*

Check whether data transfer may overflow


Synopsis
========

.. c:function:: int atapi_drain_needed( struct request * rq )

Arguments
=========

``rq``
    request to be checked


Description
===========

ATAPI commands which transfer variable length data to host might
overflow due to application error or hardare bug. This function checks
whether overflow should be drained and ignored for ``request``.


LOCKING
=======

None.


RETURNS
=======

1 if ; otherwise, 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
