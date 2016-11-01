.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/power/sbs-battery.h

.. _`sbs_platform_data`:

struct sbs_platform_data
========================

.. c:type:: struct sbs_platform_data

    platform data for sbs devices

.. _`sbs_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct sbs_platform_data {
        u32 i2c_retry_count;
        u32 poll_retry_count;
    }

.. _`sbs_platform_data.members`:

Members
-------

i2c_retry_count
    # of times to retry on i2c IO failure

poll_retry_count
    # of times to retry looking for new status after
    external change notification

.. This file was automatic generated / don't edit.

