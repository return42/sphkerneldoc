.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/iio.h

.. _`iio_chan_spec_ext_info`:

struct iio_chan_spec_ext_info
=============================

.. c:type:: struct iio_chan_spec_ext_info

    Extended channel info attribute

.. _`iio_chan_spec_ext_info.definition`:

Definition
----------

.. code-block:: c

    struct iio_chan_spec_ext_info {
        const char *name;
        enum iio_shared_by shared;
        ssize_t (*read)(struct iio_dev *, uintptr_t private, struct iio_chan_spec const *, char *buf);
        ssize_t (*write)(struct iio_dev *, uintptr_t private,struct iio_chan_spec const *, const char *buf, size_t len);
        uintptr_t private;
    }

.. _`iio_chan_spec_ext_info.members`:

Members
-------

name
    Info attribute name

shared
    Whether this attribute is shared between all channels.

read
    Read callback for this info attribute, may be NULL.

write
    Write callback for this info attribute, may be NULL.

private
    Data private to the driver.

.. _`iio_enum`:

struct iio_enum
===============

.. c:type:: struct iio_enum

    Enum channel info attribute

.. _`iio_enum.definition`:

Definition
----------

.. code-block:: c

    struct iio_enum {
        const char * const *items;
        unsigned int num_items;
        int (*set)(struct iio_dev *, const struct iio_chan_spec *, unsigned int);
        int (*get)(struct iio_dev *, const struct iio_chan_spec *);
    }

.. _`iio_enum.members`:

Members
-------

items
    An array of strings.

num_items
    Length of the item array.

set
    Set callback function, may be NULL.

get
    Get callback function, may be NULL.

.. _`iio_enum.description`:

Description
-----------

The iio_enum struct can be used to implement enum style channel attributes.
Enum style attributes are those which have a set of strings which map to
unsigned integer values. The IIO enum helper code takes care of mapping
between value and string as well as generating a "_available" file which
contains a list of all available items. The set callback will be called when
the attribute is updated. The last parameter is the index to the newly
activated item. The get callback will be used to query the currently active
item and is supposed to return the index for it.

.. _`iio_enum`:

IIO_ENUM
========

.. c:function::  IIO_ENUM( _name,  _shared,  _e)

    Initialize enum extended channel attribute

    :param  _name:
        Attribute name

    :param  _shared:
        Whether the attribute is shared between all channels

    :param  _e:
        Pointer to an iio_enum struct

.. _`iio_enum.description`:

Description
-----------

This should usually be used together with \ :c:func:`IIO_ENUM_AVAILABLE`\ 

.. _`iio_enum_available`:

IIO_ENUM_AVAILABLE
==================

.. c:function::  IIO_ENUM_AVAILABLE( _name,  _e)

    Initialize enum available extended channel attribute

    :param  _name:
        Attribute name ("_available" will be appended to the name)

    :param  _e:
        Pointer to an iio_enum struct

.. _`iio_enum_available.description`:

Description
-----------

Creates a read only attribute which lists all the available enum items in a
space separated list. This should usually be used together with \ :c:func:`IIO_ENUM`\ 

.. _`iio_mount_matrix`:

struct iio_mount_matrix
=======================

.. c:type:: struct iio_mount_matrix

    iio mounting matrix

.. _`iio_mount_matrix.definition`:

Definition
----------

.. code-block:: c

    struct iio_mount_matrix {
        const char *rotation[9];
    }

.. _`iio_mount_matrix.members`:

Members
-------

rotation
    3 dimensional space rotation matrix defining sensor alignment with
    main hardware

.. _`iio_mount_matrix`:

IIO_MOUNT_MATRIX
================

.. c:function::  IIO_MOUNT_MATRIX( _shared,  _get)

    Initialize mount matrix extended channel attribute

    :param  _shared:
        Whether the attribute is shared between all channels

    :param  _get:
        Pointer to an iio_get_mount_matrix_t accessor

.. _`iio_event_spec`:

