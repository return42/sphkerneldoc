.. -*- coding: utf-8; mode: rst -*-

.. _iiosubsys:

*******************
Industrial I/O core
*******************

The Industrial I/O core offers:

-  a unified framework for writing drivers for many different types of
   embedded sensors.
-  a standard interface to user space applications manipulating sensors.

The implementation can be found under ``
      drivers/iio/industrialio-*``


.. _iiodevice:

Industrial I/O devices
======================


.. kernel-doc:: include/linux/iio/iio.h
    :functions: iio_dev

.. kernel-doc:: drivers/iio/industrialio-core.c
    :functions: iio_device_alloc

.. kernel-doc:: drivers/iio/industrialio-core.c
    :functions: iio_device_free

.. kernel-doc:: drivers/iio/industrialio-core.c
    :functions: iio_device_register

.. kernel-doc:: drivers/iio/industrialio-core.c
    :functions: iio_device_unregister
An IIO device usually corresponds to a single hardware sensor and it
provides all the information needed by a driver handling a device. Let's
first have a look at the functionality embedded in an IIO device then we
will show how a device driver makes use of an IIO device.

There are two ways for a user space application to interact with an IIO
driver.

-  /sys/bus/iio/iio:deviceX/
   , this represents a hardware sensor and groups together the data
   channels of the same chip.
-  /dev/iio:deviceX
   , character device node interface used for buffered data transfer and
   for events information retrieval.

A typical IIO driver will register itself as an I2C or SPI driver and
will create two routines,
probe
and
remove
. At
probe
:

-  call
   iio_device_alloc
   , which allocates memory for an IIO device.
-  initialize IIO device fields with driver specific information (e.g.
   device name, device channels).
-  call
   iio_device_register
   , this registers the device with the IIO core. After this call the
   device is ready to accept requests from user space applications.

At
remove
, we free the resources allocated in
probe
in reverse order:

-  iio_device_unregister
   , unregister the device from the IIO core.
-  iio_device_free
   , free the memory allocated for the IIO device.


.. _iioattr:

IIO device sysfs interface
--------------------------

Attributes are sysfs files used to expose chip info and also allowing
applications to set various configuration parameters. For device with
index X, attributes can be found under ``/sys/bus/iio/iio:deviceX/ ``
directory. Common attributes are:

-  name
   , description of the physical chip.
-  dev
   , shows the major:minor pair associated with
   /dev/iio:deviceX
   node.
-  sampling_frequency_available
   , available discrete set of sampling frequency values for device.

Available standard attributes for IIO devices are described in the
``Documentation/ABI/testing/sysfs-bus-iio `` file in the Linux kernel
sources.


.. _iiochannel:

IIO device channels
-------------------


.. kernel-doc:: include/linux/iio/iio.h
    :functions: iio_chan_spec structure.
An IIO device channel is a representation of a data channel. An IIO
device can have one or multiple channels. For example:

-  a thermometer sensor has one channel representing the temperature
   measurement.
-  a light sensor with two channels indicating the measurements in the
   visible and infrared spectrum.
-  an accelerometer can have up to 3 channels representing acceleration
   on X, Y and Z axes.

An IIO channel is described by the `` struct iio_chan_spec
      ``. A thermometer driver for the temperature sensor in the example
above would have to describe its channel as follows:


.. code-block:: c

          static const struct iio_chan_spec temp_channel[] = {
              {
                  .type = IIO_TEMP,
                  .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED),
              },
          };

Channel sysfs attributes exposed to userspace are specified in the form
of *bitmasks*. Depending on their shared info, attributes can be set in
one of the following masks:

-  info_mask_separate
   , attributes will be specific to this channel
-  info_mask_shared_by_type
   , attributes are shared by all channels of the same type
-  info_mask_shared_by_dir
   , attributes are shared by all channels of the same direction
-  info_mask_shared_by_all
   , attributes are shared by all channels

When there are multiple data channels per channel type we have two ways
to distinguish between them:

-  set
   .modified
   field of
   iio_chan_spec
   to 1. Modifiers are specified using
   .channel2
   field of the same
   iio_chan_spec
   structure and are used to indicate a physically unique characteristic
   of the channel such as its direction or spectral response. For
   example, a light sensor can have two channels, one for infrared light
   and one for both infrared and visible light.
-  set
   .indexed
   field of
   iio_chan_spec
   to 1. In this case the channel is simply another instance with an
   index specified by the
   .channel
   field.

Here is how we can make use of the channel's modifiers:


.. code-block:: c

          static const struct iio_chan_spec light_channels[] = {
              {
                  .type = IIO_INTENSITY,
                  .modified = 1,
                  .channel2 = IIO_MOD_LIGHT_IR,
                  .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
                  .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
              },
              {
                  .type = IIO_INTENSITY,
                  .modified = 1,
                  .channel2 = IIO_MOD_LIGHT_BOTH,
                  .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
                  .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
              },
              {
                  .type = IIO_LIGHT,
                  .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED),
                  .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
              },

          }

This channel's definition will generate two separate sysfs files for raw
data retrieval:

