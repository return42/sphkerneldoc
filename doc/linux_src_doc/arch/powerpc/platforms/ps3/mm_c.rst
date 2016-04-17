.. -*- coding: utf-8; mode: rst -*-

====
mm.c
====


.. _`mem_region`:

struct mem_region
=================

.. c:type:: mem_region

    memory region structure


.. _`mem_region.definition`:

Definition
----------

.. code-block:: c

  struct mem_region {
    u64 base;
    u64 size;
    unsigned long offset;
    int destroy;
  };


.. _`mem_region.members`:

Members
-------

:``base``:
    base address

:``size``:
    size in bytes

:``offset``:
    difference between base and rm.size

:``destroy``:
    flag if region should be destroyed upon shutdown




.. _`map`:

struct map
==========

.. c:type:: map

    address space state variables holder


.. _`map.definition`:

Definition
----------

.. code-block:: c

  struct map {
    u64 total;
    u64 htab_size;
    struct mem_region rm;
    struct mem_region r1;
  };


.. _`map.members`:

Members
-------

:``total``:
    total memory available as reported by HV
    ``vas_id`` - HV virtual address space id

:``htab_size``:
    htab size in bytes

:``rm``:
    real mode (bootmem) region

:``r1``:
    highmem region(s)




.. _`map.description`:

Description
-----------

ps3 addresses



.. _`map.description`:

Description
-----------

ps3 addresses



.. _`map.virt_addr`:

virt_addr
---------

a cpu 'translated' effective address



.. _`map.phys_addr`:

phys_addr
---------

an address in what Linux thinks is the physical address space



.. _`map.lpar_addr`:

lpar_addr
---------

an address in the HV virtual address space



.. _`map.bus_addr`:

bus_addr
--------

an io controller 'translated' address on a device bus



.. _`ps3_mm_phys_to_lpar`:

ps3_mm_phys_to_lpar
===================

.. c:function:: unsigned long ps3_mm_phys_to_lpar (unsigned long phys_addr)

    translate a linux physical address to lpar address

    :param unsigned long phys_addr:
        linux physical address



.. _`ps3_mm_vas_create`:

ps3_mm_vas_create
=================

.. c:function:: void ps3_mm_vas_create (unsigned long *htab_size)

    create the virtual address space

    :param unsigned long \*htab_size:

        *undescribed*



.. _`ps3_mm_vas_destroy`:

ps3_mm_vas_destroy
==================

.. c:function:: void ps3_mm_vas_destroy ( void)

    :param void:
        no arguments



.. _`ps3_mm_region_create`:

ps3_mm_region_create
====================

.. c:function:: int ps3_mm_region_create (struct mem_region *r, unsigned long size)

    create a memory region in the vas

    :param struct mem_region \*r:
        pointer to a struct mem_region to accept initialized values

    :param unsigned long size:
        requested region size



.. _`ps3_mm_region_create.description`:

Description
-----------

This implementation creates the region with the vas large page size.
``size`` is rounded down to a multiple of the vas large page size.



.. _`ps3_mm_region_destroy`:

ps3_mm_region_destroy
=====================

.. c:function:: void ps3_mm_region_destroy (struct mem_region *r)

    destroy a memory region

    :param struct mem_region \*r:
        pointer to struct mem_region



.. _`dma_sb_lpar_to_bus`:

dma_sb_lpar_to_bus
==================

.. c:function:: unsigned long dma_sb_lpar_to_bus (struct ps3_dma_region *r, unsigned long lpar_addr)

    Translate an lpar address to ioc mapped bus address.

    :param struct ps3_dma_region \*r:
        pointer to dma region structure

    :param unsigned long lpar_addr:
        HV lpar address



.. _`dma_sb_map_pages`:

dma_sb_map_pages
================

.. c:function:: int dma_sb_map_pages (struct ps3_dma_region *r, unsigned long phys_addr, unsigned long len, struct dma_chunk **c_out, u64 iopte_flag)

    Maps dma pages into the io controller bus address space.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.

    :param unsigned long phys_addr:
        Starting physical address of the area to map.

    :param unsigned long len:
        Length in bytes of the area to map.

    :param struct dma_chunk \*\*c_out:

        *undescribed*

    :param u64 iopte_flag:

        *undescribed*



.. _`dma_sb_map_pages.c_out`:

c_out
-----

A pointer to receive an allocated struct dma_chunk for this area.

This is the lowest level dma mapping routine, and is the one that will
make the HV call to add the pages into the io controller address space.



