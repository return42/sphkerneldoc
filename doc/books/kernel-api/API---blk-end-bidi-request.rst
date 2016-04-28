.. -*- coding: utf-8; mode: rst -*-

.. _API---blk-end-bidi-request:

======================
__blk_end_bidi_request
======================

*man __blk_end_bidi_request(9)*

*4.6.0-rc5*

Complete a bidi request with queue lock held


Synopsis
========

.. c:function:: bool __blk_end_bidi_request( struct request * rq, int error, unsigned int nr_bytes, unsigned int bidi_bytes )

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

Identical to ``blk_end_bidi_request`` except that queue lock is assumed
to be locked on entry and remains so on return.


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
