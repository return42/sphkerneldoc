
.. _API-struct-iio-buffer-setup-ops:

===========================
struct iio_buffer_setup_ops
===========================

*man struct iio_buffer_setup_ops(9)*

*4.6.0-rc1*

buffer setup related callbacks


Synopsis
========

.. code-block:: c

    struct iio_buffer_setup_ops {
      int (* preenable) (struct iio_dev *);
      int (* postenable) (struct iio_dev *);
      int (* predisable) (struct iio_dev *);
      int (* postdisable) (struct iio_dev *);
      bool (* validate_scan_mask) (struct iio_dev *indio_dev,const unsigned long *scan_mask);
    };


Members
=======

preenable
    [DRIVER] function to run prior to marking buffer enabled

postenable
    [DRIVER] function to run after marking buffer enabled

predisable
    [DRIVER] function to run prior to marking buffer disabled

postdisable
    [DRIVER] function to run after marking buffer disabled

validate_scan_mask
    [DRIVER] function callback to check whether a given scan mask is valid for the device.
