.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8192e/dot11d.h

.. _`rt_dot11d_info`:

struct rt_dot11d_info
=====================

.. c:type:: struct rt_dot11d_info

    value greater than 0 if \ ``CountryIeBuf``\  contains valid country information element.

.. _`rt_dot11d_info.definition`:

Definition
----------

.. code-block:: c

    struct rt_dot11d_info {
        bool bEnabled;
        u16 CountryIeLen;
        u8 CountryIeBuf;
        u8 CountryIeSrcAddr;
        u8 CountryIeWatchdog;
        u8 channel_map;
        u8 MaxTxPwrDbmList;
        enum dot11d_state State;
    }

.. _`rt_dot11d_info.members`:

Members
-------

bEnabled
    *undescribed*

CountryIeLen
    *undescribed*

CountryIeBuf
    *undescribed*

CountryIeSrcAddr
    *undescribed*

CountryIeWatchdog
    *undescribed*

channel_map
    holds channel values
    0 - invalid,
    1 - valid (active scan),
    2 - valid (passive scan)
    \ ``CountryIeSrcAddr``\  - Source AP of the country IE

MaxTxPwrDbmList
    *undescribed*

State
    *undescribed*

.. This file was automatic generated / don't edit.

