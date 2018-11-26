.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/uv_mmtimer.c

.. _`uv_mmtimer_ioctl`:

uv_mmtimer_ioctl
================

.. c:function:: long uv_mmtimer_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    ioctl interface for /dev/uv_mmtimer

    :param file:
        file structure for the device
    :type file: struct file \*

    :param cmd:
        command to execute
    :type cmd: unsigned int

    :param arg:
        optional argument to command
    :type arg: unsigned long

.. _`uv_mmtimer_ioctl.description`:

Description
-----------

Executes the command specified by \ ``cmd``\ .  Returns 0 for success, < 0 for
failure.

.. _`uv_mmtimer_ioctl.valid-commands`:

Valid commands
--------------


\ ``MMTIMER_GETOFFSET``\  - Should return the offset (relative to the start
of the page where the registers are mapped) for the counter in question.

\ ``MMTIMER_GETRES``\  - Returns the resolution of the clock in femto (10^-15)
seconds

\ ``MMTIMER_GETFREQ``\  - Copies the frequency of the clock in Hz to the address
specified by \ ``arg``\ 

\ ``MMTIMER_GETBITS``\  - Returns the number of bits in the clock's counter

\ ``MMTIMER_MMAPAVAIL``\  - Returns 1 if registers can be mmap'd into userspace

\ ``MMTIMER_GETCOUNTER``\  - Gets the current value in the counter and places it
in the address specified by \ ``arg``\ .

.. _`uv_mmtimer_mmap`:

uv_mmtimer_mmap
===============

.. c:function:: int uv_mmtimer_mmap(struct file *file, struct vm_area_struct *vma)

    maps the clock's registers into userspace

    :param file:
        file structure for the device
    :type file: struct file \*

    :param vma:
        VMA to map the registers into
    :type vma: struct vm_area_struct \*

.. _`uv_mmtimer_mmap.description`:

Description
-----------

Calls \ :c:func:`remap_pfn_range`\  to map the clock's registers into
the calling process' address space.

.. _`uv_mmtimer_init`:

uv_mmtimer_init
===============

.. c:function:: int uv_mmtimer_init( void)

    device initialization routine

    :param void:
        no arguments
    :type void: 

.. _`uv_mmtimer_init.description`:

Description
-----------

Does initial setup for the uv_mmtimer device.

.. This file was automatic generated / don't edit.

