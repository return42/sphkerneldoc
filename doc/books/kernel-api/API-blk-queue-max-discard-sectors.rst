.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-max-discard-sectors:

=============================
blk_queue_max_discard_sectors
=============================

*man blk_queue_max_discard_sectors(9)*

*4.6.0-rc5*

set max sectors for a single discard


Synopsis
========

.. c:function:: void blk_queue_max_discard_sectors( struct request_queue * q, unsigned int max_discard_sectors )

Arguments
=========

``q``
    the request queue for the device

``max_discard_sectors``
    maximum number of sectors to discard


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
