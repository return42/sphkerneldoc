.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/options.c

.. _`dccp_parse_options`:

dccp_parse_options
==================

.. c:function:: int dccp_parse_options(struct sock *sk, struct dccp_request_sock *dreq, struct sk_buff *skb)

    Parse DCCP options present in \ ``skb``\ 

    :param sk:
        client\|server\|listening dccp socket (when \ ``dreq``\  != NULL)
    :type sk: struct sock \*

    :param dreq:
        request socket to use during connection setup, or NULL
    :type dreq: struct dccp_request_sock \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`dccp_insert_option_mandatory`:

dccp_insert_option_mandatory
============================

.. c:function:: int dccp_insert_option_mandatory(struct sk_buff *skb)

    Mandatory option (5.8.2) Note that since we are using skb_push, this function needs to be called \_after\_ inserting the option it is supposed to influence (stack order).

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`dccp_insert_fn_opt`:

dccp_insert_fn_opt
==================

.. c:function:: int dccp_insert_fn_opt(struct sk_buff *skb, u8 type, u8 feat, u8 *val, u8 len, bool repeat_first)

    Insert single Feature-Negotiation option into \ ``skb``\ 

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param type:
        \ ``DCCPO_CHANGE_L``\ , \ ``DCCPO_CHANGE_R``\ , \ ``DCCPO_CONFIRM_L``\ , \ ``DCCPO_CONFIRM_R``\ 
    :type type: u8

    :param feat:
        one out of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param val:
        NN value or SP array (preferred element first) to copy
    :type val: u8 \*

    :param len:
        true length of \ ``val``\  in bytes (excluding first element repetition)
    :type len: u8

    :param repeat_first:
        whether to copy the first element of \ ``val``\  twice
    :type repeat_first: bool

.. _`dccp_insert_fn_opt.description`:

Description
-----------

The last argument is used to construct Confirm options, where the preferred
value and the preference list appear separately (RFC 4340, 6.3.1). Preference
lists are kept such that the preferred entry is always first, so we only need
to copy twice, and avoid the overhead of cloning into a bigger array.

.. This file was automatic generated / don't edit.

