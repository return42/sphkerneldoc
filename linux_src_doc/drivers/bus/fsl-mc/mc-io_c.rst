.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/mc-io.c

.. _`fsl_create_mc_io`:

fsl_create_mc_io
================

.. c:function:: int fsl_create_mc_io(struct device *dev, phys_addr_t mc_portal_phys_addr, u32 mc_portal_size, struct fsl_mc_device *dpmcp_dev, u32 flags, struct fsl_mc_io **new_mc_io)

    :param dev:
        device to be associated with the MC I/O object
    :type dev: struct device \*

    :param mc_portal_phys_addr:
        physical address of the MC portal to use
    :type mc_portal_phys_addr: phys_addr_t

    :param mc_portal_size:
        size in bytes of the MC portal
    :type mc_portal_size: u32

    :param dpmcp_dev:
        *undescribed*
    :type dpmcp_dev: struct fsl_mc_device \*

    :param flags:
        flags for the new MC I/O object
    :type flags: u32

    :param new_mc_io:
        Area to return pointer to newly created MC I/O object
    :type new_mc_io: struct fsl_mc_io \*\*

.. _`fsl_create_mc_io.description`:

Description
-----------

Returns '0' on Success; Error code otherwise.

.. _`fsl_destroy_mc_io`:

fsl_destroy_mc_io
=================

.. c:function:: void fsl_destroy_mc_io(struct fsl_mc_io *mc_io)

    :param mc_io:
        MC I/O object to destroy
    :type mc_io: struct fsl_mc_io \*

.. _`fsl_mc_portal_allocate`:

fsl_mc_portal_allocate
======================

.. c:function:: int fsl_mc_portal_allocate(struct fsl_mc_device *mc_dev, u16 mc_io_flags, struct fsl_mc_io **new_mc_io)

    Allocates an MC portal

    :param mc_dev:
        MC device for which the MC portal is to be allocated
    :type mc_dev: struct fsl_mc_device \*

    :param mc_io_flags:
        Flags for the fsl_mc_io object that wraps the allocated
        MC portal.
    :type mc_io_flags: u16

    :param new_mc_io:
        Pointer to area where the pointer to the fsl_mc_io object
        that wraps the allocated MC portal is to be returned
    :type new_mc_io: struct fsl_mc_io \*\*

.. _`fsl_mc_portal_allocate.description`:

Description
-----------

This function allocates an MC portal from the device's parent DPRC,
from the corresponding MC bus' pool of MC portals and wraps
it in a new fsl_mc_io object. If 'mc_dev' is a DPRC itself, the
portal is allocated from its own MC bus.

.. _`fsl_mc_portal_free`:

fsl_mc_portal_free
==================

.. c:function:: void fsl_mc_portal_free(struct fsl_mc_io *mc_io)

    Returns an MC portal to the pool of free MC portals of a given MC bus

    :param mc_io:
        Pointer to the fsl_mc_io object that wraps the MC portal to free
    :type mc_io: struct fsl_mc_io \*

.. _`fsl_mc_portal_reset`:

fsl_mc_portal_reset
===================

.. c:function:: int fsl_mc_portal_reset(struct fsl_mc_io *mc_io)

    Resets the dpmcp object for a given fsl_mc_io object

    :param mc_io:
        Pointer to the fsl_mc_io object that wraps the MC portal to free
    :type mc_io: struct fsl_mc_io \*

.. This file was automatic generated / don't edit.

