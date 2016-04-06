.. -*- coding: utf-8; mode: rst -*-

==========
ccwgroup.h
==========



.. _xref_struct_ccwgroup_device:

struct ccwgroup_device
======================

.. c:type:: struct ccwgroup_device

    ccw group device



Definition
----------

.. code-block:: c

  struct ccwgroup_device {
    enum state;
    unsigned int count;
    struct device dev;
    struct work_struct ungroup_work;
    struct ccw_device * cdev[0];
  };



Members
-------

:``enum state``:
    online/offline state

:``unsigned int count``:
    number of attached slave devices

:``struct device dev``:
    embedded device structure

:``struct work_struct ungroup_work``:
    work to be done when a ccwgroup notifier has action
    	type ``BUS_NOTIFY_UNBIND_DRIVER``

:``struct ccw_device * cdev[0]``:
    variable number of slave devices, allocated as needed





.. _xref_struct_ccwgroup_driver:

struct ccwgroup_driver
======================

.. c:type:: struct ccwgroup_driver

    driver for ccw group devices



Definition
----------

.. code-block:: c

  struct ccwgroup_driver {
    int (* setup) (struct ccwgroup_device *);
    void (* remove) (struct ccwgroup_device *);
    int (* set_online) (struct ccwgroup_device *);
    int (* set_offline) (struct ccwgroup_device *);
    void (* shutdown) (struct ccwgroup_device *);
    int (* prepare) (struct ccwgroup_device *);
    void (* complete) (struct ccwgroup_device *);
    int (* freeze) (struct ccwgroup_device *);
    int (* thaw) (struct ccwgroup_device *);
    int (* restore) (struct ccwgroup_device *);
    struct device_driver driver;
  };



Members
-------

:``int (*) (struct ccwgroup_device *) setup``:
    function called during device creation to setup the device

:``void (*) (struct ccwgroup_device *) remove``:
    function called on remove

:``int (*) (struct ccwgroup_device *) set_online``:
    function called when device is set online

:``int (*) (struct ccwgroup_device *) set_offline``:
    function called when device is set offline

:``void (*)(struct ccwgroup_device *) shutdown``:
    function called when device is shut down

:``int (*) (struct ccwgroup_device *) prepare``:
    prepare for pm state transition

:``void (*) (struct ccwgroup_device *) complete``:
    undo work done in **prepare**

:``int (*)(struct ccwgroup_device *) freeze``:
    callback for freezing during hibernation snapshotting

:``int (*) (struct ccwgroup_device *) thaw``:
    undo work done in **freeze**

:``int (*)(struct ccwgroup_device *) restore``:
    callback for restoring after hibernation

:``struct device_driver driver``:
    embedded driver structure



