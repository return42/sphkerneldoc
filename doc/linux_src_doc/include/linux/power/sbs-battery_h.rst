.. -*- coding: utf-8; mode: rst -*-

=============
sbs-battery.h
=============


.. _`sbs_platform_data`:

struct sbs_platform_data
========================

.. c:type:: sbs_platform_data

    platform data for sbs devices


.. _`sbs_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct sbs_platform_data {
    int battery_detect;
    int battery_detect_present;
    int i2c_retry_count;
    int poll_retry_count;
  };


.. _`sbs_platform_data.members`:

Members
-------

:``battery_detect``:
    GPIO which is used to detect battery presence

:``battery_detect_present``:
    gpio state when battery is present (0 / 1)

:``i2c_retry_count``:
    # of times to retry on i2c IO failure

:``poll_retry_count``:
    # of times to retry looking for new status after
    external change notification


