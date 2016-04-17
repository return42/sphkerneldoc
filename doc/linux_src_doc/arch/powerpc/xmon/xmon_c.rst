.. -*- coding: utf-8; mode: rst -*-

======
xmon.c
======


.. _`write_ciabr`:

write_ciabr
===========

.. c:function:: void write_ciabr (unsigned long ciabr)

    write the CIABR SPR

    :param unsigned long ciabr:
        The value to write.



.. _`write_ciabr.description`:

Description
-----------

This function writes a value to the CIARB register either directly
through mtspr instruction if the kernel is in HV privilege mode or
call a hypervisor function to achieve the same in case the kernel
is in supervisor privilege mode.



.. _`set_ciabr`:

set_ciabr
=========

.. c:function:: void set_ciabr (unsigned long addr)

    set the CIABR

    :param unsigned long addr:
        The value to set.



.. _`set_ciabr.description`:

Description
-----------

This function sets the correct privilege value into the the HW
breakpoint address before writing it up in the CIABR register.

