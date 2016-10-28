.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/mmtimer.c

.. _`mmtimer_ioctl`:

mmtimer_ioctl
=============

.. c:function:: long mmtimer_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    ioctl interface for /dev/mmtimer

    :param struct file \*file:
        file structure for the device

    :param unsigned int cmd:
        command to execute

    :param unsigned long arg:
        optional argument to command

.. _`mmtimer_ioctl.description`:

Description
-----------

Executes the command specified by \ ``cmd``\ .  Returns 0 for success, < 0 for
failure.

.. _`mmtimer_ioctl.valid-commands`:

Valid commands
--------------


\ ``MMTIMER_GETOFFSET``\  - Should return the offset (relative to the start
of the page where the registers are mapped) for the counter in question.

\ ``MMTIMER_GETRES``\  - Returns the resolution of the clock in femto (10^-15)
seconds

\ ``MMTIMER_GETFREQ``\  - Copies the frequency of the clock in Hz to the address
specified by \ ``arg``\ 

\ ``MMTIMER_GETBITS``\  - Returns the number of bits in the clock's counter

\ ``MMTIMER_MMAPAVAIL``\  - Returns 1 if the registers can be mmap'd into userspace

\ ``MMTIMER_GETCOUNTER``\  - Gets the current value in the counter and places it
in the address specified by \ ``arg``\ .

.. _`mmtimer_mmap`:

mmtimer_mmap
============

.. c:function:: int mmtimer_mmap(struct file *file, struct vm_area_struct *vma)

    maps the clock's registers into userspace

    :param struct file \*file:
        file structure for the device

    :param struct vm_area_struct \*vma:
        VMA to map the registers into

.. _`mmtimer_mmap.description`:

Description
-----------

Calls \ :c:func:`remap_pfn_range`\  to map the clock's registers into
the calling process' address space.

.. _`mmtimer_interrupt`:

mmtimer_interrupt
=================

.. c:function:: irqreturn_t mmtimer_interrupt(int irq, void *dev_id)

    timer interrupt handler

    :param int irq:
        irq received

    :param void \*dev_id:
        device the irq came from

.. _`mmtimer_interrupt.description`:

Description
-----------

Called when one of the comarators matches the counter, This
routine will send signals to processes that have requested
them.

This interrupt is run in an interrupt context
by the SHUB. It is therefore safe to locally access SHub
registers.

.. _`mmtimer_init`:

mmtimer_init
============

.. c:function:: int mmtimer_init( void)

    device initialization routine

    :param  void:
        no arguments

.. _`mmtimer_init.description`:

Description
-----------

Does initial setup for the mmtimer device.

.. This file was automatic generated / don't edit.

