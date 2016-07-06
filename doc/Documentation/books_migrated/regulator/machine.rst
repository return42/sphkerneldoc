.. -*- coding: utf-8; mode: rst -*-

.. _machine:

*****************
Machine interface
*****************

This interface provides a way to define how regulators are connected to
consumers on a given system and what the valid operating parameters are
for the system.


.. _machine-supply:

Supplies
========

Regulator supplies are specified using
:ref:`struct regulator_consumer_supply <API-struct-regulator-consumer-supply>`.
This is done at :ref:`driver registration time <driver>` as part of
the machine constraints.


.. _machine-constraint:

Constraints
===========

As well as defining the connections the machine interface also provides
constraints defining the operations that clients are allowed to perform
and the parameters that may be set. This is required since generally
regulator devices will offer more flexibility than it is safe to use on
a given system, for example supporting higher supply voltages than the
consumers are rated for.

This is done at :ref:`driver registration time <driver>` by providing
a
:ref:`struct regulation_constraints <API-struct-regulation-constraints>`.

The constraints may also specify an initial configuration for the
regulator in the constraints, which is particularly useful for use with
static consumers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
