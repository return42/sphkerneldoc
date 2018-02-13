.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-eeprom-parse.c

.. _`iwl_eeprom_channel_flags`:

enum iwl_eeprom_channel_flags
=============================

.. c:type:: enum iwl_eeprom_channel_flags

    channel flags in EEPROM

.. _`iwl_eeprom_channel_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_eeprom_channel_flags {
        EEPROM_CHANNEL_VALID,
        EEPROM_CHANNEL_IBSS,
        EEPROM_CHANNEL_ACTIVE,
        EEPROM_CHANNEL_RADAR,
        EEPROM_CHANNEL_WIDE,
        EEPROM_CHANNEL_DFS
    };

.. _`iwl_eeprom_channel_flags.constants`:

Constants
---------

EEPROM_CHANNEL_VALID
    channel is usable for this SKU/geo

EEPROM_CHANNEL_IBSS
    usable as an IBSS channel

EEPROM_CHANNEL_ACTIVE
    active scanning allowed

EEPROM_CHANNEL_RADAR
    radar detection required

EEPROM_CHANNEL_WIDE
    20 MHz channel okay (?)

EEPROM_CHANNEL_DFS
    dynamic freq selection candidate

.. _`iwl_eeprom_channel`:

struct iwl_eeprom_channel
=========================

.. c:type:: struct iwl_eeprom_channel

    EEPROM channel data

.. _`iwl_eeprom_channel.definition`:

Definition
----------

.. code-block:: c

    struct iwl_eeprom_channel {
        u8 flags;
        s8 max_power_avg;
    }

.. _`iwl_eeprom_channel.members`:

Members
-------

flags
    \ ``EEPROM_CHANNEL``\ \_\* flags

max_power_avg
    max power (in dBm) on this channel, at most 31 dBm

.. This file was automatic generated / don't edit.

