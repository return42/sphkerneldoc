.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/driver.c

.. _`hfi1_reset_device`:

hfi1_reset_device
=================

.. c:function:: int hfi1_reset_device(int unit)

    reset the chip if possible

    :param unit:
        the device to reset
    :type unit: int

.. _`hfi1_reset_device.description`:

Description
-----------

Whether or not reset is successful, we attempt to re-initialize the chip
(that is, much like a driver unload/reload).  We clear the INITTED flag
so that the various entry points will fail until we reinitialize.  For
now, we only allow this if no user contexts are open that use chip resources

.. This file was automatic generated / don't edit.

