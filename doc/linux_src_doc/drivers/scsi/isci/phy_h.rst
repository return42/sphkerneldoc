.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/phy.h

.. _`sci_phy_properties`:

struct sci_phy_properties
=========================

.. c:type:: struct sci_phy_properties

    This structure defines the properties common to all phys that can be retrieved.

.. _`sci_phy_properties.definition`:

Definition
----------

.. code-block:: c

    struct sci_phy_properties {
        struct isci_port *iport;
        enum sas_linkrate negotiated_link_rate;
        u8 index;
    }

.. _`sci_phy_properties.members`:

Members
-------

iport
    *undescribed*

negotiated_link_rate
    *undescribed*

index
    *undescribed*

.. _`sci_phy_properties.description`:

Description
-----------



.. _`sci_sas_phy_properties`:

struct sci_sas_phy_properties
=============================

.. c:type:: struct sci_sas_phy_properties

    This structure defines the properties, specific to a SAS phy, that can be retrieved.

.. _`sci_sas_phy_properties.definition`:

Definition
----------

.. code-block:: c

    struct sci_sas_phy_properties {
        struct sas_identify_frame rcvd_iaf;
        struct sci_phy_cap rcvd_cap;
    }

.. _`sci_sas_phy_properties.members`:

Members
-------

rcvd_iaf
    *undescribed*

rcvd_cap
    *undescribed*

.. _`sci_sas_phy_properties.description`:

Description
-----------



.. _`sci_sata_phy_properties`:

struct sci_sata_phy_properties
==============================

.. c:type:: struct sci_sata_phy_properties

    This structure defines the properties, specific to a SATA phy, that can be retrieved.

.. _`sci_sata_phy_properties.definition`:

Definition
----------

.. code-block:: c

    struct sci_sata_phy_properties {
        struct dev_to_host_fis signature_fis;
        bool is_port_selector_present;
    }

.. _`sci_sata_phy_properties.members`:

Members
-------

signature_fis
    *undescribed*

is_port_selector_present
    *undescribed*

.. _`sci_sata_phy_properties.description`:

Description
-----------



.. _`sci_phy_counter_id`:

enum sci_phy_counter_id
=======================

.. c:type:: enum sci_phy_counter_id

    This enumeration depicts the various pieces of optional information that can be retrieved for a specific phy.

.. _`sci_phy_counter_id.definition`:

Definition
----------

.. code-block:: c

    enum sci_phy_counter_id {
        SCIC_PHY_COUNTER_RECEIVED_FRAME,
        SCIC_PHY_COUNTER_TRANSMITTED_FRAME,
        SCIC_PHY_COUNTER_RECEIVED_FRAME_WORD,
        SCIC_PHY_COUNTER_TRANSMITTED_FRAME_DWORD,
        SCIC_PHY_COUNTER_LOSS_OF_SYNC_ERROR,
        SCIC_PHY_COUNTER_RECEIVED_DISPARITY_ERROR,
        SCIC_PHY_COUNTER_RECEIVED_FRAME_CRC_ERROR,
        SCIC_PHY_COUNTER_RECEIVED_DONE_ACK_NAK_TIMEOUT,
        SCIC_PHY_COUNTER_TRANSMITTED_DONE_ACK_NAK_TIMEOUT,
        SCIC_PHY_COUNTER_INACTIVITY_TIMER_EXPIRED,
        SCIC_PHY_COUNTER_RECEIVED_DONE_CREDIT_TIMEOUT,
        SCIC_PHY_COUNTER_TRANSMITTED_DONE_CREDIT_TIMEOUT,
        SCIC_PHY_COUNTER_RECEIVED_CREDIT_BLOCKED,
        SCIC_PHY_COUNTER_RECEIVED_SHORT_FRAME,
        SCIC_PHY_COUNTER_RECEIVED_FRAME_WITHOUT_CREDIT,
        SCIC_PHY_COUNTER_RECEIVED_FRAME_AFTER_DONE,
        SCIC_PHY_COUNTER_SN_DWORD_SYNC_ERROR
    };

.. _`sci_phy_counter_id.constants`:

Constants
---------

SCIC_PHY_COUNTER_RECEIVED_FRAME
    *undescribed*

SCIC_PHY_COUNTER_TRANSMITTED_FRAME
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_FRAME_WORD
    *undescribed*

SCIC_PHY_COUNTER_TRANSMITTED_FRAME_DWORD
    *undescribed*

SCIC_PHY_COUNTER_LOSS_OF_SYNC_ERROR
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_DISPARITY_ERROR
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_FRAME_CRC_ERROR
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_DONE_ACK_NAK_TIMEOUT
    *undescribed*

SCIC_PHY_COUNTER_TRANSMITTED_DONE_ACK_NAK_TIMEOUT
    *undescribed*

SCIC_PHY_COUNTER_INACTIVITY_TIMER_EXPIRED
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_DONE_CREDIT_TIMEOUT
    *undescribed*

SCIC_PHY_COUNTER_TRANSMITTED_DONE_CREDIT_TIMEOUT
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_CREDIT_BLOCKED
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_SHORT_FRAME
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_FRAME_WITHOUT_CREDIT
    *undescribed*

SCIC_PHY_COUNTER_RECEIVED_FRAME_AFTER_DONE
    *undescribed*

SCIC_PHY_COUNTER_SN_DWORD_SYNC_ERROR
    *undescribed*

.. _`sci_phy_counter_id.description`:

Description
-----------

???

.. This file was automatic generated / don't edit.

