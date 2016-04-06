
.. _API-relay-file-read-start-pos:

=========================
relay_file_read_start_pos
=========================

*man relay_file_read_start_pos(9)*

*4.6.0-rc1*

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

If the ``read_pos`` is in the middle of padding, return the position of the first actually available byte, otherwise return the original value.
