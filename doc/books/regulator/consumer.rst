
.. _consumer:

=========================
Consumer driver interface
=========================

This offers a similar API to the kernel clock framework. Consumer drivers use :ref:`get <API-regulator-get>` and :ref:`put <API-regulator-put>` operations to acquire and
release regulators. Functions are provided to :ref:`enable <API-regulator-enable>` and :ref:`disable <API-regulator-disable>` the regulator and to get and set the runtime
parameters of the regulator.

When requesting regulators consumers use symbolic names for their supplies, such as "Vcc", which are mapped into actual regulator devices by the machine interface.

A stub version of this API is provided when the regulator framework is not in use in order to minimise the need to use ifdefs.


.. _consumer-enable:

Enabling and disabling
======================

The regulator API provides reference counted enabling and disabling of regulators. Consumer devices use the :ref:`regulator_enable <API-regulator-enable>` and
:ref:`regulator_disable <API-regulator-disable>`
      functions to enable and disable regulators. Calls to the two functions must be balanced.

Note that since multiple consumers may be using a regulator and machine constraints may not allow the regulator to be disabled there is no guarantee that calling
``regulator_disable`` will actually cause the supply provided by the regulator to be disabled. Consumer drivers should assume that the regulator may be enabled at all times.


.. _consumer-config:

Configuration
=============

Some consumer devices may need to be able to dynamically configure their supplies. For example, MMC drivers may need to select the correct operating voltage for their cards. This
may be done while the regulator is enabled or disabled.

The :ref:`regulator_set_voltage <API-regulator-set-voltage>`
      and :ref:`regulator_set_current_limit <API-regulator-set-current-limit>`
      functions provide the primary interface for this. Both take ranges of voltages and currents, supporting drivers that do not require a specific value (eg, CPU frequency
scaling normally permits the CPU to use a wider range of supply voltages at lower frequencies but does not require that the supply voltage be lowered). Where an exact value is
required both minimum and maximum values should be identical.


.. _consumer-callback:

Callbacks
=========

Callbacks may also be :ref:`registered <API-regulator-register-notifier>` for events such as regulation failures.
