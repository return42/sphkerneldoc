.. -*- coding: utf-8; mode: rst -*-

=======
sysfs.h
=======


.. _`iio_dev_attr`:

struct iio_dev_attr
===================

.. c:type:: iio_dev_attr

    iio specific device attribute


.. _`iio_dev_attr.definition`:

Definition
----------

.. code-block:: c

  struct iio_dev_attr {
    struct device_attribute dev_attr;
    u64 address;
    struct list_head l;
    struct iio_chan_spec const * c;
  };


.. _`iio_dev_attr.members`:

Members
-------

:``dev_attr``:
    underlying device attribute

:``address``:
    associated register address

:``l``:
    list head for maintaining list of dynamically created attrs

:``c``:
    specification for the underlying channel




.. _`iio_const_attr`:

struct iio_const_attr
=====================

.. c:type:: iio_const_attr

    constant device specific attribute often used for things like available modes


.. _`iio_const_attr.definition`:

Definition
----------

.. code-block:: c

  struct iio_const_attr {
    const char * string;
    struct device_attribute dev_attr;
  };


.. _`iio_const_attr.members`:

Members
-------

:``string``:
    attribute string

:``dev_attr``:
    underlying device attribute




.. _`iio_dev_attr_samp_freq`:

IIO_DEV_ATTR_SAMP_FREQ
======================

.. c:function:: IIO_DEV_ATTR_SAMP_FREQ ( _mode,  _show,  _store)

    sets any internal clock frequency

    :param _mode:
        sysfs file mode/permissions

    :param _show:
        output method for the attribute

    :param _store:
        input method for the attribute



.. _`iio_dev_attr_samp_freq_avail`:

IIO_DEV_ATTR_SAMP_FREQ_AVAIL
============================

.. c:function:: IIO_DEV_ATTR_SAMP_FREQ_AVAIL ( _show)

    list available sampling frequencies

    :param _show:
        output method for the attribute



.. _`iio_dev_attr_samp_freq_avail.description`:

Description
-----------

May be mode dependent on some devices



.. _`iio_const_attr_samp_freq_avail`:

IIO_CONST_ATTR_SAMP_FREQ_AVAIL
==============================

.. c:function:: IIO_CONST_ATTR_SAMP_FREQ_AVAIL ( _string)

    list available sampling frequencies

    :param _string:
        frequency string for the attribute



.. _`iio_const_attr_samp_freq_avail.description`:

Description
-----------

Constant version



.. _`iio_dev_attr_int_time_avail`:

IIO_DEV_ATTR_INT_TIME_AVAIL
===========================

.. c:function:: IIO_DEV_ATTR_INT_TIME_AVAIL ( _show)

    list available integration times

    :param _show:
        output method for the attribute



.. _`iio_const_attr_int_time_avail`:

IIO_CONST_ATTR_INT_TIME_AVAIL
=============================

.. c:function:: IIO_CONST_ATTR_INT_TIME_AVAIL ( _string)

    list available integration times

    :param _string:
        frequency string for the attribute



.. _`iio_const_attr_int_time_avail.description`:

Description
-----------

Constant version

