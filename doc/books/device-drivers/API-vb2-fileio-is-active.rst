.. -*- coding: utf-8; mode: rst -*-

.. _API-vb2-fileio-is-active:

====================
vb2_fileio_is_active
====================

*man vb2_fileio_is_active(9)*

*4.6.0-rc5*

return true if fileio is active.


Synopsis
========

.. c:function:: bool vb2_fileio_is_active( struct vb2_queue * q )

Arguments
=========

``q``
    videobuf queue


Description
===========

This returns true if ``read`` or ``write`` is used to stream the data as
opposed to stream I/O. This is almost never an important distinction,
except in rare cases. One such case is that using ``read`` or ``write``
to stream a format using V4L2_FIELD_ALTERNATE is not allowed since
there is no way you can pass the field information of each buffer
to/from userspace. A driver that supports this field format should check
for this in the queue_setup op and reject it if this function returns
true.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
