.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-max-segments:

======================
blk_queue_max_segments
======================

*man blk_queue_max_segments(9)*

*4.6.0-rc5*

set max hw segments for a request for this queue


Synopsis
========

.. c:function:: void blk_queue_max_segments( struct request_queue * q, unsigned short max_segments )

Arguments
=========

``q``
    the request queue for the device

``max_segments``
    max number of segments


Description
===========

Enables a low level driver to set an upper limit on the number of hw
data segments in a request.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
