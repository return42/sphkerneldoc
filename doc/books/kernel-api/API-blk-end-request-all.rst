.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-end-request-all:

===================
blk_end_request_all
===================

*man blk_end_request_all(9)*

*4.6.0-rc5*

Helper function for drives to finish the request.


Synopsis
========

.. c:function:: void blk_end_request_all( struct request * rq, int error )

Arguments
=========

``rq``
    the request to finish

``error``
    ``0`` for success, < ``0`` for error


Description
===========

Completely finish ``rq``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
