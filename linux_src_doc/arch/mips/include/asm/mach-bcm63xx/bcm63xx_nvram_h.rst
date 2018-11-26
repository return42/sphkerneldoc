.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mach-bcm63xx/bcm63xx_nvram.h

.. _`bcm63xx_nvram_init`:

bcm63xx_nvram_init
==================

.. c:function:: void bcm63xx_nvram_init(void *nvram)

    initializes nvram

    :param nvram:
        address of the nvram data
    :type nvram: void \*

.. _`bcm63xx_nvram_init.description`:

Description
-----------

Initialized the local nvram copy from the target address and checks
its checksum.

.. _`bcm63xx_nvram_get_name`:

bcm63xx_nvram_get_name
======================

.. c:function:: u8 *bcm63xx_nvram_get_name( void)

    returns the board name according to nvram

    :param void:
        no arguments
    :type void: 

.. _`bcm63xx_nvram_get_name.description`:

Description
-----------

Returns the board name field from nvram. Note that it might not be
null terminated if it is exactly 16 bytes long.

.. _`bcm63xx_nvram_get_mac_address`:

bcm63xx_nvram_get_mac_address
=============================

.. c:function:: int bcm63xx_nvram_get_mac_address(u8 *mac)

    register & return a new mac address

    :param mac:
        pointer to array for allocated mac
    :type mac: u8 \*

.. _`bcm63xx_nvram_get_mac_address.description`:

Description
-----------

Registers and returns a mac address from the allocated macs from nvram.

Returns 0 on success.

.. This file was automatic generated / don't edit.

