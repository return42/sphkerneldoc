.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-rq-err-bytes:

================
blk_rq_err_bytes
================

*man blk_rq_err_bytes(9)*

*4.6.0-rc5*

determine number of bytes till the next failure boundary


Synopsis
========

.. c:function:: unsigned int blk_rq_err_bytes( const struct request * rq )

Arguments
=========

``rq``
    request to examine


Description
===========

A request could be merge of IOs which require different failure
handling. This function determines the number of bytes which can be
failed from the beginning of the request without crossing into area
which need to be retried further.


Return
======

The number of bytes to fail.


Context
=======

queue_lock must be held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