-  /sys/bus/iio/iio:deviceX/in_intensity_ir_raw
-  /sys/bus/iio/iio:deviceX/in_intensity_both_raw

one file for processed data:

-  /sys/bus/iio/iio:deviceX/in_illuminance_input

and one shared sysfs file for sampling frequency:

-  /sys/bus/iio/iio:deviceX/sampling_frequency.

Here is how we can make use of the channel's indexing:


.. code-block:: c

          static const struct iio_chan_spec light_channels[] = {
              {
                  .type = IIO_VOLTAGE,
                  .indexed = 1,
                  .channel = 0,
                  .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
              },
              {
                  .type = IIO_VOLTAGE,
                  .indexed = 1,
                  .channel = 1,
                  .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
              },
          }

This will generate two separate attributes files for raw data retrieval:

-  /sys/bus/iio/devices/iio:deviceX/in_voltage0_raw
   , representing voltage measurement for channel 0.
-  /sys/bus/iio/devices/iio:deviceX/in_voltage1_raw
   , representing voltage measurement for channel 1.


.. _iiobuffer:

Industrial I/O buffers
======================


.. kernel-doc:: include/linux/iio/buffer.h
    :functions: iio_buffer

.. kernel-doc:: drivers/iio/industrialio-buffer.c
    :export:
The Industrial I/O core offers a way for continuous data capture based
on a trigger source. Multiple data channels can be read at once from
``/dev/iio:deviceX`` character device node, thus reducing the CPU load.


.. _iiobuffersysfs:

IIO buffer sysfs interface
--------------------------

An IIO buffer has an associated attributes directory under ``
      /sys/bus/iio/iio:deviceX/buffer/``. Here are the existing
attributes:

-  length
   , the total number of data samples (capacity) that can be stored by
   the buffer.
-  enable
   , activate buffer capture.


.. _iiobuffersetup:

IIO buffer setup
----------------

The meta information associated with a channel reading placed in a
buffer is called a *scan element*. The important bits configuring scan
elements are exposed to userspace applications via the ``
        /sys/bus/iio/iio:deviceX/scan_elements/`` directory. This file
contains attributes of the following form:

-  enable
   , used for enabling a channel. If and only if its attribute is non
   zero, then a triggered capture will contain data samples for this
   channel.
