.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/setup.c

.. _`pseries_cmo_feature_init`:

pSeries_cmo_feature_init
========================

.. c:function:: void pSeries_cmo_feature_init( void)

    FW_FEATURE_CMO is not stored in ibm,hypertas-functions, handle that here. (Stolen from parse_system_parameter_string)

    :param void:
        no arguments
    :type void: 

.. _`pseries_power_off`:

pseries_power_off
=================

.. c:function:: void pseries_power_off( void)

    tell firmware about how to power off the system.

    :param void:
        no arguments
    :type void: 

.. _`pseries_power_off.description`:

Description
-----------

This function calls either the power-off rtas token in normal cases
or the ibm,power-off-ups token (if present & requested) in case of
a power failure. If power-off token is used, power on will only be
possible with power button press. If ibm,power-off-ups token is used
it will allow auto poweron after power is restored.

.. This file was automatic generated / don't edit.

