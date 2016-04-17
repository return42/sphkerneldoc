.. -*- coding: utf-8; mode: rst -*-

=============
rtl2832_sdr.h
=============


.. _`rtl2832_sdr_platform_data`:

struct rtl2832_sdr_platform_data
================================

.. c:type:: rtl2832_sdr_platform_data

    Platform data for the rtl2832_sdr driver


.. _`rtl2832_sdr_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct rtl2832_sdr_platform_data {
    u32 clk;
    #define RTL2832_SDR_TUNER_FC2580    0x21
    #define RTL2832_SDR_TUNER_TUA9001   0x24
    #define RTL2832_SDR_TUNER_FC0012    0x26
    #define RTL2832_SDR_TUNER_E4000     0x27
    #define RTL2832_SDR_TUNER_FC0013    0x29
    #define RTL2832_SDR_TUNER_R820T     0x2a
    #define RTL2832_SDR_TUNER_R828D     0x2b
    u8 tuner;
    struct i2c_client * i2c_client;
    int (* bulk_read) (struct i2c_client *, unsigned int, void *, size_t);
    int (* bulk_write) (struct i2c_client *, unsigned int, const void *, size_t);
    int (* update_bits) (struct i2c_client *, unsigned int, unsigned int, unsigned int);
    struct dvb_frontend * dvb_frontend;
    struct v4l2_subdev * v4l2_subdev;
    struct dvb_usb_device * dvb_usb_device;
  };


.. _`rtl2832_sdr_platform_data.members`:

Members
-------

:``clk``:
    Clock frequency (4000000, 16000000, 25000000, 28800000).

:``tuner``:
    Used tuner model.

:``i2c_client``:
    rtl2832 demod driver I2C client.

:``bulk_read``:
    rtl2832 driver private I/O interface.

:``bulk_write``:
    rtl2832 driver private I/O interface.

:``update_bits``:
    rtl2832 driver private I/O interface.

:``dvb_frontend``:
    rtl2832 DVB frontend.

:``v4l2_subdev``:
    Tuner v4l2 controls.

:``dvb_usb_device``:
    DVB USB interface for USB streaming.


