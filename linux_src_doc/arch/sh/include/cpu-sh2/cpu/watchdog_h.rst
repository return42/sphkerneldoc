.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/include/cpu-sh2/cpu/watchdog.h

.. _`sh_wdt_read_rstcsr`:

sh_wdt_read_rstcsr
==================

.. c:function:: __u8 sh_wdt_read_rstcsr( void)

    Read from Reset Control/Status Register

    :param void:
        no arguments
    :type void: 

.. _`sh_wdt_read_rstcsr.description`:

Description
-----------

Reads back the RSTCSR value.

.. _`sh_wdt_write_rstcsr`:

sh_wdt_write_rstcsr
===================

.. c:function:: void sh_wdt_write_rstcsr(__u8 val)

    Write to Reset Control/Status Register

    :param val:
        Value to write
    :type val: __u8

.. _`sh_wdt_write_rstcsr.description`:

Description
-----------

Writes the given value \ ``val``\  to the lower byte of the control/status
register. The upper byte is set manually on each write.

.. This file was automatic generated / don't edit.

