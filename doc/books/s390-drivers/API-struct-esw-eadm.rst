
.. _API-struct-esw-eadm:

===============
struct esw_eadm
===============

*man struct esw_eadm(9)*

*4.6.0-rc1*

EADM Subchannel Extended Status Word (ESW)


Synopsis
========

.. code-block:: c

    struct esw_eadm {
      __u32 sublog;
      struct erw_eadm erw;
    };


Members
=======

sublog
    subchannel logout

erw
    extended report word
