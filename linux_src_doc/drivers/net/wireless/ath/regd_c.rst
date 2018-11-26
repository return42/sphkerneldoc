.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/regd.c

.. _`ath_reg_apply_ir_flags`:

ath_reg_apply_ir_flags
======================

.. c:function:: void ath_reg_apply_ir_flags(struct wiphy *wiphy, struct ath_regulatory *reg, enum nl80211_reg_initiator initiator)

    :param wiphy:
        the wiphy to use
    :type wiphy: struct wiphy \*

    :param reg:
        *undescribed*
    :type reg: struct ath_regulatory \*

    :param initiator:
        the regulatory hint initiator
    :type initiator: enum nl80211_reg_initiator

.. _`ath_reg_apply_ir_flags.description`:

Description
-----------

If no country IE has been received always enable passive scan
and no-ibss on these channels. This is only done for specific
regulatory SKUs.

If a country IE has been received check its rule for this
channel first before enabling active scan. The passive scan
would have been enforced by the initial processing of our
custom regulatory domain.

.. This file was automatic generated / don't edit.

