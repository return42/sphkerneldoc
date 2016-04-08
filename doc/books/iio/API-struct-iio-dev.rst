
.. _API-struct-iio-dev:

==============
struct iio_dev
==============

*man struct iio_dev(9)*

*4.6.0-rc1*

industrial I/O device


Synopsis
========

.. code-block:: c

    struct iio_dev {
      int id;
      int modes;
      int currentmode;
      struct device dev;
      struct iio_event_interface * event_interface;
      struct iio_buffer * buffer;
      struct list_head buffer_list;
      int scan_bytes;
      struct mutex mlock;
      const unsigned long * available_scan_masks;
      unsigned masklength;
      const unsigned long * active_scan_mask;
      bool scan_timestamp;
      unsigned scan_index_timestamp;
      struct iio_trigger * trig;
      struct iio_poll_func * pollfunc;
      struct iio_poll_func * pollfunc_event;
      struct iio_chan_spec const * channels;
      int num_channels;
      struct list_head channel_attr_list;
      struct attribute_group chan_attr_group;
      const char * name;
      const struct iio_info * info;
      struct mutex info_exist_lock;
      const struct iio_buffer_setup_ops * setup_ops;
      struct cdev chrdev;
    #define IIO_MAX_GROUPS 6
      const struct attribute_group * groups[IIO_MAX_GROUPS + 1];
      int groupcounter;
      unsigned long flags;
    #if defined(CONFIG_DEBUG_FS)
      struct dentry * debugfs_dentry;
      unsigned cached_reg_addr;
    #endif
    };


Members
=======

id
    [INTERN] used to identify device internally

modes
    [DRIVER] operating modes supported by device

currentmode
    [DRIVER] current operating mode

dev
    [DRIVER] device structure, should be assigned a parent and owner

event_interface
    [INTERN] event chrdevs associated with interrupt lines

buffer
    [DRIVER] any buffer present

buffer_list
    [INTERN] list of all buffers currently attached

scan_bytes
    [INTERN] num bytes captured to be fed to buffer demux

mlock
    [DRIVER] lock used to prevent simultaneous device state changes

available_scan_masks
    [DRIVER] optional array of allowed bitmasks

masklength
    [INTERN] the length of the mask established from channels

active_scan_mask
    [INTERN] union of all scan masks requested by buffers

scan_timestamp
    [INTERN] set if any buffers have requested timestamp

scan_index_timestamp
    [INTERN] cache of the index to the timestamp

trig
    [INTERN] current device trigger (buffer modes)

pollfunc
    [DRIVER] function run on trigger being received

pollfunc_event
    [DRIVER] function run on events trigger being received

channels
    [DRIVER] channel specification structure table

num_channels
    [DRIVER] number of channels specified in ``channels``.

channel_attr_list
    [INTERN] keep track of automatically created channel attributes

chan_attr_group
    [INTERN] group for all attrs in base directory

name
    [DRIVER] name of the device.

info
    [DRIVER] callbacks and constant info from driver

info_exist_lock
    [INTERN] lock to prevent use during removal

setup_ops
    [DRIVER] callbacks to call before and after buffer enable/disable

chrdev
    [INTERN] associated character device

groups[IIO_MAX_GROUPS + 1]
    [INTERN] attribute groups

groupcounter
    [INTERN] index of next attribute group

flags
    [INTERN] file ops related flags including busy flag.

debugfs_dentry
    [INTERN] device specific debugfs dentry.

cached_reg_addr
    [INTERN] cached register address for debugfs reads.
