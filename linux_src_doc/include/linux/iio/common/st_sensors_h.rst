.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/common/st_sensors.h

.. _`st_sensor_bdu`:

struct st_sensor_bdu
====================

.. c:type:: struct st_sensor_bdu

    ST sensor device block data update

.. _`st_sensor_bdu.definition`:

Definition
----------

.. code-block:: c

    struct st_sensor_bdu {
        u8 addr;
        u8 mask;
    }

.. _`st_sensor_bdu.members`:

Members
-------

addr
    address of the register.

mask
    mask to write the block data update flag.

.. _`st_sensor_das`:

struct st_sensor_das
====================

.. c:type:: struct st_sensor_das

    ST sensor device data alignment selection

.. _`st_sensor_das.definition`:

Definition
----------

.. code-block:: c

    struct st_sensor_das {
        u8 addr;
        u8 mask;
    }

.. _`st_sensor_das.members`:

Members
-------

addr
    address of the register.

mask
    mask to write the das flag for left alignment.

.. _`st_sensor_data_ready_irq`:

struct st_sensor_data_ready_irq
===============================

.. c:type:: struct st_sensor_data_ready_irq

    ST sensor device data-ready interrupt

.. _`st_sensor_data_ready_irq.definition`:

Definition
----------

.. code-block:: c

    struct st_sensor_data_ready_irq {
        u8 addr;
        u8 mask_int1;
        u8 mask_int2;
        u8 addr_ihl;
        u8 mask_ihl;
        u8 addr_od;
        u8 mask_od;
        u8 addr_stat_drdy;
        struct {
            u8 en_addr;
            u8 en_mask;
        } ig1;
    }

.. _`st_sensor_data_ready_irq.members`:

Members
-------

addr
    address of the register.

mask_int1
    mask to enable/disable IRQ on INT1 pin.

mask_int2
    mask to enable/disable IRQ on INT2 pin.

addr_ihl
    address to enable/disable active low on the INT lines.

mask_ihl
    mask to enable/disable active low on the INT lines.

addr_od
    address to enable/disable Open Drain on the INT lines.

mask_od
    mask to enable/disable Open Drain on the INT lines.

addr_stat_drdy
    address to read status of DRDY (data ready) interrupt
    struct ig1 - represents the Interrupt Generator 1 of sensors.

ig1
    *undescribed*

.. _`st_sensor_transfer_buffer`:

struct st_sensor_transfer_buffer
================================

.. c:type:: struct st_sensor_transfer_buffer

    ST sensor device I/O buffer

.. _`st_sensor_transfer_buffer.definition`:

Definition
----------

.. code-block:: c

    struct st_sensor_transfer_buffer {
        struct mutex buf_lock;
        u8 rx_buf[ST_SENSORS_RX_MAX_LENGTH];
        u8 tx_buf[ST_SENSORS_TX_MAX_LENGTH] ____cacheline_aligned;
    }

.. _`st_sensor_transfer_buffer.members`:

Members
-------

buf_lock
    Mutex to protect rx and tx buffers.

rx_buf
    Buffer used by SPI transfer to receive data from sensors.
    This buffer is used to avoid DMA not-aligned issue.

tx_buf
    Buffer used by SPI transfer function to send data to the sensors.
    This buffer is used to avoid DMA not-aligned issue.

.. _`st_sensor_transfer_function`:

struct st_sensor_transfer_function
==================================

.. c:type:: struct st_sensor_transfer_function

    ST sensor device I/O function

.. _`st_sensor_transfer_function.definition`:

Definition
----------

.. code-block:: c

    struct st_sensor_transfer_function {
        int (*read_byte) (struct st_sensor_transfer_buffer *tb, struct device *dev, u8 reg_addr, u8 *res_byte);
        int (*write_byte) (struct st_sensor_transfer_buffer *tb, struct device *dev, u8 reg_addr, u8 data);
        int (*read_multiple_byte) (struct st_sensor_transfer_buffer *tb,struct device *dev, u8 reg_addr, int len, u8 *data, bool multiread_bit);
    }

.. _`st_sensor_transfer_function.members`:

Members
-------

read_byte
    Function used to read one byte.

