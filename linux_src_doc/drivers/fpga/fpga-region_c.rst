.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/fpga-region.c

.. _`fpga_region_get`:

fpga_region_get
===============

.. c:function:: struct fpga_region *fpga_region_get(struct fpga_region *region)

    get an exclusive reference to a fpga region

    :param region:
        FPGA Region struct
    :type region: struct fpga_region \*

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

    :param region:
        FPGA region
    :type region: struct fpga_region \*

.. _`fpga_region_program_fpga`:

fpga_region_program_fpga
========================

.. c:function:: int fpga_region_program_fpga(struct fpga_region *region)

    program FPGA

    :param region:
        FPGA region
    :type region: struct fpga_region \*

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

    :param dev:
        device parent
    :type dev: struct device \*

    :param mgr:
        manager that programs this region
    :type mgr: struct fpga_manager \*

    :param int (\*get_bridges)(struct fpga_region \*):
        optional function to get bridges to a list

.. _`fpga_region_create.description`:

Description
-----------

The caller of this function is responsible for freeing the resulting region
struct with \ :c:func:`fpga_region_free`\ .  Using \ :c:func:`devm_fpga_region_create`\  instead is
recommended.

.. _`fpga_region_create.return`:

Return
------

struct fpga_region or NULL

.. _`fpga_region_free`:

fpga_region_free
================

.. c:function:: void fpga_region_free(struct fpga_region *region)

    free a FPGA region created by \ :c:func:`fpga_region_create`\ 

    :param region:
        FPGA region
    :type region: struct fpga_region \*

.. _`devm_fpga_region_create`:

devm_fpga_region_create
=======================

.. c:function:: struct fpga_region *devm_fpga_region_create(struct device *dev, struct fpga_manager *mgr, int (*get_bridges)(struct fpga_region *))

    create and initialize a managed FPGA region struct

    :param dev:
        device parent
    :type dev: struct device \*

    :param mgr:
        manager that programs this region
    :type mgr: struct fpga_manager \*

    :param int (\*get_bridges)(struct fpga_region \*):
        optional function to get bridges to a list

.. _`devm_fpga_region_create.description`:

Description
-----------

This function is intended for use in a FPGA region driver's probe function.
After the region driver creates the region struct with
\ :c:func:`devm_fpga_region_create`\ , it should register it with \ :c:func:`fpga_region_register`\ .
The region driver's remove function should call \ :c:func:`fpga_region_unregister`\ .
The region struct allocated with this function will be freed automatically on
driver detach.  This includes the case of a probe function returning error
before calling \ :c:func:`fpga_region_register`\ , the struct will still get cleaned up.

.. _`devm_fpga_region_create.return`:

Return
------

struct fpga_region or NULL

.. _`fpga_region_register`:

fpga_region_register
====================

.. c:function:: int fpga_region_register(struct fpga_region *region)

    register a FPGA region

    :param region:
        FPGA region
    :type region: struct fpga_region \*

.. _`fpga_region_register.return`:

Return
------

0 or -errno

.. _`fpga_region_unregister`:

fpga_region_unregister
======================

.. c:function:: void fpga_region_unregister(struct fpga_region *region)

    unregister a FPGA region

    :param region:
        FPGA region
    :type region: struct fpga_region \*

.. _`fpga_region_unregister.description`:

Description
-----------

This function is intended for use in a FPGA region driver's remove function.

.. _`fpga_region_init`:

fpga_region_init
================

.. c:function:: int fpga_region_init( void)

    init function for fpga_region class Creates the fpga_region class and registers a reconfig notifier.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

