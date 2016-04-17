.. -*- coding: utf-8; mode: rst -*-

========
max197.h
========


.. _`max197_platform_data`:

struct max197_platform_data
===========================

.. c:type:: max197_platform_data

    MAX197 connectivity info


.. _`max197_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct max197_platform_data {
    int (* convert) (u8 ctrl);
  };


.. _`max197_platform_data.members`:

Members
-------

:``convert``:
    Function used to start a conversion with control byte ctrl.
    It must return the raw data, or a negative error code.


