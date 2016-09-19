.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rmi.h

.. _`rmi_2d_axis_alignment`:

struct rmi_2d_axis_alignment
============================

.. c:type:: struct rmi_2d_axis_alignment

    target axis alignment

.. _`rmi_2d_axis_alignment.definition`:

Definition
----------

.. code-block:: c

    struct rmi_2d_axis_alignment {
        bool swap_axes;
        bool flip_x;
        bool flip_y;
        u16 clip_x_low;
        u16 clip_y_low;
        u16 clip_x_high;
        u16 clip_y_high;
        u16 offset_x;
        u16 offset_y;
        u8 delta_x_threshold;
        u8 delta_y_threshold;
    }

.. _`rmi_2d_axis_alignment.members`:

Members
-------

swap_axes
    set to TRUE if desired to swap x- and y-axis

flip_x
    set to TRUE if desired to flip direction on x-axis

flip_y
    set to TRUE if desired to flip direction on y-axis
    \ ``clip_x_low``\  - reported X coordinates below this setting will be clipped to
    the specified value
    \ ``clip_x_high``\  - reported X coordinates above this setting will be clipped to
    the specified value
    \ ``clip_y_low``\  - reported Y coordinates below this setting will be clipped to
    the specified value
    \ ``clip_y_high``\  - reported Y coordinates above this setting will be clipped to
    the specified value
    \ ``offset_x``\  - this value will be added to all reported X coordinates
    \ ``offset_y``\  - this value will be added to all reported Y coordinates
    \ ``rel_report_enabled``\  - if set to true, the relative reporting will be
    automatically enabled for this sensor.

clip_x_low
    *undescribed*

clip_y_low
    *undescribed*

clip_x_high
    *undescribed*

clip_y_high
    *undescribed*

offset_x
    *undescribed*

offset_y
    *undescribed*

delta_x_threshold
    *undescribed*

delta_y_threshold
    *undescribed*

.. _`rmi_2d_sensor_platform_data`:

struct rmi_2d_sensor_platform_data
==================================

.. c:type:: struct rmi_2d_sensor_platform_data

    overrides defaults for a 2D sensor. \ ``axis_align``\  - provides axis alignment overrides (see above). \ ``sensor_type``\  - Forces the driver to treat the sensor as an indirect pointing device (touchpad) rather than a direct pointing device (touchscreen).  This is useful when F11_2D_QUERY14 register is not available. \ ``disable_report_mask``\  - Force data to not be reported even if it is supported by the firware. \ ``topbuttonpad``\  - Used with the "5 buttons touchpads" found on the Lenovo 40 series \ ``kernel_tracking``\  - most moderns RMI f11 firmwares implement Multifinger Type B protocol. However, there are some corner cases where the user triggers some jumps by tapping with two fingers on the touchpad. Use this setting and dmax to filter out these jumps. Also, when using an old sensor using MF Type A behavior, set to true to report an actual MT protocol B. \ ``dmax``\  - the maximum distance (in sensor units) the kernel tracking allows two distincts fingers to be considered the same.

