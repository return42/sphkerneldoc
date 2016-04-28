.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-erw-eadm:

===============
struct erw_eadm
===============

*man struct erw_eadm(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
