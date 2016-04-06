
.. _API-struct-nand-manufacturers:

=========================
struct nand_manufacturers
=========================

*man struct nand_manufacturers(9)*

*4.6.0-rc1*

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
