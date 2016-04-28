.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-update-request:

==================
blk_update_request
==================

*man blk_update_request(9)*

*4.6.0-rc5*

Special helper function for request stacking drivers


Synopsis
========

.. c:function:: bool blk_update_request( struct request * req, int error, unsigned int nr_bytes )

Arguments
=========

``req``
    the request being processed

``error``
    ``0`` for success, < ``0`` for error

``nr_bytes``
    number of bytes to complete ``req``


Description
===========

Ends I/O on a number of bytes attached to ``req``, but doesn't complete
the request structure even if ``req`` doesn't have leftover. If ``req``
has leftover, sets it up for the next range of segments.

This special helper function is only for request stacking drivers (e.g.
request-based dm) so that they can handle partial completion. Actual
device drivers should use blk_end_request instead.

Passing the result of ``blk_rq_bytes`` as ``nr_bytes`` guarantees
``false`` return from this function.


Return
======

``false`` - this request doesn't have any more data ``true`` - this
request has more data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
