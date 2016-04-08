
.. _API-struct-ccwgroup-driver:

======================
struct ccwgroup_driver
======================

*man struct ccwgroup_driver(9)*

*4.6.0-rc1*

driver for ccw group devices


Synopsis
========

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
=======

setup
    function called during device creation to setup the device

remove
    function called on remove

set_online
    function called when device is set online

set_offline
    function called when device is set offline

shutdown
    function called when device is shut down

prepare
    prepare for pm state transition

complete
    undo work done in ``prepare``

freeze
    callback for freezing during hibernation snapshotting

thaw
    undo work done in ``freeze``

restore
    callback for restoring after hibernation

driver
    embedded driver structure
