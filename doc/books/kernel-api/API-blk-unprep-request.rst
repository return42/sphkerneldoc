.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-unprep-request:

==================
blk_unprep_request
==================

*man blk_unprep_request(9)*

*4.6.0-rc5*

unprepare a request


Synopsis
========

.. c:function:: void blk_unprep_request( struct request * req )

Arguments
=========

``req``
    the request


Description
===========

This function makes a request ready for complete resubmission (or
completion). It happens only after all error handling is complete, so
represents the appropriate moment to deallocate any resources that were
allocated to the request in the prep_rq_fn. The queue lock is held
when calling this.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
