.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/rc-core.h

.. _`rc_driver_type`:

enum rc_driver_type
===================

.. c:type:: enum rc_driver_type

    type of the RC output

.. _`rc_driver_type.definition`:

Definition
----------

.. code-block:: c

    enum rc_driver_type {
        RC_DRIVER_SCANCODE,
        RC_DRIVER_IR_RAW,
        RC_DRIVER_IR_RAW_TX
    };

.. _`rc_driver_type.constants`:

Constants
---------

RC_DRIVER_SCANCODE
    Driver or hardware generates a scancode

RC_DRIVER_IR_RAW
    Driver or hardware generates pulse/space sequences.
    It needs a Infra-Red pulse/space decoder

RC_DRIVER_IR_RAW_TX
    Device transmitter only,
    driver requires pulse/space data sequence.

.. _`rc_scancode_filter`:

struct rc_scancode_filter
=========================

.. c:type:: struct rc_scancode_filter

    Filter scan codes.

.. _`rc_scancode_filter.definition`:

Definition
----------

.. code-block:: c

    struct rc_scancode_filter {
        u32 data;
        u32 mask;
    }

.. _`rc_scancode_filter.members`:

Members
-------

data
    Scancode data to match.

mask
    Mask of bits of scancode to compare.

.. _`rc_filter_type`:

enum rc_filter_type
===================

.. c:type:: enum rc_filter_type

    Filter type constants.

.. _`rc_filter_type.definition`:

Definition
----------

.. code-block:: c

    enum rc_filter_type {
        RC_FILTER_NORMAL,
        RC_FILTER_WAKEUP,
        RC_FILTER_MAX
    };

.. _`rc_filter_type.constants`:

Constants
---------

RC_FILTER_NORMAL
    Filter for normal operation.

RC_FILTER_WAKEUP
    Filter for waking from suspend.

RC_FILTER_MAX
    Number of filter types.

.. _`rc_dev`:

struct rc_dev
=============

.. c:type:: struct rc_dev

    represents a remote control device

.. _`rc_dev.definition`:

Definition
----------

.. code-block:: c

    struct rc_dev {
        struct device dev;
        bool managed_alloc;
        const struct attribute_group  *sysfs_groups;
        const char *device_name;
        const char *input_phys;
        struct input_id input_id;
        const char *driver_name;
        const char *map_name;
        struct rc_map rc_map;
        struct mutex lock;
        unsigned int minor;
        struct ir_raw_event_ctrl *raw;
        struct input_dev *input_dev;
        enum rc_driver_type driver_type;
        bool idle;
        bool encode_wakeup;
        u64 allowed_protocols;
        u64 enabled_protocols;
        u64 allowed_wakeup_protocols;
        enum rc_proto wakeup_protocol;
        struct rc_scancode_filter scancode_filter;
        struct rc_scancode_filter scancode_wakeup_filter;
        u32 scancode_mask;
        u32 users;
        void *priv;
        spinlock_t keylock;
        bool keypressed;
        unsigned long keyup_jiffies;
        struct timer_list timer_keyup;
        u32 last_keycode;
        enum rc_proto last_protocol;
        u32 last_scancode;
        u8 last_toggle;
        u32 timeout;
        u32 min_timeout;
        u32 max_timeout;
        u32 rx_resolution;
        u32 tx_resolution;
        int (*change_protocol)(struct rc_dev *dev, u64 *rc_proto);
        int (*open)(struct rc_dev *dev);
        void (*close)(struct rc_dev *dev);
        int (*s_tx_mask)(struct rc_dev *dev, u32 mask);
        int (*s_tx_carrier)(struct rc_dev *dev, u32 carrier);
        int (*s_tx_duty_cycle)(struct rc_dev *dev, u32 duty_cycle);
        int (*s_rx_carrier_range)(struct rc_dev *dev, u32 min, u32 max);
        int (*tx_ir)(struct rc_dev *dev, unsigned *txbuf, unsigned n);
        void (*s_idle)(struct rc_dev *dev, bool enable);
        int (*s_learning_mode)(struct rc_dev *dev, int enable);
        int (*s_carrier_report)(struct rc_dev *dev, int enable);
        int (*s_filter)(struct rc_dev *dev, struct rc_scancode_filter *filter);
        int (*s_wakeup_filter)(struct rc_dev *dev, struct rc_scancode_filter *filter);
        int (*s_timeout)(struct rc_dev *dev, unsigned int timeout);
    }

.. _`rc_dev.members`:

Members
-------

dev
    driver model's view of this device

managed_alloc
    devm_rc_allocate_device was used to create rc_dev

sysfs_groups
    sysfs attribute groups

device_name
    name of the rc child device

input_phys
    physical path to the input child device

input_id
    id of the input child device (struct input_id)

driver_name
    name of the hardware driver which registered this device

map_name
    name of the default keymap

rc_map
    current scan/key table

lock
    used to ensure we've filled in all protocol details before
    anyone can call show_protocols or store_protocols

