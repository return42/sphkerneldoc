.. -*- coding: utf-8; mode: rst -*-

==========
op-reset.c
==========

.. _`wimax_reset`:

wimax_reset
===========

.. c:function:: int wimax_reset (struct wimax_dev *wimax_dev)

    Reset a WiMAX device

    :param struct wimax_dev \*wimax_dev:
        WiMAX device descriptor


.. _`wimax_reset.description`:

Description
-----------

Returns:

``0`` if ok and a warm reset was done (the device still exists in
the system).

-\ ``ENODEV`` if a cold/bus reset had to be done (device has
disconnected and reconnected, so current handle is not valid
any more).

-\ ``EINVAL`` if the device is not even registered.

Any other negative error code shall be considered as
non-recoverable.

Description:

Called when wanting to reset the device for any reason. Device is
taken back to power on status.

This call blocks; on successful return, the device has completed the
reset process and is ready to operate.

