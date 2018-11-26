.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/fman/fman.c

.. _`fman_register_intr`:

fman_register_intr
==================

.. c:function:: void fman_register_intr(struct fman *fman, enum fman_event_modules module, u8 mod_id, enum fman_intr_type intr_type, void (*isr_cb)(void *src_arg), void *src_arg)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

    :param module:
        *undescribed*
    :type module: enum fman_event_modules

    :param mod_id:
        Module id (if more than 1 exists, '0' if not)
    :type mod_id: u8

    :param intr_type:
        Interrupt type (error/normal) selection.
    :type intr_type: enum fman_intr_type

    :param void (\*isr_cb)(void \*src_arg):
        *undescribed*

    :param src_arg:
        *undescribed*
    :type src_arg: void \*

.. _`fman_register_intr.description`:

Description
-----------

Used to register an event handler to be processed by FMan

.. _`fman_register_intr.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_unregister_intr`:

fman_unregister_intr
====================

.. c:function:: void fman_unregister_intr(struct fman *fman, enum fman_event_modules module, u8 mod_id, enum fman_intr_type intr_type)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

    :param module:
        *undescribed*
    :type module: enum fman_event_modules

    :param mod_id:
        Module id (if more than 1 exists, '0' if not)
    :type mod_id: u8

    :param intr_type:
        Interrupt type (error/normal) selection.
    :type intr_type: enum fman_intr_type

.. _`fman_unregister_intr.description`:

Description
-----------

Used to unregister an event handler to be processed by FMan

.. _`fman_unregister_intr.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_set_port_params`:

fman_set_port_params
====================

.. c:function:: int fman_set_port_params(struct fman *fman, struct fman_port_init_params *port_params)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

    :param port_params:
        Port parameters
    :type port_params: struct fman_port_init_params \*

.. _`fman_set_port_params.description`:

Description
-----------

Used by FMan Port to pass parameters to the FMan

.. _`fman_set_port_params.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_reset_mac`:

fman_reset_mac
==============

.. c:function:: int fman_reset_mac(struct fman *fman, u8 mac_id)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

    :param mac_id:
        MAC id to be reset
    :type mac_id: u8

.. _`fman_reset_mac.description`:

Description
-----------

Reset a specific MAC

.. _`fman_reset_mac.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_set_mac_max_frame`:

fman_set_mac_max_frame
======================

.. c:function:: int fman_set_mac_max_frame(struct fman *fman, u8 mac_id, u16 mfl)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

    :param mac_id:
        MAC id
    :type mac_id: u8

    :param mfl:
        Maximum frame length
    :type mfl: u16

.. _`fman_set_mac_max_frame.description`:

Description
-----------

Set maximum frame length of specific MAC in FMan driver

.. _`fman_set_mac_max_frame.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_get_clock_freq`:

fman_get_clock_freq
===================

.. c:function:: u16 fman_get_clock_freq(struct fman *fman)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

.. _`fman_get_clock_freq.description`:

Description
-----------

Get FMan clock frequency

.. _`fman_get_clock_freq.return`:

Return
------

FMan clock frequency

.. _`fman_get_bmi_max_fifo_size`:

fman_get_bmi_max_fifo_size
==========================

.. c:function:: u32 fman_get_bmi_max_fifo_size(struct fman *fman)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

.. _`fman_get_bmi_max_fifo_size.description`:

Description
-----------

Get FMan maximum FIFO size

.. _`fman_get_bmi_max_fifo_size.return`:

Return
------

FMan Maximum FIFO size

.. _`fman_get_revision`:

fman_get_revision
=================

.. c:function:: void fman_get_revision(struct fman *fman, struct fman_rev_info *rev_info)

    \ ``fman``\                 - Pointer to the FMan module \ ``rev_info``\             - A structure of revision information parameters.

    :param fman:
        *undescribed*
    :type fman: struct fman \*

    :param rev_info:
        *undescribed*
    :type rev_info: struct fman_rev_info \*

.. _`fman_get_revision.description`:

Description
-----------

Returns the FM revision

Allowed only following \ :c:func:`fman_init`\ .

.. _`fman_get_revision.return`:

Return
------

0 on success; Error code otherwise.

.. _`fman_get_qman_channel_id`:

fman_get_qman_channel_id
========================

.. c:function:: u32 fman_get_qman_channel_id(struct fman *fman, u32 port_id)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

    :param port_id:
        Port id
    :type port_id: u32

.. _`fman_get_qman_channel_id.description`:

Description
-----------

Get QMan channel ID associated to the Port id

.. _`fman_get_qman_channel_id.return`:

Return
------

QMan channel ID

.. _`fman_get_mem_region`:

fman_get_mem_region
===================

.. c:function:: struct resource *fman_get_mem_region(struct fman *fman)

    :param fman:
        A Pointer to FMan device
    :type fman: struct fman \*

.. _`fman_get_mem_region.description`:

Description
-----------

Get FMan memory region

.. _`fman_get_mem_region.return`:

Return
------

A structure with FMan memory region information

.. _`fman_get_max_frm`:

fman_get_max_frm
================

.. c:function:: u16 fman_get_max_frm( void)

    :param void:
        no arguments
    :type void: 

.. _`fman_get_max_frm.return`:

Return
------

Max frame length configured in the FM driver

.. _`fman_get_rx_extra_headroom`:

fman_get_rx_extra_headroom
==========================

.. c:function:: int fman_get_rx_extra_headroom( void)

    :param void:
        no arguments
    :type void: 

.. _`fman_get_rx_extra_headroom.return`:

Return
------

Extra headroom size configured in the FM driver

.. _`fman_bind`:

fman_bind
=========

.. c:function:: struct fman *fman_bind(struct device *fm_dev)

    :param fm_dev:
        *undescribed*
    :type fm_dev: struct device \*

.. _`fman_bind.description`:

Description
-----------

Bind to a specific FMan device.

Allowed only after the port was created.

.. _`fman_bind.return`:

Return
------

A pointer to the FMan device

.. This file was automatic generated / don't edit.

