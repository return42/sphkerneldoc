.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/fw/api/alive.h

.. _`iwl_extended_cfg_flags`:

enum iwl_extended_cfg_flags
===========================

.. c:type:: enum iwl_extended_cfg_flags

    commands driver may send before finishing init flow

.. _`iwl_extended_cfg_flags.definition`:

Definition
----------

.. code-block:: c

    enum iwl_extended_cfg_flags {
        IWL_INIT_DEBUG_CFG,
        IWL_INIT_NVM,
        IWL_INIT_PHY
    };

.. _`iwl_extended_cfg_flags.constants`:

Constants
---------

IWL_INIT_DEBUG_CFG
    driver is going to send debug config command

IWL_INIT_NVM
    driver is going to send NVM_ACCESS commands

IWL_INIT_PHY
    driver is going to send PHY_DB commands

.. _`iwl_init_extended_cfg_cmd`:

struct iwl_init_extended_cfg_cmd
================================

.. c:type:: struct iwl_init_extended_cfg_cmd

    mark what commands ucode should wait for before finishing init flows

.. _`iwl_init_extended_cfg_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_init_extended_cfg_cmd {
        __le32 init_flags;
    }

.. _`iwl_init_extended_cfg_cmd.members`:

Members
-------

init_flags
    values from iwl_extended_cfg_flags

.. _`iwl_radio_version_notif`:

struct iwl_radio_version_notif
==============================

.. c:type:: struct iwl_radio_version_notif

    information on the radio version ( RADIO_VERSION_NOTIFICATION = 0x68 )

.. _`iwl_radio_version_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_radio_version_notif {
        __le32 radio_flavor;
        __le32 radio_step;
        __le32 radio_dash;
    }

.. _`iwl_radio_version_notif.members`:

Members
-------

radio_flavor
    radio flavor

radio_step
    radio version step

radio_dash
    radio version dash

.. _`iwl_card_state_notif`:

struct iwl_card_state_notif
===========================

.. c:type:: struct iwl_card_state_notif

    information on the card state ( CARD_STATE_NOTIFICATION = 0xa1 )

.. _`iwl_card_state_notif.definition`:

Definition
----------

.. code-block:: c

    struct iwl_card_state_notif {
        __le32 flags;
    }

.. _`iwl_card_state_notif.members`:

Members
-------

flags
    \ :c:type:`enum iwl_card_state_flags <iwl_card_state_flags>`\ 

.. This file was automatic generated / don't edit.