struct iio_event_spec
=====================

.. c:type:: struct iio_event_spec

    specification for a channel event

.. _`iio_event_spec.definition`:

Definition
----------

.. code-block:: c

    struct iio_event_spec {
        enum iio_event_type type;
        enum iio_event_direction dir;
        unsigned long mask_separate;
        unsigned long mask_shared_by_type;
        unsigned long mask_shared_by_dir;
        unsigned long mask_shared_by_all;
    }

.. _`iio_event_spec.members`:

Members
-------

type
    Type of the event

dir
    Direction of the event

mask_separate
    Bit mask of enum iio_event_info values. Attributes
    set in this mask will be registered per channel.

mask_shared_by_type
    Bit mask of enum iio_event_info values. Attributes
    set in this mask will be shared by channel type.

mask_shared_by_dir
    Bit mask of enum iio_event_info values. Attributes
    set in this mask will be shared by channel type and
    direction.

mask_shared_by_all
    Bit mask of enum iio_event_info values. Attributes
    set in this mask will be shared by all channels.

.. _`iio_chan_spec`:

struct iio_chan_spec
====================

.. c:type:: struct iio_chan_spec

    specification of a single channel

.. _`iio_chan_spec.definition`:

Definition
----------

.. code-block:: c

    struct iio_chan_spec {
        enum iio_chan_type type;
        int channel;
        int channel2;
        unsigned long address;
        int scan_index;
        struct {
            char sign;
            u8 realbits;
            u8 storagebits;
            u8 shift;
            u8 repeat;
            enum iio_endian endianness;
        } scan_type;
        long info_mask_separate;
        long info_mask_separate_available;
        long info_mask_shared_by_type;
        long info_mask_shared_by_type_available;
        long info_mask_shared_by_dir;
        long info_mask_shared_by_dir_available;
        long info_mask_shared_by_all;
        long info_mask_shared_by_all_available;
        const struct iio_event_spec *event_spec;
        unsigned int num_event_specs;
        const struct iio_chan_spec_ext_info *ext_info;
        const char *extend_name;
        const char *datasheet_name;
        unsigned modified:1;
        unsigned indexed:1;
        unsigned output:1;
        unsigned differential:1;
    }

.. _`iio_chan_spec.members`:

Members
-------

type
    What type of measurement is the channel making.

channel
    What number do we wish to assign the channel.

channel2
    If there is a second number for a differential
    channel then this is it. If modified is set then the
    value here specifies the modifier.

address
    Driver specific identifier.

scan_index
    Monotonic index to give ordering in scans when read
    from a buffer.

scan_type
    sign:           's' or 'u' to specify signed or unsigned
    realbits:       Number of valid bits of data
    storagebits:    Realbits + padding
    shift:          Shift right by this before masking out
    realbits.
    repeat:         Number of times real/storage bits
    repeats. When the repeat element is
    more than 1, then the type element in
    sysfs will show a repeat value.
    Otherwise, the number of repetitions is
    omitted.
    endianness:     little or big endian

info_mask_separate
    What information is to be exported that is specific to
    this channel.

info_mask_separate_available
    What availability information is to be
    exported that is specific to this channel.

info_mask_shared_by_type
    What information is to be exported that is shared
    by all channels of the same type.

info_mask_shared_by_type_available
    What availability information is to be
    exported that is shared by all channels of the same
    type.

info_mask_shared_by_dir
    What information is to be exported that is shared
    by all channels of the same direction.

info_mask_shared_by_dir_available
    What availability information is to be
    exported that is shared by all channels of the same
    direction.

info_mask_shared_by_all
    What information is to be exported that is shared
    by all channels.

info_mask_shared_by_all_available
    What availability information is to be
    exported that is shared by all channels.

event_spec
    Array of events which should be registered for this
    channel.

num_event_specs
    Size of the event_spec array.

ext_info
    Array of extended info attributes for this channel.
    The array is NULL terminated, the last element should
    have its name field set to NULL.

