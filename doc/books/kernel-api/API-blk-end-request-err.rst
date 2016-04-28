.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-end-request-err:

===================
blk_end_request_err
===================

*man blk_end_request_err(9)*

*4.6.0-rc5*

Finish a request till the next failure boundary.


Synopsis
========

.. c:function:: bool blk_end_request_err( struct request * rq, int error )

Arguments
=========

``rq``
    the request to finish till the next failure boundary for

``error``
    must be negative errno


Description
===========

Complete ``rq`` till the next failure boundary.


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
