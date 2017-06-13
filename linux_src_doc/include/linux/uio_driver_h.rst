.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/uio_driver.h

.. _`uio_mem`:

struct uio_mem
==============

.. c:type:: struct uio_mem

    description of a UIO memory region

.. _`uio_mem.definition`:

Definition
----------

.. code-block:: c

    struct uio_mem {
        const char *name;
        phys_addr_t addr;
        unsigned long offs;
        resource_size_t size;
        int memtype;
        void __iomem *internal_addr;
        struct uio_map *map;
    }

.. _`uio_mem.members`:

Members
-------

name
    name of the memory region for identification

addr
    address of the device's memory rounded to page
    size (phys_addr is used since addr can be
    logical, virtual, or physical & phys_addr_t
    should always be large enough to handle any of
    the address types)

offs
    offset of device memory within the page

size
    size of IO (multiple of page size)

memtype
    type of memory addr points to

internal_addr
    ioremap-ped version of addr, for driver internal use

map
    for use by the UIO core only.

.. _`uio_port`:

struct uio_port
===============

.. c:type:: struct uio_port

    description of a UIO port region

.. _`uio_port.definition`:

Definition
----------

.. code-block:: c

    struct uio_port {
        const char *name;
        unsigned long start;
        unsigned long size;
        int porttype;
        struct uio_portio *portio;
    }

.. _`uio_port.members`:

Members
-------

name
    name of the port region for identification

start
    start of port region

size
    size of port region

porttype
    type of port (see UIO_PORT_* below)

portio
    for use by the UIO core only.

.. _`uio_info`:

struct uio_info
===============

.. c:type:: struct uio_info

    UIO device capabilities

.. _`uio_info.definition`:

Definition
----------

.. code-block:: c

    struct uio_info {
        struct uio_device *uio_dev;
        const char *name;
        const char *version;
        struct uio_mem mem;
        struct uio_port port;
        long irq;
        unsigned long irq_flags;
        void *priv;
        irqreturn_t (*handler)(int irq, struct uio_info *dev_info);
        int (*mmap)(struct uio_info *info, struct vm_area_struct *vma);
        int (*open)(struct uio_info *info, struct inode *inode);
        int (*release)(struct uio_info *info, struct inode *inode);
        int (*irqcontrol)(struct uio_info *info, s32 irq_on);
    }

.. _`uio_info.members`:

Members
-------

uio_dev
    the UIO device this info belongs to

name
    device name

version
    device driver version

mem
    list of mappable memory regions, size==0 for end of list

port
    list of port regions, size==0 for end of list

irq
    interrupt number or UIO_IRQ_CUSTOM

irq_flags
    flags for \ :c:func:`request_irq`\ 

priv
    optional private data

handler
    the device's irq handler

mmap
    mmap operation for this uio device

open
    open operation for this uio device

release
    release operation for this uio device

irqcontrol
    disable/enable irqs when 0/1 is written to /dev/uioX

.. This file was automatic generated / don't edit.