extend_name
    Allows labeling of channel attributes with an
    informative name. Note this has no effect codes etc,
    unlike modifiers.

datasheet_name
    A name used in in-kernel mapping of channels. It should
    correspond to the first name that the channel is referred
    to by in the datasheet (e.g. IND), or the nearest
    possible compound name (e.g. IND-INC).

modified
    Does a modifier apply to this channel. What these are
    depends on the channel type.  Modifier is set in
    channel2. Examples are IIO_MOD_X for axial sensors about
    the 'x' axis.

indexed
    Specify the channel has a numerical index. If not,
    the channel index number will be suppressed for sysfs
    attributes but not for event codes.

output
    Channel is output.

differential
    Channel is differential.

.. _`iio_channel_has_info`:

iio_channel_has_info
====================

.. c:function:: bool iio_channel_has_info(const struct iio_chan_spec *chan, enum iio_chan_info_enum type)

    Checks whether a channel supports a info attribute

    :param const struct iio_chan_spec \*chan:
        The channel to be queried

    :param enum iio_chan_info_enum type:
        Type of the info attribute to be checked

.. _`iio_channel_has_info.description`:

Description
-----------

Returns true if the channels supports reporting values for the given info
attribute type, false otherwise.

.. _`iio_channel_has_available`:

iio_channel_has_available
=========================

.. c:function:: bool iio_channel_has_available(const struct iio_chan_spec *chan, enum iio_chan_info_enum type)

    Checks if a channel has an available attribute

    :param const struct iio_chan_spec \*chan:
        The channel to be queried

    :param enum iio_chan_info_enum type:
        Type of the available attribute to be checked

.. _`iio_channel_has_available.description`:

Description
-----------

Returns true if the channel supports reporting available values for the
given attribute type, false otherwise.

.. _`iio_info`:

struct iio_info
===============

.. c:type:: struct iio_info

    constant information about device

.. _`iio_info.definition`:

Definition
----------

.. code-block:: c

    struct iio_info {
        const struct attribute_group *event_attrs;
        const struct attribute_group *attrs;
        int (*read_raw)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,int *val,int *val2, long mask);
        int (*read_raw_multi)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,int max_len,int *vals,int *val_len, long mask);
        int (*read_avail)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,const int **vals,int *type,int *length, long mask);
        int (*write_raw)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,int val,int val2, long mask);
        int (*write_raw_get_fmt)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan, long mask);
        int (*read_event_config)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type, enum iio_event_direction dir);
        int (*write_event_config)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type,enum iio_event_direction dir, int state);
        int (*read_event_value)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type,enum iio_event_direction dir, enum iio_event_info info, int *val, int *val2);
        int (*write_event_value)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type,enum iio_event_direction dir, enum iio_event_info info, int val, int val2);
        int (*validate_trigger)(struct iio_dev *indio_dev, struct iio_trigger *trig);
        int (*update_scan_mode)(struct iio_dev *indio_dev, const unsigned long *scan_mask);
        int (*debugfs_reg_access)(struct iio_dev *indio_dev,unsigned reg, unsigned writeval, unsigned *readval);
        int (*of_xlate)(struct iio_dev *indio_dev, const struct of_phandle_args *iiospec);
        int (*hwfifo_set_watermark)(struct iio_dev *indio_dev, unsigned val);
        int (*hwfifo_flush_to_buffer)(struct iio_dev *indio_dev, unsigned count);
    }

.. _`iio_info.members`:

Members
-------

event_attrs
    event control attributes

attrs
    general purpose device attributes

read_raw
    function to request a value from the device.
    mask specifies which value. Note 0 means a reading of
    the channel in question.  Return value will specify the
    type of value returned by the device. val and val2 will
    contain the elements making up the returned value.

read_raw_multi
    function to return values from the device.
    mask specifies which value. Note 0 means a reading of
    the channel in question.  Return value will specify the
    type of value returned by the device. vals pointer
    contain the elements making up the returned value.
    max_len specifies maximum number of elements
    vals pointer can contain. val_len is used to return
    length of valid elements in vals.

