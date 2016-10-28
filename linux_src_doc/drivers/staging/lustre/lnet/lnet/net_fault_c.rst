.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lnet/lnet/net_fault.c

.. _`lnet_drop_rule_add`:

lnet_drop_rule_add
==================

.. c:function:: int lnet_drop_rule_add(struct lnet_fault_attr *attr)

    :param struct lnet_fault_attr \*attr:
        *undescribed*

.. _`lnet_drop_rule_del`:

lnet_drop_rule_del
==================

.. c:function:: int lnet_drop_rule_del(lnet_nid_t src, lnet_nid_t dst)

    \a dst will be removed. If \a src is zero, then all rules have \a dst as destination will be remove If \a dst is zero, then all rules have \a src as source will be removed If both of them are zero, all rules will be removed

    :param lnet_nid_t src:
        *undescribed*

    :param lnet_nid_t dst:
        *undescribed*

.. _`lnet_drop_rule_list`:

lnet_drop_rule_list
===================

.. c:function:: int lnet_drop_rule_list(int pos, struct lnet_fault_attr *attr, struct lnet_fault_stat *stat)

    :param int pos:
        *undescribed*

    :param struct lnet_fault_attr \*attr:
        *undescribed*

    :param struct lnet_fault_stat \*stat:
        *undescribed*

.. _`lnet_drop_rule_reset`:

lnet_drop_rule_reset
====================

.. c:function:: void lnet_drop_rule_reset( void)

    :param  void:
        no arguments

.. _`drop_rule_match`:

drop_rule_match
===============

.. c:function:: bool drop_rule_match(struct lnet_drop_rule *rule, lnet_nid_t src, lnet_nid_t dst, unsigned int type, unsigned int portal)

    decide whether should drop this message or not

    :param struct lnet_drop_rule \*rule:
        *undescribed*

    :param lnet_nid_t src:
        *undescribed*

    :param lnet_nid_t dst:
        *undescribed*

    :param unsigned int type:
        *undescribed*

    :param unsigned int portal:
        *undescribed*

.. _`lnet_drop_rule_match`:

lnet_drop_rule_match
====================

.. c:function:: bool lnet_drop_rule_match(lnet_hdr_t *hdr)

    :param lnet_hdr_t \*hdr:
        *undescribed*

.. _`msg_delay_send`:

msg_delay_send
==============

.. c:function::  msg_delay_send()

.. _`delay_rule_match`:

delay_rule_match
================

.. c:function:: bool delay_rule_match(struct lnet_delay_rule *rule, lnet_nid_t src, lnet_nid_t dst, unsigned int type, unsigned int portal, struct lnet_msg *msg)

    decide whether should delay this message or not

    :param struct lnet_delay_rule \*rule:
        *undescribed*

    :param lnet_nid_t src:
        *undescribed*

    :param lnet_nid_t dst:
        *undescribed*

    :param unsigned int type:
        *undescribed*

    :param unsigned int portal:
        *undescribed*

    :param struct lnet_msg \*msg:
        *undescribed*

.. _`lnet_delay_rule_match_locked`:

lnet_delay_rule_match_locked
============================

.. c:function:: bool lnet_delay_rule_match_locked(lnet_hdr_t *hdr, struct lnet_msg *msg)

    will be delayed if there is a match.

    :param lnet_hdr_t \*hdr:
        *undescribed*

    :param struct lnet_msg \*msg:
        *undescribed*

.. _`lnet_delay_rule_check`:

lnet_delay_rule_check
=====================

.. c:function:: void lnet_delay_rule_check( void)

    This function can either be called by delay_rule_daemon, or by lnet_finalise

    :param  void:
        no arguments

.. _`lnet_delay_rule_add`:

lnet_delay_rule_add
===================

.. c:function:: int lnet_delay_rule_add(struct lnet_fault_attr *attr)

    There is no check for duplicated delay rule, all rules will be checked for incoming message.

    :param struct lnet_fault_attr \*attr:
        *undescribed*

.. _`lnet_delay_rule_del`:

lnet_delay_rule_del
===================

.. c:function:: int lnet_delay_rule_del(lnet_nid_t src, lnet_nid_t dst, bool shutdown)

    and \a dst are zero, all rules will be removed, otherwise only matched rules will be removed. If \a src is zero, then all rules have \a dst as destination will be remove If \a dst is zero, then all rules have \a src as source will be removed

    :param lnet_nid_t src:
        *undescribed*

    :param lnet_nid_t dst:
        *undescribed*

    :param bool shutdown:
        *undescribed*

.. _`lnet_delay_rule_del.description`:

Description
-----------

When a delay rule is removed, all delayed messages of this rule will be
processed immediately.

.. _`lnet_delay_rule_list`:

lnet_delay_rule_list
====================

.. c:function:: int lnet_delay_rule_list(int pos, struct lnet_fault_attr *attr, struct lnet_fault_stat *stat)

    :param int pos:
        *undescribed*

    :param struct lnet_fault_attr \*attr:
        *undescribed*

    :param struct lnet_fault_stat \*stat:
        *undescribed*

.. _`lnet_delay_rule_reset`:

lnet_delay_rule_reset
=====================

.. c:function:: void lnet_delay_rule_reset( void)

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

