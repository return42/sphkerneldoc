.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-esw3:

===========
struct esw3
===========

*man struct esw3(9)*

*4.6.0-rc5*

Format 3 Extended Status Word (ESW)


Synopsis
========

.. code-block:: c

    struct esw3 {
      __u8 zero0;
      __u8 lpum;
      __u16 res;
      struct erw erw;
      __u32 zeros[3];
    };


Members
=======

zero0
    reserved zeros

lpum
    last path used mask

res
    reserved

erw
    extended report word

zeros[3]
    three fullwords of zeros


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
