.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/lsm_audit.c

.. _`ipv4_skb_to_auditdata`:

ipv4_skb_to_auditdata
=====================

.. c:function:: int ipv4_skb_to_auditdata(struct sk_buff *skb, struct common_audit_data *ad, u8 *proto)

    fill auditdata from skb

    :param skb:
        the skb
    :type skb: struct sk_buff \*

    :param ad:
        the audit data to fill
    :type ad: struct common_audit_data \*

    :param proto:
        the layer 4 protocol
    :type proto: u8 \*

.. _`ipv4_skb_to_auditdata.description`:

Description
-----------

return  0 on success

.. _`ipv6_skb_to_auditdata`:

ipv6_skb_to_auditdata
=====================

.. c:function:: int ipv6_skb_to_auditdata(struct sk_buff *skb, struct common_audit_data *ad, u8 *proto)

    fill auditdata from skb

    :param skb:
        the skb
    :type skb: struct sk_buff \*

    :param ad:
        the audit data to fill
    :type ad: struct common_audit_data \*

    :param proto:
        the layer 4 protocol
    :type proto: u8 \*

.. _`ipv6_skb_to_auditdata.description`:

Description
-----------

return  0 on success

.. _`dump_common_audit_data`:

dump_common_audit_data
======================

.. c:function:: void dump_common_audit_data(struct audit_buffer *ab, struct common_audit_data *a)

    helper to dump common audit data

    :param ab:
        *undescribed*
    :type ab: struct audit_buffer \*

    :param a:
        common audit data
    :type a: struct common_audit_data \*

.. _`common_lsm_audit`:

common_lsm_audit
================

.. c:function:: void common_lsm_audit(struct common_audit_data *a, void (*pre_audit)(struct audit_buffer *, void *), void (*post_audit)(struct audit_buffer *, void *))

    generic LSM auditing function

    :param a:
        auxiliary audit data
    :type a: struct common_audit_data \*

    :param void (\*pre_audit)(struct audit_buffer \*, void \*):
        lsm-specific pre-audit callback

    :param void (\*post_audit)(struct audit_buffer \*, void \*):
        lsm-specific post-audit callback

.. _`common_lsm_audit.description`:

Description
-----------

setup the audit buffer for common security information
uses callback to print LSM specific information

.. This file was automatic generated / don't edit.

