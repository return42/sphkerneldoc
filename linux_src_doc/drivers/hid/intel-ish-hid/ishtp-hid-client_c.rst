.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp-hid-client.c

.. _`report_bad_packet`:

report_bad_packet
=================

.. c:function:: void report_bad_packet(struct ishtp_cl *hid_ishtp_cl, void *recv_buf, size_t cur_pos, size_t payload_len)

    Report bad packets

    :param struct ishtp_cl \*hid_ishtp_cl:
        Client instance to get stats

    :param void \*recv_buf:
        Raw received host interface message

    :param size_t cur_pos:
        Current position index in payload

    :param size_t payload_len:
        Length of payload expected

.. _`report_bad_packet.description`:

Description
-----------

Dumps error in case bad packet is received

.. _`process_recv`:

process_recv
============

.. c:function:: void process_recv(struct ishtp_cl *hid_ishtp_cl, void *recv_buf, size_t data_len)

    Received and parse incoming packet

    :param struct ishtp_cl \*hid_ishtp_cl:
        Client instance to get stats

    :param void \*recv_buf:
        Raw received host interface message

    :param size_t data_len:
        length of the message

.. _`process_recv.description`:

Description
-----------

Parse the incoming packet. If it is a response packet then it will update
per instance flags and wake up the caller waiting to for the response.

.. _`ish_cl_event_cb`:

ish_cl_event_cb
===============

.. c:function:: void ish_cl_event_cb(struct ishtp_cl_device *device)

    bus driver callback for incoming message/packet

    :param struct ishtp_cl_device \*device:
        Pointer to the the ishtp client device for which this message
        is targeted

.. _`ish_cl_event_cb.description`:

Description
-----------

Remove the packet from the list and process the message by calling
process_recv

.. _`hid_ishtp_set_feature`:

hid_ishtp_set_feature
=====================

.. c:function:: void hid_ishtp_set_feature(struct hid_device *hid, char *buf, unsigned int len, int report_id)

    send request to ISH FW to set a feature request

    :param struct hid_device \*hid:
        hid device instance for this request

    :param char \*buf:
        feature buffer

    :param unsigned int len:
        Length of feature buffer

    :param int report_id:
        Report id for the feature set request

.. _`hid_ishtp_set_feature.description`:

Description
-----------

This is called from hid core .request() callback. This function doesn't wait
for response.

.. _`hid_ishtp_get_report`:

hid_ishtp_get_report
====================

.. c:function:: void hid_ishtp_get_report(struct hid_device *hid, int report_id, int report_type)

    request to get feature/input report

    :param struct hid_device \*hid:
        hid device instance for this request

    :param int report_id:
        Report id for the get request

    :param int report_type:
        Report type for the this request

.. _`hid_ishtp_get_report.description`:

Description
-----------

This is called from hid core .request() callback. This function will send
request to FW and return without waiting for response.

.. _`ishtp_hid_link_ready_wait`:

ishtp_hid_link_ready_wait
=========================

.. c:function:: int ishtp_hid_link_ready_wait(struct ishtp_cl_data *client_data)

    Wait for link ready

    :param struct ishtp_cl_data \*client_data:
        client data instance

.. _`ishtp_hid_link_ready_wait.description`:

Description
-----------

If the transport link started suspend process, then wait, till either
resumed or timeout

.. _`ishtp_hid_link_ready_wait.return`:

Return
------

0 on success, non zero on error

.. _`ishtp_enum_enum_devices`:

ishtp_enum_enum_devices
=======================

.. c:function:: int ishtp_enum_enum_devices(struct ishtp_cl *hid_ishtp_cl)

    Enumerate hid devices

    :param struct ishtp_cl \*hid_ishtp_cl:
        client instance

.. _`ishtp_enum_enum_devices.description`:

Description
-----------

Helper function to send request to firmware to enumerate HID devices

.. _`ishtp_enum_enum_devices.return`:

Return
------

0 on success, non zero on error

.. _`ishtp_get_hid_descriptor`:

ishtp_get_hid_descriptor
========================

.. c:function:: int ishtp_get_hid_descriptor(struct ishtp_cl *hid_ishtp_cl, int index)

    Get hid descriptor

    :param struct ishtp_cl \*hid_ishtp_cl:
        client instance

    :param int index:
        Index into the hid_descr array

.. _`ishtp_get_hid_descriptor.description`:

Description
-----------

