.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/vmmouse.c

.. _`vmmouse_data`:

struct vmmouse_data
===================

.. c:type:: struct vmmouse_data

    private data structure for the vmmouse driver

.. _`vmmouse_data.definition`:

Definition
----------

.. code-block:: c

    struct vmmouse_data {
        struct input_dev *abs_dev;
        char phys[32];
        char dev_name[128];
    }

.. _`vmmouse_data.members`:

Members
-------

abs_dev
    "Absolute" device used to report absolute mouse movement.

phys
    Physical path for the absolute device.

dev_name
    Name attribute name for the absolute device.

.. _`vmmouse_cmd`:

VMMOUSE_CMD
===========

.. c:function::  VMMOUSE_CMD( cmd,  in1,  out1,  out2,  out3,  out4)

    specific bi-directional communication channel implementing the vmmouse protocol. Should never execute on bare metal hardware.

    :param  cmd:
        *undescribed*

    :param  in1:
        *undescribed*

    :param  out1:
        *undescribed*

    :param  out2:
        *undescribed*

    :param  out3:
        *undescribed*

    :param  out4:
        *undescribed*

.. _`vmmouse_report_button`:

vmmouse_report_button
=====================

.. c:function:: void vmmouse_report_button(struct psmouse *psmouse, struct input_dev *abs_dev, struct input_dev *rel_dev, struct input_dev *pref_dev, unsigned int code, int value)

    report button state on the correct input device

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

    :param struct input_dev \*abs_dev:
        The absolute input device

    :param struct input_dev \*rel_dev:
        The relative input device

    :param struct input_dev \*pref_dev:
        The preferred device for reporting

    :param unsigned int code:
        Button code

    :param int value:
        Button value

.. _`vmmouse_report_button.description`:

Description
-----------

Report \ ``value``\  and \ ``code``\  on \ ``pref_dev``\ , unless the button is already
pressed on the other device, in which case the state is reported on that
device.

.. _`vmmouse_report_events`:

vmmouse_report_events
=====================

.. c:function:: psmouse_ret_t vmmouse_report_events(struct psmouse *psmouse)

    process events on the vmmouse communications channel

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

.. _`vmmouse_report_events.description`:

Description
-----------

This function pulls events from the vmmouse communications channel and
reports them on the correct (absolute or relative) input device. When the
communications channel is drained, or if we've processed more than 255
psmouse commands, the function returns PSMOUSE_FULL_PACKET. If there is a
host- or synchronization error, the function returns PSMOUSE_BAD_DATA in
the hope that the caller will reset the communications channel.

.. _`vmmouse_process_byte`:

vmmouse_process_byte
====================

.. c:function:: psmouse_ret_t vmmouse_process_byte(struct psmouse *psmouse)

    process data on the ps/2 channel

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

.. _`vmmouse_process_byte.description`:

Description
-----------

When the ps/2 channel indicates that there is vmmouse data available,
call vmmouse channel processing. Otherwise, continue to accept bytes. If
there is a synchronization or communication data error, return
PSMOUSE_BAD_DATA in the hope that the caller will reset the mouse.

.. _`vmmouse_disable`:

vmmouse_disable
===============

.. c:function:: void vmmouse_disable(struct psmouse *psmouse)

    Disable vmmouse

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

.. _`vmmouse_disable.description`:

Description
-----------

Tries to disable vmmouse mode.

.. _`vmmouse_enable`:

vmmouse_enable
==============

.. c:function:: int vmmouse_enable(struct psmouse *psmouse)

    Enable vmmouse and request absolute mode.

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

.. _`vmmouse_enable.description`:

Description
-----------

Tries to enable vmmouse mode. Performs basic checks and requests
absolute vmmouse mode.
Returns 0 on success, -ENODEV on failure.

.. _`vmmouse_check_hypervisor`:

vmmouse_check_hypervisor
========================

.. c:function:: bool vmmouse_check_hypervisor( void)

    Check if we're running on a supported hypervisor

    :param  void:
        no arguments

.. _`vmmouse_detect`:

vmmouse_detect
==============

.. c:function:: int vmmouse_detect(struct psmouse *psmouse, bool set_properties)

    Probe whether vmmouse is available

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

    :param bool set_properties:
        Whether to set psmouse name and vendor

.. _`vmmouse_detect.description`:

Description
-----------

Returns 0 if vmmouse channel is available. Negative error code if not.

.. _`vmmouse_disconnect`:

vmmouse_disconnect
==================

.. c:function:: void vmmouse_disconnect(struct psmouse *psmouse)

    Take down vmmouse driver

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

.. _`vmmouse_disconnect.description`:

Description
-----------

Takes down vmmouse driver and frees resources set up in \ :c:func:`vmmouse_init`\ .

.. _`vmmouse_reconnect`:

vmmouse_reconnect
=================

.. c:function:: int vmmouse_reconnect(struct psmouse *psmouse)

    Reset the ps/2 - and vmmouse connections

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

.. _`vmmouse_reconnect.description`:

Description
-----------

Attempts to reset the mouse connections. Returns 0 on success and
-1 on failure.

.. _`vmmouse_init`:

vmmouse_init
============

.. c:function:: int vmmouse_init(struct psmouse *psmouse)

    Initialize the vmmouse driver

    :param struct psmouse \*psmouse:
        Pointer to the psmouse struct

.. _`vmmouse_init.description`:

Description
-----------

Requests the device and tries to enable vmmouse mode.
If successful, sets up the input device for relative movement events.
It also allocates another input device and sets it up for absolute motion
events. Returns 0 on success and -1 on failure.

.. This file was automatic generated / don't edit.

