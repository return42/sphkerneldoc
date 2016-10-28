.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/cmf.c

.. _`cmb_format`:

enum cmb_format
===============

.. c:type:: enum cmb_format

    types of supported measurement block formats

.. _`cmb_format.definition`:

Definition
----------

.. code-block:: c

    enum cmb_format {
        CMF_BASIC,
        CMF_EXTENDED,
        CMF_AUTODETECT
    };

.. _`cmb_format.constants`:

Constants
---------

CMF_BASIC
    traditional channel measurement blocks supported
    by all machines that we run on

CMF_EXTENDED
    improved format that was introduced with the z990
    machine

CMF_AUTODETECT
    default: use extended format when running on a machine
    supporting extended format, otherwise fall back to
    basic format

.. _`cmb_operations`:

struct cmb_operations
=====================

.. c:type:: struct cmb_operations

    functions to use depending on cmb_format

.. _`cmb_operations.definition`:

Definition
----------

.. code-block:: c

    struct cmb_operations {
        int (*alloc)(struct ccw_device *);
        void (*free)(struct ccw_device *);
        int (*set)(struct ccw_device *, u32);
        u64 (*read)(struct ccw_device *, int);
        int (*readall)(struct ccw_device *, struct cmbdata *);
        void (*reset)(struct ccw_device *);
    }

.. _`cmb_operations.members`:

Members
-------

alloc
    allocate memory for a channel measurement block,
    either with the help of a special pool or with kmalloc

free
    free memory allocated with \ ``alloc``\ 

set
    enable or disable measurement

read
    read a measurement entry at an index

readall
    read a measurement block in a common format

reset
    clear the data in the associated measurement block and
    reset its time stamp

.. _`cmb_operations.description`:

Description
-----------

Most of these functions operate on a struct ccw_device. There is only
one instance of struct cmb_operations because the format of the measurement
data is guaranteed to be the same for every ccw_device.

.. _`cmb_area`:

struct cmb_area
===============

.. c:type:: struct cmb_area

    container for global cmb data

.. _`cmb_area.definition`:

Definition
----------

.. code-block:: c

    struct cmb_area {
        struct cmb *mem;
        struct list_head list;
        int num_channels;
        spinlock_t lock;
    }

.. _`cmb_area.members`:

Members
-------

mem
    pointer to CMBs (only in basic measurement mode)

list
    contains a linked list of all subchannels

num_channels
    number of channels to be measured

lock
    protect concurrent access to \ ``mem``\  and \ ``list``\ 

.. _`cmb`:

struct cmb
==========

.. c:type:: struct cmb

    basic channel measurement block

.. _`cmb.definition`:

Definition
----------

.. code-block:: c

    struct cmb {
        u16 ssch_rsch_count;
        u16 sample_count;
        u32 device_connect_time;
        u32 function_pending_time;
        u32 device_disconnect_time;
        u32 control_unit_queuing_time;
        u32 device_active_only_time;
        u32 reserved[2];
    }

.. _`cmb.members`:

Members
-------

ssch_rsch_count
    number of ssch and rsch

sample_count
    number of samples

device_connect_time
    time of device connect

function_pending_time
    time of function pending

device_disconnect_time
    time of device disconnect

control_unit_queuing_time
    time of control unit queuing

device_active_only_time
    time of device active only

reserved
    unused in basic measurement mode

.. _`cmb.description`:

Description
-----------

The measurement block as used by the hardware. The fields are described
further in z/Architecture Principles of Operation, chapter 17.

The cmb area made up from these blocks must be a contiguous array and may
not be reallocated or freed.
Only one cmb area can be present in the system.

.. _`cmbe`:

struct cmbe
===========

.. c:type:: struct cmbe

    extended channel measurement block

.. _`cmbe.definition`:

Definition
----------

.. code-block:: c

    struct cmbe {
        u32 ssch_rsch_count;
        u32 sample_count;
        u32 device_connect_time;
        u32 function_pending_time;
        u32 device_disconnect_time;
        u32 control_unit_queuing_time;
        u32 device_active_only_time;
        u32 device_busy_time;
        u32 initial_command_response_time;
        u32 reserved[7];
    }

.. _`cmbe.members`:

Members
-------

ssch_rsch_count
    number of ssch and rsch

sample_count
    number of samples

device_connect_time
    time of device connect

function_pending_time
    time of function pending

device_disconnect_time
    time of device disconnect

control_unit_queuing_time
    time of control unit queuing

device_active_only_time
    time of device active only

device_busy_time
    time of device busy

initial_command_response_time
    initial command response time

reserved
    unused

.. _`cmbe.description`:

Description
-----------

The measurement block as used by the hardware. May be in any 64 bit physical
location.
The fields are described further in z/Architecture Principles of Operation,
third edition, chapter 17.

.. _`enable_cmf`:

enable_cmf
==========

.. c:function:: int enable_cmf(struct ccw_device *cdev)

    switch on the channel measurement for a specific device

    :param struct ccw_device \*cdev:
        The ccw device to be enabled

.. _`enable_cmf.description`:

Description
-----------

Returns \ ``0``\  for success or a negative error value.

.. _`enable_cmf.context`:

Context
-------

non-atomic

.. _`__disable_cmf`:

__disable_cmf
=============

.. c:function:: int __disable_cmf(struct ccw_device *cdev)

    switch off the channel measurement for a specific device

    :param struct ccw_device \*cdev:
        The ccw device to be disabled

.. _`__disable_cmf.description`:

Description
-----------

Returns \ ``0``\  for success or a negative error value.

.. _`__disable_cmf.context`:

Context
-------

non-atomic, \ :c:func:`device_lock`\  held.

.. _`disable_cmf`:

disable_cmf
===========

.. c:function:: int disable_cmf(struct ccw_device *cdev)

    switch off the channel measurement for a specific device

    :param struct ccw_device \*cdev:
        The ccw device to be disabled

.. _`disable_cmf.description`:

Description
-----------

Returns \ ``0``\  for success or a negative error value.

.. _`disable_cmf.context`:

Context
-------

non-atomic

.. _`cmf_read`:

cmf_read
========

.. c:function:: u64 cmf_read(struct ccw_device *cdev, int index)

    read one value from the current channel measurement block

    :param struct ccw_device \*cdev:
        the channel to be read

    :param int index:
        the index of the value to be read

.. _`cmf_read.description`:

Description
-----------

Returns the value read or \ ``0``\  if the value cannot be read.

.. _`cmf_read.context`:

Context
-------

any

.. _`cmf_readall`:

cmf_readall
===========

.. c:function:: int cmf_readall(struct ccw_device *cdev, struct cmbdata *data)

    read the current channel measurement block

    :param struct ccw_device \*cdev:
        the channel to be read

    :param struct cmbdata \*data:
        a pointer to a data block that will be filled

.. _`cmf_readall.description`:

Description
-----------

Returns \ ``0``\  on success, a negative error value otherwise.

.. _`cmf_readall.context`:

Context
-------

any

.. _`cmf_reactivate`:

cmf_reactivate
==============

.. c:function:: void cmf_reactivate( void)

    reactivate measurement block updates

    :param  void:
        no arguments

.. _`cmf_reactivate.description`:

Description
-----------

Use this during resume from hibernate.

.. This file was automatic generated / don't edit.

