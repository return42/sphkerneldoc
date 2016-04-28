.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-part-iter-next:

===================
disk_part_iter_next
===================

*man disk_part_iter_next(9)*

*4.6.0-rc5*

proceed iterator to the next partition and return it


Synopsis
========

.. c:function:: struct hd_struct * disk_part_iter_next( struct disk_part_iter * piter )

Arguments
=========

``piter``
    iterator of interest


Description
===========

Proceed ``piter`` to the next partition and return it.


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
