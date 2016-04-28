.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-nand-manufacturers:

=========================
struct nand_manufacturers
=========================

*man struct nand_manufacturers(9)*

*4.6.0-rc5*

NAND Flash Manufacturer ID Structure


Synopsis
========

.. code-block:: c

    struct nand_manufacturers {
      int id;
      char * name;
    };


Members
=======

id
    manufacturer ID code of device.

name
    Manufacturer name


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
