.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-end-bidi-request:

====================
blk_end_bidi_request
====================

*man blk_end_bidi_request(9)*

*4.6.0-rc5*

Complete a bidi request


Synopsis
========

.. c:function:: bool blk_end_bidi_request( struct request * rq, int error, unsigned int nr_bytes, unsigned int bidi_bytes )

Arguments
=========

``rq``
    the request to complete

``error``
    ``0`` for success, < ``0`` for error

``nr_bytes``
    number of bytes to complete ``rq``

``bidi_bytes``
    number of bytes to complete ``rq``->next_rq


Description
===========

Ends I/O on a number of bytes attached to ``rq`` and ``rq``->next_rq.
Drivers that supports bidi can safely call this member for any type of
request, bidi or uni. In the later case ``bidi_bytes`` is just ignored.


Return
======

``false`` - we are done with this request ``true`` - still buffers
pending for this request


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
