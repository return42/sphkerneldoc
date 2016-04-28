.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rc-dev:

=============
struct rc_dev
=============

*man struct rc_dev(9)*

*4.6.0-rc5*

represents a remote control device


Synopsis
========

.. code-block:: c

    struct rc_dev {
      struct device dev;
      atomic_t initialized;
      const struct attribute_group * sysfs_groups[5];
      const char * input_name;
      const char * input_phys;
      struct input_id input_id;
      char * driver_name;
      const char * map_name;
      struct rc_map rc_map;
      struct mutex lock;
      unsigned int minor;
      struct ir_raw_event_ctrl * raw;
      struct input_dev * input_dev;
      enum rc_driver_type driver_type;
      bool idle;
      u64 allowed_protocols;
      u64 enabled_protocols;
      u64 allowed_wakeup_protocols;
      u64 enabled_wakeup_protocols;
      struct rc_scancode_filter scancode_filter;
      struct rc_scancode_filter scancode_wakeup_filter;
      u32 scancode_mask;
      u32 users;
      void * priv;
      spinlock_t keylock;
      bool keypressed;
      unsigned long keyup_jiffies;
      struct timer_list timer_keyup;
      u32 last_keycode;
      enum rc_type last_protocol;
      u32 last_scancode;
      u8 last_toggle;
      u32 timeout;
      u32 min_timeout;
      u32 max_timeout;
      u32 rx_resolution;
      u32 tx_resolution;
      int (* change_protocol) (struct rc_dev *dev, u64 *rc_type);
      int (* change_wakeup_protocol) (struct rc_dev *dev, u64 *rc_type);
      int (* open) (struct rc_dev *dev);
      void (* close) (struct rc_dev *dev);
      int (* s_tx_mask) (struct rc_dev *dev, u32 mask);
      int (* s_tx_carrier) (struct rc_dev *dev, u32 carrier);
      int (* s_tx_duty_cycle) (struct rc_dev *dev, u32 duty_cycle);
      int (* s_rx_carrier_range) (struct rc_dev *dev, u32 min, u32 max);
      int (* tx_ir) (struct rc_dev *dev, unsigned *txbuf, unsigned n);
      void (* s_idle) (struct rc_dev *dev, bool enable);
      int (* s_learning_mode) (struct rc_dev *dev, int enable);
      int (* s_carrier_report) (struct rc_dev *dev, int enable);
      int (* s_filter) (struct rc_dev *dev,struct rc_scancode_filter *filter);
      int (* s_wakeup_filter) (struct rc_dev *dev,struct rc_scancode_filter *filter);
    };


Members
=======

dev
    driver model's view of this device

initialized
    1 if the device init has completed, 0 otherwise

sysfs_groups[5]
    sysfs attribute groups

input_name
    name of the input child device

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
    used to ensure we've filled in all protocol details before anyone
    can call show_protocols or store_protocols

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

allowed_protocols
    bitmask with the supported RC_BIT_* protocols

enabled_protocols
    bitmask with the enabled RC_BIT_* protocols

allowed_wakeup_protocols
    bitmask with the supported RC_BIT_* wakeup protocols

enabled_wakeup_protocols
    bitmask with the enabled RC_BIT_* wakeup protocols

scancode_filter
    scancode filter

scancode_wakeup_filter
    scancode wakeup filters

scancode_mask
    some hardware decoders are not capable of providing the full
    scancode to the application. As this is a hardware limit, we can't
    do anything with it. Yet, as the same keycode table can be used with
    other devices, a mask is provided to allow its usage. Drivers should
    generally leave this field in blank

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

change_wakeup_protocol
    allow changing the protocol used for wakeup filtering

open
    callback to allow drivers to enable polling/irq when IR input device
    is opened.

close
    callback to allow drivers to disable polling/irq when IR input
    device is opened.

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
    enable/disable hardware idle mode, upon which, device doesn't
    interrupt host until it sees IR pulses

s_learning_mode
    enable wide band receiver used for learning

s_carrier_report
    enable carrier reports

s_filter
    set the scancode filter

s_wakeup_filter
    set the wakeup scancode filter


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
