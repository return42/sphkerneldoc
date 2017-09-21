.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-nvm-parse.c

.. _`iwl_nvm_channel_flags`:

enum iwl_nvm_channel_flags
==========================

.. c:type:: enum iwl_nvm_channel_flags

    channel flags in NVM

.. _`iwl_nvm_channel_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_nvm_channel_flags {
        NVM_CHANNEL_VALID,
        NVM_CHANNEL_IBSS,
        NVM_CHANNEL_ACTIVE,
        NVM_CHANNEL_RADAR,
        NVM_CHANNEL_INDOOR_ONLY,
        NVM_CHANNEL_GO_CONCURRENT,
        NVM_CHANNEL_UNIFORM,
        NVM_CHANNEL_20MHZ,
        NVM_CHANNEL_40MHZ,
        NVM_CHANNEL_80MHZ,
        NVM_CHANNEL_160MHZ,
        NVM_CHANNEL_DC_HIGH
    };

.. _`iwl_nvm_channel_flags.constants`:

Constants
---------

NVM_CHANNEL_VALID
    channel is usable for this SKU/geo

NVM_CHANNEL_IBSS
    usable as an IBSS channel

NVM_CHANNEL_ACTIVE
    active scanning allowed

NVM_CHANNEL_RADAR
    radar detection required

NVM_CHANNEL_INDOOR_ONLY
    only indoor use is allowed

NVM_CHANNEL_GO_CONCURRENT
    GO operation is allowed when connected to BSS
    on same channel on 2.4 or same UNII band on 5.2

NVM_CHANNEL_UNIFORM
    uniform spreading required

NVM_CHANNEL_20MHZ
    20 MHz channel okay

NVM_CHANNEL_40MHZ
    40 MHz channel okay

NVM_CHANNEL_80MHZ
    80 MHz channel okay

NVM_CHANNEL_160MHZ
    160 MHz channel okay

NVM_CHANNEL_DC_HIGH
    DC HIGH required/allowed (?)

.. This file was automatic generated / don't edit.

