.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-rx6110.c

.. _`rx6110_rtc_tm_to_data`:

rx6110_rtc_tm_to_data
=====================

.. c:function:: int rx6110_rtc_tm_to_data(struct rtc_time *tm, u8 *data)

    convert rtc_time to native time encoding

    :param struct rtc_time \*tm:
        holds date and time

    :param u8 \*data:
        holds the encoding in rx6110 native form

.. _`rx6110_data_to_rtc_tm`:

rx6110_data_to_rtc_tm
=====================

.. c:function:: int rx6110_data_to_rtc_tm(u8 *data, struct rtc_time *tm)

    convert native time encoding to rtc_time

    :param u8 \*data:
        holds the encoding in rx6110 native form

    :param struct rtc_time \*tm:
        holds date and time

.. _`rx6110_set_time`:

rx6110_set_time
===============

.. c:function:: int rx6110_set_time(struct device *dev, struct rtc_time *tm)

    set the current time in the rx6110 registers

    :param struct device \*dev:
        the rtc device in use

    :param struct rtc_time \*tm:
        holds date and time

.. _`rx6110_set_time.bug`:

BUG
---

The HW assumes every year that is a multiple of 4 to be a leap
year. Next time this is wrong is 2100, which will not be a leap year

.. _`rx6110_set_time.note`:

Note
----

If STOP is not set/cleared, the clock will start when the seconds
register is written

.. _`rx6110_get_time`:

rx6110_get_time
===============

.. c:function:: int rx6110_get_time(struct device *dev, struct rtc_time *tm)

    get the current time from the rx6110 registers

    :param struct device \*dev:
        the rtc device in use

    :param struct rtc_time \*tm:
        holds date and time

.. _`rx6110_init`:

rx6110_init
===========

.. c:function:: int rx6110_init(struct rx6110_data *rx6110)

    initialize the rx6110 registers

    :param struct rx6110_data \*rx6110:
        pointer to the rx6110 struct in use

.. _`rx6110_probe`:

rx6110_probe
============

.. c:function:: int rx6110_probe(struct spi_device *spi)

    initialize rtc driver

    :param struct spi_device \*spi:
        pointer to spi device

.. This file was automatic generated / don't edit.

