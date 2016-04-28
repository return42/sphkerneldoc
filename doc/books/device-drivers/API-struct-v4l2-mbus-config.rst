.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-mbus-config:

=======================
struct v4l2_mbus_config
=======================

*man struct v4l2_mbus_config(9)*

*4.6.0-rc5*

media bus configuration


Synopsis
========

.. code-block:: c

    struct v4l2_mbus_config {
      enum v4l2_mbus_type type;
      unsigned int flags;
    };


Members
=======

type
    in: interface type

flags
    in / out: configuration flags, depending on ``type``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
