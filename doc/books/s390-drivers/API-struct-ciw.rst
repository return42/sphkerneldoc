.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ciw:

==========
struct ciw
==========

*man struct ciw(9)*

*4.6.0-rc5*

command information word (CIW) layout


Synopsis
========

.. code-block:: c

    struct ciw {
      __u32 et:2;
      __u32 reserved:2;
      __u32 ct:4;
      __u32 cmd:8;
      __u32 count:16;
    };


Members
=======

et
    entry type

reserved
    reserved bits

ct
    command type

cmd
    command code

count
    command count


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
