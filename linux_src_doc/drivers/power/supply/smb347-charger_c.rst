.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/smb347-charger.c

.. _`smb347_charger`:

struct smb347_charger
=====================

.. c:type:: struct smb347_charger

    smb347 charger instance

.. _`smb347_charger.definition`:

Definition
----------

.. code-block:: c

    struct smb347_charger {
        struct mutex lock;
        struct device *dev;
        struct regmap *regmap;
        struct power_supply *mains;
        struct power_supply *usb;
        struct power_supply *battery;
        bool mains_online;
        bool usb_online;
        bool charging_enabled;
        const struct smb347_charger_platform_data *pdata;
    }

.. _`smb347_charger.members`:

Members
-------

lock
    protects concurrent access to online variables

dev
    pointer to device

regmap
    pointer to driver regmap

mains
    power_supply instance for AC/DC power

usb
    power_supply instance for USB power

battery
    power_supply instance for battery

mains_online
    is AC/DC input connected

usb_online
    is USB input connected

charging_enabled
    is charging enabled

pdata
    pointer to platform data

.. _`smb347_update_ps_status`:

smb347_update_ps_status
=======================

.. c:function:: int smb347_update_ps_status(struct smb347_charger *smb)

    refreshes the power source status

    :param struct smb347_charger \*smb:
        pointer to smb347 charger instance

.. _`smb347_update_ps_status.description`:

Description
-----------

Function checks whether any power source is connected to the charger and
updates internal state accordingly. If there is a change to previous state
function returns \ ``1``\ , otherwise \ ``0``\  and negative errno in case of errror.

.. _`smb347_charging_status`:

smb347_charging_status
======================

.. c:function:: int smb347_charging_status(struct smb347_charger *smb)

    returns status of charging

    :param struct smb347_charger \*smb:
        pointer to smb347 charger instance

.. _`smb347_charging_status.description`:

Description
-----------

Function returns charging status. \ ``0``\  means no charging is in progress,
\ ``1``\  means pre-charging, \ ``2``\  fast-charging and \ ``3``\  taper-charging.

.. This file was automatic generated / don't edit.

