.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/accel/sca3000_ring.c

.. _`sca3000_read_first_n_hw_rb`:

sca3000_read_first_n_hw_rb
==========================

.. c:function:: int sca3000_read_first_n_hw_rb(struct iio_buffer *r, size_t count, char __user *buf)

    main ring access, pulls data from ring

    :param struct iio_buffer \*r:
        the ring

    :param size_t count:
        number of samples to try and pull

    :param char __user \*buf:
        *undescribed*

.. _`sca3000_read_first_n_hw_rb.description`:

Description
-----------

Currently does not provide timestamps.  As the hardware doesn't add them they
can only be inferred approximately from ring buffer events such as 50% full
and knowledge of when buffer was last emptied.  This is left to userspace.

.. _`sca3000_query_ring_int`:

sca3000_query_ring_int
======================

.. c:function:: ssize_t sca3000_query_ring_int(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`sca3000_set_ring_int`:

sca3000_set_ring_int
====================

.. c:function:: ssize_t sca3000_set_ring_int(struct device *dev, struct device_attribute *attr, const char *buf, size_t len)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        *undescribed*

    :param size_t len:
        *undescribed*

.. _`sca3000_hw_ring_preenable`:

sca3000_hw_ring_preenable
=========================

.. c:function:: int sca3000_hw_ring_preenable(struct iio_dev *indio_dev)

    :param struct iio_dev \*indio_dev:
        *undescribed*

.. _`sca3000_hw_ring_preenable.description`:

Description
-----------

Very simple enable function as the chip will allows normal reads
during ring buffer operation so as long as it is indeed running
before we notify the core, the precise ordering does not matter.

.. _`sca3000_ring_int_process`:

sca3000_ring_int_process
========================

.. c:function:: void sca3000_ring_int_process(u8 val, struct iio_buffer *ring)

    :param u8 val:
        *undescribed*

    :param struct iio_buffer \*ring:
        *undescribed*

.. _`sca3000_ring_int_process.description`:

Description
-----------

This is only split from the main interrupt handler so as to
reduce the amount of code if the ring buffer is not enabled.

.. This file was automatic generated / don't edit.

