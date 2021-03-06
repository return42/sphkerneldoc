.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/consumer.h

.. _`iio_channel`:

struct iio_channel
==================

.. c:type:: struct iio_channel

    everything needed for a consumer to use a channel

.. _`iio_channel.definition`:

Definition
----------

.. code-block:: c

    struct iio_channel {
        struct iio_dev *indio_dev;
        const struct iio_chan_spec *channel;
        void *data;
    }

.. _`iio_channel.members`:

Members
-------

indio_dev
    Device on which the channel exists.

channel
    Full description of the channel.

data
    Data about the channel used by consumer.

.. _`iio_channel_get`:

iio_channel_get
===============

.. c:function:: struct iio_channel *iio_channel_get(struct device *dev, const char *consumer_channel)

    get description of all that is needed to access channel.

    :param dev:
        Pointer to consumer device. Device name must match
        the name of the device as provided in the iio_map
        with which the desired provider to consumer mapping
        was registered.
    :type dev: struct device \*

    :param consumer_channel:
        Unique name to identify the channel on the consumer
        side. This typically describes the channels use within
        the consumer. E.g. 'battery_voltage'
    :type consumer_channel: const char \*

.. _`iio_channel_release`:

iio_channel_release
===================

.. c:function:: void iio_channel_release(struct iio_channel *chan)

    release channels obtained via iio_channel_get

    :param chan:
        The channel to be released.
    :type chan: struct iio_channel \*

.. _`devm_iio_channel_get`:

devm_iio_channel_get
====================

.. c:function:: struct iio_channel *devm_iio_channel_get(struct device *dev, const char *consumer_channel)

    Resource managed version of \ :c:func:`iio_channel_get`\ .

    :param dev:
        Pointer to consumer device. Device name must match
        the name of the device as provided in the iio_map
        with which the desired provider to consumer mapping
        was registered.
    :type dev: struct device \*

    :param consumer_channel:
        Unique name to identify the channel on the consumer
        side. This typically describes the channels use within
        the consumer. E.g. 'battery_voltage'
    :type consumer_channel: const char \*

.. _`devm_iio_channel_get.description`:

Description
-----------

Returns a pointer to negative errno if it is not able to get the iio channel
otherwise returns valid pointer for iio channel.

The allocated iio channel is automatically released when the device is
unbound.

.. _`devm_iio_channel_release`:

devm_iio_channel_release
========================

.. c:function:: void devm_iio_channel_release(struct device *dev, struct iio_channel *chan)

    Resource managed version of \ :c:func:`iio_channel_release`\ .

    :param dev:
        Pointer to consumer device for which resource
        is allocared.
    :type dev: struct device \*

    :param chan:
        The channel to be released.
    :type chan: struct iio_channel \*

.. _`iio_channel_get_all`:

iio_channel_get_all
===================

.. c:function:: struct iio_channel *iio_channel_get_all(struct device *dev)

    get all channels associated with a client

    :param dev:
        Pointer to consumer device.
    :type dev: struct device \*

.. _`iio_channel_get_all.description`:

Description
-----------

Returns an array of iio_channel structures terminated with one with
null iio_dev pointer.
This function is used by fairly generic consumers to get all the
channels registered as having this consumer.

.. _`iio_channel_release_all`:

iio_channel_release_all
=======================

.. c:function:: void iio_channel_release_all(struct iio_channel *chan)

    reverse iio_channel_get_all

    :param chan:
        Array of channels to be released.
    :type chan: struct iio_channel \*

.. _`devm_iio_channel_get_all`:

devm_iio_channel_get_all
========================

.. c:function:: struct iio_channel *devm_iio_channel_get_all(struct device *dev)

    Resource managed version of \ :c:func:`iio_channel_get_all`\ .

    :param dev:
        Pointer to consumer device.
    :type dev: struct device \*

.. _`devm_iio_channel_get_all.description`:

Description
-----------

Returns a pointer to negative errno if it is not able to get the iio channel
otherwise returns an array of iio_channel structures terminated with one with
null iio_dev pointer.

This function is used by fairly generic consumers to get all the
channels registered as having this consumer.

The allocated iio channels are automatically released when the device is
unbounded.

.. _`devm_iio_channel_release_all`:

devm_iio_channel_release_all
============================

