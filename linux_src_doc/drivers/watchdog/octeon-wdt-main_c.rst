.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/octeon-wdt-main.c

.. _`octeon_wdt_poke_irq`:

octeon_wdt_poke_irq
===================

.. c:function:: irqreturn_t octeon_wdt_poke_irq(int cpl, void *dev_id)

    :param cpl:
        *undescribed*
    :type cpl: int

    :param dev_id:
        *undescribed*
    :type dev_id: void \*

.. _`octeon_wdt_poke_irq.description`:

Description
-----------

Returns

.. _`octeon_wdt_write_string`:

octeon_wdt_write_string
=======================

.. c:function:: void octeon_wdt_write_string(const char *str)

    :param str:
        String to write
    :type str: const char \*

.. _`octeon_wdt_write_hex`:

octeon_wdt_write_hex
====================

.. c:function:: void octeon_wdt_write_hex(u64 value, int digits)

    :param value:
        Number to display
    :type value: u64

    :param digits:
        Number of digits to print (1 to 16)
    :type digits: int

.. _`octeon_wdt_nmi_stage3`:

octeon_wdt_nmi_stage3
=====================

.. c:function:: void octeon_wdt_nmi_stage3(u64 reg)

    1) The first NMI handler enables CVMSEG and transfers from the bootbus region into normal memory. It is careful to not destroy any registers. 2) The second stage handler uses CVMSEG to save the registers and create a stack for C code. It then calls the third level handler with one argument, a pointer to the register values. 3) The third, and final, level handler is the following C function that prints out some useful infomration.

    :param reg:
        Pointer to register state before the NMI
    :type reg: u64

.. _`octeon_wdt_init`:

octeon_wdt_init
===============

.. c:function:: int octeon_wdt_init( void)

    :param void:
        no arguments
    :type void: 

.. _`octeon_wdt_init.description`:

Description
-----------

Returns Zero on success

.. _`octeon_wdt_cleanup`:

octeon_wdt_cleanup
==================

.. c:function:: void __exit octeon_wdt_cleanup( void)

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

