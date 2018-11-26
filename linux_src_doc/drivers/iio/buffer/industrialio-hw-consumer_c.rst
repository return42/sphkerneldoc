.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/buffer/industrialio-hw-consumer.c

.. _`iio_hw_consumer`:

struct iio_hw_consumer
======================

.. c:type:: struct iio_hw_consumer

    IIO hw consumer block

.. _`iio_hw_consumer.definition`:

Definition
----------

.. code-block:: c

    struct iio_hw_consumer {
        struct list_head buffers;
        struct iio_channel *channels;
    }

.. _`iio_hw_consumer.members`:

Members
-------

buffers
    hardware buffers list head.

channels
    IIO provider channels.

.. _`iio_hw_consumer_alloc`:

iio_hw_consumer_alloc
=====================

.. c:function:: struct iio_hw_consumer *iio_hw_consumer_alloc(struct device *dev)

    Allocate IIO hardware consumer

    :param dev:
        Pointer to consumer device.
    :type dev: struct device \*

.. _`iio_hw_consumer_alloc.description`:

Description
-----------

Returns a valid iio_hw_consumer on success or a \ :c:func:`ERR_PTR`\  on failure.

.. _`iio_hw_consumer_free`:

iio_hw_consumer_free
====================

.. c:function:: void iio_hw_consumer_free(struct iio_hw_consumer *hwc)

    Free IIO hardware consumer

    :param hwc:
        hw consumer to free.
    :type hwc: struct iio_hw_consumer \*

.. _`devm_iio_hw_consumer_alloc`:

devm_iio_hw_consumer_alloc
==========================

.. c:function:: struct iio_hw_consumer *devm_iio_hw_consumer_alloc(struct device *dev)

    Resource-managed \ :c:func:`iio_hw_consumer_alloc`\ 

    :param dev:
        Pointer to consumer device.
    :type dev: struct device \*

.. _`devm_iio_hw_consumer_alloc.description`:

Description
-----------

Managed iio_hw_consumer_alloc. iio_hw_consumer allocated with this function
is automatically freed on driver detach.

If an iio_hw_consumer allocated with this function needs to be freed
separately, \ :c:func:`devm_iio_hw_consumer_free`\  must be used.

returns pointer to allocated iio_hw_consumer on success, NULL on failure.

.. _`devm_iio_hw_consumer_free`:

devm_iio_hw_consumer_free
=========================

.. c:function:: void devm_iio_hw_consumer_free(struct device *dev, struct iio_hw_consumer *hwc)

    Resource-managed \ :c:func:`iio_hw_consumer_free`\ 

    :param dev:
        Pointer to consumer device.
    :type dev: struct device \*

    :param hwc:
        iio_hw_consumer to free.
    :type hwc: struct iio_hw_consumer \*

.. _`devm_iio_hw_consumer_free.description`:

Description
-----------

Free iio_hw_consumer allocated with \ :c:func:`devm_iio_hw_consumer_alloc`\ .

.. _`iio_hw_consumer_enable`:

iio_hw_consumer_enable
======================

.. c:function:: int iio_hw_consumer_enable(struct iio_hw_consumer *hwc)

    Enable IIO hardware consumer

    :param hwc:
        iio_hw_consumer to enable.
    :type hwc: struct iio_hw_consumer \*

.. _`iio_hw_consumer_enable.description`:

Description
-----------

Returns 0 on success.

.. _`iio_hw_consumer_disable`:

iio_hw_consumer_disable
=======================

.. c:function:: void iio_hw_consumer_disable(struct iio_hw_consumer *hwc)

    Disable IIO hardware consumer

    :param hwc:
        iio_hw_consumer to disable.
    :type hwc: struct iio_hw_consumer \*

.. This file was automatic generated / don't edit.

