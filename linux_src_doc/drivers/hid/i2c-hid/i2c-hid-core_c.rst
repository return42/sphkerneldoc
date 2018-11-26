.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/i2c-hid/i2c-hid-core.c

.. _`i2c_hid_set_or_send_report`:

i2c_hid_set_or_send_report
==========================

.. c:function:: int i2c_hid_set_or_send_report(struct i2c_client *client, u8 reportType, u8 reportID, unsigned char *buf, size_t data_len, bool use_data)

    forward an incoming report to the device

    :param client:
        the i2c_client of the device
    :type client: struct i2c_client \*

    :param reportType:
        0x03 for HID_FEATURE_REPORT ; 0x02 for HID_OUTPUT_REPORT
    :type reportType: u8

    :param reportID:
        the report ID
    :type reportID: u8

    :param buf:
        the actual data to transfer, without the report ID
    :type buf: unsigned char \*

    :param data_len:
        *undescribed*
    :type data_len: size_t

    :param use_data:
        true: use SET_REPORT HID command, false: send plain OUTPUT report
    :type use_data: bool

.. This file was automatic generated / don't edit.

