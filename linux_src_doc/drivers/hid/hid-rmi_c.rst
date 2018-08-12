.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-rmi.c

.. _`rmi_data`:

struct rmi_data
===============

.. c:type:: struct rmi_data

    stores information for hid communication

.. _`rmi_data.definition`:

Definition
----------

.. code-block:: c

    struct rmi_data {
        struct mutex page_mutex;
        int page;
        struct rmi_transport_dev xport;
        wait_queue_head_t wait;
        u8 *writeReport;
        u8 *readReport;
        u32 input_report_size;
        u32 output_report_size;
        unsigned long flags;
        struct work_struct reset_work;
        struct hid_device *hdev;
        unsigned long device_flags;
        struct irq_domain *domain;
        int rmi_irq;
    }

.. _`rmi_data.members`:

Members
-------

page_mutex
    Locks current page to avoid changing pages in unexpected ways.

page
    Keeps track of the current virtual page

xport
    transport device to be registered with the RMI4 core.

wait
    Used for waiting for read data

writeReport
    output buffer when writing RMI registers

readReport
    input buffer when reading RMI registers

input_report_size
    size of an input report (advertised by HID)

output_report_size
    size of an output report (advertised by HID)

flags
    flags for the current device (started, reading, etc...)

reset_work
    worker which will be called in case of a mouse report

hdev
    pointer to the struct hid_device

device_flags
    flags which describe the device

domain
    the IRQ domain allocated for this RMI4 device

rmi_irq
    the irq that will be used to generate events to rmi-core

.. _`rmi_set_page`:

rmi_set_page
============

.. c:function:: int rmi_set_page(struct hid_device *hdev, u8 page)

    Set RMI page

    :param struct hid_device \*hdev:
        The pointer to the hid_device struct

    :param u8 page:
        The new page address.

.. _`rmi_set_page.description`:

Description
-----------

RMI devices have 16-bit addressing, but some of the physical
implementations (like SMBus) only have 8-bit addressing. So RMI implements
a page address at 0xff of every page so we can reliable page addresses
every 256 registers.

The page_mutex lock must be held when this function is entered.

Returns zero on success, non-zero on failure.

.. This file was automatic generated / don't edit.

