
.. _API-struct-nand-buffers:

===================
struct nand_buffers
===================

*man struct nand_buffers(9)*

*4.6.0-rc1*

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

Do not change the order of buffers. databuf and oobrbuf must be in consecutive order.
