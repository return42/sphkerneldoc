
.. _API-struct-iio-trigger-ops:

======================
struct iio_trigger_ops
======================

*man struct iio_trigger_ops(9)*

*4.6.0-rc1*

operations structure for an iio_trigger.


Synopsis
========

.. code-block:: c

    struct iio_trigger_ops {
      struct module * owner;
      int (* set_trigger_state) (struct iio_trigger *trig, bool state);
      int (* try_reenable) (struct iio_trigger *trig);
      int (* validate_device) (struct iio_trigger *trig,struct iio_dev *indio_dev);
    };


Members
=======

owner
    used to monitor usage count of the trigger.

set_trigger_state
    switch on/off the trigger on demand

try_reenable
    function to reenable the trigger when the use count is zero (may be NULL)

validate_device
    function to validate the device when the current trigger gets changed.


Description
===========

This is typically static const within a driver and shared by instances of a given device.
