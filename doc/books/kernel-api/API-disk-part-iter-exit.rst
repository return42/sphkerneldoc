.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-part-iter-exit:

===================
disk_part_iter_exit
===================

*man disk_part_iter_exit(9)*

*4.6.0-rc5*

finish up partition iteration


Synopsis
========

.. c:function:: void disk_part_iter_exit( struct disk_part_iter * piter )

Arguments
=========

``piter``
    iter of interest


Description
===========

Called when iteration is over. Cleans up ``piter``.


CONTEXT
=======

Don't care.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
