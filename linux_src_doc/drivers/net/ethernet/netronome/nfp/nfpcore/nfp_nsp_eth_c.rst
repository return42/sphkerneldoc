.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nsp_eth.c

.. _`nfp_eth_read_ports`:

nfp_eth_read_ports
==================

.. c:function:: struct nfp_eth_table *nfp_eth_read_ports(struct nfp_cpp *cpp)

    retrieve port information

    :param cpp:
        NFP CPP handle
    :type cpp: struct nfp_cpp \*

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

    :param nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 
    :type nsp: struct nfp_nsp \*

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

    :param cpp:
        NFP CPP handle
    :type cpp: struct nfp_cpp \*

    :param idx:
        NFP chip-wide port index
    :type idx: unsigned int

    :param enable:
        Desired state
    :type enable: bool

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

    :param cpp:
        NFP CPP handle
    :type cpp: struct nfp_cpp \*

    :param idx:
        NFP chip-wide port index
    :type idx: unsigned int

    :param configed:
        Desired state
    :type configed: bool

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

    :param nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 
    :type nsp: struct nfp_nsp \*

    :param mode:
        Desired autonegotiation mode
    :type mode: enum nfp_eth_aneg

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

    :param nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 
    :type nsp: struct nfp_nsp \*

    :param mode:
        Desired fec mode
    :type mode: enum nfp_eth_fec

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

    :param cpp:
        NFP CPP handle
    :type cpp: struct nfp_cpp \*

    :param idx:
        NFP chip-wide port index
    :type idx: unsigned int

    :param mode:
        Desired fec mode
    :type mode: enum nfp_eth_fec

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

    :param nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 
    :type nsp: struct nfp_nsp \*

    :param speed:
        Desired speed (per lane)
    :type speed: unsigned int

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

    :param nsp:
        NFP NSP handle returned from \ :c:func:`nfp_eth_config_start`\ 
    :type nsp: struct nfp_nsp \*

    :param lanes:
        Desired lanes per port
    :type lanes: unsigned int

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