.. _`dma_sb_region_create`:

dma_sb_region_create
====================

.. c:function:: int dma_sb_region_create (struct ps3_dma_region *r)

    Create a device dma region.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.



.. _`dma_sb_region_create.description`:

Description
-----------

This is the lowest level dma region create routine, and is the one that
will make the HV call to create the region.



.. _`dma_sb_region_free`:

dma_sb_region_free
==================

.. c:function:: int dma_sb_region_free (struct ps3_dma_region *r)

    Free a device dma region.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.



.. _`dma_sb_region_free.description`:

Description
-----------

This is the lowest level dma region free routine, and is the one that
will make the HV call to free the region.



.. _`dma_sb_map_area`:

dma_sb_map_area
===============

.. c:function:: int dma_sb_map_area (struct ps3_dma_region *r, unsigned long virt_addr, unsigned long len, dma_addr_t *bus_addr, u64 iopte_flag)

    Map an area of memory into a device dma region.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.

    :param unsigned long virt_addr:
        Starting virtual address of the area to map.

    :param unsigned long len:
        Length in bytes of the area to map.

    :param dma_addr_t \*bus_addr:
        A pointer to return the starting ioc bus address of the area to
        map.

    :param u64 iopte_flag:

        *undescribed*



.. _`dma_sb_map_area.description`:

Description
-----------

This is the common dma mapping routine.



.. _`dma_sb_unmap_area`:

dma_sb_unmap_area
=================

.. c:function:: int dma_sb_unmap_area (struct ps3_dma_region *r, dma_addr_t bus_addr, unsigned long len)

    Unmap an area of memory from a device dma region.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.

    :param dma_addr_t bus_addr:
        The starting ioc bus address of the area to unmap.

    :param unsigned long len:
        Length in bytes of the area to unmap.



.. _`dma_sb_unmap_area.description`:

Description
-----------

This is the common dma unmap routine.



.. _`dma_sb_region_create_linear`:

dma_sb_region_create_linear
===========================

.. c:function:: int dma_sb_region_create_linear (struct ps3_dma_region *r)

    Setup a linear dma mapping for a device.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.



.. _`dma_sb_region_create_linear.description`:

Description
-----------

This routine creates an HV dma region for the device and maps all available
ram into the io controller bus address space.



.. _`dma_sb_region_free_linear`:

dma_sb_region_free_linear
=========================

.. c:function:: int dma_sb_region_free_linear (struct ps3_dma_region *r)

    Free a linear dma mapping for a device.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.



.. _`dma_sb_region_free_linear.description`:

Description
-----------

This routine will unmap all mapped areas and free the HV dma region.



.. _`dma_sb_map_area_linear`:

dma_sb_map_area_linear
======================

.. c:function:: int dma_sb_map_area_linear (struct ps3_dma_region *r, unsigned long virt_addr, unsigned long len, dma_addr_t *bus_addr, u64 iopte_flag)

    Map an area of memory into a device dma region.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.

    :param unsigned long virt_addr:
        Starting virtual address of the area to map.

    :param unsigned long len:
        Length in bytes of the area to map.

    :param dma_addr_t \*bus_addr:
        A pointer to return the starting ioc bus address of the area to
        map.

    :param u64 iopte_flag:

        *undescribed*



.. _`dma_sb_map_area_linear.description`:

Description
-----------

This routine just returns the corresponding bus address.  Actual mapping
occurs in :c:func:`dma_region_create_linear`.



.. _`dma_sb_unmap_area_linear`:

dma_sb_unmap_area_linear
========================

.. c:function:: int dma_sb_unmap_area_linear (struct ps3_dma_region *r, dma_addr_t bus_addr, unsigned long len)

    Unmap an area of memory from a device dma region.

    :param struct ps3_dma_region \*r:
        Pointer to a struct ps3_dma_region.

    :param dma_addr_t bus_addr:
        The starting ioc bus address of the area to unmap.

    :param unsigned long len:
        Length in bytes of the area to unmap.



.. _`dma_sb_unmap_area_linear.description`:

Description
-----------

This routine does nothing.  Unmapping occurs in :c:func:`dma_sb_region_free_linear`.



.. _`ps3_mm_init`:

ps3_mm_init
===========

.. c:function:: void ps3_mm_init ( void)

    initialize the address space state variables

    :param void:
        no arguments



.. _`ps3_mm_shutdown`:

ps3_mm_shutdown
===============

.. c:function:: void ps3_mm_shutdown ( void)

    final cleanup of address space

    :param void:
        no arguments

