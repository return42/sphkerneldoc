
.. _API-struct-vif-params:

=================
struct vif_params
=================

*man struct vif_params(9)*

*4.6.0-rc1*

describes virtual interface parameters


Synopsis
========

.. code-block:: c

    struct vif_params {
      int use_4addr;
      u8 macaddr[ETH_ALEN];
    };


Members
=======

use_4addr
    use 4-address frames

macaddr[ETH_ALEN]
    address to use for this virtual interface. If this parameter is set to zero address the driver may determine the address as needed. This feature is only fully supported by
    drivers that enable the ``NL80211_FEATURE_MAC_ON_CREATE`` flag. Others may support creating ⋆ only p2p devices with specified MAC.
