.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-esw-eadm:

===============
struct esw_eadm
===============

*man struct esw_eadm(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