read_avail
    function to return the available values from the device.
    mask specifies which value. Note 0 means the available
    values for the channel in question.  Return value
    specifies if a IIO_AVAIL_LIST or a IIO_AVAIL_RANGE is
    returned in vals. The type of the vals are returned in
    type and the number of vals is returned in length. For
    ranges, there are always three vals returned; min, step
    and max. For lists, all possible values are enumerated.

write_raw
    function to write a value to the device.
    Parameters are the same as for read_raw.

write_raw_get_fmt
    callback function to query the expected
    format/precision. If not set by the driver, write_raw
    returns IIO_VAL_INT_PLUS_MICRO.

read_event_config
    find out if the event is enabled.

write_event_config
    set if the event is enabled.

read_event_value
    read a configuration value associated with the event.

write_event_value
    write a configuration value for the event.

validate_trigger
    function to validate the trigger when the
    current trigger gets changed.

update_scan_mode
    function to configure device and scan buffer when
    channels have changed

debugfs_reg_access
    function to read or write register value of device

of_xlate
    function pointer to obtain channel specifier index.
    When #iio-cells is greater than '0', the driver could
    provide a custom of_xlate function that reads the
    *args* and returns the appropriate index in registered
    IIO channels array.

hwfifo_set_watermark
    function pointer to set the current hardware
    fifo watermark level; see hwfifo_* entries in
    Documentation/ABI/testing/sysfs-bus-iio for details on
    how the hardware fifo operates

hwfifo_flush_to_buffer
    function pointer to flush the samples stored
    in the hardware fifo to the device buffer. The driver
    should not flush more than count samples. The function
    must return the number of samples flushed, 0 if no
    samples were flushed or a negative integer if no samples
    were flushed and there was an error.

.. _`iio_buffer_setup_ops`:

struct iio_buffer_setup_ops
===========================

.. c:type:: struct iio_buffer_setup_ops

    buffer setup related callbacks

.. _`iio_buffer_setup_ops.definition`:

Definition
----------

.. code-block:: c

    struct iio_buffer_setup_ops {
        int (*preenable)(struct iio_dev *);
        int (*postenable)(struct iio_dev *);
        int (*predisable)(struct iio_dev *);
        int (*postdisable)(struct iio_dev *);
        bool (*validate_scan_mask)(struct iio_dev *indio_dev, const unsigned long *scan_mask);
    }

.. _`iio_buffer_setup_ops.members`:

Members
-------

preenable
    [DRIVER] function to run prior to marking buffer enabled

postenable
    [DRIVER] function to run after marking buffer enabled

predisable
    [DRIVER] function to run prior to marking buffer
    disabled

postdisable
    [DRIVER] function to run after marking buffer disabled

validate_scan_mask
    [DRIVER] function callback to check whether a given
    scan mask is valid for the device.

.. _`iio_dev`:

struct iio_dev
==============

.. c:type:: struct iio_dev

    industrial I/O device

.. _`iio_dev.definition`:

Definition
----------

.. code-block:: c

    struct iio_dev {
        int id;
        struct module *driver_module;
        int modes;
        int currentmode;
        struct device dev;
        struct iio_event_interface *event_interface;
        struct iio_buffer *buffer;
        struct list_head buffer_list;
        int scan_bytes;
        struct mutex mlock;
        const unsigned long *available_scan_masks;
        unsigned masklength;
        const unsigned long *active_scan_mask;
        bool scan_timestamp;
        unsigned scan_index_timestamp;
        struct iio_trigger *trig;
        bool trig_readonly;
        struct iio_poll_func *pollfunc;
        struct iio_poll_func *pollfunc_event;
        struct iio_chan_spec const *channels;
        int num_channels;
        struct list_head channel_attr_list;
        struct attribute_group chan_attr_group;
        const char *name;
        const struct iio_info *info;
        clockid_t clock_id;
        struct mutex info_exist_lock;
        const struct iio_buffer_setup_ops *setup_ops;
        struct cdev chrdev;
    #define IIO_MAX_GROUPS 6
        const struct attribute_group *groups[IIO_MAX_GROUPS + 1];
        int groupcounter;
        unsigned long flags;
    #if defined(CONFIG_DEBUG_FS)
        struct dentry *debugfs_dentry;
        unsigned cached_reg_addr;
    #endif
    }

