.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/dvb-usb/friio.c

.. _`gl861_i2c_ctrlmsg_data`:

gl861_i2c_ctrlmsg_data
======================

.. c:function:: int gl861_i2c_ctrlmsg_data(struct dvb_usb_device *d, u8 addr, u8 *wbuf, u16 wlen, u8 *rbuf, u16 rlen)

    whole I2C protocol data to the PLL is sent via the FE's I2C register. This is done by a control msg to the FE with the I2C data accompanied, and a specific USB request number is assigned for that purpose.

    :param struct dvb_usb_device \*d:
        *undescribed*

    :param u8 addr:
        *undescribed*

    :param u8 \*wbuf:
        *undescribed*

    :param u16 wlen:
        *undescribed*

    :param u8 \*rbuf:
        *undescribed*

    :param u16 rlen:
        *undescribed*

.. _`gl861_i2c_ctrlmsg_data.description`:

Description
-----------

this func sends wbuf[1..] to the I2C register wbuf[0] at addr (= at FE).

.. _`gl861_i2c_ctrlmsg_data.todo`:

TODO
----

refoctored, smarter i2c functions.

.. This file was automatic generated / don't edit.

