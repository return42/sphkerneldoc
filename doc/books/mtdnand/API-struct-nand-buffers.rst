.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-nand-buffers:

===================
struct nand_buffers
===================

*man struct nand_buffers(9)*

*4.6.0-rc5*

buffer structure for read/write


Synopsis
========

.. code-block:: c

    struct nand_buffers {
      uint8_t * ecccalc;
      uint8_t * ecccode;
      uint8_t * databuf;
    };


Members
=======

ecccalc
    buffer pointer for calculated ECC, size is oobsize.

ecccode
    buffer pointer for ECC read from flash, size is oobsize.

databuf
    buffer pointer for data, size is (page size + oobsize).


Description
===========

Do not change the order of buffers. databuf and oobrbuf must be in
consecutive order.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
