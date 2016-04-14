.. -*- coding: utf-8; mode: rst -*-

===============
drm_dp_helper.c
===============

.. _`dp-helpers`:

dp helpers
==========

These functions contain some common logic and helpers at various abstraction
levels to deal with Display Port sink devices and related things like DP aux
channel transfers, EDID reading over DP aux channels, decoding certain DPCD
blocks, ...


.. _`dp-helpers`:

dp helpers
==========

The DisplayPort AUX channel is an abstraction to allow generic, driver-
independent access to AUX functionality. Drivers can take advantage of
this by filling in the fields of the drm_dp_aux structure.

Transactions are described using a hardware-independent drm_dp_aux_msg
structure, which is passed into a driver's .:c:func:`transfer` implementation.
Both native and I2C-over-AUX transactions are supported.


.. _`drm_dp_dpcd_read`:

drm_dp_dpcd_read
================

.. c:function:: ssize_t drm_dp_dpcd_read (struct drm_dp_aux *aux, unsigned int offset, void *buffer, size_t size)

    read a series of bytes from the DPCD

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param unsigned int offset:
        address of the (first) register to read

    :param void \*buffer:
        buffer to store the register values

    :param size_t size:
        number of bytes in ``buffer``


.. _`drm_dp_dpcd_read.description`:

Description
-----------

Returns the number of bytes transferred on success, or a negative error
code on failure. -EIO is returned if the request was NAKed by the sink or
if the retry count was exceeded. If not all bytes were transferred, this
function returns -EPROTO. Errors from the underlying AUX channel transfer
function, with the exception of -EBUSY (which causes the transaction to
be retried), are propagated to the caller.


.. _`drm_dp_dpcd_write`:

drm_dp_dpcd_write
=================

.. c:function:: ssize_t drm_dp_dpcd_write (struct drm_dp_aux *aux, unsigned int offset, void *buffer, size_t size)

    write a series of bytes to the DPCD

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param unsigned int offset:
        address of the (first) register to write

    :param void \*buffer:
        buffer containing the values to write

    :param size_t size:
        number of bytes in ``buffer``


.. _`drm_dp_dpcd_write.description`:

Description
-----------

Returns the number of bytes transferred on success, or a negative error
code on failure. -EIO is returned if the request was NAKed by the sink or
if the retry count was exceeded. If not all bytes were transferred, this
function returns -EPROTO. Errors from the underlying AUX channel transfer
function, with the exception of -EBUSY (which causes the transaction to
be retried), are propagated to the caller.


.. _`drm_dp_dpcd_read_link_status`:

drm_dp_dpcd_read_link_status
============================

.. c:function:: int drm_dp_dpcd_read_link_status (struct drm_dp_aux *aux, u8 status[DP_LINK_STATUS_SIZE])

    read DPCD link status (bytes 0x202-0x207)

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param u8 status:
        buffer to store the link status in (must be at least 6 bytes)


.. _`drm_dp_dpcd_read_link_status.description`:

Description
-----------

Returns the number of bytes transferred on success or a negative error
code on failure.


.. _`drm_dp_link_probe`:

drm_dp_link_probe
=================

.. c:function:: int drm_dp_link_probe (struct drm_dp_aux *aux, struct drm_dp_link *link)

    probe a DisplayPort link for capabilities

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param struct drm_dp_link \*link:
        pointer to structure in which to return link capabilities


.. _`drm_dp_link_probe.description`:

Description
-----------

The structure filled in by this function can usually be passed directly
into :c:func:`drm_dp_link_power_up` and :c:func:`drm_dp_link_configure` to power up and
configure the link based on the link's capabilities.

Returns 0 on success or a negative error code on failure.


.. _`drm_dp_link_power_up`:

drm_dp_link_power_up
====================

.. c:function:: int drm_dp_link_power_up (struct drm_dp_aux *aux, struct drm_dp_link *link)

    power up a DisplayPort link

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param struct drm_dp_link \*link:
        pointer to a structure containing the link configuration


.. _`drm_dp_link_power_up.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`drm_dp_link_power_down`:

drm_dp_link_power_down
======================

.. c:function:: int drm_dp_link_power_down (struct drm_dp_aux *aux, struct drm_dp_link *link)

    power down a DisplayPort link

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param struct drm_dp_link \*link:
        pointer to a structure containing the link configuration


.. _`drm_dp_link_power_down.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`drm_dp_link_configure`:

drm_dp_link_configure
=====================

.. c:function:: int drm_dp_link_configure (struct drm_dp_aux *aux, struct drm_dp_link *link)

    configure a DisplayPort link

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param struct drm_dp_link \*link:
        pointer to a structure containing the link configuration


.. _`drm_dp_link_configure.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`drm_dp_aux_register`:

drm_dp_aux_register
===================

.. c:function:: int drm_dp_aux_register (struct drm_dp_aux *aux)

    initialise and register aux channel

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel


.. _`drm_dp_aux_register.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.


.. _`drm_dp_aux_unregister`:

drm_dp_aux_unregister
=====================

.. c:function:: void drm_dp_aux_unregister (struct drm_dp_aux *aux)

    unregister an AUX adapter

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