.. c:function:: void devm_iio_channel_release_all(struct device *dev, struct iio_channel *chan)

    Resource managed version of \ :c:func:`iio_channel_release_all`\ .

    :param dev:
        Pointer to consumer device for which resource
        is allocared.
    :type dev: struct device \*

    :param chan:
        Array channel to be released.
    :type chan: struct iio_channel \*

.. _`iio_channel_get_all_cb`:

iio_channel_get_all_cb
======================

.. c:function:: struct iio_cb_buffer *iio_channel_get_all_cb(struct device *dev, int (*cb)(const void *data, void *private), void *private)

    register callback for triggered capture

    :param dev:
        Pointer to client device.
    :type dev: struct device \*

    :param int (\*cb)(const void \*data, void \*private):
        Callback function.

    :param private:
        Private data passed to callback.
    :type private: void \*

.. _`iio_channel_get_all_cb.description`:

Description
-----------

NB right now we have no ability to mux data from multiple devices.
So if the channels requested come from different devices this will
fail.

.. _`iio_channel_cb_set_buffer_watermark`:

iio_channel_cb_set_buffer_watermark
===================================

.. c:function:: int iio_channel_cb_set_buffer_watermark(struct iio_cb_buffer *cb_buffer, size_t watermark)

    set the buffer watermark.

    :param cb_buffer:
        The callback buffer from whom we want the channel
        information.
    :type cb_buffer: struct iio_cb_buffer \*

    :param watermark:
        buffer watermark in bytes.
    :type watermark: size_t

.. _`iio_channel_cb_set_buffer_watermark.description`:

Description
-----------

This function allows to configure the buffer watermark.

.. _`iio_channel_release_all_cb`:

iio_channel_release_all_cb
==========================

.. c:function:: void iio_channel_release_all_cb(struct iio_cb_buffer *cb_buffer)

    release and unregister the callback.

    :param cb_buffer:
        The callback buffer that was allocated.
    :type cb_buffer: struct iio_cb_buffer \*

.. _`iio_channel_start_all_cb`:

iio_channel_start_all_cb
========================

.. c:function:: int iio_channel_start_all_cb(struct iio_cb_buffer *cb_buff)

    start the flow of data through callback.

    :param cb_buff:
        The callback buffer we are starting.
    :type cb_buff: struct iio_cb_buffer \*

.. _`iio_channel_stop_all_cb`:

iio_channel_stop_all_cb
=======================

.. c:function:: void iio_channel_stop_all_cb(struct iio_cb_buffer *cb_buff)

    stop the flow of data through the callback.

    :param cb_buff:
        The callback buffer we are stopping.
    :type cb_buff: struct iio_cb_buffer \*

.. _`iio_channel_cb_get_channels`:

iio_channel_cb_get_channels
===========================

.. c:function:: struct iio_channel *iio_channel_cb_get_channels(const struct iio_cb_buffer *cb_buffer)

    get access to the underlying channels.

    :param cb_buffer:
        The callback buffer from whom we want the channel
        information.
    :type cb_buffer: const struct iio_cb_buffer \*

.. _`iio_channel_cb_get_channels.description`:

Description
-----------

This function allows one to obtain information about the channels.
Whilst this may allow direct reading if all buffers are disabled, the
primary aim is to allow drivers that are consuming a channel to query
things like scaling of the channel.

.. _`iio_channel_cb_get_iio_dev`:

iio_channel_cb_get_iio_dev
==========================

.. c:function:: struct iio_dev *iio_channel_cb_get_iio_dev(const struct iio_cb_buffer *cb_buffer)

    get access to the underlying device.

    :param cb_buffer:
        The callback buffer from whom we want the device
        information.
    :type cb_buffer: const struct iio_cb_buffer \*

.. _`iio_channel_cb_get_iio_dev.description`:

Description
-----------

This function allows one to obtain information about the device.
The primary aim is to allow drivers that are consuming a device to query
things like current trigger.

.. _`iio_read_channel_raw`:

iio_read_channel_raw
====================

.. c:function:: int iio_read_channel_raw(struct iio_channel *chan, int *val)

    read from a given channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        Value read back.
    :type val: int \*

.. _`iio_read_channel_raw.description`:

Description
-----------

