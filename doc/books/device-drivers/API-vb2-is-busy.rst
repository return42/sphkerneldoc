.. -*- coding: utf-8; mode: rst -*-

.. _API-vb2-is-busy:

===========
vb2_is_busy
===========

*man vb2_is_busy(9)*

*4.6.0-rc5*

return busy status of the queue


Synopsis
========

.. c:function:: bool vb2_is_busy( struct vb2_queue * q )

Arguments
=========

``q``
    videobuf queue


Description
===========

This function checks if queue has any buffers allocated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
