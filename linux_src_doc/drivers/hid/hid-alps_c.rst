.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-alps.c

.. _`alps_dev`:

struct alps_dev
===============

.. c:type:: struct alps_dev


.. _`alps_dev.definition`:

Definition
----------

.. code-block:: c

    struct alps_dev {
        struct input_dev *input;
        struct input_dev *input2;
        struct hid_device *hdev;
        enum dev_num dev_type;
        u8 max_fingers;
        u8 has_sp;
        u8 sp_btn_info;
        u32 x_active_len_mm;
        u32 y_active_len_mm;
        u32 x_max;
        u32 y_max;
        u32 x_min;
        u32 y_min;
        u32 btn_cnt;
        u32 sp_btn_cnt;
    }

.. _`alps_dev.members`:

Members
-------

input
    pointer to the kernel input device

input2
    pointer to the kernel input2 device

hdev
    pointer to the struct hid_device

dev_type
    device type

max_fingers
    total number of fingers

has_sp
    boolean of sp existense

sp_btn_info
    button information

x_active_len_mm
    active area length of X (mm)

y_active_len_mm
    active area length of Y (mm)

x_max
    maximum x coordinate value

y_max
    maximum y coordinate value

x_min
    minimum x coordinate value

y_min
    minimum y coordinate value

btn_cnt
    number of buttons

sp_btn_cnt
    number of stick buttons

.. This file was automatic generated / don't edit.

