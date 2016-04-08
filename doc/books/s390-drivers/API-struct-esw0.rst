
.. _API-struct-esw0:

===========
struct esw0
===========

*man struct esw0(9)*

*4.6.0-rc1*

Format 0 Extended Status Word (ESW)


Synopsis
========

.. code-block:: c

    struct esw0 {
      struct sublog sublog;
      struct erw erw;
      __u32 faddr[2];
      __u32 saddr;
    };


Members
=======

sublog
    subchannel logout

erw
    extended report word

faddr[2]
    failing storage address

saddr
    secondary ccw address
