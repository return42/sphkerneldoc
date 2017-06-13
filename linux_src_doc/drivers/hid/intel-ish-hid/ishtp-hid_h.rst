.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp-hid.h

.. _`ishtp_cl_data`:

struct ishtp_cl_data
====================

.. c:type:: struct ishtp_cl_data

    Encapsulate per ISH TP HID Client

.. _`ishtp_cl_data.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_cl_data {
        bool enum_devices_done;
        bool hid_descr_done;
        bool report_descr_done;
        bool init_done;
        bool suspended;
        unsigned int num_hid_devices;
        unsigned int cur_hid_dev;
        unsigned int hid_dev_count;
        struct device_info *hid_devices;
        unsigned char  *report_descr;
        int report_descr_size;
        struct hid_device  *hid_sensor_hubs;
        unsigned char  *hid_descr;
        int hid_descr_size;
        wait_queue_head_t init_wait;
        wait_queue_head_t ishtp_resume_wait;
        struct ishtp_cl *hid_ishtp_cl;
        unsigned int bad_recv_cnt;
        int multi_packet_cnt;
        struct work_struct work;
        struct ishtp_cl_device *cl_device;
    }

.. _`ishtp_cl_data.members`:

Members
-------

enum_devices_done
    *undescribed*

hid_descr_done
    HID descriptor complete flag

report_descr_done
    Get report descriptor complete flag

init_done
    Init process completed successfully

suspended
    System is under suspend state or in progress

num_hid_devices
    Number of HID devices enumerated in this client

cur_hid_dev
    This keeps track of the device index for which
    initialization and registration with HID core
    in progress.

hid_dev_count
    *undescribed*

hid_devices
    Store vid/pid/devid for each enumerated HID device

report_descr
    Stores the raw report descriptors for each HID device

report_descr_size
    Report description of size of above repo_descr[]

hid_sensor_hubs
    Pointer to hid_device for all HID device, so that
    when clients are removed, they can be freed

hid_descr
    Pointer to hid descriptor for each enumerated hid
    device

hid_descr_size
    Size of each above report descriptor

init_wait
    Wait queue to wait during initialization, where the
    client send message to ISH FW and wait for response

ishtp_resume_wait
    *undescribed*

hid_ishtp_cl
    *undescribed*

bad_recv_cnt
    Running count of packets received with error

multi_packet_cnt
    Count of fragmented packet count

work
    *undescribed*

cl_device
    *undescribed*

.. _`ishtp_cl_data.description`:

Description
-----------

This structure is used to store completion flags and per client data like
like report description, number of HID devices etc.

.. _`ishtp_hid_data`:

struct ishtp_hid_data
=====================

.. c:type:: struct ishtp_hid_data

    Per instance HID data

.. _`ishtp_hid_data.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_hid_data {
        int index;
        bool request_done;
        struct ishtp_cl_data *client_data;
        wait_queue_head_t hid_wait;
    }

.. _`ishtp_hid_data.members`:

Members
-------

index
    Device index in the order of enumeration

request_done
    Get Feature/Input report complete flag
    used during get/set request from hid core

client_data
    Link to the client instance

hid_wait
    Completion waitq

.. _`ishtp_hid_data.description`:

Description
-----------

Used to tie hid hid->driver data to driver client instance

.. This file was automatic generated / don't edit.

