.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/icm.c

.. _`icm`:

struct icm
==========

.. c:type:: struct icm

    Internal connection manager private data

.. _`icm.definition`:

Definition
----------

.. code-block:: c

    struct icm {
        struct mutex request_lock;
        struct delayed_work rescan_work;
        struct pci_dev *upstream_port;
        int vnd_cap;
        bool safe_mode;
        bool (*is_supported)(struct tb *tb);
        int (*get_mode)(struct tb *tb);
        int (*get_route)(struct tb *tb, u8 link, u8 depth, u64 *route);
        void (*device_connected)(struct tb *tb, const struct icm_pkg_header *hdr);
        void (*device_disconnected)(struct tb *tb, const struct icm_pkg_header *hdr);
        void (*xdomain_connected)(struct tb *tb, const struct icm_pkg_header *hdr);
        void (*xdomain_disconnected)(struct tb *tb, const struct icm_pkg_header *hdr);
    }

.. _`icm.members`:

Members
-------

request_lock
    Makes sure only one message is send to ICM at time

rescan_work
    Work used to rescan the surviving switches after resume

upstream_port
    Pointer to the PCIe upstream port this host
    controller is connected. This is only set for systems
    where ICM needs to be started manually

vnd_cap
    Vendor defined capability where PCIe2CIO mailbox resides
    (only set when \ ``upstream_port``\  is not \ ``NULL``\ )

safe_mode
    ICM is in safe mode

is_supported
    Checks if we can support ICM on this controller

get_mode
    Read and return the ICM firmware mode (optional)

get_route
    Find a route string for given switch

device_connected
    Handle device connected ICM message

device_disconnected
    Handle device disconnected ICM message
    \ ``xdomain_connected``\  - Handle XDomain connected ICM message
    \ ``xdomain_disconnected``\  - Handle XDomain disconnected ICM message

xdomain_connected
    *undescribed*

xdomain_disconnected
    *undescribed*

.. This file was automatic generated / don't edit.

