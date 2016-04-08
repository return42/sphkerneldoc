
.. _API-struct-erw-eadm:

===============
struct erw_eadm
===============

*man struct erw_eadm(9)*

*4.6.0-rc1*

EADM Subchannel extended report word


Synopsis
========

.. code-block:: c

    struct erw_eadm {
      __u32 b:1;
      __u32 r:1;
    };


Members
=======

b
    aob error

r
    arsb error