-  type
   , description of the scan element data storage within the buffer and
   hence the form in which it is read from user space. Format is
   [be|le]:[s|u]bits/storagebitsXrepeat[>>shift]
   .

   -  be
      or
      le
      , specifies big or little endian.
   -  s
      or
      u
      , specifies if signed (2's complement) or unsigned.
   -  bits
      , is the number of valid data bits.
   -  storagebits
      , is the number of bits (after padding) that it occupies in the
      buffer.
   -  shift
      , if specified, is the shift that needs to be applied prior to
      masking out unused bits.
   -  repeat
      , specifies the number of bits/storagebits repetitions. When the
      repeat element is 0 or 1, then the repeat value is omitted.

For example, a driver for a 3-axis accelerometer with 12 bit resolution
where data is stored in two 8-bits registers as follows:


.. code-block:: c

            7   6   5   4   3   2   1   0
          +---+---+---+---+---+---+---+---+
          |D3 |D2 |D1 |D0 | X | X | X | X | (LOW byte, address 0x06)
          +---+---+---+---+---+---+---+---+

            7   6   5   4   3   2   1   0
          +---+---+---+---+---+---+---+---+
          |D11|D10|D9 |D8 |D7 |D6 |D5 |D4 | (HIGH byte, address 0x07)
          +---+---+---+---+---+---+---+---+

will have the following scan element type for each axis:


.. code-block:: c

          $ cat /sys/bus/iio/devices/iio:device0/scan_elements/in_accel_y_type
          le:s12/16>>4

A user space application will interpret data samples read from the
buffer as two byte little endian signed data, that needs a 4 bits right
shift before masking out the 12 valid bits of data.

For implementing buffer support a driver should initialize the following
fields in ``iio_chan_spec`` definition:


.. code-block:: c

              struct iio_chan_spec {
                  /* other members */
                  int scan_index
                  struct {
                      char sign;
                      u8 realbits;
                      u8 storagebits;
                      u8 shift;
                      u8 repeat;
                      enum iio_endian endianness;
                  } scan_type;
              };

The driver implementing the accelerometer described above will have the
following channel definition:


.. code-block:: c

          struct struct iio_chan_spec accel_channels[] = {
              {
                .type = IIO_ACCEL,
                .modified = 1,
                .channel2 = IIO_MOD_X,
                /* other stuff here */
                .scan_index = 0,
                .scan_type = {
                  .sign = 's',
                  .realbits = 12,
                  .storagebits = 16,
                  .shift = 4,
                  .endianness = IIO_LE,
                },
            }
            /* similar for Y (with channel2 = IIO_MOD_Y, scan_index = 1)
             * and Z (with channel2 = IIO_MOD_Z, scan_index = 2) axis
             */
        }

Here *scan_index* defines the order in which the enabled channels are
placed inside the buffer. Channels with a lower scan_index will be
placed before channels with a higher index. Each channel needs to have a
unique scan_index.

Setting scan_index to -1 can be used to indicate that the specific
channel does not support buffered capture. In this case no entries will
be created for the channel in the scan_elements directory.


.. _iiotrigger:

Industrial I/O triggers
=======================


.. kernel-doc:: include/linux/iio/trigger.h
    :functions: iio_trigger

.. kernel-doc:: drivers/iio/industrialio-trigger.c
    :export:
In many situations it is useful for a driver to be able to capture data
based on some external event (trigger) as opposed to periodically
polling for data. An IIO trigger can be provided by a device driver that
also has an IIO device based on hardware generated events (e.g. data
ready or threshold exceeded) or provided by a separate driver from an
independent interrupt source (e.g. GPIO line connected to some external
system, timer interrupt or user space writing a specific file in sysfs).
A trigger may initiate data capture for a number of sensors and also it
may be completely unrelated to the sensor itself.


.. _iiotrigsysfs:

IIO trigger sysfs interface
---------------------------

-  /sys/bus/iio/devices/triggerY
   , this file is created once an IIO trigger is registered with the IIO
   core and corresponds to trigger with index Y. Because triggers can be
   very different depending on type there are few standard attributes
   that we can describe here:

   -  name
      , trigger name that can be later used for association with a
      device.
   -  sampling_frequency
      , some timer based triggers use this attribute to specify the
      frequency for trigger calls.

-  /sys/bus/iio/devices/iio:deviceX/trigger/
   , this directory is created once the device supports a triggered
   buffer. We can associate a trigger with our device by writing the
   trigger's name in the
   current_trigger
   file.


.. _iiotrigattr:

IIO trigger setup
-----------------

Let's see a simple example of how to setup a trigger to be used by a
driver.


.. code-block:: c

          struct iio_trigger_ops trigger_ops = {
              .set_trigger_state = sample_trigger_state,
              .validate_device = sample_validate_device,
          }

          struct iio_trigger *trig;

          /* first, allocate memory for our trigger */
          trig = iio_trigger_alloc(dev, "trig-%s-%d", name, idx);

          /* setup trigger operations field */
          trig->ops = &trigger_ops;

          /* now register the trigger with the IIO core */
          iio_trigger_register(trig);


.. _iiotrigsetup:

IIO trigger ops
---------------


.. kernel-doc:: include/linux/iio/trigger.h
    :functions: iio_trigger_ops
Notice that a trigger has a set of operations attached:

-  set_trigger_state
   , switch the trigger on/off on demand.
-  validate_device
   , function to validate the device when the current trigger gets
   changed.


.. _iiotriggered_buffer:

Industrial I/O triggered buffers
================================

Now that we know what buffers and triggers are let's see how they work
together.


.. _iiotrigbufsetup:

IIO triggered buffer setup
--------------------------


.. kernel-doc:: drivers/iio/buffer/industrialio-triggered-buffer.c
    :export:

.. kernel-doc:: include/linux/iio/iio.h
    :functions: iio_buffer_setup_ops
A typical triggered buffer setup looks like this:


.. code-block:: c

        const struct iio_buffer_setup_ops sensor_buffer_setup_ops = {
          .preenable    = sensor_buffer_preenable,
          .postenable   = sensor_buffer_postenable,
          .postdisable  = sensor_buffer_postdisable,
          .predisable   = sensor_buffer_predisable,
        };

        irqreturn_t sensor_iio_pollfunc(int irq, void *p)
        {
            pf->timestamp = iio_get_time_ns();
            return IRQ_WAKE_THREAD;
        }

        irqreturn_t sensor_trigger_handler(int irq, void *p)
        {
            u16 buf[8];
            int i = 0;

            /* read data for each active channel */
            for_each_set_bit(bit, active_scan_mask, masklength)
                buf[i++] = sensor_get_data(bit)

            iio_push_to_buffers_with_timestamp(indio_dev, buf, timestamp);

            iio_trigger_notify_done(trigger);
            return IRQ_HANDLED;
        }

        /* setup triggered buffer, usually in probe function */
        iio_triggered_buffer_setup(indio_dev, sensor_iio_polfunc,
                                   sensor_trigger_handler,
                                   sensor_buffer_setup_ops);

The important things to notice here are:

-  iio_buffer_setup_ops
   , the buffer setup functions to be called at predefined points in the
   buffer configuration sequence (e.g. before enable, after disable). If
   not specified, the IIO core uses the default
   iio_triggered_buffer_setup_ops
   .
-  sensor_iio_pollfunc
   , the function that will be used as top half of poll function. It
   should do as little processing as possible, because it runs in
   interrupt context. The most common operation is recording of the
   current timestamp and for this reason one can use the IIO core
   defined
   iio_pollfunc_store_time
   function.
-  sensor_trigger_handler
   , the function that will be used as bottom half of the poll function.
   This runs in the context of a kernel thread and all the processing
   takes place here. It usually reads data from the device and stores it
   in the internal buffer together with the timestamp recorded in the
   top half.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