write_byte
    Function used to write one byte.

read_multiple_byte
    Function used to read multiple byte.

.. _`st_sensor_settings`:

struct st_sensor_settings
=========================

.. c:type:: struct st_sensor_settings

    ST specific sensor settings

.. _`st_sensor_settings.definition`:

Definition
----------

.. code-block:: c

    struct st_sensor_settings {
        u8 wai;
        u8 wai_addr;
        char sensors_supported[ST_SENSORS_MAX_4WAI][ST_SENSORS_MAX_NAME];
        struct iio_chan_spec *ch;
        int num_ch;
        struct st_sensor_odr odr;
        struct st_sensor_power pw;
        struct st_sensor_axis enable_axis;
        struct st_sensor_fullscale fs;
        struct st_sensor_bdu bdu;
        struct st_sensor_das das;
        struct st_sensor_data_ready_irq drdy_irq;
        struct st_sensor_sim sim;
        bool multi_read_bit;
        unsigned int bootime;
    }

.. _`st_sensor_settings.members`:

Members
-------

wai
    Contents of WhoAmI register.

wai_addr
    The address of WhoAmI register.

sensors_supported
    List of supported sensors by struct itself.

ch
    IIO channels for the sensor.

num_ch
    *undescribed*

odr
    Output data rate register and ODR list available.

pw
    Power register of the sensor.

enable_axis
    Enable one or more axis of the sensor.

fs
    Full scale register and full scale list available.

bdu
    Block data update register.

das
    Data Alignment Selection register.

drdy_irq
    Data ready register of the sensor.

sim
    SPI serial interface mode register of the sensor.

multi_read_bit
    Use or not particular bit for [I2C/SPI] multi-read.

bootime
    samples to discard when sensor passing from power-down to power-up.

.. _`st_sensor_data`:

struct st_sensor_data
=====================

.. c:type:: struct st_sensor_data

    ST sensor device status

.. _`st_sensor_data.definition`:

Definition
----------

.. code-block:: c

    struct st_sensor_data {
        struct device *dev;
        struct iio_trigger *trig;
        struct st_sensor_settings *sensor_settings;
        struct st_sensor_fullscale_avl *current_fullscale;
        struct regulator *vdd;
        struct regulator *vdd_io;
        bool enabled;
        bool multiread_bit;
        char *buffer_data;
        unsigned int odr;
        unsigned int num_data_channels;
        u8 drdy_int_pin;
        bool int_pin_open_drain;
        unsigned int (*get_irq_data_ready) (struct iio_dev *indio_dev);
        const struct st_sensor_transfer_function *tf;
        struct st_sensor_transfer_buffer tb;
        bool edge_irq;
        bool hw_irq_trigger;
        s64 hw_timestamp;
    }

.. _`st_sensor_data.members`:

Members
-------

dev
    Pointer to instance of struct device (I2C or SPI).

trig
    The trigger in use by the core driver.

sensor_settings
    Pointer to the specific sensor settings in use.

current_fullscale
    Maximum range of measure by the sensor.

vdd
    Pointer to sensor's Vdd power supply

vdd_io
    Pointer to sensor's Vdd-IO power supply

enabled
    Status of the sensor (false->off, true->on).

multiread_bit
    Use or not particular bit for [I2C/SPI] multiread.

buffer_data
    Data used by buffer part.

odr
    Output data rate of the sensor [Hz].

num_data_channels
    *undescribed*

drdy_int_pin
    Redirect DRDY on pin 1 (1) or pin 2 (2).

int_pin_open_drain
    Set the interrupt/DRDY to open drain.

get_irq_data_ready
    Function to get the IRQ used for data ready signal.

tf
    Transfer function structure used by I/O operations.

tb
    Transfer buffers and mutex used by I/O operations.

edge_irq
    the IRQ triggers on edges and need special handling.

hw_irq_trigger
    if we're using the hardware interrupt on the sensor.

hw_timestamp
    Latest timestamp from the interrupt handler, when in use.

.. _`st_sensor_data.num_data_channels`:

num_data_channels
-----------------

Number of data channels used in buffer.

.. This file was automatic generated / don't edit.

