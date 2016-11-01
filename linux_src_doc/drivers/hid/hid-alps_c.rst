.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-alps.c

.. _`u1_dev`:

struct u1_dev
=============

.. c:type:: struct u1_dev


.. _`u1_dev.definition`:

Definition
----------

.. code-block:: c

    struct u1_dev {
        struct input_dev *input;
        struct input_dev *input2;
        struct hid_device *hdev;
        u8 dev_ctrl;
        u8 dev_type;
        u8 sen_line_num_x;
        u8 sen_line_num_y;
        u8 pitch_x;
        u8 pitch_y;
        u8 resolution;
        u8 btn_info;
        u8 sp_btn_info;
        u32 x_active_len_mm;
        u32 y_active_len_mm;
        u32 x_max;
        u32 y_max;
        u32 btn_cnt;
        u32 sp_btn_cnt;
    }

.. _`u1_dev.members`:

Members
-------

input
    pointer to the kernel input device

input2
    pointer to the kernel input2 device

hdev
    pointer to the struct hid_device

dev_ctrl
    device control parameter

dev_type
    device type

sen_line_num_x
    number of sensor line of X

sen_line_num_y
    number of sensor line of Y

pitch_x
    sensor pitch of X

pitch_y
    sensor pitch of Y

resolution
    resolution

btn_info
    button information

sp_btn_info
    *undescribed*

x_active_len_mm
    active area length of X (mm)

y_active_len_mm
    active area length of Y (mm)

x_max
    maximum x coordinate value

y_max
    maximum y coordinate value

btn_cnt
    number of buttons

sp_btn_cnt
    number of stick buttons

.. This file was automatic generated / don't edit.