Note raw reads from iio channels are in adc counts and hence
scale will need to be applied if standard units required.

.. _`iio_read_channel_average_raw`:

iio_read_channel_average_raw
============================

.. c:function:: int iio_read_channel_average_raw(struct iio_channel *chan, int *val)

    read from a given channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        Value read back.
    :type val: int \*

.. _`iio_read_channel_average_raw.description`:

Description
-----------

Note raw reads from iio channels are in adc counts and hence
scale will need to be applied if standard units required.

In opposit to the normal iio_read_channel_raw this function
returns the average of multiple reads.

.. _`iio_read_channel_processed`:

iio_read_channel_processed
==========================

.. c:function:: int iio_read_channel_processed(struct iio_channel *chan, int *val)

    read processed value from a given channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        Value read back.
    :type val: int \*

.. _`iio_read_channel_processed.description`:

Description
-----------

Returns an error code or 0.

This function will read a processed value from a channel. A processed value
means that this value will have the correct unit and not some device internal
representation. If the device does not support reporting a processed value
the function will query the raw value and the channels scale and offset and
do the appropriate transformation.

.. _`iio_write_channel_attribute`:

iio_write_channel_attribute
===========================

.. c:function:: int iio_write_channel_attribute(struct iio_channel *chan, int val, int val2, enum iio_chan_info_enum attribute)

    Write values to the device attribute.

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        Value being written.
    :type val: int

    :param val2:
        Value being written.val2 use depends on attribute type.
    :type val2: int

    :param attribute:
        info attribute to be read.
    :type attribute: enum iio_chan_info_enum

.. _`iio_write_channel_attribute.description`:

Description
-----------

Returns an error code or 0.

.. _`iio_read_channel_attribute`:

iio_read_channel_attribute
==========================

.. c:function:: int iio_read_channel_attribute(struct iio_channel *chan, int *val, int *val2, enum iio_chan_info_enum attribute)

    Read values from the device attribute.

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        Value being written.
    :type val: int \*

    :param val2:
        Value being written.Val2 use depends on attribute type.
    :type val2: int \*

    :param attribute:
        info attribute to be written.
    :type attribute: enum iio_chan_info_enum

.. _`iio_read_channel_attribute.description`:

Description
-----------

Returns an error code if failed. Else returns a description of what is in val
and val2, such as IIO_VAL_INT_PLUS_MICRO telling us we have a value of val
+ val2/1e6

.. _`iio_write_channel_raw`:

iio_write_channel_raw
=====================

.. c:function:: int iio_write_channel_raw(struct iio_channel *chan, int val)

    write to a given channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        Value being written.
    :type val: int

.. _`iio_write_channel_raw.description`:

Description
-----------

Note raw writes to iio channels are in dac counts and hence
scale will need to be applied if standard units required.

.. _`iio_read_max_channel_raw`:

iio_read_max_channel_raw
========================

.. c:function:: int iio_read_max_channel_raw(struct iio_channel *chan, int *val)

    read maximum available raw value from a given channel, i.e. the maximum possible value.

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        Value read back.
    :type val: int \*

.. _`iio_read_max_channel_raw.description`:

Description
-----------

Note raw reads from iio channels are in adc counts and hence
scale will need to be applied if standard units are required.

.. _`iio_read_avail_channel_raw`:

iio_read_avail_channel_raw
==========================

.. c:function:: int iio_read_avail_channel_raw(struct iio_channel *chan, const int **vals, int *length)

    read available raw values from a given channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param vals:
        Available values read back.
    :type vals: const int \*\*

    :param length:
        Number of entries in vals.
    :type length: int \*

.. _`iio_read_avail_channel_raw.description`:

Description
-----------

Returns an error code, IIO_AVAIL_RANGE or IIO_AVAIL_LIST.

For ranges, three vals are always returned; min, step and max.
For lists, all the possible values are enumerated.

Note raw available values from iio channels are in adc counts and
hence scale will need to be applied if standard units are required.

.. _`iio_get_channel_type`:

iio_get_channel_type
====================

.. c:function:: int iio_get_channel_type(struct iio_channel *channel, enum iio_chan_type *type)

    get the type of a channel

    :param channel:
        The channel being queried.
    :type channel: struct iio_channel \*

    :param type:
        The type of the channel.
    :type type: enum iio_chan_type \*

