.. -*- coding: utf-8; mode: rst -*-

.. _about:

*********
About UIO
*********

If you use UIO for your card's driver, here's what you get:

-  only one small kernel module to write and maintain.

-  develop the main part of your driver in user space, with all the
   tools and libraries you're used to.

-  bugs in your driver won't crash the kernel.

-  updates of your driver can take place without recompiling the kernel.


.. _how_uio_works:

How UIO works
=============

Each UIO device is accessed through a device file and several sysfs
attribute files. The device file will be called ``/dev/uio0`` for the
first device, and ``/dev/uio1``, ``/dev/uio2`` and so on for subsequent
devices.

``/dev/uioX`` is used to access the address space of the card. Just use
:c:func:`mmap()` to access registers or RAM locations of your card.

Interrupts are handled by reading from ``/dev/uioX``. A blocking
:c:func:`read()` from ``/dev/uioX`` will return as soon as an
interrupt occurs. You can also use :c:func:`select()` on ``/dev/uioX``
to wait for an interrupt. The integer value read from ``/dev/uioX``
represents the total interrupt count. You can use this number to figure
out if you missed some interrupts.

For some hardware that has more than one interrupt source internally,
but not separate IRQ mask and status registers, there might be
situations where userspace cannot determine what the interrupt source
was if the kernel handler disables them by writing to the chip's IRQ
register. In such a case, the kernel has to disable the IRQ completely
to leave the chip's register untouched. Now the userspace part can
determine the cause of the interrupt, but it cannot re-enable
interrupts. Another cornercase is chips where re-enabling interrupts is
a read-modify-write operation to a combined IRQ status/acknowledge
register. This would be racy if a new interrupt occurred simultaneously.

To address these problems, UIO also implements a write() function. It is
normally not used and can be ignored for hardware that has only a single
interrupt source or has separate IRQ mask and status registers. If you
need it, however, a write to ``/dev/uioX`` will call the
:c:func:`irqcontrol()` function implemented by the driver. You have to
write a 32-bit value that is usually either 0 or 1 to disable or enable
interrupts. If a driver does not implement :c:func:`irqcontrol()`,
:c:func:`write()` will return with ``-ENOSYS``.

To handle interrupts properly, your custom kernel module can provide its
own interrupt handler. It will automatically be called by the built-in
handler.

For cards that don't generate interrupts but need to be polled, there is
the possibility to set up a timer that triggers the interrupt handler at
configurable time intervals. This interrupt simulation is done by
calling :c:func:`uio_event_notify()` from the timer's event handler.

Each driver provides attributes that are used to read or write
variables. These attributes are accessible through sysfs files. A custom
kernel driver module can add its own attributes to the device owned by
the uio driver, but not added to the UIO device itself at this time.
This might change in the future if it would be found to be useful.

The following standard attributes are provided by the UIO framework:

-  ``name``: The name of your device. It is recommended to use the name
   of your kernel module for this.

-  ``version``: A version string defined by your driver. This allows the
   user space part of your driver to deal with different versions of the
   kernel module.

-  ``event``: The total number of interrupts handled by the driver since
   the last time the device node was read.

These attributes appear under the ``/sys/class/uio/uioX`` directory.
Please note that this directory might be a symlink, and not a real
directory. Any userspace code that accesses it must be able to handle
this.

Each UIO device can make one or more memory regions available for memory
mapping. This is necessary because some industrial I/O cards require
access to more than one PCI memory region in a driver.

Each mapping has its own directory in sysfs, the first mapping appears
as ``/sys/class/uio/uioX/maps/map0/``. Subsequent mappings create
directories ``map1/``, ``map2/``, and so on. These directories will only
appear if the size of the mapping is not 0.

Each ``mapX/`` directory contains four read-only files that show
attributes of the memory:

-  ``name``: A string identifier for this mapping. This is optional, the
   string can be empty. Drivers can set this to make it easier for
   userspace to find the correct mapping.

-  ``addr``: The address of memory that can be mapped.

-  ``size``: The size, in bytes, of the memory pointed to by addr.

-  ``offset``: The offset, in bytes, that has to be added to the pointer
   returned by :c:func:`mmap()` to get to the actual device memory.
   This is important if the device's memory is not page aligned.
   Remember that pointers returned by :c:func:`mmap()` are always page
   aligned, so it is good style to always add this offset.

From userspace, the different mappings are distinguished by adjusting
the ``offset`` parameter of the :c:func:`mmap()` call. To map the
memory of mapping N, you have to use N times the page size as your
offset:


.. code-block:: c

    offset = N * getpagesize();

Sometimes there is hardware with memory-like regions that can not be
mapped with the technique described here, but there are still ways to
access them from userspace. The most common example are x86 ioports. On
x86 systems, userspace can access these ioports using
:c:func:`ioperm()`, :c:func:`iopl()`, :c:func:`inb()`,
:c:func:`outb()`, and similar functions.

Since these ioport regions can not be mapped, they will not appear under
``/sys/class/uio/uioX/maps/`` like the normal memory described above.
Without information about the port regions a hardware has to offer, it
becomes difficult for the userspace part of the driver to find out which
ports belong to which UIO device.

To address this situation, the new directory
``/sys/class/uio/uioX/portio/`` was added. It only exists if the driver
wants to pass information about one or more port regions to userspace.
If that is the case, subdirectories named ``port0``, ``port1``, and so
on, will appear underneath ``/sys/class/uio/uioX/portio/``.

Each ``portX/`` directory contains four read-only files that show name,
start, size, and type of the port region:

-  ``name``: A string identifier for this port region. The string is
   optional and can be empty. Drivers can set it to make it easier for
   userspace to find a certain port region.

-  ``start``: The first port of this region.

-  ``size``: The number of ports in this region.

-  ``porttype``: A string describing the type of port.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
