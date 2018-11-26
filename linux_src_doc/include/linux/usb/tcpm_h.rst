.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/tcpm.h

.. _`tcpc_config`:

struct tcpc_config
==================

.. c:type:: struct tcpc_config

    Port configuration

.. _`tcpc_config.definition`:

Definition
----------

.. code-block:: c

    struct tcpc_config {
        const u32 *src_pdo;
        unsigned int nr_src_pdo;
        const u32 *snk_pdo;
        unsigned int nr_snk_pdo;
        const u32 *snk_vdo;
        unsigned int nr_snk_vdo;
        unsigned int operating_snk_mw;
        enum typec_port_type type;
        enum typec_port_data data;
        enum typec_role default_role;
        bool try_role_hw;
        const struct typec_altmode_desc *alt_modes;
    }

.. _`tcpc_config.members`:

Members
-------

src_pdo
    PDO parameters sent to port partner as response to
    PD_CTRL_GET_SOURCE_CAP message

nr_src_pdo
    Number of entries in \ ``src_pdo``\ 

snk_pdo
    PDO parameters sent to partner as response to
    PD_CTRL_GET_SINK_CAP message

nr_snk_pdo
    Number of entries in \ ``snk_pdo``\ 

snk_vdo
    *undescribed*

nr_snk_vdo
    *undescribed*

operating_snk_mw
    Required operating sink power in mW

type
    Port type (TYPEC_PORT_DFP, TYPEC_PORT_UFP, or
    TYPEC_PORT_DRP)

data
    *undescribed*

default_role
    Default port role (TYPEC_SINK or TYPEC_SOURCE).
    Set to TYPEC_NO_PREFERRED_ROLE if no default role.

try_role_hw
    True if try.{Src,Snk} is implemented in hardware

alt_modes
    List of supported alternate modes

.. _`tcpc_dev`:

struct tcpc_dev
===============

.. c:type:: struct tcpc_dev

    Port configuration and callback functions

.. _`tcpc_dev.definition`:

Definition
----------

.. code-block:: c

    struct tcpc_dev {
        const struct tcpc_config *config;
        struct fwnode_handle *fwnode;
        int (*init)(struct tcpc_dev *dev);
        int (*get_vbus)(struct tcpc_dev *dev);
        int (*get_current_limit)(struct tcpc_dev *dev);
        int (*set_cc)(struct tcpc_dev *dev, enum typec_cc_status cc);
        int (*get_cc)(struct tcpc_dev *dev, enum typec_cc_status *cc1, enum typec_cc_status *cc2);
        int (*set_polarity)(struct tcpc_dev *dev, enum typec_cc_polarity polarity);
        int (*set_vconn)(struct tcpc_dev *dev, bool on);
        int (*set_vbus)(struct tcpc_dev *dev, bool on, bool charge);
        int (*set_current_limit)(struct tcpc_dev *dev, u32 max_ma, u32 mv);
        int (*set_pd_rx)(struct tcpc_dev *dev, bool on);
        int (*set_roles)(struct tcpc_dev *dev, bool attached, enum typec_role role, enum typec_data_role data);
        int (*start_drp_toggling)(struct tcpc_dev *dev, enum typec_cc_status cc);
        int (*try_role)(struct tcpc_dev *dev, int role);
        int (*pd_transmit)(struct tcpc_dev *dev, enum tcpm_transmit_type type, const struct pd_message *msg);
    }

.. _`tcpc_dev.members`:

Members
-------

config
    Pointer to port configuration

fwnode
    Pointer to port fwnode

init
    *undescribed*

get_vbus
    Called to read current VBUS state

get_current_limit
    Optional; called by the tcpm core when configured as a snk
    and cc=Rp-def. This allows the tcpm to provide a fallback
    current-limit detection method for the cc=Rp-def case.
    For example, some tcpcs may include BC1.2 charger detection
    and use that in this case.

set_cc
    Called to set value of CC pins

get_cc
    Called to read current CC pin values

set_polarity
    Called to set polarity

set_vconn
    Called to enable or disable VCONN

set_vbus
    Called to enable or disable VBUS

set_current_limit
    Optional; called to set current limit as negotiated
    with partner.

set_pd_rx
    Called to enable or disable reception of PD messages

set_roles
    Called to set power and data roles

start_drp_toggling
    Optional; if supported by hardware, called to start DRP
    toggling. DRP toggling is stopped automatically if
    a connection is established.

try_role
    Optional; called to set a preferred role

pd_transmit
    Called to transmit PD message

.. This file was automatic generated / don't edit.

