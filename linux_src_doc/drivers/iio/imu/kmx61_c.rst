.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/kmx61.c

.. _`kmx61_set_mode`:

kmx61_set_mode
==============

.. c:function:: int kmx61_set_mode(struct kmx61_data *data, u8 mode, u8 device, bool update)

    set KMX61 device operating mode \ ``data``\  - kmx61 device private data pointer \ ``mode``\  - bitmask, indicating operating mode for \ ``device``\  \ ``device``\  - bitmask, indicating device for which \ ``mode``\  needs to be set \ ``update``\  - update stby bits stored in device's private  \ ``data``\ 

    :param data:
        *undescribed*
    :type data: struct kmx61_data \*

    :param mode:
        *undescribed*
    :type mode: u8

    :param device:
        *undescribed*
    :type device: u8

    :param update:
        *undescribed*
    :type update: bool

.. _`kmx61_set_mode.description`:

Description
-----------

For each sensor (accelerometer/magnetometer) there are two operating modes
STANDBY and OPERATION. Neither accel nor magn can be disabled independently
if they are both enabled. Internal sensors state is saved in acc_stby and
mag_stby members of driver's private \ ``data``\ .

.. _`kmx61_set_power_state`:

kmx61_set_power_state
=====================

.. c:function:: int kmx61_set_power_state(struct kmx61_data *data, bool on, u8 device)

    set power state for kmx61 \ ``device``\  \ ``data``\  - kmx61 device private pointer \ ``on``\  - power state to be set for \ ``device``\  \ ``device``\  - bitmask indicating device for which \ ``on``\  state needs to be set

    :param data:
        *undescribed*
    :type data: struct kmx61_data \*

    :param on:
        *undescribed*
    :type on: bool

    :param device:
        *undescribed*
    :type device: u8

.. _`kmx61_set_power_state.description`:

Description
-----------

Notice that when ACC power state needs to be set to ON and MAG is in
OPERATION then we know that kmx61_runtime_resume was already called
so we must set ACC OPERATION mode here. The same happens when MAG power
state needs to be set to ON and ACC is in OPERATION.

.. This file was automatic generated / don't edit.

