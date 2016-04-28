.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-file-read-end-pos:

=======================
relay_file_read_end_pos
=======================

*man relay_file_read_end_pos(9)*

*4.6.0-rc5*

return the new read position


Synopsis
========

.. c:function:: size_t relay_file_read_end_pos( struct rchan_buf * buf, size_t read_pos, size_t count )

Arguments
=========

``buf``
    relay channel buffer

``read_pos``
    file read position

``count``
    number of bytes to be read


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
