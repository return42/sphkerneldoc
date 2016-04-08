
.. _API-struct-esw2:

===========
struct esw2
===========

*man struct esw2(9)*

*4.6.0-rc1*

Format 2 Extended Status Word (ESW)


Synopsis
========

.. code-block:: c

    struct esw2 {
      __u8 zero0;
      __u8 lpum;
      __u16 dcti;
      struct erw erw;
      __u32 zeros[3];
    };


Members
=======

zero0
    reserved zeros

lpum
    last path used mask

dcti
    device-connect-time interval

erw
    extended report word

zeros[3]
    three fullwords of zeros
