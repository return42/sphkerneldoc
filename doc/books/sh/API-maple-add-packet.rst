.. -*- coding: utf-8; mode: rst -*-

.. _API-maple-add-packet:

================
maple_add_packet
================

*man maple_add_packet(9)*

*4.6.0-rc5*

add a single instruction to the maple bus queue


Synopsis
========

.. c:function:: int maple_add_packet( struct maple_device * mdev, u32 function, u32 command, size_t length, void * data )

Arguments
=========

``mdev``
    maple device

``function``
    function on device being queried

``command``
    maple command to add

``length``
    length of command string (in 32 bit words)

``data``
    remainder of command string


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
