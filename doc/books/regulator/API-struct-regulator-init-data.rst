.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulator-init-data:

==========================
struct regulator_init_data
==========================

*man struct regulator_init_data(9)*

*4.6.0-rc5*

regulator platform initialisation data.


Synopsis
========

.. code-block:: c

    struct regulator_init_data {
      const char * supply_regulator;
      struct regulation_constraints constraints;
      int num_consumer_supplies;
      struct regulator_consumer_supply * consumer_supplies;
      int (* regulator_init) (void *driver_data);
      void * driver_data;
    };


Members
=======

supply_regulator
    Parent regulator. Specified using the regulator name as it appears
    in the name field in sysfs, which can be explicitly set using the
    constraints field 'name'.

constraints
    Constraints. These must be specified for the regulator to be usable.

num_consumer_supplies
    Number of consumer device supplies.

consumer_supplies
    Consumer device supply configuration.

regulator_init
    Callback invoked when the regulator has been registered.

driver_data
    Data passed to regulator_init.


Description
===========

Initialisation constraints, our supply and consumers supplies.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
