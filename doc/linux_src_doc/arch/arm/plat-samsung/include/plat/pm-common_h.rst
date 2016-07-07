.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/pm-common.h

.. _`sleep_save`:

struct sleep_save
=================

.. c:type:: struct sleep_save

    save information for shared peripherals.

.. _`sleep_save.definition`:

Definition
----------

.. code-block:: c

    struct sleep_save {
        void __iomem *reg;
        unsigned long val;
    }

.. _`sleep_save.members`:

Members
-------

reg
    Pointer to the register to save.

val
    Holder for the value saved from reg.

.. _`sleep_save.description`:

Description
-----------

This describes a list of registers which is used by the pm core and
other subsystem to save and restore register values over suspend.

.. _`pm_uart_save`:

struct pm_uart_save
===================

.. c:type:: struct pm_uart_save

    save block for core UART

.. _`pm_uart_save.definition`:

Definition
----------

.. code-block:: c

    struct pm_uart_save {
        u32 ulcon;
        u32 ucon;
        u32 ufcon;
        u32 umcon;
        u32 ubrdiv;
        u32 udivslot;
    }

.. _`pm_uart_save.members`:

Members
-------

ulcon
    Save value for S3C2410_ULCON

ucon
    Save value for S3C2410_UCON

ufcon
    Save value for S3C2410_UFCON

umcon
    Save value for S3C2410_UMCON

ubrdiv
    Save value for S3C2410_UBRDIV

udivslot
    *undescribed*

.. _`pm_uart_save.description`:

Description
-----------

Save block for UART registers to be held over sleep and restored if they
are needed (say by debug).

.. _`s3c_pm_dbg`:

s3c_pm_dbg
==========

.. c:function:: void s3c_pm_dbg(const char *msg,  ...)

    low level debug function for use in suspend/resume.

    :param const char \*msg:
        The message to print.

    :param ... :
        variable arguments

.. _`s3c_pm_dbg.description`:

Description
-----------

This function is used mainly to debug the resume process before the system
can rely on printk/console output. It uses the low-level debugging output
routine \ :c:func:`printascii`\  to do its work.

.. _`s3c_pm_debug_init`:

s3c_pm_debug_init
=================

.. c:function:: void s3c_pm_debug_init( void)

    suspend/resume low level debug initialization.

    :param  void:
        no arguments

.. _`s3c_pm_debug_init.description`:

Description
-----------

This function needs to be called before \ :c:func:`S3C_PMDBG`\  can be used, to set up
UART port base address and configuration.

.. This file was automatic generated / don't edit.

