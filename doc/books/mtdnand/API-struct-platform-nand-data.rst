
.. _API-struct-platform-nand-data:

=========================
struct platform_nand_data
=========================

*man struct platform_nand_data(9)*

*4.6.0-rc1*

container structure for platform-specific data


Synopsis
========

.. code-block:: c

    struct platform_nand_data {
      struct platform_nand_chip chip;
      struct platform_nand_ctrl ctrl;
    };


Members
=======

chip
    chip level chip structure

ctrl
    controller level device structure
