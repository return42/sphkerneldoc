.. -*- coding: utf-8; mode: rst -*-

.. _custom_kernel_module:

******************************
Writing your own kernel module
******************************

Please have a look at ``uio_cif.c`` as an example. The following
paragraphs explain the different sections of this file.


.. _uio_info:

struct uio_info
===============

This structure tells the framework the details of your driver, Some of
the members are required, others are optional.

-  ``const char *name``: Required. The name of your driver as it will
   appear in sysfs. I recommend using the name of your module for this.

-  ``const char *version``: Required. This string appears in
   ``/sys/class/uio/uioX/version``.

-  ``struct uio_mem mem[ MAX_UIO_MAPS ]``: Required if you have memory
   that can be mapped with ``mmap()``. For each mapping you need to fill
   one of the ``uio_mem`` structures. See the description below for
   details.

-  ``struct uio_port port[ MAX_UIO_PORTS_REGIONS ]``: Required if you
   want to pass information about ioports to userspace. For each port
   region you need to fill one of the ``uio_port`` structures. See the
   description below for details.

-  ``long irq``: Required. If your hardware generates an interrupt, it's
   your modules task to determine the irq number during initialization.
   If you don't have a hardware generated interrupt but want to trigger
   the interrupt handler in some other way, set ``irq`` to
   ``UIO_IRQ_CUSTOM``. If you had no interrupt at all, you could set
   ``irq`` to ``UIO_IRQ_NONE``, though this rarely makes sense.

-  ``unsigned long irq_flags``: Required if you've set ``irq`` to a
   hardware interrupt number. The flags given here will be used in the
   call to ``request_irq()``.

-  ``int (*mmap)(struct uio_info *info, struct vm_area_struct
   *vma)``: Optional. If you need a special ``mmap()`` function, you can
   set it here. If this pointer is not NULL, your ``mmap()`` will be
   called instead of the built-in one.

-  ``int (*open)(struct uio_info *info, struct inode *inode)
   ``: Optional. You might want to have your own ``open()``, e.g. to
   enable interrupts only when your device is actually used.

-  ``int (*release)(struct uio_info *info, struct inode *inode)
   ``: Optional. If you define your own ``open()``, you will probably
   also want a custom ``release()`` function.

-  ``int (*irqcontrol)(struct uio_info *info, s32 irq_on)
   ``: Optional. If you need to be able to enable or disable interrupts
   from userspace by writing to ``/dev/uioX``, you can implement this
   function. The parameter ``irq_on`` will be 0 to disable interrupts
   and 1 to enable them.

Usually, your device will have one or more memory regions that can be
mapped to user space. For each region, you have to set up a
``struct uio_mem`` in the ``mem[]`` array. Here's a description of the
fields of ``struct uio_mem``:

-  ``const char *name``: Optional. Set this to help identify the memory
   region, it will show up in the corresponding sysfs node.

-  ``int memtype``: Required if the mapping is used. Set this to
   ``UIO_MEM_PHYS`` if you you have physical memory on your card to be
   mapped. Use ``UIO_MEM_LOGICAL`` for logical memory (e.g. allocated
   with ``kmalloc()``). There's also ``UIO_MEM_VIRTUAL`` for virtual
   memory.

-  ``phys_addr_t addr``: Required if the mapping is used. Fill in the
   address of your memory block. This address is the one that appears in
   sysfs.

-  ``resource_size_t size``: Fill in the size of the memory block that
   ``addr`` points to. If ``size`` is zero, the mapping is considered
   unused. Note that you *must* initialize ``size`` with zero for all
   unused mappings.

-  ``void *internal_addr``: If you have to access this memory region
   from within your kernel module, you will want to map it internally by
   using something like ``ioremap()``. Addresses returned by this
   function cannot be mapped to user space, so you must not store it in
   ``addr``. Use ``internal_addr`` instead to remember such an address.

Please do not touch the ``map`` element of ``struct uio_mem``! It is
used by the UIO framework to set up sysfs files for this mapping. Simply
leave it alone.

Sometimes, your device can have one or more port regions which can not
be mapped to userspace. But if there are other possibilities for
userspace to access these ports, it makes sense to make information
about the ports available in sysfs. For each region, you have to set up
a ``struct uio_port`` in the ``port[]`` array. Here's a description of
the fields of ``struct uio_port``:

-  ``char *porttype``: Required. Set this to one of the predefined
   constants. Use ``UIO_PORT_X86`` for the ioports found in x86
   architectures.

-  ``unsigned long start``: Required if the port region is used. Fill in
   the number of the first port of this region.

-  ``unsigned long size``: Fill in the number of ports in this region.
   If ``size`` is zero, the region is considered unused. Note that you
   *must* initialize ``size`` with zero for all unused regions.

Please do not touch the ``portio`` element of ``struct uio_port``! It is
used internally by the UIO framework to set up sysfs files for this
region. Simply leave it alone.


.. _adding_irq_handler:

Adding an interrupt handler
===========================

What you need to do in your interrupt handler depends on your hardware
and on how you want to handle it. You should try to keep the amount of
code in your kernel interrupt handler low. If your hardware requires no
action that you *have* to perform after each interrupt, then your
handler can be empty.

