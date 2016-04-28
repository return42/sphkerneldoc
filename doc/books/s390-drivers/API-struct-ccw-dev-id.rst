.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ccw-dev-id:

=================
struct ccw_dev_id
=================

*man struct ccw_dev_id(9)*

*4.6.0-rc5*

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

This structure is not directly based on any hardware structure. The
hardware identifies a device by its device number and its subchannel,
which is in turn identified by its id. In order to get a unique
identifier for ccw devices across subchannel sets, ``struct``
ccw_dev_id has been introduced.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
