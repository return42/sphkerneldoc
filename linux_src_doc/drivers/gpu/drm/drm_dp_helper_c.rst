.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dp_helper.c

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
structure, which is passed into a driver's .transfer() implementation.
Both native and I2C-over-AUX transactions are supported.

.. _`drm_dp_dpcd_read`:

drm_dp_dpcd_read
================

.. c:function:: ssize_t drm_dp_dpcd_read(struct drm_dp_aux *aux, unsigned int offset, void *buffer, size_t size)

    read a series of bytes from the DPCD

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param offset:
        address of the (first) register to read
    :type offset: unsigned int

    :param buffer:
        buffer to store the register values
    :type buffer: void \*

    :param size:
        number of bytes in \ ``buffer``\ 
    :type size: size_t

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

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param offset:
        address of the (first) register to write
    :type offset: unsigned int

    :param buffer:
        buffer containing the values to write
    :type buffer: void \*

    :param size:
        number of bytes in \ ``buffer``\ 
    :type size: size_t

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

.. c:function:: int drm_dp_dpcd_read_link_status(struct drm_dp_aux *aux, u8 status)

    read DPCD link status (bytes 0x202-0x207)

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param status:
        buffer to store the link status in (must be at least 6 bytes)
    :type status: u8

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

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param link:
        pointer to structure in which to return link capabilities
    :type link: struct drm_dp_link \*

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

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param link:
        pointer to a structure containing the link configuration
    :type link: struct drm_dp_link \*

.. _`drm_dp_link_power_up.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_link_power_down`:

drm_dp_link_power_down
======================

.. c:function:: int drm_dp_link_power_down(struct drm_dp_aux *aux, struct drm_dp_link *link)

    power down a DisplayPort link

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param link:
        pointer to a structure containing the link configuration
    :type link: struct drm_dp_link \*

.. _`drm_dp_link_power_down.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_link_configure`:

drm_dp_link_configure
=====================

.. c:function:: int drm_dp_link_configure(struct drm_dp_aux *aux, struct drm_dp_link *link)

    configure a DisplayPort link

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param link:
        pointer to a structure containing the link configuration
    :type link: struct drm_dp_link \*

.. _`drm_dp_link_configure.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_downstream_max_clock`:

drm_dp_downstream_max_clock
===========================

.. c:function:: int drm_dp_downstream_max_clock(const u8 dpcd, const u8 port_cap)

    extract branch device max pixel rate for legacy VGA converter or max TMDS clock rate for others

    :param dpcd:
        DisplayPort configuration data
    :type dpcd: const u8

    :param port_cap:
        port capabilities
    :type port_cap: const u8

.. _`drm_dp_downstream_max_clock.description`:

Description
-----------

Returns max clock in kHz on success or 0 if max clock not defined

.. _`drm_dp_downstream_max_bpc`:

drm_dp_downstream_max_bpc
=========================

.. c:function:: int drm_dp_downstream_max_bpc(const u8 dpcd, const u8 port_cap)

    extract branch device max bits per component

    :param dpcd:
        DisplayPort configuration data
    :type dpcd: const u8

    :param port_cap:
        port capabilities
    :type port_cap: const u8

.. _`drm_dp_downstream_max_bpc.description`:

Description
-----------

Returns max bpc on success or 0 if max bpc not defined

.. _`drm_dp_downstream_id`:

drm_dp_downstream_id
====================

.. c:function:: int drm_dp_downstream_id(struct drm_dp_aux *aux, char id)

    identify branch device

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param id:
        DisplayPort branch device id
    :type id: char

.. _`drm_dp_downstream_id.description`:

Description
-----------

Returns branch device id on success or NULL on failure

.. _`drm_dp_downstream_debug`:

drm_dp_downstream_debug
=======================

.. c:function:: void drm_dp_downstream_debug(struct seq_file *m, const u8 dpcd, const u8 port_cap, struct drm_dp_aux *aux)

    debug DP branch devices

    :param m:
        pointer for debugfs file
    :type m: struct seq_file \*

    :param dpcd:
        DisplayPort configuration data
    :type dpcd: const u8

    :param port_cap:
        port capabilities
    :type port_cap: const u8

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

.. _`drm_dp_aux_init`:

drm_dp_aux_init
===============

.. c:function:: void drm_dp_aux_init(struct drm_dp_aux *aux)

    minimally initialise an aux channel

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

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

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

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

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

.. _`drm_dp_psr_setup_time`:

drm_dp_psr_setup_time
=====================

.. c:function:: int drm_dp_psr_setup_time(const u8 psr_cap)

    PSR setup in time usec

    :param psr_cap:
        PSR capabilities from DPCD
    :type psr_cap: const u8

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

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param crtc:
        CRTC displaying the frames whose CRCs are to be captured
    :type crtc: struct drm_crtc \*

.. _`drm_dp_start_crc.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_stop_crc`:

drm_dp_stop_crc
===============

.. c:function:: int drm_dp_stop_crc(struct drm_dp_aux *aux)

    stop capture of frame CRCs

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

.. _`drm_dp_stop_crc.description`:

Description
-----------

Returns 0 on success or a negative error code on failure.

.. _`drm_dp_read_desc`:

drm_dp_read_desc
================

.. c:function:: int drm_dp_read_desc(struct drm_dp_aux *aux, struct drm_dp_desc *desc, bool is_branch)

    read sink/branch descriptor from DPCD

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param desc:
        Device decriptor to fill from DPCD
    :type desc: struct drm_dp_desc \*

    :param is_branch:
        true for branch devices, false for sink devices
    :type is_branch: bool

.. _`drm_dp_read_desc.description`:

Description
-----------

Read DPCD 0x400 (sink) or 0x500 (branch) into \ ``desc``\ . Also debug log the
identification.

Returns 0 on success or a negative error code on failure.

.. This file was automatic generated / don't edit.

