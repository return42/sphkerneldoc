
.. _API-struct-uio-info:

===============
struct uio_info
===============

*man struct uio_info(9)*

*4.6.0-rc1*

UIO device capabilities


Synopsis
========

.. code-block:: c

    struct uio_info {
      struct uio_device * uio_dev;
      const char * name;
      const char * version;
      struct uio_mem mem[MAX_UIO_MAPS];
      struct uio_port port[MAX_UIO_PORT_REGIONS];
      long irq;
      unsigned long irq_flags;
      void * priv;
      irqreturn_t (* handler) (int irq, struct uio_info *dev_info);
      int (* mmap) (struct uio_info *info, struct vm_area_struct *vma);
      int (* open) (struct uio_info *info, struct inode *inode);
      int (* release) (struct uio_info *info, struct inode *inode);
      int (* irqcontrol) (struct uio_info *info, s32 irq_on);
    };


Members
=======

uio_dev
    the UIO device this info belongs to

name
    device name

version
    device driver version

mem[MAX_UIO_MAPS]
    list of mappable memory regions, size==0 for end of list

port[MAX_UIO_PORT_REGIONS]
    list of port regions, size==0 for end of list

irq
    interrupt number or UIO_IRQ_CUSTOM

irq_flags
    flags for ``request_irq``

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
