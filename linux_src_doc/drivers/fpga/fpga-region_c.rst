.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/fpga-region.c

.. _`fpga_region_get`:

fpga_region_get
===============

.. c:function:: struct fpga_region *fpga_region_get(struct fpga_region *region)

    get an exclusive reference to a fpga region

    :param struct fpga_region \*region:
        FPGA Region struct

.. _`fpga_region_get.description`:

Description
-----------

Caller should call \ :c:func:`fpga_region_put`\  when done with region.

Return fpga_region struct if successful.
Return -EBUSY if someone already has a reference to the region.
Return -ENODEV if \ ``np``\  is not a FPGA Region.

.. _`fpga_region_put`:

fpga_region_put
===============

.. c:function:: void fpga_region_put(struct fpga_region *region)

    release a reference to a region

    :param struct fpga_region \*region:
        FPGA region

.. _`fpga_region_program_fpga`:

fpga_region_program_fpga
========================

.. c:function:: int fpga_region_program_fpga(struct fpga_region *region)

    program FPGA

    :param struct fpga_region \*region:
        FPGA region
        Program an FPGA using fpga image info (region->info).
        Return 0 for success or negative error code.

.. _`fpga_region_init`:

fpga_region_init
================

.. c:function:: int fpga_region_init( void)

    init function for fpga_region class Creates the fpga_region class and registers a reconfig notifier.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

