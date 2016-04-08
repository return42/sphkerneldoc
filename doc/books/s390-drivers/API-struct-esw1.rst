
.. _API-struct-esw1:

===========
struct esw1
===========

*man struct esw1(9)*

*4.6.0-rc1*

Format 1 Extended Status Word (ESW)


Synopsis
========

.. code-block:: c

    struct esw1 {
      __u8 zero0;
      __u8 lpum;
      __u16 zero16;
      struct erw erw;
      __u32 zeros[3];
    };


Members
=======

zero0
    reserved zeros

lpum
    last path used mask

zero16
    reserved zeros

erw
    extended report word

zeros[3]
    three fullwords of zeros
