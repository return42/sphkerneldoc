.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-platform-nand-data:

=========================
struct platform_nand_data
=========================

*man struct platform_nand_data(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
