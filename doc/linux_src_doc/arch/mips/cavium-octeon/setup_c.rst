.. -*- coding: utf-8; mode: rst -*-

=======
setup.c
=======


.. _`octeon_is_simulation`:

octeon_is_simulation
====================

.. c:function:: int octeon_is_simulation ( void)

    :param void:
        no arguments



.. _`octeon_is_simulation.description`:

Description
-----------


Returns



.. _`octeon_is_pci_host`:

octeon_is_pci_host
==================

.. c:function:: int octeon_is_pci_host ( void)

    :param void:
        no arguments



.. _`octeon_is_pci_host.description`:

Description
-----------

Linux can control the PCI bus.

Returns Non zero if Octeon in host mode.



.. _`octeon_get_clock_rate`:

octeon_get_clock_rate
=====================

.. c:function:: uint64_t octeon_get_clock_rate ( void)

    :param void:
        no arguments



.. _`octeon_get_clock_rate.description`:

Description
-----------


Returns Clock rate in HZ



.. _`octeon_write_lcd`:

octeon_write_lcd
================

.. c:function:: void octeon_write_lcd (const char *s)

    :param const char \*s:
        String to write



.. _`octeon_write_lcd.description`:

Description
-----------

exists on most Cavium evaluation boards. If it doesn't exist, then
this function doesn't do anything.



.. _`octeon_get_boot_uart`:

octeon_get_boot_uart
====================

.. c:function:: int octeon_get_boot_uart ( void)

    :param void:
        no arguments



.. _`octeon_get_boot_uart.description`:

Description
-----------


Returns uart          (0 or 1)



.. _`octeon_get_boot_coremask`:

octeon_get_boot_coremask
========================

.. c:function:: int octeon_get_boot_coremask ( void)

    :param void:
        no arguments



.. _`octeon_get_boot_coremask.description`:

Description
-----------


Returns Core mask



.. _`octeon_check_cpu_bist`:

octeon_check_cpu_bist
=====================

.. c:function:: void octeon_check_cpu_bist ( void)

    :param void:
        no arguments



.. _`octeon_restart`:

octeon_restart
==============

.. c:function:: void octeon_restart (char *command)

    :param char \*command:
        Command to pass to the bootloader. Currently ignored.



.. _`octeon_kill_core`:

octeon_kill_core
================

.. c:function:: void octeon_kill_core (void *arg)

    :param void \*arg:
        Ignored.



.. _`octeon_halt`:

octeon_halt
===========

.. c:function:: void octeon_halt ( void)

    :param void:
        no arguments



.. _`octeon_board_type_string`:

octeon_board_type_string
========================

.. c:function:: const char *octeon_board_type_string ( void)

    :param void:
        no arguments



.. _`octeon_board_type_string.description`:

Description
-----------


Returns



.. _`prom_init`:

prom_init
=========

.. c:function:: void prom_init ( void)

    :param void:
        no arguments

