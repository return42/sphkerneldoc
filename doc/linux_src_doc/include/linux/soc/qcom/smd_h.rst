.. -*- coding: utf-8; mode: rst -*-

=====
smd.h
=====


.. _`qcom_smd_id`:

struct qcom_smd_id
==================

.. c:type:: qcom_smd_id

    struct used for matching a smd device


.. _`qcom_smd_id.definition`:

Definition
----------

.. code-block:: c

  struct qcom_smd_id {
    char name[20];
  };


.. _`qcom_smd_id.members`:

Members
-------

:``name[20]``:
    name of the channel




.. _`qcom_smd_device`:

struct qcom_smd_device
======================

.. c:type:: qcom_smd_device

    smd device struct


.. _`qcom_smd_device.definition`:

Definition
----------

.. code-block:: c

  struct qcom_smd_device {
    struct device dev;
    struct qcom_smd_channel * channel;
  };


.. _`qcom_smd_device.members`:

Members
-------

:``dev``:
    the device struct

:``channel``:
    handle to the smd channel for this device




.. _`qcom_smd_driver`:

struct qcom_smd_driver
======================

.. c:type:: qcom_smd_driver

    smd driver struct


.. _`qcom_smd_driver.definition`:

Definition
----------

.. code-block:: c

  struct qcom_smd_driver {
    struct device_driver driver;
    const struct qcom_smd_id * smd_match_table;
    int (* probe) (struct qcom_smd_device *dev);
    void (* remove) (struct qcom_smd_device *dev);
    int (* callback) (struct qcom_smd_device *, const void *, size_t);
  };


.. _`qcom_smd_driver.members`:

Members
-------

:``driver``:
    underlying device driver

:``smd_match_table``:
    static channel match table

:``probe``:
    invoked when the smd channel is found

:``remove``:
    invoked when the smd channel is closed

:``callback``:
    invoked when an inbound message is received on the channel,
    should return 0 on success or -EBUSY if the data cannot be
    consumed at this time


