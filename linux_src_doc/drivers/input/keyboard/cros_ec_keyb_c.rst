.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/keyboard/cros_ec_keyb.c

.. _`cros_ec_keyb_report_bs`:

cros_ec_keyb_report_bs
======================

.. c:function:: void cros_ec_keyb_report_bs(struct cros_ec_keyb *ckdev, unsigned int ev_type, u32 mask)

    Report non-matrixed buttons or switches

    :param ckdev:
        The keyboard device.
    :type ckdev: struct cros_ec_keyb \*

    :param ev_type:
        The input event type (e.g., EV_KEY).
    :type ev_type: unsigned int

    :param mask:
        A bitmap of buttons from the EC.
    :type mask: u32

.. _`cros_ec_keyb_report_bs.description`:

Description
-----------

This takes a bitmap of buttons or switches from the EC and reports events,
syncing at the end.

.. _`cros_ec_keyb_info`:

cros_ec_keyb_info
=================

.. c:function:: int cros_ec_keyb_info(struct cros_ec_device *ec_dev, enum ec_mkbp_info_type info_type, enum ec_mkbp_event event_type, union ec_response_get_next_data *result, size_t result_size)

    Wrap the EC command EC_CMD_MKBP_INFO

    :param ec_dev:
        The EC device
    :type ec_dev: struct cros_ec_device \*

    :param info_type:
        Either EC_MKBP_INFO_SUPPORTED or EC_MKBP_INFO_CURRENT.
    :type info_type: enum ec_mkbp_info_type

    :param event_type:
        Either EC_MKBP_EVENT_BUTTON or EC_MKBP_EVENT_SWITCH.  Actually
        in some cases this could be EC_MKBP_EVENT_KEY_MATRIX or
        EC_MKBP_EVENT_HOST_EVENT too but we don't use in this driver.
    :type event_type: enum ec_mkbp_event

    :param result:
        Where we'll store the result; a union
    :type result: union ec_response_get_next_data \*

    :param result_size:
        The size of the result.  Expected to be the size of one of
        the elements in the union.
    :type result_size: size_t

.. _`cros_ec_keyb_info.description`:

Description
-----------

This wraps the EC_CMD_MKBP_INFO, abstracting out all of the marshalling and
unmarshalling and different version nonsense into something simple.

Returns 0 if no error or -error upon error.

.. _`cros_ec_keyb_query_switches`:

cros_ec_keyb_query_switches
===========================

.. c:function:: int cros_ec_keyb_query_switches(struct cros_ec_keyb *ckdev)

    Query the state of switches and report

    :param ckdev:
        The keyboard device
    :type ckdev: struct cros_ec_keyb \*

.. _`cros_ec_keyb_query_switches.description`:

Description
-----------

This will ask the EC about the current state of switches and report to the
kernel.  Note that we don't query for buttons because they are more
transitory and we'll get an update on the next release / press.

Returns 0 if no error or -error upon error.

.. _`cros_ec_keyb_resume`:

cros_ec_keyb_resume
===================

.. c:function:: __maybe_unused int cros_ec_keyb_resume(struct device *dev)

    Resume the keyboard

    :param dev:
        The keyboard device
    :type dev: struct device \*

.. _`cros_ec_keyb_resume.description`:

Description
-----------

We use the resume notification as a chance to query the EC for switches.

Returns 0 if no error or -error upon error.

.. _`cros_ec_keyb_register_bs`:

cros_ec_keyb_register_bs
========================

.. c:function:: int cros_ec_keyb_register_bs(struct cros_ec_keyb *ckdev)

    Register non-matrix buttons/switches

    :param ckdev:
        The keyboard device
    :type ckdev: struct cros_ec_keyb \*

.. _`cros_ec_keyb_register_bs.description`:

Description
-----------

Handles all the bits of the keyboard driver related to non-matrix buttons
and switches, including asking the EC about which are present and telling
the kernel to expect them.

If this device has no support for buttons and switches we'll return no error
but the ckdev->bs_idev will remain NULL when this function exits.

Returns 0 if no error or -error upon error.

.. _`cros_ec_keyb_register_matrix`:

cros_ec_keyb_register_matrix
============================

.. c:function:: int cros_ec_keyb_register_matrix(struct cros_ec_keyb *ckdev)

    Register matrix keys

    :param ckdev:
        The keyboard device
    :type ckdev: struct cros_ec_keyb \*

.. _`cros_ec_keyb_register_matrix.description`:

Description
-----------

Handles all the bits of the keyboard driver related to matrix keys.

Returns 0 if no error or -error upon error.

.. This file was automatic generated / don't edit.

