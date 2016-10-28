.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/i2c-hid/i2c-hid.c

.. _`i2c_hid_set_or_send_report`:

i2c_hid_set_or_send_report
==========================

.. c:function:: int i2c_hid_set_or_send_report(struct i2c_client *client, u8 reportType, u8 reportID, unsigned char *buf, size_t data_len, bool use_data)

    forward an incoming report to the device

    :param struct i2c_client \*client:
        the i2c_client of the device

    :param u8 reportType:
        0x03 for HID_FEATURE_REPORT ; 0x02 for HID_OUTPUT_REPORT

    :param u8 reportID:
        the report ID

    :param unsigned char \*buf:
        the actual data to transfer, without the report ID

    :param size_t data_len:
        *undescribed*

    :param bool use_data:
        true: use SET_REPORT HID command, false: send plain OUTPUT report

.. This file was automatic generated / don't edit.

