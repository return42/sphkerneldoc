.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nsp_eth.c

.. _`nfp_eth_read_ports`:

nfp_eth_read_ports
==================

.. c:function:: struct nfp_eth_table *nfp_eth_read_ports(struct nfp_cpp *cpp)

    retrieve port information

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

.. _`nfp_eth_read_ports.description`:

Description
-----------

Read the port information from the device.  Returned structure should
be freed with \ :c:func:`kfree`\  once no longer needed.

.. _`nfp_eth_read_ports.return`:

Return
------

populated ETH table or NULL on error.

.. _`nfp_eth_config_commit_end`:

nfp_eth_config_commit_end
=========================

.. c:function:: int nfp_eth_config_commit_end(struct nfp_nsp *nsp)

    perform recorded configuration changes

    :param struct nfp_nsp \*nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 

.. _`nfp_eth_config_commit_end.description`:

Description
-----------

Perform the configuration which was requested with \__nfp_eth_set\_\*()
helpers and recorded in \ ``nsp``\  state.  If device was already configured
as requested or no \__nfp_eth_set\_\*() operations were made no NSP command
will be performed.

.. _`nfp_eth_config_commit_end.return`:

Return
------

0 - configuration successful;
1 - no changes were needed;
-ERRNO - configuration failed.

.. _`nfp_eth_set_mod_enable`:

nfp_eth_set_mod_enable
======================

.. c:function:: int nfp_eth_set_mod_enable(struct nfp_cpp *cpp, unsigned int idx, bool enable)

    set PHY module enable control bit

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param unsigned int idx:
        NFP chip-wide port index

    :param bool enable:
        Desired state

.. _`nfp_eth_set_mod_enable.description`:

Description
-----------

Enable or disable PHY module (this usually means setting the TX lanes
disable bits).

.. _`nfp_eth_set_mod_enable.return`:

Return
------

0 - configuration successful;
1 - no changes were needed;
-ERRNO - configuration failed.

.. _`nfp_eth_set_configured`:

nfp_eth_set_configured
======================

.. c:function:: int nfp_eth_set_configured(struct nfp_cpp *cpp, unsigned int idx, bool configed)

    set PHY module configured control bit

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param unsigned int idx:
        NFP chip-wide port index

    :param bool configed:
        Desired state

.. _`nfp_eth_set_configured.description`:

Description
-----------

Set the ifup/ifdown state on the PHY.

.. _`nfp_eth_set_configured.return`:

Return
------

0 - configuration successful;
1 - no changes were needed;
-ERRNO - configuration failed.

.. _`__nfp_eth_set_aneg`:

\__nfp_eth_set_aneg
===================

.. c:function:: int __nfp_eth_set_aneg(struct nfp_nsp *nsp, enum nfp_eth_aneg mode)

    set PHY autonegotiation control bit

    :param struct nfp_nsp \*nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 

    :param enum nfp_eth_aneg mode:
        Desired autonegotiation mode

.. _`__nfp_eth_set_aneg.description`:

Description
-----------

Allow/disallow PHY module to advertise/perform autonegotiation.
Will write to hwinfo overrides in the flash (persistent config).

.. _`__nfp_eth_set_aneg.return`:

Return
------

0 or -ERRNO.

.. _`__nfp_eth_set_fec`:

\__nfp_eth_set_fec
==================

.. c:function:: int __nfp_eth_set_fec(struct nfp_nsp *nsp, enum nfp_eth_fec mode)

    set PHY forward error correction control bit

    :param struct nfp_nsp \*nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 

    :param enum nfp_eth_fec mode:
        Desired fec mode

.. _`__nfp_eth_set_fec.description`:

Description
-----------

Set the PHY module forward error correction mode.
Will write to hwinfo overrides in the flash (persistent config).

.. _`__nfp_eth_set_fec.return`:

Return
------

0 or -ERRNO.

.. _`nfp_eth_set_fec`:

nfp_eth_set_fec
===============

.. c:function:: int nfp_eth_set_fec(struct nfp_cpp *cpp, unsigned int idx, enum nfp_eth_fec mode)

    set PHY forward error correction control mode

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param unsigned int idx:
        NFP chip-wide port index

    :param enum nfp_eth_fec mode:
        Desired fec mode

.. _`nfp_eth_set_fec.return`:

Return
------

0 - configuration successful;
1 - no changes were needed;
-ERRNO - configuration failed.

.. _`__nfp_eth_set_speed`:

\__nfp_eth_set_speed
====================

.. c:function:: int __nfp_eth_set_speed(struct nfp_nsp *nsp, unsigned int speed)

    set interface speed/rate

    :param struct nfp_nsp \*nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 

    :param unsigned int speed:
        Desired speed (per lane)

.. _`__nfp_eth_set_speed.description`:

Description
-----------

Set lane speed.  Provided \ ``speed``\  value should be subport speed divided
by number of lanes this subport is spanning (i.e. 10000 for 40G, 25000 for
50G, etc.)
Will write to hwinfo overrides in the flash (persistent config).

.. _`__nfp_eth_set_speed.return`:

Return
------

0 or -ERRNO.

.. _`__nfp_eth_set_split`:

\__nfp_eth_set_split
====================

.. c:function:: int __nfp_eth_set_split(struct nfp_nsp *nsp, unsigned int lanes)

    set interface lane split

    :param struct nfp_nsp \*nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 

    :param unsigned int lanes:
        Desired lanes per port

.. _`__nfp_eth_set_split.description`:

Description
-----------

Set number of lanes in the port.
Will write to hwinfo overrides in the flash (persistent config).

.. _`__nfp_eth_set_split.return`:

Return
------

0 or -ERRNO.

.. This file was automatic generated / don't edit.

