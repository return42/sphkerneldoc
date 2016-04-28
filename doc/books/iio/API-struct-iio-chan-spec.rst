.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-iio-chan-spec:

====================
struct iio_chan_spec
====================

*man struct iio_chan_spec(9)*

*4.6.0-rc5*

specification of a single channel


Synopsis
========

.. code-block:: c

    struct iio_chan_spec {
      enum iio_chan_type type;
      int channel;
      int channel2;
      unsigned long address;
      int scan_index;
      struct scan_type;
      long info_mask_separate;
      long info_mask_shared_by_type;
      long info_mask_shared_by_dir;
      long info_mask_shared_by_all;
      const struct iio_event_spec * event_spec;
      unsigned int num_event_specs;
      const struct iio_chan_spec_ext_info * ext_info;
      const char * extend_name;
      const char * datasheet_name;
      unsigned modified:1;
      unsigned indexed:1;
      unsigned output:1;
      unsigned differential:1;
    };


Members
=======

type
    What type of measurement is the channel making.

channel
    What number do we wish to assign the channel.

channel2
    If there is a second number for a differential channel then this is
    it. If modified is set then the value here specifies the modifier.

address
    Driver specific identifier.

scan_index
    Monotonic index to give ordering in scans when read from a buffer.

scan_type
    sign: 's' or 'u' to specify signed or unsigned

info_mask_separate
    What information is to be exported that is specific to this channel.

info_mask_shared_by_type
    What information is to be exported that is shared by all channels of
    the same type.

info_mask_shared_by_dir
    What information is to be exported that is shared by all channels of
    the same direction.

info_mask_shared_by_all
    What information is to be exported that is shared by all channels.

event_spec
    Array of events which should be registered for this channel.

num_event_specs
    Size of the event_spec array.

ext_info
    Array of extended info attributes for this channel. The array is
    NULL terminated, the last element should have its name field set to
    NULL.

extend_name
    Allows labeling of channel attributes with an informative name. Note
    this has no effect codes etc, unlike modifiers.

datasheet_name
    A name used in in-kernel mapping of channels. It should correspond
    to the first name that the channel is referred to by in the
    datasheet (e.g. IND), or the nearest possible compound name (e.g.
    IND-INC).

modified
    Does a modifier apply to this channel. What these are depends on the
    channel type. Modifier is set in channel2. Examples are IIO_MOD_X
    for axial sensors about the 'x' axis.

indexed
    Specify the channel has a numerical index. If not, the channel index
    number will be suppressed for sysfs attributes but not for event
    codes.

output
    Channel is output.

differential
    Channel is differential.


realbits
========

Number of valid bits of data


storagebits
===========

Realbits + padding


shift
=====

Shift right by this before masking out realbits.


repeat
======

Number of times real/storage bits repeats. When the repeat element is
more than 1, then the type element in sysfs will show a repeat value.
Otherwise, the number of repetitions is omitted.


endianness
==========

little or big endian


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
