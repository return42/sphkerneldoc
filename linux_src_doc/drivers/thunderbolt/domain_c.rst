.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/domain.c

.. _`tb_domain_alloc`:

tb_domain_alloc
===============

.. c:function:: struct tb *tb_domain_alloc(struct tb_nhi *nhi, size_t privsize)

    Allocate a domain

    :param struct tb_nhi \*nhi:
        Pointer to the host controller

    :param size_t privsize:
        Size of the connection manager private data

.. _`tb_domain_alloc.description`:

Description
-----------

Allocates and initializes a new Thunderbolt domain. Connection
managers are expected to call this and then fill in \ ``cm_ops``\ 
accordingly.

Call \ :c:func:`tb_domain_put`\  to release the domain before it has been added
to the system.

.. _`tb_domain_alloc.return`:

Return
------

allocated domain structure on \ ``NULL``\  in case of error

.. _`tb_domain_add`:

tb_domain_add
=============

.. c:function:: int tb_domain_add(struct tb *tb)

    Add domain to the system

    :param struct tb \*tb:
        Domain to add

.. _`tb_domain_add.description`:

Description
-----------

Starts the domain and adds it to the system. Hotplugging devices will
work after this has been returned successfully. In order to remove
and release the domain after this function has been called, call
\ :c:func:`tb_domain_remove`\ .

.. _`tb_domain_add.return`:

Return
------

%0 in case of success and negative errno in case of error

.. _`tb_domain_remove`:

tb_domain_remove
================

.. c:function:: void tb_domain_remove(struct tb *tb)

    Removes and releases a domain

    :param struct tb \*tb:
        Domain to remove

.. _`tb_domain_remove.description`:

Description
-----------

Stops the domain, removes it from the system and releases all
resources once the last reference has been released.

.. _`tb_domain_suspend_noirq`:

tb_domain_suspend_noirq
=======================

.. c:function:: int tb_domain_suspend_noirq(struct tb *tb)

    Suspend a domain

    :param struct tb \*tb:
        Domain to suspend

.. _`tb_domain_suspend_noirq.description`:

Description
-----------

Suspends all devices in the domain and stops the control channel.

.. _`tb_domain_resume_noirq`:

tb_domain_resume_noirq
======================

.. c:function:: int tb_domain_resume_noirq(struct tb *tb)

    Resume a domain

    :param struct tb \*tb:
        Domain to resume

.. _`tb_domain_resume_noirq.description`:

Description
-----------

Re-starts the control channel, and resumes all devices connected to
the domain.

.. _`tb_domain_approve_switch`:

tb_domain_approve_switch
========================

.. c:function:: int tb_domain_approve_switch(struct tb *tb, struct tb_switch *sw)

    Approve switch

    :param struct tb \*tb:
        Domain the switch belongs to

    :param struct tb_switch \*sw:
        Switch to approve

.. _`tb_domain_approve_switch.description`:

Description
-----------

This will approve switch by connection manager specific means. In
case of success the connection manager will create tunnels for all
supported protocols.

.. _`tb_domain_approve_switch_key`:

tb_domain_approve_switch_key
============================

.. c:function:: int tb_domain_approve_switch_key(struct tb *tb, struct tb_switch *sw)

    Approve switch and add key

    :param struct tb \*tb:
        Domain the switch belongs to

    :param struct tb_switch \*sw:
        Switch to approve

.. _`tb_domain_approve_switch_key.description`:

Description
-----------

For switches that support secure connect, this function first adds
key to the switch NVM using connection manager specific means. If
adding the key is successful, the switch is approved and connected.

.. _`tb_domain_approve_switch_key.return`:

Return
------

%0 on success and negative errno in case of failure.

.. _`tb_domain_challenge_switch_key`:

tb_domain_challenge_switch_key
==============================

.. c:function:: int tb_domain_challenge_switch_key(struct tb *tb, struct tb_switch *sw)

    Challenge and approve switch

    :param struct tb \*tb:
        Domain the switch belongs to

    :param struct tb_switch \*sw:
        Switch to approve

.. _`tb_domain_challenge_switch_key.description`:

Description
-----------

For switches that support secure connect, this function generates
random challenge and sends it to the switch. The switch responds to
this and if the response matches our random challenge, the switch is
approved and connected.

.. _`tb_domain_challenge_switch_key.return`:

Return
------

%0 on success and negative errno in case of failure.

.. _`tb_domain_disconnect_pcie_paths`:

tb_domain_disconnect_pcie_paths
===============================

.. c:function:: int tb_domain_disconnect_pcie_paths(struct tb *tb)

    Disconnect all PCIe paths

    :param struct tb \*tb:
        Domain whose PCIe paths to disconnect

.. _`tb_domain_disconnect_pcie_paths.description`:

Description
-----------

This needs to be called in preparation for NVM upgrade of the host
controller. Makes sure all PCIe paths are disconnected.

Return \ ``0``\  on success and negative errno in case of error.

.. _`tb_domain_approve_xdomain_paths`:

tb_domain_approve_xdomain_paths
===============================

.. c:function:: int tb_domain_approve_xdomain_paths(struct tb *tb, struct tb_xdomain *xd)

    Enable DMA paths for XDomain

    :param struct tb \*tb:
        Domain enabling the DMA paths

    :param struct tb_xdomain \*xd:
        XDomain DMA paths are created to

.. _`tb_domain_approve_xdomain_paths.description`:

Description
-----------

Calls connection manager specific method to enable DMA paths to the
XDomain in question.

.. _`tb_domain_approve_xdomain_paths.return`:

Return
------

0% in case of success and negative errno otherwise. In
particular returns \ ``-ENOTSUPP``\  if the connection manager
implementation does not support XDomains.

.. _`tb_domain_disconnect_xdomain_paths`:

tb_domain_disconnect_xdomain_paths
==================================

.. c:function:: int tb_domain_disconnect_xdomain_paths(struct tb *tb, struct tb_xdomain *xd)

    Disable DMA paths for XDomain

    :param struct tb \*tb:
        Domain disabling the DMA paths

    :param struct tb_xdomain \*xd:
        XDomain whose DMA paths are disconnected

.. _`tb_domain_disconnect_xdomain_paths.description`:

Description
-----------

Calls connection manager specific method to disconnect DMA paths to
the XDomain in question.

.. _`tb_domain_disconnect_xdomain_paths.return`:

Return
------

0% in case of success and negative errno otherwise. In
particular returns \ ``-ENOTSUPP``\  if the connection manager
implementation does not support XDomains.

.. _`tb_domain_disconnect_all_paths`:

tb_domain_disconnect_all_paths
==============================

.. c:function:: int tb_domain_disconnect_all_paths(struct tb *tb)

    Disconnect all paths for the domain

    :param struct tb \*tb:
        Domain whose paths are disconnected

.. _`tb_domain_disconnect_all_paths.description`:

Description
-----------

This function can be used to disconnect all paths (PCIe, XDomain) for
example in preparation for host NVM firmware upgrade. After this is
called the paths cannot be established without resetting the switch.

.. _`tb_domain_disconnect_all_paths.return`:

Return
------

%0 in case of success and negative errno otherwise.

.. This file was automatic generated / don't edit.

