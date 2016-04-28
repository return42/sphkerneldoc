.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ccw1:

===========
struct ccw1
===========

*man struct ccw1(9)*

*4.6.0-rc5*

channel command word


Synopsis
========

.. code-block:: c

    struct ccw1 {
      __u8 cmd_code;
      __u8 flags;
      __u16 count;
      __u32 cda;
    };


Members
=======

cmd_code
    command code

flags
    flags, like IDA addressing, etc.

count
    byte count

cda
    data address


Description
===========

The ccw is the basic structure to build channel programs that perform
operations with the device or the control unit. Only Format-1 channel
command words are supported.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
