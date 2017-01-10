.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e.h

.. _`i40e_is_mac_710`:

i40e_is_mac_710
===============

.. c:function:: bool i40e_is_mac_710(struct i40e_hw *hw)

    Return true if MAC is X710/XL710

    :param struct i40e_hw \*hw:
        ptr to the hardware info

.. _`i40e_addr_to_hkey`:

i40e_addr_to_hkey
=================

.. c:function:: u64 i40e_addr_to_hkey(const u8 *macaddr)

    Convert a 6-byte MAC Address to a u64 hash key

    :param const u8 \*macaddr:
        the MAC Address as the base key

.. _`i40e_addr_to_hkey.description`:

Description
-----------

Simply copies the address and returns it as a u64 for hashing

.. _`i40e_nvm_version_str`:

i40e_nvm_version_str
====================

.. c:function:: char *i40e_nvm_version_str(struct i40e_hw *hw)

    format the NVM version strings

    :param struct i40e_hw \*hw:
        ptr to the hardware info

.. _`i40e_netdev_to_pf`:

i40e_netdev_to_pf
=================

.. c:function:: struct i40e_pf *i40e_netdev_to_pf(struct net_device *netdev)

    Retrieve the PF struct for given netdev

    :param struct net_device \*netdev:
        the corresponding netdev

.. _`i40e_netdev_to_pf.description`:

Description
-----------

Return the PF struct for the given netdev

.. _`i40e_rx_is_programming_status`:

i40e_rx_is_programming_status
=============================

.. c:function:: bool i40e_rx_is_programming_status(u64 qw)

    check for programming status descriptor

    :param u64 qw:
        the first quad word of the program status descriptor

.. _`i40e_rx_is_programming_status.description`:

Description
-----------

The value of in the descriptor length field indicate if this
is a programming status descriptor for flow director or FCoE
by the value of I40E_RX_PROG_STATUS_DESC_LENGTH, otherwise
it is a packet descriptor.

.. _`i40e_get_fd_cnt_all`:

i40e_get_fd_cnt_all
===================

.. c:function:: int i40e_get_fd_cnt_all(struct i40e_pf *pf)

    get the total FD filter space available

    :param struct i40e_pf \*pf:
        pointer to the PF struct

.. _`i40e_find_vsi_by_type`:

i40e_find_vsi_by_type
=====================

.. c:function:: struct i40e_vsi *i40e_find_vsi_by_type(struct i40e_pf *pf, u16 type)

    Find and return Flow Director VSI

    :param struct i40e_pf \*pf:
        PF to search for VSI

    :param u16 type:
        Value indicating type of VSI we are looking for

.. _`i40e_irq_dynamic_enable`:

i40e_irq_dynamic_enable
=======================

.. c:function:: void i40e_irq_dynamic_enable(struct i40e_vsi *vsi, int vector)

    Enable default interrupt generation settings

    :param struct i40e_vsi \*vsi:
        pointer to a vsi

    :param int vector:
        enable a particular Hw Interrupt vector, without base_vector

.. This file was automatic generated / don't edit.