.. _`rmi_2d_sensor_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct rmi_2d_sensor_platform_data {
        struct rmi_2d_axis_alignment axis_align;
        enum rmi_sensor_type sensor_type;
        int x_mm;
        int y_mm;
        int disable_report_mask;
        u16 rezero_wait;
        bool topbuttonpad;
        bool kernel_tracking;
        int dmax;
    }

.. _`rmi_2d_sensor_platform_data.members`:

Members
-------

axis_align
    *undescribed*

sensor_type
    *undescribed*

x_mm
    *undescribed*

y_mm
    *undescribed*

disable_report_mask
    *undescribed*

rezero_wait
    *undescribed*

topbuttonpad
    *undescribed*

kernel_tracking
    *undescribed*

dmax
    *undescribed*

.. _`rmi_f30_data`:

struct rmi_f30_data
===================

.. c:type:: struct rmi_f30_data

    overrides defaults for a single F30 GPIOs/LED chip. \ ``buttonpad``\  - the touchpad is a buttonpad, so enable only the first actual button that is found. \ ``trackstick_buttons``\  - Set when the function 30 is handling the physical buttons of the trackstick (as a PD/2 passthrough device. \ ``disable``\  - the touchpad incorrectly reports F30 and it should be ignored. This is a special case which is due to misconfigured firmware.

.. _`rmi_f30_data.definition`:

Definition
----------

.. code-block:: c

    struct rmi_f30_data {
        bool buttonpad;
        bool trackstick_buttons;
        bool disable;
    }

.. _`rmi_f30_data.members`:

Members
-------

buttonpad
    *undescribed*

trackstick_buttons
    *undescribed*

disable
    *undescribed*

.. _`rmi_f01_power_management`:

struct rmi_f01_power_management
===============================

.. c:type:: struct rmi_f01_power_management

    When non-zero, these values will be written to the touch sensor to override the default firmware settigns.  For a detailed explanation of what each field does, see the corresponding documention in the RMI4 specification.

.. _`rmi_f01_power_management.definition`:

Definition
----------

.. code-block:: c

    struct rmi_f01_power_management {
        enum rmi_f01_nosleep nosleep;
        u8 wakeup_threshold;
        u8 doze_holdoff;
        u8 doze_interval;
    }

.. _`rmi_f01_power_management.members`:

Members
-------

nosleep
    *undescribed*

wakeup_threshold
    *undescribed*

doze_holdoff
    *undescribed*

doze_interval
    *undescribed*

.. _`rmi_f01_power_management.description`:

Description
-----------

\ ``nosleep``\  - specifies whether the device is permitted to sleep or doze (that
is, enter a temporary low power state) when no fingers are touching the
sensor.
\ ``wakeup_threshold``\  - controls the capacitance threshold at which the touch
sensor will decide to wake up from that low power state.
\ ``doze_holdoff``\  - controls how long the touch sensor waits after the last
finger lifts before entering the doze state, in units of 100ms.
\ ``doze_interval``\  - controls the interval between checks for finger presence
when the touch sensor is in doze mode, in units of 10ms.

.. _`rmi_device_platform_data_spi`:

struct rmi_device_platform_data_spi
===================================

.. c:type:: struct rmi_device_platform_data_spi

    provides parameters used in SPI communications.  All Synaptics SPI products support a standard SPI interface; some also support what is called SPI V2 mode, depending on firmware and/or ASIC limitations.  In V2 mode, the touch sensor can support shorter delays during certain operations, and these are specified separately from the standard mode delays.

.. _`rmi_device_platform_data_spi.definition`:

Definition
----------

.. code-block:: c

    struct rmi_device_platform_data_spi {
        u32 block_delay_us;
        u32 split_read_block_delay_us;
        u32 read_delay_us;
        u32 write_delay_us;
        u32 split_read_byte_delay_us;
        u32 pre_delay_us;
        u32 post_delay_us;
        u8 bits_per_word;
        u16 mode;
        void *cs_assert_data;
        int (*cs_assert)(const void *cs_assert_data, const bool assert);
    }

.. _`rmi_device_platform_data_spi.members`:

Members
-------

block_delay_us
    *undescribed*

split_read_block_delay_us
    *undescribed*

read_delay_us
    *undescribed*

write_delay_us
    *undescribed*

split_read_byte_delay_us
    *undescribed*

pre_delay_us
    *undescribed*

post_delay_us
    *undescribed*

bits_per_word
    *undescribed*

mode
    *undescribed*

cs_assert_data
    *undescribed*

cs_assert
    *undescribed*

.. _`rmi_device_platform_data_spi.description`:

Description
-----------

\ ``block_delay``\  - for standard SPI transactions consisting of both a read and
write operation, the delay (in microseconds) between the read and write
operations.
\ ``split_read_block_delay_us``\  - for V2 SPI transactions consisting of both a
read and write operation, the delay (in microseconds) between the read and
write operations.
\ ``read_delay_us``\  - the delay between each byte of a read operation in normal
SPI mode.
\ ``write_delay_us``\  - the delay between each byte of a write operation in normal
SPI mode.
\ ``split_read_byte_delay_us``\  - the delay between each byte of a read operation
in V2 mode.
\ ``pre_delay_us``\  - the delay before the start of a SPI transaction.  This is
typically useful in conjunction with custom chip select assertions (see
below).
\ ``post_delay_us``\  - the delay after the completion of an SPI transaction.  This
is typically useful in conjunction with custom chip select assertions (see
below).
\ ``cs_assert``\  - For systems where the SPI subsystem does not control the CS/SSB
line, or where such control is broken, you can provide a custom routine to
handle a GPIO as CS/SSB.  This routine will be called at the beginning and
end of each SPI transaction.  The RMI SPI implementation will wait
pre_delay_us after this routine returns before starting the SPI transfer;
and post_delay_us after completion of the SPI transfer(s) before calling it
with assert==FALSE.

.. _`rmi_device_platform_data`:

struct rmi_device_platform_data
===============================

.. c:type:: struct rmi_device_platform_data

    system specific configuration info.

.. _`rmi_device_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct rmi_device_platform_data {
        int reset_delay_ms;
        struct rmi_device_platform_data_spi spi_data;
        struct rmi_2d_sensor_platform_data *sensor_pdata;
        struct rmi_f01_power_management power_management;
        struct rmi_f30_data *f30_data;
    }

.. _`rmi_device_platform_data.members`:

Members
-------

reset_delay_ms
    *undescribed*

spi_data
    *undescribed*

sensor_pdata
    *undescribed*

