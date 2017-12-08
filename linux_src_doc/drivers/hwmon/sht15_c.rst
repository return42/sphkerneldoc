.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwmon/sht15.c

.. _`sht15_temppair`:

struct sht15_temppair
=====================

.. c:type:: struct sht15_temppair

    elements of voltage dependent temp calc

.. _`sht15_temppair.definition`:

Definition
----------

.. code-block:: c

    struct sht15_temppair {
        int vdd;
        int d1;
    }

.. _`sht15_temppair.members`:

Members
-------

vdd
    supply voltage in microvolts

d1
    see data sheet

.. _`sht15_data`:

struct sht15_data
=================

.. c:type:: struct sht15_data

    device instance specific data

.. _`sht15_data.definition`:

Definition
----------

.. code-block:: c

    struct sht15_data {
        struct gpio_desc *sck;
        struct gpio_desc *data;
        struct work_struct read_work;
        wait_queue_head_t wait_queue;
        uint16_t val_temp;
        uint16_t val_humid;
        u8 val_status;
        bool checksum_ok;
        bool checksumming;
        enum sht15_state state;
        bool measurements_valid;
        bool status_valid;
        unsigned long last_measurement;
        unsigned long last_status;
        struct mutex read_lock;
        struct device *dev;
        struct device *hwmon_dev;
        struct regulator *reg;
        struct notifier_block nb;
        int supply_uv;
        bool supply_uv_valid;
        struct work_struct update_supply_work;
        atomic_t interrupt_handled;
    }

.. _`sht15_data.members`:

Members
-------

sck
    clock GPIO line

data
    data GPIO line

read_work
    bh of interrupt handler.

wait_queue
    wait queue for getting values from device.

val_temp
    last temperature value read from device.

val_humid
    last humidity value read from device.

val_status
    last status register value read from device.

checksum_ok
    last value read from the device passed CRC validation.

checksumming
    flag used to enable the data validation with CRC.

state
    state identifying the action the driver is doing.

measurements_valid
    are the current stored measures valid (start condition).

status_valid
    is the current stored status valid (start condition).

last_measurement
    time of last measure.

last_status
    time of last status reading.

read_lock
    mutex to ensure only one read in progress at a time.

dev
    associate device structure.

hwmon_dev
    device associated with hwmon subsystem.

reg
    associated regulator (if specified).

nb
    notifier block to handle notifications of voltage
    changes.

supply_uv
    local copy of supply voltage used to allow use of
    regulator consumer if available.

supply_uv_valid
    indicates that an updated value has not yet been
    obtained from the regulator and so any calculations
    based upon it will be invalid.

update_supply_work
    work struct that is used to update the supply_uv.

interrupt_handled
    flag used to indicate a handler has been scheduled.

.. _`sht15_crc8`:

sht15_crc8
==========

.. c:function:: u8 sht15_crc8(struct sht15_data *data, const u8 *value, int len)

    compute crc8

    :param struct sht15_data \*data:
        sht15 specific data.

    :param const u8 \*value:
        sht15 retrieved data.

    :param int len:
        *undescribed*

.. _`sht15_crc8.description`:

Description
-----------

This implements section 2 of the CRC datasheet.

.. _`sht15_connection_reset`:

sht15_connection_reset
======================

.. c:function:: int sht15_connection_reset(struct sht15_data *data)

    reset the comms interface

    :param struct sht15_data \*data:
        sht15 specific data

.. _`sht15_connection_reset.description`:

Description
-----------

This implements section 3.4 of the data sheet

.. _`sht15_send_bit`:

sht15_send_bit
==============

.. c:function:: void sht15_send_bit(struct sht15_data *data, int val)

    send an individual bit to the device

    :param struct sht15_data \*data:
        device state data

    :param int val:
        value of bit to be sent

.. _`sht15_transmission_start`:

sht15_transmission_start
========================

.. c:function:: int sht15_transmission_start(struct sht15_data *data)

    specific sequence for new transmission

    :param struct sht15_data \*data:
        device state data

.. _`sht15_transmission_start.description`:

Description
-----------

Timings for this are not documented on the data sheet, so very
conservative ones used in implementation. This implements
figure 12 on the data sheet.

.. _`sht15_send_byte`:

sht15_send_byte
===============

.. c:function:: void sht15_send_byte(struct sht15_data *data, u8 byte)

    send a single byte to the device

    :param struct sht15_data \*data:
        device state

    :param u8 byte:
        value to be sent

.. _`sht15_wait_for_response`:

sht15_wait_for_response
=======================

.. c:function:: int sht15_wait_for_response(struct sht15_data *data)

    checks for ack from device

    :param struct sht15_data \*data:
        device state

.. _`sht15_send_cmd`:

sht15_send_cmd
==============

.. c:function:: int sht15_send_cmd(struct sht15_data *data, u8 cmd)

    Sends a command to the device.

    :param struct sht15_data \*data:
        device state

    :param u8 cmd:
        command byte to be sent

.. _`sht15_send_cmd.description`:

Description
-----------

On entry, sck is output low, data is output pull high
and the interrupt disabled.

.. _`sht15_soft_reset`:

sht15_soft_reset
================

.. c:function:: int sht15_soft_reset(struct sht15_data *data)

    send a soft reset command

    :param struct sht15_data \*data:
        sht15 specific data.

.. _`sht15_soft_reset.description`:

Description
-----------

As described in section 3.2 of the datasheet.

.. _`sht15_ack`:

sht15_ack
=========

.. c:function:: int sht15_ack(struct sht15_data *data)

    send a ack

    :param struct sht15_data \*data:
        sht15 specific data.

.. _`sht15_ack.description`:

