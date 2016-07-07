.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/net_tstamp.h

.. _`hwtstamp_config`:

struct hwtstamp_config
======================

.. c:type:: struct hwtstamp_config

    \ ``SIOCGHWTSTAMP``\  and \ ``SIOCSHWTSTAMP``\  parameter

.. _`hwtstamp_config.definition`:

Definition
----------

.. code-block:: c

    struct hwtstamp_config {
        int flags;
        int tx_type;
        int rx_filter;
    }

.. _`hwtstamp_config.members`:

Members
-------

flags
    no flags defined right now, must be zero for \ ``SIOCSHWTSTAMP``\ 

tx_type
    one of HWTSTAMP_TX\_\*

rx_filter
    one of HWTSTAMP_FILTER\_\*

.. _`hwtstamp_config.description`:

Description
-----------

\ ``SIOCGHWTSTAMP``\  and \ ``SIOCSHWTSTAMP``\  expect a \ :c:type:`struct ifreq <ifreq>`\  with a
ifr_data pointer to this structure.  For \ ``SIOCSHWTSTAMP``\ , if the
driver or hardware does not support the requested \ ``rx_filter``\  value,
the driver may use a more general filter mode.  In this case
\ ``rx_filter``\  will indicate the actual mode on return.

.. This file was automatic generated / don't edit.