.. _`iio_get_channel_type.description`:

Description
-----------

returns the enum iio_chan_type of the channel

.. _`iio_read_channel_offset`:

iio_read_channel_offset
=======================

.. c:function:: int iio_read_channel_offset(struct iio_channel *chan, int *val, int *val2)

    read the offset value for a channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        First part of value read back.
    :type val: int \*

    :param val2:
        Second part of value read back.
    :type val2: int \*

.. _`iio_read_channel_offset.description`:

Description
-----------

Note returns a description of what is in val and val2, such
as IIO_VAL_INT_PLUS_MICRO telling us we have a value of val
+ val2/1e6

.. _`iio_read_channel_scale`:

iio_read_channel_scale
======================

.. c:function:: int iio_read_channel_scale(struct iio_channel *chan, int *val, int *val2)

    read the scale value for a channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param val:
        First part of value read back.
    :type val: int \*

    :param val2:
        Second part of value read back.
    :type val2: int \*

.. _`iio_read_channel_scale.description`:

Description
-----------

Note returns a description of what is in val and val2, such
as IIO_VAL_INT_PLUS_MICRO telling us we have a value of val
+ val2/1e6

.. _`iio_convert_raw_to_processed`:

iio_convert_raw_to_processed
============================

.. c:function:: int iio_convert_raw_to_processed(struct iio_channel *chan, int raw, int *processed, unsigned int scale)

    Converts a raw value to a processed value

    :param chan:
        The channel being queried
    :type chan: struct iio_channel \*

    :param raw:
        The raw IIO to convert
    :type raw: int

    :param processed:
        The result of the conversion
    :type processed: int \*

    :param scale:
        Scale factor to apply during the conversion
    :type scale: unsigned int

.. _`iio_convert_raw_to_processed.description`:

Description
-----------

Returns an error code or 0.

This function converts a raw value to processed value for a specific channel.
A raw value is the device internal representation of a sample and the value
returned by iio_read_channel_raw, so the unit of that value is device
depended. A processed value on the other hand is value has a normed unit
according with the IIO specification.

The scale factor allows to increase the precession of the returned value. For
a scale factor of 1 the function will return the result in the normal IIO
unit for the channel type. E.g. millivolt for voltage channels, if you want
nanovolts instead pass 1000000 as the scale factor.

.. _`iio_get_channel_ext_info_count`:

iio_get_channel_ext_info_count
==============================

.. c:function:: unsigned int iio_get_channel_ext_info_count(struct iio_channel *chan)

    get number of ext_info attributes connected to the channel.

    :param chan:
        The channel being queried
    :type chan: struct iio_channel \*

.. _`iio_get_channel_ext_info_count.description`:

Description
-----------

Returns the number of ext_info attributes

.. _`iio_read_channel_ext_info`:

iio_read_channel_ext_info
=========================

.. c:function:: ssize_t iio_read_channel_ext_info(struct iio_channel *chan, const char *attr, char *buf)

    read ext_info attribute from a given channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param attr:
        The ext_info attribute to read.
    :type attr: const char \*

    :param buf:
        Where to store the attribute value. Assumed to hold
        at least PAGE_SIZE bytes.
    :type buf: char \*

.. _`iio_read_channel_ext_info.description`:

Description
-----------

Returns the number of bytes written to buf (perhaps w/o zero termination;
it need not even be a string), or an error code.

.. _`iio_write_channel_ext_info`:

iio_write_channel_ext_info
==========================

.. c:function:: ssize_t iio_write_channel_ext_info(struct iio_channel *chan, const char *attr, const char *buf, size_t len)

    write ext_info attribute from a given channel

    :param chan:
        The channel being queried.
    :type chan: struct iio_channel \*

    :param attr:
        The ext_info attribute to read.
    :type attr: const char \*

    :param buf:
        The new attribute value. Strings needs to be zero-
        terminated, but the terminator should not be included
        in the below len.
    :type buf: const char \*

    :param len:
        The size of the new attribute value.
    :type len: size_t

.. _`iio_write_channel_ext_info.description`:

Description
-----------

Returns the number of accepted bytes, which should be the same as len.
An error code can also be returned.

.. This file was automatic generated / don't edit.

