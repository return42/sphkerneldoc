
.. _API-struct-ccw-dev-id:

=================
struct ccw_dev_id
=================

*man struct ccw_dev_id(9)*

*4.6.0-rc1*

unique identifier for ccw devices


Synopsis
========

.. code-block:: c

    struct ccw_dev_id {
      u8 ssid;
      u16 devno;
    };


Members
=======

ssid
    subchannel set id

devno
    device number


Description
===========

This structure is not directly based on any hardware structure. The hardware identifies a device by its device number and its subchannel, which is in turn identified by its id. In
order to get a unique identifier for ccw devices across subchannel sets, ``struct`` ccw_dev_id has been introduced.
