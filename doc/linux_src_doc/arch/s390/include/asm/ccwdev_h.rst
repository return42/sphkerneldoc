.. -*- coding: utf-8; mode: rst -*-

========
ccwdev.h
========



.. _xref_struct_ccw_device:

struct ccw_device
=================

.. c:type:: struct ccw_device

    channel attached device



Definition
----------

.. code-block:: c

  struct ccw_device {
    spinlock_t * ccwlock;
    struct ccw_device_id id;
    struct ccw_driver * drv;
    struct device dev;
    int online;
    void (* handler) (struct ccw_device *, unsigned long, struct irb *);
  };



Members
-------

:``spinlock_t * ccwlock``:
    pointer to device lock

:``struct ccw_device_id id``:
    id of this device

:``struct ccw_driver * drv``:
    ccw driver for this device

:``struct device dev``:
    embedded device structure

:``int online``:
    online status of device

:``void (*) (struct ccw_device *, unsigned long, struct irb *) handler``:
    interrupt handler




Description
-----------

**handler** is a member of the device rather than the driver since a driver
can have different interrupt handlers for different ccw devices
(multi-subchannel drivers).




.. _xref_struct_ccw_driver:

struct ccw_driver
=================

.. c:type:: struct ccw_driver

    device driver for channel attached devices



Definition
----------

.. code-block:: c

  struct ccw_driver {
    struct ccw_device_id * ids;
    int (* probe) (struct ccw_device *);
    void (* remove) (struct ccw_device *);
    int (* set_online) (struct ccw_device *);
    int (* set_offline) (struct ccw_device *);
    int (* notify) (struct ccw_device *, int);
    void (* path_event) (struct ccw_device *, int *);
    void (* shutdown) (struct ccw_device *);
    int (* prepare) (struct ccw_device *);
    void (* complete) (struct ccw_device *);
    int (* freeze) (struct ccw_device *);
    int (* thaw) (struct ccw_device *);
    int (* restore) (struct ccw_device *);
    enum uc_todo (* uc_handler) (struct ccw_device *, struct irb *);
    struct device_driver driver;
    enum interruption_class int_class;
  };



Members
-------

:``struct ccw_device_id * ids``:
    ids supported by this driver

:``int (*) (struct ccw_device *) probe``:
    function called on probe

:``void (*) (struct ccw_device *) remove``:
    function called on remove

:``int (*) (struct ccw_device *) set_online``:
    called when setting device online

:``int (*) (struct ccw_device *) set_offline``:
    called when setting device offline

:``int (*) (struct ccw_device *, int) notify``:
    notify driver of device state changes

:``void (*) (struct ccw_device *, int *) path_event``:
    notify driver of channel path events

:``void (*) (struct ccw_device *) shutdown``:
    called at device shutdown

:``int (*) (struct ccw_device *) prepare``:
    prepare for pm state transition

:``void (*) (struct ccw_device *) complete``:
    undo work done in **prepare**

:``int (*)(struct ccw_device *) freeze``:
    callback for freezing during hibernation snapshotting

:``int (*) (struct ccw_device *) thaw``:
    undo work done in **freeze**

:``int (*)(struct ccw_device *) restore``:
    callback for restoring after hibernation

:``enum uc_todo (*) (struct ccw_device *, struct irb *) uc_handler``:
    callback for unit check handler

:``struct device_driver driver``:
    embedded device driver structure

:``enum interruption_class int_class``:
    interruption class to use for accounting interrupts



