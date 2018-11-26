.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/typec/bus.c

.. _`typec_altmode_set_mux`:

typec_altmode_set_mux
=====================

.. c:function:: int typec_altmode_set_mux(struct altmode *alt, u8 state)

    C Alternate Modes

    :param alt:
        *undescribed*
    :type alt: struct altmode \*

    :param state:
        *undescribed*
    :type state: u8

.. _`typec_altmode_set_mux.description`:

Description
-----------

Copyright (C) 2018 Intel Corporation
Author: Heikki Krogerus <heikki.krogerus@linux.intel.com>

.. _`typec_altmode_notify`:

typec_altmode_notify
====================

.. c:function:: int typec_altmode_notify(struct typec_altmode *adev, unsigned long conf, void *data)

    Communication between the OS and alternate mode driver

    :param adev:
        Handle to the alternate mode
    :type adev: struct typec_altmode \*

    :param conf:
        Alternate mode specific configuration value
    :type conf: unsigned long

    :param data:
        Alternate mode specific data
    :type data: void \*

.. _`typec_altmode_notify.description`:

Description
-----------

The primary purpose for this function is to allow the alternate mode drivers
to tell which pin configuration has been negotiated with the partner. That
information will then be used for example to configure the muxes.
Communication to the other direction is also possible, and low level device
drivers can also send notifications to the alternate mode drivers. The actual
communication will be specific for every SVID.

.. _`typec_altmode_enter`:

typec_altmode_enter
===================

.. c:function:: int typec_altmode_enter(struct typec_altmode *adev)

    Enter Mode

    :param adev:
        The alternate mode
    :type adev: struct typec_altmode \*

.. _`typec_altmode_enter.description`:

Description
-----------

The alternate mode drivers use this function to enter mode. The port drivers
use this to inform the alternate mode drivers that the partner has initiated
Enter Mode command.

.. _`typec_altmode_exit`:

typec_altmode_exit
==================

.. c:function:: int typec_altmode_exit(struct typec_altmode *adev)

    Exit Mode

    :param adev:
        The alternate mode
    :type adev: struct typec_altmode \*

.. _`typec_altmode_exit.description`:

Description
-----------

The partner of \ ``adev``\  has initiated Exit Mode command.

.. _`typec_altmode_attention`:

typec_altmode_attention
=======================

.. c:function:: void typec_altmode_attention(struct typec_altmode *adev, u32 vdo)

    Attention command

    :param adev:
        The alternate mode
    :type adev: struct typec_altmode \*

    :param vdo:
        VDO for the Attention command
    :type vdo: u32

.. _`typec_altmode_attention.description`:

Description
-----------

Notifies the partner of \ ``adev``\  about Attention command.

.. _`typec_altmode_vdm`:

typec_altmode_vdm
=================

.. c:function:: int typec_altmode_vdm(struct typec_altmode *adev, const u32 header, const u32 *vdo, int count)

    Send Vendor Defined Messages (VDM) to the partner

    :param adev:
        Alternate mode handle
    :type adev: struct typec_altmode \*

    :param header:
        VDM Header
    :type header: const u32

    :param vdo:
        Array of Vendor Defined Data Objects
    :type vdo: const u32 \*

    :param count:
        Number of Data Objects
    :type count: int

.. _`typec_altmode_vdm.description`:

Description
-----------

The alternate mode drivers use this function for SVID specific communication
with the partner. The port drivers use it to deliver the Structured VDMs
received from the partners to the alternate mode drivers.

.. _`typec_altmode_get_plug`:

typec_altmode_get_plug
======================

.. c:function:: struct typec_altmode *typec_altmode_get_plug(struct typec_altmode *adev, enum typec_plug_index index)

    Find cable plug alternate mode

    :param adev:
        Handle to partner alternate mode
    :type adev: struct typec_altmode \*

    :param index:
        Cable plug index
    :type index: enum typec_plug_index

.. _`typec_altmode_get_plug.description`:

Description
-----------

Increment reference count for cable plug alternate mode device. Returns
handle to the cable plug alternate mode, or NULL if none is found.

.. _`typec_altmode_put_plug`:

typec_altmode_put_plug
======================

.. c:function:: void typec_altmode_put_plug(struct typec_altmode *plug)

    Decrement cable plug alternate mode reference count

    :param plug:
        Handle to the cable plug alternate mode
    :type plug: struct typec_altmode \*

.. _`typec_match_altmode`:

typec_match_altmode
===================

.. c:function:: struct typec_altmode *typec_match_altmode(struct typec_altmode **altmodes, size_t n, u16 svid, u8 mode)

    Match SVID and mode to an array of alternate modes

    :param altmodes:
        Array of alternate modes
    :type altmodes: struct typec_altmode \*\*

    :param n:
        Number of elements in the array, or -1 for NULL terminated arrays
    :type n: size_t

    :param svid:
        Standard or Vendor ID to match with
    :type svid: u16

    :param mode:
        Mode to match with
    :type mode: u8

.. _`typec_match_altmode.description`:

Description
-----------

Return pointer to an alternate mode with SVID matching \ ``svid``\ , or NULL when no
match is found.

.. This file was automatic generated / don't edit.

