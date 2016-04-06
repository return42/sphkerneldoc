
.. _API-struct-v4l2-mbus-config:

=======================
struct v4l2_mbus_config
=======================

*man struct v4l2_mbus_config(9)*

*4.6.0-rc1*

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