minor
    unique minor remote control device number

raw
    additional data for raw pulse/space devices

input_dev
    the input child device used to communicate events to userspace

driver_type
    specifies if protocol decoding is done in hardware or software

idle
    used to keep track of RX state

encode_wakeup
    wakeup filtering uses IR encode API, therefore the allowed
    wakeup protocols is the set of all raw encoders

allowed_protocols
    bitmask with the supported RC_PROTO_BIT_* protocols

enabled_protocols
    bitmask with the enabled RC_PROTO_BIT_* protocols

allowed_wakeup_protocols
    bitmask with the supported RC_PROTO_BIT_* wakeup
    protocols

wakeup_protocol
    the enabled RC_PROTO_* wakeup protocol or
    RC_PROTO_UNKNOWN if disabled.

scancode_filter
    scancode filter

scancode_wakeup_filter
    scancode wakeup filters

scancode_mask
    some hardware decoders are not capable of providing the full
    scancode to the application. As this is a hardware limit, we can't do
    anything with it. Yet, as the same keycode table can be used with other
    devices, a mask is provided to allow its usage. Drivers should generally
    leave this field in blank

users
    number of current users of the device

priv
    driver-specific data

keylock
    protects the remaining members of the struct

keypressed
    whether a key is currently pressed

keyup_jiffies
    time (in jiffies) when the current keypress should be released

timer_keyup
    timer for releasing a keypress

last_keycode
    keycode of last keypress

last_protocol
    protocol of last keypress

last_scancode
    scancode of last keypress

last_toggle
    toggle value of last command

timeout
    optional time after which device stops sending data

min_timeout
    minimum timeout supported by device

max_timeout
    maximum timeout supported by device

rx_resolution
    resolution (in ns) of input sampler

tx_resolution
    resolution (in ns) of output sampler

change_protocol
    allow changing the protocol used on hardware decoders

open
    callback to allow drivers to enable polling/irq when IR input device
    is opened.

close
    callback to allow drivers to disable polling/irq when IR input device
    is opened.

s_tx_mask
    set transmitter mask (for devices with multiple tx outputs)

s_tx_carrier
    set transmit carrier frequency

s_tx_duty_cycle
    set transmit duty cycle (0% - 100%)

s_rx_carrier_range
    inform driver about carrier it is expected to handle

tx_ir
    transmit IR

s_idle
    enable/disable hardware idle mode, upon which,
    device doesn't interrupt host until it sees IR pulses

s_learning_mode
    enable wide band receiver used for learning

s_carrier_report
    enable carrier reports

s_filter
    set the scancode filter

s_wakeup_filter
    set the wakeup scancode filter. If the mask is zero
    then wakeup should be disabled. wakeup_protocol will be set to
    a valid protocol if mask is nonzero.

s_timeout
    set hardware timeout in ns

.. _`rc_allocate_device`:

rc_allocate_device
==================

.. c:function:: struct rc_dev *rc_allocate_device(enum rc_driver_type)

    Allocates a RC device

    :param enum rc_driver_type:
        specifies the type of the RC output to be allocated
        returns a pointer to struct rc_dev.

.. _`devm_rc_allocate_device`:

devm_rc_allocate_device
=======================

.. c:function:: struct rc_dev *devm_rc_allocate_device(struct device *dev, enum rc_driver_type)

    Managed RC device allocation

    :param struct device \*dev:
        pointer to struct device

    :param enum rc_driver_type:
        specifies the type of the RC output to be allocated
        returns a pointer to struct rc_dev.

.. _`rc_free_device`:

rc_free_device
==============

.. c:function:: void rc_free_device(struct rc_dev *dev)

    Frees a RC device

    :param struct rc_dev \*dev:
        pointer to struct rc_dev.

.. _`rc_register_device`:

rc_register_device
==================

.. c:function:: int rc_register_device(struct rc_dev *dev)

    Registers a RC device

    :param struct rc_dev \*dev:
        pointer to struct rc_dev.

.. _`devm_rc_register_device`:

devm_rc_register_device
=======================

.. c:function:: int devm_rc_register_device(struct device *parent, struct rc_dev *dev)

    Manageded registering of a RC device

    :param struct device \*parent:
        pointer to struct device.

    :param struct rc_dev \*dev:
        pointer to struct rc_dev.

.. _`rc_unregister_device`:

rc_unregister_device
====================

.. c:function:: void rc_unregister_device(struct rc_dev *dev)

    Unregisters a RC device

    :param struct rc_dev \*dev:
        pointer to struct rc_dev.

.. _`rc_open`:

rc_open
=======

.. c:function:: int rc_open(struct rc_dev *rdev)

    Opens a RC device

    :param struct rc_dev \*rdev:
        pointer to struct rc_dev.

.. _`rc_close`:

rc_close
========

.. c:function:: void rc_close(struct rc_dev *rdev)

    Closes a RC device

    :param struct rc_dev \*rdev:
        pointer to struct rc_dev.

.. This file was automatic generated / don't edit.

