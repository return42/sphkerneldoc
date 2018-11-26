.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/kernel/setup.c

.. _`reserve_memory`:

reserve_memory
==============

.. c:function:: void reserve_memory( void)

    setup reserved memory areas

    :param void:
        no arguments
    :type void: 

.. _`reserve_memory.description`:

Description
-----------

Setup the reserved memory areas set aside for the boot parameters,
initrd, etc.  There are currently \ ``IA64_MAX_RSVD_REGIONS``\  defined,
see arch/ia64/include/asm/meminit.h if you need to define more.

.. _`find_initrd`:

find_initrd
===========

.. c:function:: void find_initrd( void)

    get initrd parameters from the boot parameter structure

    :param void:
        no arguments
    :type void: 

.. _`find_initrd.description`:

Description
-----------

Grab the initrd start and end from the boot parameter struct given us by
the boot loader.

.. _`early_console_setup`:

early_console_setup
===================

.. c:function:: int early_console_setup(char *cmdline)

    setup debugging console

    :param cmdline:
        *undescribed*
    :type cmdline: char \*

.. _`early_console_setup.description`:

Description
-----------

Consoles started here require little enough setup that we can start using
them very early in the boot process, either right after the machine
vector initialization, or even before if the drivers can detect their hw.

Returns non-zero if a console couldn't be setup.

.. This file was automatic generated / don't edit.

