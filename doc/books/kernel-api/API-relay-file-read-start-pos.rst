.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-file-read-start-pos:

=========================
relay_file_read_start_pos
=========================

*man relay_file_read_start_pos(9)*

*4.6.0-rc5*

find the first available byte to read


Synopsis
========

.. c:function:: size_t relay_file_read_start_pos( size_t read_pos, struct rchan_buf * buf )

Arguments
=========

``read_pos``
    file read position

``buf``
    relay channel buffer


Description
===========

If the ``read_pos`` is in the middle of padding, return the position of
the first actually available byte, otherwise return the original value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
