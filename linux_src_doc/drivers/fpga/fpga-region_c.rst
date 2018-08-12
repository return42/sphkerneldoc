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

.. _`fpga_region_program_fpga.description`:

Description
-----------

Program an FPGA using fpga image info (region->info).
If the region has a get_bridges function, the exclusive reference for the
bridges will be held if programming succeeds.  This is intended to prevent
reprogramming the region until the caller considers it safe to do so.
The caller will need to call \ :c:func:`fpga_bridges_put`\  before attempting to
reprogram the region.

Return 0 for success or negative error code.

.. _`fpga_region_create`:

fpga_region_create
==================

.. c:function:: struct fpga_region *fpga_region_create(struct device *dev, struct fpga_manager *mgr, int (*get_bridges)(struct fpga_region *))

    alloc and init a struct fpga_region

    :param struct device \*dev:
        device parent

    :param struct fpga_manager \*mgr:
        manager that programs this region

    :param int (\*get_bridges)(struct fpga_region \*):
        optional function to get bridges to a list

.. _`fpga_region_create.return`:

Return
------

struct fpga_region or NULL

.. _`fpga_region_free`:

fpga_region_free
================

.. c:function:: void fpga_region_free(struct fpga_region *region)

    free a struct fpga_region

    :param struct fpga_region \*region:
        FPGA region created by fpga_region_create

.. _`fpga_region_register`:

fpga_region_register
====================

.. c:function:: int fpga_region_register(struct fpga_region *region)

    register a FPGA region

    :param struct fpga_region \*region:
        FPGA region created by fpga_region_create

.. _`fpga_region_register.return`:

Return
------

0 or -errno

.. _`fpga_region_unregister`:

fpga_region_unregister
======================

.. c:function:: void fpga_region_unregister(struct fpga_region *region)

    unregister and free a FPGA region

    :param struct fpga_region \*region:
        FPGA region

.. _`fpga_region_init`:

fpga_region_init
================

.. c:function:: int fpga_region_init( void)

    init function for fpga_region class Creates the fpga_region class and registers a reconfig notifier.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

