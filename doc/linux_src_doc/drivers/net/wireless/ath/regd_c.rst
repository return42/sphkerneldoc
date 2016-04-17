.. -*- coding: utf-8; mode: rst -*-

======
regd.c
======


.. _`ath_reg_apply_ir_flags`:

ath_reg_apply_ir_flags
======================

.. c:function:: void ath_reg_apply_ir_flags (struct wiphy *wiphy, struct ath_regulatory *reg, enum nl80211_reg_initiator initiator)

    :param struct wiphy \*wiphy:
        the wiphy to use

    :param struct ath_regulatory \*reg:

        *undescribed*

    :param enum nl80211_reg_initiator initiator:
        the regulatory hint initiator



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