Helper function to send request to firmware get HID descriptor of a device

.. _`ishtp_get_hid_descriptor.return`:

Return
------

0 on success, non zero on error

.. _`ishtp_get_report_descriptor`:

ishtp_get_report_descriptor
===========================

.. c:function:: int ishtp_get_report_descriptor(struct ishtp_cl *hid_ishtp_cl, int index)

    Get report descriptor

    :param struct ishtp_cl \*hid_ishtp_cl:
        client instance

    :param int index:
        Index into the hid_descr array

.. _`ishtp_get_report_descriptor.description`:

Description
-----------

Helper function to send request to firmware get HID report descriptor of
a device

.. _`ishtp_get_report_descriptor.return`:

Return
------

0 on success, non zero on error

.. _`hid_ishtp_cl_init`:

hid_ishtp_cl_init
=================

.. c:function:: int hid_ishtp_cl_init(struct ishtp_cl *hid_ishtp_cl, int reset)

    Init function for ISHTP client

    :param struct ishtp_cl \*hid_ishtp_cl:
        ISHTP client instance

    :param int reset:
        true if called for init after reset

.. _`hid_ishtp_cl_init.description`:

Description
-----------

This function complete the initializtion of the client. The summary of

.. _`hid_ishtp_cl_init.processing`:

processing
----------

- Send request to enumerate the hid clients
Get the HID descriptor for each enumearated device
Get report description of each device
Register each device wik hid core by calling ishtp_hid_probe

.. _`hid_ishtp_cl_init.return`:

Return
------

0 on success, non zero on error

.. _`hid_ishtp_cl_deinit`:

hid_ishtp_cl_deinit
===================

.. c:function:: void hid_ishtp_cl_deinit(struct ishtp_cl *hid_ishtp_cl)

    Deinit function for ISHTP client

    :param struct ishtp_cl \*hid_ishtp_cl:
        ISHTP client instance

.. _`hid_ishtp_cl_deinit.description`:

Description
-----------

Unlink and free hid client

.. _`hid_ishtp_cl_probe`:

hid_ishtp_cl_probe
==================

.. c:function:: int hid_ishtp_cl_probe(struct ishtp_cl_device *cl_device)

    ISHTP client driver probe

    :param struct ishtp_cl_device \*cl_device:
        ISHTP client device instance

.. _`hid_ishtp_cl_probe.description`:

Description
-----------

This function gets called on device create on ISHTP bus

.. _`hid_ishtp_cl_probe.return`:

Return
------

0 on success, non zero on error

.. _`hid_ishtp_cl_remove`:

hid_ishtp_cl_remove
===================

.. c:function:: int hid_ishtp_cl_remove(struct ishtp_cl_device *cl_device)

    ISHTP client driver remove

    :param struct ishtp_cl_device \*cl_device:
        ISHTP client device instance

.. _`hid_ishtp_cl_remove.description`:

Description
-----------

This function gets called on device remove on ISHTP bus

.. _`hid_ishtp_cl_remove.return`:

Return
------

0

.. _`hid_ishtp_cl_reset`:

hid_ishtp_cl_reset
==================

.. c:function:: int hid_ishtp_cl_reset(struct ishtp_cl_device *cl_device)

    ISHTP client driver reset

    :param struct ishtp_cl_device \*cl_device:
        ISHTP client device instance

.. _`hid_ishtp_cl_reset.description`:

Description
-----------

This function gets called on device reset on ISHTP bus

.. _`hid_ishtp_cl_reset.return`:

Return
------

0

.. _`hid_ishtp_cl_suspend`:

hid_ishtp_cl_suspend
====================

.. c:function:: int hid_ishtp_cl_suspend(struct device *device)

    ISHTP client driver suspend

    :param struct device \*device:
        device instance

.. _`hid_ishtp_cl_suspend.description`:

Description
-----------

This function gets called on system suspend

.. _`hid_ishtp_cl_suspend.return`:

Return
------

0

.. _`hid_ishtp_cl_resume`:

hid_ishtp_cl_resume
===================

.. c:function:: int hid_ishtp_cl_resume(struct device *device)

    ISHTP client driver resume

    :param struct device \*device:
        device instance

.. _`hid_ishtp_cl_resume.description`:

Description
-----------

This function gets called on system resume

.. _`hid_ishtp_cl_resume.return`:

Return
------

0

.. This file was automatic generated / don't edit.

