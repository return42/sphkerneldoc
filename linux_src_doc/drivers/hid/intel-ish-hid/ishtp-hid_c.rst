.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp-hid.c

.. _`ishtp_hid_parse`:

ishtp_hid_parse
===============

.. c:function:: int ishtp_hid_parse(struct hid_device *hid)

    hid-core .parse() callback

    :param struct hid_device \*hid:
        hid device instance

.. _`ishtp_hid_parse.description`:

Description
-----------

This function gets called during call to hid_add_device

.. _`ishtp_hid_parse.return`:

Return
------

0 on success and non zero on error

.. _`ishtp_hid_request`:

ishtp_hid_request
=================

.. c:function:: void ishtp_hid_request(struct hid_device *hid, struct hid_report *rep, int reqtype)

    hid-core .request() callback

    :param struct hid_device \*hid:
        hid device instance

    :param struct hid_report \*rep:
        pointer to hid_report

    :param int reqtype:
        type of req. [GET\|SET]_REPORT

.. _`ishtp_hid_request.description`:

Description
-----------

This function is used to set/get feaure/input report.

.. _`ishtp_wait_for_response`:

ishtp_wait_for_response
=======================

.. c:function:: int ishtp_wait_for_response(struct hid_device *hid)

    hid-core .wait() callback

    :param struct hid_device \*hid:
        hid device instance

.. _`ishtp_wait_for_response.description`:

Description
-----------

This function is used to wait after get feaure/input report.

.. _`ishtp_wait_for_response.return`:

Return
------

0 on success and non zero on error

.. _`ishtp_hid_wakeup`:

ishtp_hid_wakeup
================

.. c:function:: void ishtp_hid_wakeup(struct hid_device *hid)

    Wakeup caller

    :param struct hid_device \*hid:
        hid device instance

.. _`ishtp_hid_wakeup.description`:

Description
-----------

This function will wakeup caller waiting for Get/Set feature report

.. _`ishtp_hid_probe`:

ishtp_hid_probe
===============

.. c:function:: int ishtp_hid_probe(unsigned int cur_hid_dev, struct ishtp_cl_data *client_data)

    hid register ll driver

    :param unsigned int cur_hid_dev:
        Index of hid device calling to register

    :param struct ishtp_cl_data \*client_data:
        Client data pointer

.. _`ishtp_hid_probe.description`:

Description
-----------

This function is used to allocate and add HID device.

.. _`ishtp_hid_probe.return`:

Return
------

0 on success, non zero on error

.. _`ishtp_hid_remove`:

ishtp_hid_remove
================

.. c:function:: void ishtp_hid_remove(struct ishtp_cl_data *client_data)

    Remove registered hid device

    :param struct ishtp_cl_data \*client_data:
        client data pointer

.. _`ishtp_hid_remove.description`:

Description
-----------

This function is used to destroy allocatd HID device.

.. This file was automatic generated / don't edit.

