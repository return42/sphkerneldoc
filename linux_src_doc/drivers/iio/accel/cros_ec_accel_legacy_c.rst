.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/accel/cros_ec_accel_legacy.c

.. _`read_ec_until_not_busy`:

read_ec_until_not_busy
======================

.. c:function:: int read_ec_until_not_busy(struct cros_ec_accel_legacy_state *st)

    Read from EC status byte until it reads not busy.

    :param st:
        Pointer to state information for device.
    :type st: struct cros_ec_accel_legacy_state \*

.. _`read_ec_until_not_busy.description`:

Description
-----------

This function reads EC status until its busy bit gets cleared. It does not
wait indefinitely and returns -EIO if the EC status is still busy after a
few hundreds milliseconds.

.. _`read_ec_until_not_busy.return`:

Return
------

8-bit status if ok, -EIO on error

.. _`read_ec_accel_data_unsafe`:

read_ec_accel_data_unsafe
=========================

.. c:function:: void read_ec_accel_data_unsafe(struct cros_ec_accel_legacy_state *st, unsigned long scan_mask, s16 *data)

    Read acceleration data from EC shared memory.

    :param st:
        Pointer to state information for device.
    :type st: struct cros_ec_accel_legacy_state \*

    :param scan_mask:
        Bitmap of the sensor indices to scan.
    :type scan_mask: unsigned long

    :param data:
        Location to store data.
    :type data: s16 \*

.. _`read_ec_accel_data_unsafe.description`:

Description
-----------

This is the unsafe function for reading the EC data. It does not guarantee
that the EC will not modify the data as it is being read in.

.. _`read_ec_accel_data`:

read_ec_accel_data
==================

.. c:function:: int read_ec_accel_data(struct cros_ec_accel_legacy_state *st, unsigned long scan_mask, s16 *data)

    Read acceleration data from EC shared memory.

    :param st:
        Pointer to state information for device.
    :type st: struct cros_ec_accel_legacy_state \*

    :param scan_mask:
        Bitmap of the sensor indices to scan.
    :type scan_mask: unsigned long

    :param data:
        Location to store data.
    :type data: s16 \*

.. _`read_ec_accel_data.description`:

Description
-----------

This is the safe function for reading the EC data. It guarantees that
the data sampled was not modified by the EC while being read.

.. _`read_ec_accel_data.return`:

Return
------

0 if ok, -ve on error

.. _`cros_ec_accel_legacy_capture`:

cros_ec_accel_legacy_capture
============================

.. c:function:: irqreturn_t cros_ec_accel_legacy_capture(int irq, void *p)

    The trigger handler function

    :param irq:
        The interrupt number.
    :type irq: int

    :param p:
        Private data - always a pointer to the poll func.
    :type p: void \*

.. _`cros_ec_accel_legacy_capture.description`:

Description
-----------

On a trigger event occurring, if the pollfunc is attached then this
handler is called as a threaded interrupt (and hence may sleep). It
is responsible for grabbing data from the device and pushing it into
the associated buffer.

.. _`cros_ec_accel_legacy_capture.return`:

Return
------

IRQ_HANDLED

.. This file was automatic generated / don't edit.