power_management
    *undescribed*

f30_data
    *undescribed*

.. _`rmi_device_platform_data.description`:

Description
-----------

\ ``reset_delay_ms``\  - after issuing a reset command to the touch sensor, the
driver waits a few milliseconds to give the firmware a chance to
to re-initialize.  You can override the default wait period here.

.. _`rmi_function_descriptor`:

struct rmi_function_descriptor
==============================

.. c:type:: struct rmi_function_descriptor

    RMI function base addresses

.. _`rmi_function_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct rmi_function_descriptor {
        u16 query_base_addr;
        u16 command_base_addr;
        u16 control_base_addr;
        u16 data_base_addr;
        u8 interrupt_source_count;
        u8 function_number;
        u8 function_version;
    }

.. _`rmi_function_descriptor.members`:

Members
-------

query_base_addr
    The RMI Query base address

command_base_addr
    The RMI Command base address

control_base_addr
    The RMI Control base address

data_base_addr
    The RMI Data base address

interrupt_source_count
    The number of irqs this RMI function needs

function_number
    The RMI function number

function_version
    *undescribed*

.. _`rmi_function_descriptor.description`:

Description
-----------

This struct is used when iterating the Page Description Table. The addresses
are 16-bit values to include the current page address.

.. _`rmi_transport_dev`:

struct rmi_transport_dev
========================

.. c:type:: struct rmi_transport_dev

    represent an RMI transport device

.. _`rmi_transport_dev.definition`:

Definition
----------

.. code-block:: c

    struct rmi_transport_dev {
        struct device *dev;
        struct rmi_device *rmi_dev;
        const char *proto_name;
        const struct rmi_transport_ops *ops;
        struct rmi_device_platform_data pdata;
        struct input_dev *input;
        void *attn_data;
        int attn_size;
    }

.. _`rmi_transport_dev.members`:

Members
-------

dev
    Pointer to the communication device, e.g. i2c or spi

rmi_dev
    Pointer to the RMI device

proto_name
    name of the transport protocol (SPI, i2c, etc)

ops
    pointer to transport operations implementation

pdata
    *undescribed*

input
    *undescribed*

attn_data
    *undescribed*

attn_size
    *undescribed*

.. _`rmi_transport_dev.description`:

Description
-----------

The RMI transport device implements the glue between different communication
buses such as I2C and SPI.

.. _`rmi_transport_ops`:

struct rmi_transport_ops
========================

.. c:type:: struct rmi_transport_ops

    defines transport protocol operations.

.. _`rmi_transport_ops.definition`:

Definition
----------

.. code-block:: c

    struct rmi_transport_ops {
        int (*write_block)(struct rmi_transport_dev *xport, u16 addr,const void *buf, size_t len);
        int (*read_block)(struct rmi_transport_dev *xport, u16 addr,void *buf, size_t len);
        int (*reset)(struct rmi_transport_dev *xport, u16 reset_addr);
    }

.. _`rmi_transport_ops.members`:

Members
-------

write_block
    Writing a block of data to the specified address

read_block
    Read a block of data from the specified address.

reset
    *undescribed*

.. _`rmi_driver`:

struct rmi_driver
=================

.. c:type:: struct rmi_driver

    driver for an RMI4 sensor on the RMI bus.

.. _`rmi_driver.definition`:

Definition
----------

.. code-block:: c

    struct rmi_driver {
        struct device_driver driver;
        int (*reset_handler)(struct rmi_device *rmi_dev);
        int (*clear_irq_bits)(struct rmi_device *rmi_dev, unsigned long *mask);
        int (*set_irq_bits)(struct rmi_device *rmi_dev, unsigned long *mask);
        int (*store_productid)(struct rmi_device *rmi_dev);
        int (*set_input_params)(struct rmi_device *rmi_dev,struct input_dev *input);
        void *data;
    }

.. _`rmi_driver.members`:

Members
-------

driver
    Device driver model driver

reset_handler
    Called when a reset is detected.

clear_irq_bits
    Clear the specified bits in the current interrupt mask.

set_irq_bits
    *undescribed*

store_productid
    Callback for cache product id from function 01

set_input_params
    *undescribed*

data
    Private data pointer

.. _`rmi_device`:

struct rmi_device
=================

.. c:type:: struct rmi_device

    represents an RMI4 sensor device on the RMI bus.

.. _`rmi_device.definition`:

Definition
----------

.. code-block:: c

    struct rmi_device {
        struct device dev;
        int number;
        struct rmi_driver *driver;
        struct rmi_transport_dev *xport;
    }

.. _`rmi_device.members`:

Members
-------

dev
    The device created for the RMI bus

number
    Unique number for the device on the bus.

driver
    Pointer to associated driver

xport
    Pointer to the transport interface

.. This file was automatic generated / don't edit.

