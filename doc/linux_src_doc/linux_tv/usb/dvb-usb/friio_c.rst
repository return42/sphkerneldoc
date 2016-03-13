.. -*- coding: utf-8; mode: rst -*-

=======
friio.c
=======



.. _xref_gl861_i2c_ctrlmsg_data:

gl861_i2c_ctrlmsg_data
======================

.. c:function:: int gl861_i2c_ctrlmsg_data (struct dvb_usb_device * d, u8 addr, u8 * wbuf, u16 wlen, u8 * rbuf, u16 rlen)

    

    :param struct dvb_usb_device * d:

        _undescribed_

    :param u8 addr:

        _undescribed_

    :param u8 * wbuf:

        _undescribed_

    :param u16 wlen:

        _undescribed_

    :param u8 * rbuf:

        _undescribed_

    :param u16 rlen:

        _undescribed_



Description
-----------

whole I2C protocol data to the PLL is sent via the FE's I2C register.
This is done by a control msg to the FE with the I2C data accompanied, and
a specific USB request number is assigned for that purpose.


this func sends wbuf[1..] to the I2C register wbuf[0] at addr (= at FE).



TODO
----

refoctored, smarter i2c functions.


