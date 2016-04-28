.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-end-request-cur:

===================
blk_end_request_cur
===================

*man blk_end_request_cur(9)*

*4.6.0-rc5*

Helper function to finish the current request chunk.


Synopsis
========

.. c:function:: bool blk_end_request_cur( struct request * rq, int error )

Arguments
=========

``rq``
    the request to finish the current chunk for

``error``
    ``0`` for success, < ``0`` for error


Description
===========

Complete the current consecutively mapped chunk from ``rq``.


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
