.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-erw:

==========
struct erw
==========

*man struct erw(9)*

*4.6.0-rc5*

extended report word


Synopsis
========

.. code-block:: c

    struct erw {
      __u32 res0:3;
      __u32 auth:1;
      __u32 pvrf:1;
      __u32 cpt:1;
      __u32 fsavf:1;
      __u32 cons:1;
      __u32 scavf:1;
      __u32 fsaf:1;
      __u32 scnt:6;
      __u32 res16:16;
    };


Members
=======

res0
    reserved

auth
    authorization check

pvrf
    path-verification-required flag

cpt
    channel-path timeout

fsavf
    failing storage address validity flag

cons
    concurrent sense

scavf
    secondary ccw address validity flag

fsaf
    failing storage address format

scnt
    sense count, if ``cons`` == ``1``

res16
    reserved


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
