.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-platform-nand-ctrl:

=========================
struct platform_nand_ctrl
=========================

*man struct platform_nand_ctrl(9)*

*4.6.0-rc5*

controller level device structure


Synopsis
========

.. code-block:: c

    struct platform_nand_ctrl {
      int (* probe) (struct platform_device *pdev);
      void (* remove) (struct platform_device *pdev);
      void (* hwcontrol) (struct mtd_info *mtd, int cmd);
      int (* dev_ready) (struct mtd_info *mtd);
      void (* select_chip) (struct mtd_info *mtd, int chip);
      void (* cmd_ctrl) (struct mtd_info *mtd, int dat, unsigned int ctrl);
      void (* write_buf) (struct mtd_info *mtd, const uint8_t *buf, int len);
      void (* read_buf) (struct mtd_info *mtd, uint8_t *buf, int len);
      unsigned char (* read_byte) (struct mtd_info *mtd);
      void * priv;
    };


Members
=======

probe
    platform specific function to probe/setup hardware

remove
    platform specific function to remove/teardown hardware

hwcontrol
    platform specific hardware control structure

dev_ready
    platform specific function to read ready/busy pin

select_chip
    platform specific chip select function

cmd_ctrl
    platform specific function for controlling ALE/CLE/nCE. Also used to
    write command and address

write_buf
    platform specific function for write buffer

read_buf
    platform specific function for read buffer

read_byte
    platform specific function to read one byte from chip

priv
    private data to transport driver specific settings


Description
===========

All fields are optional and depend on the hardware driver requirements


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
