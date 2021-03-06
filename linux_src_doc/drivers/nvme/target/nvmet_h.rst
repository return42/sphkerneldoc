.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/target/nvmet.h

.. _`nvmet_port`:

struct nvmet_port
=================

.. c:type:: struct nvmet_port

    Common structure to keep port information for the target.

.. _`nvmet_port.definition`:

Definition
----------

.. code-block:: c

    struct nvmet_port {
        struct list_head entry;
        struct nvmf_disc_rsp_page_entry disc_addr;
        struct config_group group;
        struct config_group subsys_group;
        struct list_head subsystems;
        struct config_group referrals_group;
        struct list_head referrals;
        struct config_group ana_groups_group;
        struct nvmet_ana_group ana_default_group;
        enum nvme_ana_state *ana_state;
        void *priv;
        bool enabled;
        int inline_data_size;
    }

.. _`nvmet_port.members`:

Members
-------

entry
    Entry into referrals or transport list.

disc_addr
    Address information is stored in a format defined
    for a discovery log page entry.

group
    ConfigFS group for this element's folder.

subsys_group
    *undescribed*

subsystems
    *undescribed*

referrals_group
    *undescribed*

referrals
    *undescribed*

ana_groups_group
    *undescribed*

ana_default_group
    *undescribed*

ana_state
    *undescribed*

priv
    Private data for the transport.

enabled
    *undescribed*

inline_data_size
    *undescribed*

.. This file was automatic generated / don't edit.