Description
-----------

Each byte of data is acknowledged by pulling the data line
low for one clock pulse.

.. _`sht15_end_transmission`:

sht15_end_transmission
======================

.. c:function:: int sht15_end_transmission(struct sht15_data *data)

    notify device of end of transmission

    :param struct sht15_data \*data:
        device state.

.. _`sht15_end_transmission.description`:

Description
-----------

This is basically a NAK (single clock pulse, data high).

.. _`sht15_read_byte`:

sht15_read_byte
===============

.. c:function:: u8 sht15_read_byte(struct sht15_data *data)

    Read a byte back from the device

    :param struct sht15_data \*data:
        device state.

.. _`sht15_send_status`:

sht15_send_status
=================

.. c:function:: int sht15_send_status(struct sht15_data *data, u8 status)

    write the status register byte

    :param struct sht15_data \*data:
        sht15 specific data.

    :param u8 status:
        the byte to set the status register with.

.. _`sht15_send_status.description`:

Description
-----------

As described in figure 14 and table 5 of the datasheet.

.. _`sht15_update_status`:

sht15_update_status
===================

.. c:function:: int sht15_update_status(struct sht15_data *data)

    get updated status register from device if too old

    :param struct sht15_data \*data:
        device instance specific data.

.. _`sht15_update_status.description`:

Description
-----------

As described in figure 15 and table 5 of the datasheet.

.. _`sht15_measurement`:

sht15_measurement
=================

.. c:function:: int sht15_measurement(struct sht15_data *data, int command, int timeout_msecs)

    get a new value from device

    :param struct sht15_data \*data:
        device instance specific data

    :param int command:
        command sent to request value

    :param int timeout_msecs:
        timeout after which comms are assumed
        to have failed are reset.

.. _`sht15_update_measurements`:

sht15_update_measurements
=========================

.. c:function:: int sht15_update_measurements(struct sht15_data *data)

    get updated measures from device if too old

    :param struct sht15_data \*data:
        device state

.. _`sht15_calc_temp`:

sht15_calc_temp
===============

.. c:function:: int sht15_calc_temp(struct sht15_data *data)

    convert the raw reading to a temperature

    :param struct sht15_data \*data:
        device state

.. _`sht15_calc_temp.description`:

Description
-----------

As per section 4.3 of the data sheet.

.. _`sht15_calc_humid`:

sht15_calc_humid
================

.. c:function:: int sht15_calc_humid(struct sht15_data *data)

    using last temperature convert raw to humid

    :param struct sht15_data \*data:
        device state

.. _`sht15_calc_humid.description`:

Description
-----------

This is the temperature compensated version as per section 4.2 of
the data sheet.

The sensor is assumed to be V3, which is compatible with V4.
Humidity conversion coefficients are shown in table 7 of the datasheet.

.. _`sht15_show_status`:

sht15_show_status
=================

.. c:function:: ssize_t sht15_show_status(struct device *dev, struct device_attribute *attr, char *buf)

    show status information in sysfs

    :param struct device \*dev:
        device.

    :param struct device_attribute \*attr:
        device attribute.

    :param char \*buf:
        sysfs buffer where information is written to.

.. _`sht15_show_status.description`:

Description
-----------

Will be called on read access to temp1_fault, humidity1_fault
and heater_enable sysfs attributes.
Returns number of bytes written into buffer, negative errno on error.

.. _`sht15_store_heater`:

sht15_store_heater
==================

.. c:function:: ssize_t sht15_store_heater(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    change heater state via sysfs

    :param struct device \*dev:
        device.

    :param struct device_attribute \*attr:
        device attribute.

    :param const char \*buf:
        sysfs buffer to read the new heater state from.

    :param size_t count:
        length of the data.

.. _`sht15_store_heater.description`:

Description
-----------

Will be called on write access to heater_enable sysfs attribute.
Returns number of bytes actually decoded, negative errno on error.

.. _`sht15_show_temp`:

sht15_show_temp
===============

.. c:function:: ssize_t sht15_show_temp(struct device *dev, struct device_attribute *attr, char *buf)

    show temperature measurement value in sysfs

    :param struct device \*dev:
        device.

    :param struct device_attribute \*attr:
        device attribute.

    :param char \*buf:
        sysfs buffer where measurement values are written to.

.. _`sht15_show_temp.description`:

Description
-----------

Will be called on read access to temp1_input sysfs attribute.
Returns number of bytes written into buffer, negative errno on error.

.. _`sht15_show_humidity`:

sht15_show_humidity
===================

.. c:function:: ssize_t sht15_show_humidity(struct device *dev, struct device_attribute *attr, char *buf)

    show humidity measurement value in sysfs

    :param struct device \*dev:
        device.

    :param struct device_attribute \*attr:
        device attribute.

    :param char \*buf:
        sysfs buffer where measurement values are written to.

.. _`sht15_show_humidity.description`:

Description
-----------

Will be called on read access to humidity1_input sysfs attribute.
Returns number of bytes written into buffer, negative errno on error.

.. _`sht15_invalidate_voltage`:

sht15_invalidate_voltage
========================

.. c:function:: int sht15_invalidate_voltage(struct notifier_block *nb, unsigned long event, void *ignored)

    mark supply voltage invalid when notified by reg

    :param struct notifier_block \*nb:
        associated notification structure

    :param unsigned long event:
        voltage regulator state change event code

    :param void \*ignored:
        function parameter - ignored here

.. _`sht15_invalidate_voltage.description`:

Description
-----------

Note that as the notification code holds the regulator lock, we have
to schedule an update of the supply voltage rather than getting it directly.

.. This file was automatic generated / don't edit.

