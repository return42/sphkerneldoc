.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/bcm47xxpart.c

.. _`bcm47xxpart_bootpartition`:

bcm47xxpart_bootpartition
=========================

.. c:function:: int bcm47xxpart_bootpartition( void)

    gets index of TRX partition used by bootloader

    :param  void:
        no arguments

.. _`bcm47xxpart_bootpartition.description`:

Description
-----------

Some devices may have more than one TRX partition. In such case one of them
is the main one and another a failsafe one. Bootloader may fallback to the
failsafe firmware if it detects corruption of the main image.

This function provides info about currently used TRX partition. It's the one
containing kernel started by the bootloader.

.. This file was automatic generated / don't edit.

