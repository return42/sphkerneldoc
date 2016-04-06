
.. _API-struct-uio-mem:

==============
struct uio_mem
==============

*man struct uio_mem(9)*

*4.6.0-rc1*

description of a UIO memory region


Synopsis
========

.. code-block:: c

    struct uio_mem {
      const char * name;
      phys_addr_t addr;
      resource_size_t size;
      int memtype;
      void __iomem * internal_addr;
      struct uio_map * map;
    };


Members
=======

name
    name of the memory region for identification

addr
    address of the device's memory (phys_addr is used since addr can be logical, virtual, or physical & phys_addr_t should always be large enough to handle any of the address
    types)

size
    size of IO

memtype
    type of memory addr points to

internal_addr
    ioremap-ped version of addr, for driver internal use

map
    for use by the UIO core only.
