.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-pre-runtime-resume:

======================
blk_pre_runtime_resume
======================

*man blk_pre_runtime_resume(9)*

*4.6.0-rc5*

Pre runtime resume processing


Synopsis
========

.. c:function:: void blk_pre_runtime_resume( struct request_queue * q )

Arguments
=========

``q``
    the queue of the device


Description
===========

Update the queue's runtime status to RESUMING in preparation for the
runtime resume of the device.

This function should be called near the start of the device's
runtime_resume callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