If, on the other hand, your hardware *needs* some action to be performed
after each interrupt, then you *must* do it in your kernel module. Note
that you cannot rely on the userspace part of your driver. Your
userspace program can terminate at any time, possibly leaving your
hardware in a state where proper interrupt handling is still required.

There might also be applications where you want to read data from your
hardware at each interrupt and buffer it in a piece of kernel memory
you've allocated for that purpose. With this technique you could avoid
loss of data if your userspace program misses an interrupt.

A note on shared interrupts: Your driver should support interrupt
sharing whenever this is possible. It is possible if and only if your
driver can detect whether your hardware has triggered the interrupt or
not. This is usually done by looking at an interrupt status register. If
your driver sees that the IRQ bit is actually set, it will perform its
actions, and the handler returns IRQ_HANDLED. If the driver detects
that it was not your hardware that caused the interrupt, it will do
nothing and return IRQ_NONE, allowing the kernel to call the next
possible interrupt handler.

If you decide not to support shared interrupts, your card won't work in
computers with no free interrupts. As this frequently happens on the PC
platform, you can save yourself a lot of trouble by supporting interrupt
sharing.


.. _using_uio_pdrv:

Using uio_pdrv for platform devices
===================================

In many cases, UIO drivers for platform devices can be handled in a
generic way. In the same place where you define your
``struct platform_device``, you simply also implement your interrupt
handler and fill your ``struct uio_info``. A pointer to this
``struct uio_info`` is then used as ``platform_data`` for your platform
device.

You also need to set up an array of ``struct resource`` containing
addresses and sizes of your memory mappings. This information is passed
to the driver using the ``.resource`` and ``.num_resources`` elements of
``struct platform_device``.

You now have to set the ``.name`` element of ``struct platform_device``
to ``"uio_pdrv"`` to use the generic UIO platform device driver. This
driver will fill the ``mem[]`` array according to the resources given,
and register the device.

The advantage of this approach is that you only have to edit a file you
need to edit anyway. You do not have to create an extra driver.


.. _using_uio_pdrv_genirq:

Using uio_pdrv_genirq for platform devices
==========================================

Especially in embedded devices, you frequently find chips where the irq
pin is tied to its own dedicated interrupt line. In such cases, where
you can be really sure the interrupt is not shared, we can take the
concept of ``uio_pdrv`` one step further and use a generic interrupt
handler. That's what ``uio_pdrv_genirq`` does.

The setup for this driver is the same as described above for
``uio_pdrv``, except that you do not implement an interrupt handler. The
``.handler`` element of ``struct uio_info`` must remain ``NULL``. The
``.irq_flags`` element must not contain ``IRQF_SHARED``.

You will set the ``.name`` element of ``struct platform_device`` to
``"uio_pdrv_genirq"`` to use this driver.

The generic interrupt handler of ``uio_pdrv_genirq`` will simply disable
the interrupt line using ``disable_irq_nosync()``. After doing its work,
userspace can reenable the interrupt by writing 0x00000001 to the UIO
device file. The driver already implements an ``irq_control()`` to make
this possible, you must not implement your own.

Using ``uio_pdrv_genirq`` not only saves a few lines of interrupt
handler code. You also do not need to know anything about the chip's
internal registers to create the kernel part of the driver. All you need
to know is the irq number of the pin the chip is connected to.


.. _using-uio_dmem_genirq:

Using uio_dmem_genirq for platform devices
==========================================

In addition to statically allocated memory ranges, they may also be a
desire to use dynamically allocated regions in a user space driver. In
particular, being able to access memory made available through the
dma-mapping API, may be particularly useful. The ``uio_dmem_genirq``
driver provides a way to accomplish this.

This driver is used in a similar manner to the ``"uio_pdrv_genirq"``
driver with respect to interrupt configuration and handling.

Set the ``.name`` element of ``struct platform_device`` to
``"uio_dmem_genirq"`` to use this driver.

When using this driver, fill in the ``.platform_data`` element of
``struct platform_device``, which is of type
``struct uio_dmem_genirq_pdata`` and which contains the following
elements:

-  ``struct uio_info uioinfo``: The same structure used as the
   ``uio_pdrv_genirq`` platform data

-  ``unsigned int *dynamic_region_sizes``: Pointer to list of sizes of
   dynamic memory regions to be mapped into user space.

-  ``unsigned int num_dynamic_regions``: Number of elements in
   ``dynamic_region_sizes`` array.

The dynamic regions defined in the platform data will be appended to the
`` mem[] `` array after the platform device resources, which implies
that the total number of static and dynamic memory regions cannot exceed
``MAX_UIO_MAPS``.

The dynamic memory regions will be allocated when the UIO device file,
``/dev/uioX`` is opened. Similar to static memory resources, the memory
region information for dynamic regions is then visible via sysfs at
``/sys/class/uio/uioX/maps/mapY/*``. The dynamic memory regions will be
freed when the UIO device file is closed. When no processes are holding
the device file open, the address returned to userspace is ~0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