.. _`iio_dev.members`:

Members
-------

id
    [INTERN] used to identify device internally

driver_module
    [INTERN] used to make it harder to undercut users

modes
    [DRIVER] operating modes supported by device

currentmode
    [DRIVER] current operating mode

dev
    [DRIVER] device structure, should be assigned a parent
    and owner

event_interface
    [INTERN] event chrdevs associated with interrupt lines

buffer
    [DRIVER] any buffer present

buffer_list
    [INTERN] list of all buffers currently attached

scan_bytes
    [INTERN] num bytes captured to be fed to buffer demux

mlock
    [DRIVER] lock used to prevent simultaneous device state
    changes

available_scan_masks
    [DRIVER] optional array of allowed bitmasks

masklength
    [INTERN] the length of the mask established from
    channels

active_scan_mask
    [INTERN] union of all scan masks requested by buffers

scan_timestamp
    [INTERN] set if any buffers have requested timestamp

scan_index_timestamp
    [INTERN] cache of the index to the timestamp

trig
    [INTERN] current device trigger (buffer modes)

trig_readonly
    [INTERN] mark the current trigger immutable

pollfunc
    [DRIVER] function run on trigger being received

pollfunc_event
    [DRIVER] function run on events trigger being received

channels
    [DRIVER] channel specification structure table

num_channels
    [DRIVER] number of channels specified in \ ``channels``\ .

channel_attr_list
    [INTERN] keep track of automatically created channel
    attributes

chan_attr_group
    [INTERN] group for all attrs in base directory

name
    [DRIVER] name of the device.

info
    [DRIVER] callbacks and constant info from driver

clock_id
    [INTERN] timestamping clock posix identifier

info_exist_lock
    [INTERN] lock to prevent use during removal

setup_ops
    [DRIVER] callbacks to call before and after buffer
    enable/disable

chrdev
    [INTERN] associated character device

groups
    [INTERN] attribute groups

groupcounter
    [INTERN] index of next attribute group

flags
    [INTERN] file ops related flags including busy flag.

debugfs_dentry
    [INTERN] device specific debugfs dentry.

cached_reg_addr
    [INTERN] cached register address for debugfs reads.

.. _`iio_device_register`:

iio_device_register
===================

.. c:function::  iio_device_register( indio_dev)

    register a device with the IIO subsystem

    :param  indio_dev:
        Device structure filled by the device driver

.. _`devm_iio_device_register`:

devm_iio_device_register
========================

.. c:function::  devm_iio_device_register( dev,  indio_dev)

    Resource-managed \ :c:func:`iio_device_register`\ 

    :param  dev:
        Device to allocate iio_dev for

    :param  indio_dev:
        Device structure filled by the device driver

.. _`devm_iio_device_register.description`:

Description
-----------

Managed iio_device_register.  The IIO device registered with this
function is automatically unregistered on driver detach. This function
calls \ :c:func:`iio_device_register`\  internally. Refer to that function for more
information.

If an iio_dev registered with this function needs to be unregistered
separately, \ :c:func:`devm_iio_device_unregister`\  must be used.

.. _`devm_iio_device_register.return`:

Return
------

0 on success, negative error number on failure.

.. _`iio_device_put`:

iio_device_put
==============

.. c:function:: void iio_device_put(struct iio_dev *indio_dev)

    reference counted deallocation of struct device

    :param struct iio_dev \*indio_dev:
        IIO device structure containing the device

