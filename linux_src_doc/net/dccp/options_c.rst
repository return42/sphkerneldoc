.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/options.c

.. _`dccp_parse_options`:

dccp_parse_options
==================

.. c:function:: int dccp_parse_options(struct sock *sk, struct dccp_request_sock *dreq, struct sk_buff *skb)

    Parse DCCP options present in \ ``skb``\ 

    :param struct sock \*sk:
        client\|server\|listening dccp socket (when \ ``dreq``\  != NULL)

    :param struct dccp_request_sock \*dreq:
        request socket to use during connection setup, or NULL

    :param struct sk_buff \*skb:
        *undescribed*

.. _`dccp_insert_option_mandatory`:

dccp_insert_option_mandatory
============================

.. c:function:: int dccp_insert_option_mandatory(struct sk_buff *skb)

    Mandatory option (5.8.2) Note that since we are using skb_push, this function needs to be called \_after\_ inserting the option it is supposed to influence (stack order).

    :param struct sk_buff \*skb:
        *undescribed*

.. _`dccp_insert_fn_opt`:

dccp_insert_fn_opt
==================

.. c:function:: int dccp_insert_fn_opt(struct sk_buff *skb, u8 type, u8 feat, u8 *val, u8 len, bool repeat_first)

    Insert single Feature-Negotiation option into \ ``skb``\ 

    :param struct sk_buff \*skb:
        *undescribed*

    :param u8 type:
        \ ``DCCPO_CHANGE_L``\ , \ ``DCCPO_CHANGE_R``\ , \ ``DCCPO_CONFIRM_L``\ , \ ``DCCPO_CONFIRM_R``\ 

    :param u8 feat:
        one out of \ ``dccp_feature_numbers``\ 

    :param u8 \*val:
        NN value or SP array (preferred element first) to copy

    :param u8 len:
        true length of \ ``val``\  in bytes (excluding first element repetition)

    :param bool repeat_first:
        whether to copy the first element of \ ``val``\  twice

.. _`dccp_insert_fn_opt.description`:

Description
-----------

The last argument is used to construct Confirm options, where the preferred
value and the preference list appear separately (RFC 4340, 6.3.1). Preference
lists are kept such that the preferred entry is always first, so we only need
to copy twice, and avoid the overhead of cloning into a bigger array.

.. This file was automatic generated / don't edit.

