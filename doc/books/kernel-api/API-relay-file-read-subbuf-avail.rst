.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-file-read-subbuf-avail:

============================
relay_file_read_subbuf_avail
============================

*man relay_file_read_subbuf_avail(9)*

*4.6.0-rc5*

return bytes available in sub-buffer


Synopsis
========

.. c:function:: size_t relay_file_read_subbuf_avail( size_t read_pos, struct rchan_buf * buf )

Arguments
=========

``read_pos``
    file read position

``buf``
    relay channel buffer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