.. _`iio_device_get_clock`:

iio_device_get_clock
====================

.. c:function:: clockid_t iio_device_get_clock(const struct iio_dev *indio_dev)

    Retrieve current timestamping clock for the device

    :param const struct iio_dev \*indio_dev:
        IIO device structure containing the device

.. _`dev_to_iio_dev`:

dev_to_iio_dev
==============

.. c:function:: struct iio_dev *dev_to_iio_dev(struct device *dev)

    Get IIO device struct from a device struct

    :param struct device \*dev:
        The device embedded in the IIO device

.. _`dev_to_iio_dev.note`:

Note
----

The device must be a IIO device, otherwise the result is undefined.

.. _`iio_device_get`:

iio_device_get
==============

.. c:function:: struct iio_dev *iio_device_get(struct iio_dev *indio_dev)

    increment reference count for the device

    :param struct iio_dev \*indio_dev:
        IIO device structure

.. _`iio_device_get.return`:

Return
------

The passed IIO device

.. _`iio_device_set_drvdata`:

iio_device_set_drvdata
======================

.. c:function:: void iio_device_set_drvdata(struct iio_dev *indio_dev, void *data)

    Set device driver data

    :param struct iio_dev \*indio_dev:
        IIO device structure

    :param void \*data:
        Driver specific data

.. _`iio_device_set_drvdata.description`:

Description
-----------

Allows to attach an arbitrary pointer to an IIO device, which can later be
retrieved by \ :c:func:`iio_device_get_drvdata`\ .

.. _`iio_device_get_drvdata`:

iio_device_get_drvdata
======================

.. c:function:: void *iio_device_get_drvdata(struct iio_dev *indio_dev)

    Get device driver data

    :param struct iio_dev \*indio_dev:
        IIO device structure

.. _`iio_device_get_drvdata.description`:

Description
-----------

Returns the data previously set with \ :c:func:`iio_device_set_drvdata`\ 

.. _`iio_buffer_enabled`:

iio_buffer_enabled
==================

.. c:function:: bool iio_buffer_enabled(struct iio_dev *indio_dev)

    helper function to test if the buffer is enabled

    :param struct iio_dev \*indio_dev:
        IIO device structure for device

.. _`iio_get_debugfs_dentry`:

iio_get_debugfs_dentry
======================

.. c:function:: struct dentry *iio_get_debugfs_dentry(struct iio_dev *indio_dev)

    helper function to get the debugfs_dentry

    :param struct iio_dev \*indio_dev:
        IIO device structure for device

.. _`iio_degree_to_rad`:

IIO_DEGREE_TO_RAD
=================

.. c:function::  IIO_DEGREE_TO_RAD( deg)

    Convert degree to rad

    :param  deg:
        A value in degree

.. _`iio_degree_to_rad.description`:

Description
-----------

Returns the given value converted from degree to rad

.. _`iio_rad_to_degree`:

IIO_RAD_TO_DEGREE
=================

.. c:function::  IIO_RAD_TO_DEGREE( rad)

    Convert rad to degree

    :param  rad:
        A value in rad

.. _`iio_rad_to_degree.description`:

Description
-----------

Returns the given value converted from rad to degree

.. _`iio_g_to_m_s_2`:

IIO_G_TO_M_S_2
==============

.. c:function::  IIO_G_TO_M_S_2( g)

    Convert g to meter / second**2

    :param  g:
        A value in g

.. _`iio_g_to_m_s_2.description`:

Description
-----------

Returns the given value converted from g to meter / second**2

.. _`iio_m_s_2_to_g`:

IIO_M_S_2_TO_G
==============

.. c:function::  IIO_M_S_2_TO_G( ms2)

    Convert meter / second**2 to g

    :param  ms2:
        A value in meter / second**2

.. _`iio_m_s_2_to_g.description`:

Description
-----------

Returns the given value converted from meter / second**2 to g

.. This file was automatic generated / don't edit.

