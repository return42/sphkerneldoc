.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ccw-driver:

=================
struct ccw_driver
=================

*man struct ccw_driver(9)*

*4.6.0-rc5*

device driver for channel attached devices


Synopsis
========

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
=======

ids
    ids supported by this driver

probe
    function called on probe

remove
    function called on remove

set_online
    called when setting device online

set_offline
    called when setting device offline

notify
    notify driver of device state changes

path_event
    notify driver of channel path events

shutdown
    called at device shutdown

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

uc_handler
    callback for unit check handler

driver
    embedded device driver structure

int_class
    interruption class to use for accounting interrupts


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
