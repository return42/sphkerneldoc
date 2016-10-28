.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/intel_mid_battery.c

.. _`pmic_scu_ipc_battery_cc_read`:

pmic_scu_ipc_battery_cc_read
============================

.. c:function:: int pmic_scu_ipc_battery_cc_read(u32 *value)

    read battery cc

    :param u32 \*value:
        battery coulomb counter read

.. _`pmic_scu_ipc_battery_cc_read.description`:

Description
-----------

Reads the battery couloumb counter value, returns 0 on success, or
an error code

This function may sleep. Locking for SCU accesses is handled for
the caller.

.. _`pmic_scu_ipc_battery_property_get`:

pmic_scu_ipc_battery_property_get
=================================

.. c:function:: int pmic_scu_ipc_battery_property_get(struct battery_property *prop)

    fetch properties

    :param struct battery_property \*prop:
        battery properties

.. _`pmic_scu_ipc_battery_property_get.description`:

Description
-----------

Retrieve the battery properties from the power management

This function may sleep. Locking for SCU accesses is handled for
the caller.

.. _`pmic_scu_ipc_set_charger`:

pmic_scu_ipc_set_charger
========================

.. c:function:: int pmic_scu_ipc_set_charger(int charger)

    set charger

    :param int charger:
        charger to select

.. _`pmic_scu_ipc_set_charger.description`:

Description
-----------

Switch the charging mode for the SCU

.. _`pmic_battery_log_event`:

pmic_battery_log_event
======================

.. c:function:: void pmic_battery_log_event(enum batt_event event)

    log battery events

    :param enum batt_event event:
        battery event to be logged

.. _`pmic_battery_log_event.context`:

Context
-------

can sleep

.. _`pmic_battery_log_event.description`:

Description
-----------

There are multiple battery events which may be of interest to users;
this battery function logs the different battery events onto the
kernel log messages.

.. _`pmic_battery_read_status`:

pmic_battery_read_status
========================

.. c:function:: void pmic_battery_read_status(struct pmic_power_module_info *pbi)

    read battery status information

    :param struct pmic_power_module_info \*pbi:
        device info structure to update the read information

.. _`pmic_battery_read_status.context`:

Context
-------

can sleep

.. _`pmic_battery_read_status.description`:

Description
-----------

PMIC power source information need to be updated based on the data read
from the PMIC battery registers.

.. _`pmic_usb_get_property`:

pmic_usb_get_property
=====================

.. c:function:: int pmic_usb_get_property(struct power_supply *psy, enum power_supply_property psp, union power_supply_propval *val)

    usb power source get property

    :param struct power_supply \*psy:
        usb power supply context

    :param enum power_supply_property psp:
        usb power source property

    :param union power_supply_propval \*val:
        usb power source property value

.. _`pmic_usb_get_property.context`:

Context
-------

can sleep

.. _`pmic_usb_get_property.description`:

Description
-----------

PMIC usb power source property needs to be provided to power_supply
subsytem for it to provide the information to users.

.. _`pmic_battery_get_property`:

pmic_battery_get_property
=========================

.. c:function:: int pmic_battery_get_property(struct power_supply *psy, enum power_supply_property psp, union power_supply_propval *val)

    battery power source get property

    :param struct power_supply \*psy:
        battery power supply context

    :param enum power_supply_property psp:
        battery power source property

    :param union power_supply_propval \*val:
        battery power source property value

.. _`pmic_battery_get_property.context`:

Context
-------

can sleep

.. _`pmic_battery_get_property.description`:

Description
-----------

PMIC battery power source property needs to be provided to power_supply
subsytem for it to provide the information to users.

.. _`pmic_battery_monitor`:

pmic_battery_monitor
====================

.. c:function:: void pmic_battery_monitor(struct work_struct *work)

    monitor battery status

    :param struct work_struct \*work:
        work structure

.. _`pmic_battery_monitor.context`:

Context
-------

can sleep

.. _`pmic_battery_monitor.description`:

Description
-----------

PMIC battery status needs to be monitored for any change
and information needs to be frequently updated.

.. _`pmic_battery_set_charger`:

pmic_battery_set_charger
========================

.. c:function:: int pmic_battery_set_charger(struct pmic_power_module_info *pbi, enum batt_charge_type chrg)

    set battery charger

    :param struct pmic_power_module_info \*pbi:
        device info structure

    :param enum batt_charge_type chrg:
        charge mode to set battery charger in

.. _`pmic_battery_set_charger.context`:

Context
-------

can sleep

.. _`pmic_battery_set_charger.description`:

Description
-----------

PMIC battery charger needs to be enabled based on the usb charge
capabilities connected to the platform.

.. _`pmic_battery_interrupt_handler`:

pmic_battery_interrupt_handler
==============================

.. c:function:: irqreturn_t pmic_battery_interrupt_handler(int id, void *dev)

    pmic battery interrupt handler

    :param int id:
        *undescribed*

    :param void \*dev:
        *undescribed*

.. _`pmic_battery_interrupt_handler.context`:

Context
-------

interrupt context

.. _`pmic_battery_interrupt_handler.description`:

Description
-----------

PMIC battery interrupt handler which will be called with either
battery full condition occurs or usb otg & battery connect
condition occurs.

.. _`pmic_battery_handle_intrpt`:

pmic_battery_handle_intrpt
==========================

.. c:function:: void pmic_battery_handle_intrpt(struct work_struct *work)

    pmic battery service interrupt

    :param struct work_struct \*work:
        work structure

.. _`pmic_battery_handle_intrpt.context`:

Context
-------

can sleep

.. _`pmic_battery_handle_intrpt.description`:

Description
-----------

PMIC battery needs to either update the battery status as full
if it detects battery full condition caused the interrupt or needs
to enable battery charger if it detects usb and battery detect
caused the source of interrupt.

.. _`probe`:

probe
=====

.. c:function:: int probe(int irq, struct device *dev)

    pmic battery initialize

    :param int irq:
        pmic battery device irq

    :param struct device \*dev:
        pmic battery device structure

.. _`probe.context`:

Context
-------

can sleep

.. _`probe.description`:

Description
-----------

PMIC battery initializes its internal data structue and other
infrastructure components for it to work as expected.

.. _`platform_pmic_battery_remove`:

platform_pmic_battery_remove
============================

.. c:function:: int platform_pmic_battery_remove(struct platform_device *pdev)

    pmic battery finalize

    :param struct platform_device \*pdev:
        *undescribed*

.. _`platform_pmic_battery_remove.context`:

Context
-------

can sleep

.. _`platform_pmic_battery_remove.description`:

Description
-----------

PMIC battery finalizes its internal data structue and other
infrastructure components that it initialized in
pmic_battery_probe.

.. This file was automatic generated / don't edit.

