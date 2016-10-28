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
        wait_queue_head_t wait;
        u8 *writeReport;
        u8 *readReport;
        int input_report_size;
        int output_report_size;
        unsigned long flags;
        struct rmi_function f01;
        struct rmi_function f11;
        struct rmi_function f30;
        unsigned int max_fingers;
        unsigned int max_x;
        unsigned int max_y;
        unsigned int x_size_mm;
        unsigned int y_size_mm;
        bool read_f11_ctrl_regs;
        u8 f11_ctrl_regs[RMI_F11_CTRL_REG_COUNT];
        unsigned int gpio_led_count;
        unsigned int button_count;
        unsigned long button_mask;
        unsigned long button_state_mask;
        struct input_dev *input;
        struct work_struct reset_work;
        struct hid_device *hdev;
        unsigned long device_flags;
        unsigned long firmware_id;
        u8 f01_ctrl0;
        u8 interrupt_enable_mask;
        bool restore_interrupt_mask;
    }

.. _`rmi_data.members`:

Members
-------

page_mutex
    Locks current page to avoid changing pages in unexpected ways.

page
    Keeps track of the current virtual page

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

f01
    *undescribed*

f11
    placeholder of internal RMI function F11 description

f30
    placeholder of internal RMI function F30 description

max_fingers
    maximum finger count reported by the device

max_x
    maximum x value reported by the device

max_y
    maximum y value reported by the device

x_size_mm
    *undescribed*

y_size_mm
    *undescribed*

read_f11_ctrl_regs
    *undescribed*

gpio_led_count
    count of GPIOs + LEDs reported by F30

button_count
    actual physical buttons count

button_mask
    button mask used to decode GPIO ATTN reports

button_state_mask
    pull state of the buttons

input
    pointer to the kernel input device

reset_work
    worker which will be called in case of a mouse report

hdev
    pointer to the struct hid_device

device_flags
    *undescribed*

firmware_id
    *undescribed*

f01_ctrl0
    *undescribed*

interrupt_enable_mask
    *undescribed*

restore_interrupt_mask
    *undescribed*

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

