
.. _API-struct-ccwgroup-device:

======================
struct ccwgroup_device
======================

*man struct ccwgroup_device(9)*

*4.6.0-rc1*

ccw group device


Synopsis
========

.. code-block:: c

    struct ccwgroup_device {
      enum state;
      unsigned int count;
      struct device dev;
      struct work_struct ungroup_work;
      struct ccw_device * cdev[0];
    };


Members
=======

state
    online/offline state

count
    number of attached slave devices

dev
    embedded device structure

ungroup_work
    work to be done when a ccwgroup notifier has action type ``BUS_NOTIFY_UNBIND_DRIVER``

cdev[0]
    variable number of slave devices, allocated as needed
