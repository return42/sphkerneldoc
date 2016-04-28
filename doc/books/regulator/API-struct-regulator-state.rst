.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulator-state:

======================
struct regulator_state
======================

*man struct regulator_state(9)*

*4.6.0-rc5*

regulator state during low power system states


Synopsis
========

.. code-block:: c

    struct regulator_state {
      int uV;
      unsigned int mode;
      int enabled;
      int disabled;
    };


Members
=======

uV
    Operating voltage during suspend.

mode
    Operating mode during suspend.

enabled
    Enabled during suspend.

disabled
    Disabled during suspend.


Description
===========

This describes a regulators state during a system wide low power state.
One of enabled or disabled must be set for the configuration to be
applied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
