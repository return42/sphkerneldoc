.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dp_helper.c

.. _`drm_dp_dpcd_read`:

drm_dp_dpcd_read
================

.. c:function:: ssize_t drm_dp_dpcd_read(struct drm_dp_aux *aux, unsigned int offset, void *buffer, size_t size)

    read a series of bytes from the DPCD

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param unsigned int offset:
        address of the (first) register to read

    :param void \*buffer:
        buffer to store the register values

    :param size_t size:
        number of bytes in \ ``buffer``\ 

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

.. c:function:: ssize_t drm_dp_dpcd_write(struct drm_dp_aux *aux, unsigned int offset, void *buffer, size_t size)

    write a series of bytes to the DPCD

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param unsigned int offset:
        address of the (first) register to write

    :param void \*buffer:
        buffer containing the values to write

    :param size_t size:
        number of bytes in \ ``buffer``\ 

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

.. c:function:: int drm_dp_dpcd_read_link_status(struct drm_dp_aux *aux, u8 status[DP_LINK_STATUS_SIZE])

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

.. c:function:: int drm_dp_link_probe(struct drm_dp_aux *aux, struct drm_dp_link *link)

    probe a DisplayPort link for capabilities

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param struct drm_dp_link \*link:
        pointer to structure in which to return link capabilities

.. _`drm_dp_link_probe.description`:

Description
-----------

The structure filled in by this function can usually be passed directly
into \ :c:func:`drm_dp_link_power_up`\  and \ :c:func:`drm_dp_link_configure`\  to power up and
configure the link based on the link's capabilities.

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_link_power_up`:

drm_dp_link_power_up
====================

.. c:function:: int drm_dp_link_power_up(struct drm_dp_aux *aux, struct drm_dp_link *link)

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

.. c:function:: int drm_dp_link_power_down(struct drm_dp_aux *aux, struct drm_dp_link *link)

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

.. c:function:: int drm_dp_link_configure(struct drm_dp_aux *aux, struct drm_dp_link *link)

    configure a DisplayPort link

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param struct drm_dp_link \*link:
        pointer to a structure containing the link configuration

.. _`drm_dp_link_configure.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_downstream_max_clock`:

drm_dp_downstream_max_clock
===========================

.. c:function:: int drm_dp_downstream_max_clock(const u8 dpcd[DP_RECEIVER_CAP_SIZE], const u8 port_cap[4])

    extract branch device max pixel rate for legacy VGA converter or max TMDS clock rate for others

    :param const u8 dpcd:
        DisplayPort configuration data

    :param const u8 port_cap:
        port capabilities

.. _`drm_dp_downstream_max_clock.description`:

Description
-----------

Returns max clock in kHz on success or 0 if max clock not defined

.. _`drm_dp_downstream_max_bpc`:

drm_dp_downstream_max_bpc
=========================

.. c:function:: int drm_dp_downstream_max_bpc(const u8 dpcd[DP_RECEIVER_CAP_SIZE], const u8 port_cap[4])

    extract branch device max bits per component

    :param const u8 dpcd:
        DisplayPort configuration data

    :param const u8 port_cap:
        port capabilities

.. _`drm_dp_downstream_max_bpc.description`:

Description
-----------

Returns max bpc on success or 0 if max bpc not defined

.. _`drm_dp_downstream_id`:

drm_dp_downstream_id
====================

.. c:function:: int drm_dp_downstream_id(struct drm_dp_aux *aux, char id[6])

    identify branch device

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param char id:
        DisplayPort branch device id

.. _`drm_dp_downstream_id.description`:

Description
-----------

Returns branch device id on success or NULL on failure

.. _`drm_dp_downstream_debug`:

drm_dp_downstream_debug
=======================

.. c:function:: void drm_dp_downstream_debug(struct seq_file *m, const u8 dpcd[DP_RECEIVER_CAP_SIZE], const u8 port_cap[4], struct drm_dp_aux *aux)

    debug DP branch devices

    :param struct seq_file \*m:
        pointer for debugfs file

    :param const u8 dpcd:
        DisplayPort configuration data

    :param const u8 port_cap:
        port capabilities

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

.. _`drm_dp_aux_init`:

drm_dp_aux_init
===============

.. c:function:: void drm_dp_aux_init(struct drm_dp_aux *aux)

    minimally initialise an aux channel

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

.. _`drm_dp_aux_init.description`:

Description
-----------

If you need to use the drm_dp_aux's i2c adapter prior to registering it
with the outside world, call \ :c:func:`drm_dp_aux_init`\  first. You must still
call \ :c:func:`drm_dp_aux_register`\  once the connector has been registered to
allow userspace access to the auxiliary DP channel.

.. _`drm_dp_aux_register`:

drm_dp_aux_register
===================

.. c:function:: int drm_dp_aux_register(struct drm_dp_aux *aux)

    initialise and register aux channel

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

.. _`drm_dp_aux_register.description`:

Description
-----------

Automatically calls \ :c:func:`drm_dp_aux_init`\  if this hasn't been done yet.

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_aux_unregister`:

drm_dp_aux_unregister
=====================

.. c:function:: void drm_dp_aux_unregister(struct drm_dp_aux *aux)

    unregister an AUX adapter

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

.. _`drm_dp_psr_setup_time`:

drm_dp_psr_setup_time
=====================

.. c:function:: int drm_dp_psr_setup_time(const u8 psr_cap[EDP_PSR_RECEIVER_CAP_SIZE])

    PSR setup in time usec

    :param const u8 psr_cap:
        PSR capabilities from DPCD

.. _`drm_dp_psr_setup_time.return`:

Return
------

PSR setup time for the panel in microseconds,  negative
error code on failure.

.. _`drm_dp_start_crc`:

drm_dp_start_crc
================

.. c:function:: int drm_dp_start_crc(struct drm_dp_aux *aux, struct drm_crtc *crtc)

    start capture of frame CRCs

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

    :param struct drm_crtc \*crtc:
        CRTC displaying the frames whose CRCs are to be captured

.. _`drm_dp_start_crc.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_stop_crc`:

drm_dp_stop_crc
===============

.. c:function:: int drm_dp_stop_crc(struct drm_dp_aux *aux)

    stop capture of frame CRCs

    :param struct drm_dp_aux \*aux:
        DisplayPort AUX channel

.. _`drm_dp_stop_crc.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. This file was automatic generated / don't edit.

