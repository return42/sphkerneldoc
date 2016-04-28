.. -*- coding: utf-8; mode: rst -*-

.. _driver:

==========================
Regulator driver interface
==========================

Drivers for regulator chips :ref:`register <API-regulator-register>`
the regulators with the regulator core, providing operations structures
to the core. A :ref:`notifier <API-regulator-notifier-call-chain>`
interface allows error conditions to be reported to the core.

Registration should be triggered by explicit setup done by the platform,
supplying a
:ref:`struct regulator_init_data <API-struct-regulator-init-data>`
for the regulator containing :ref:`constraint <machine-constraint>`
and :ref:`supply <machine-supply>` information.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
