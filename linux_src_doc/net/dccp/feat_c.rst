.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/feat.c

.. _`dccp_feat_index`:

dccp_feat_index
===============

.. c:function:: int dccp_feat_index(u8 feat_num)

    Hash function to map feature number into array position Returns consecutive array index or -1 if the feature is not understood.

    :param feat_num:
        *undescribed*
    :type feat_num: u8

.. _`dccp_feat_activate`:

dccp_feat_activate
==================

.. c:function:: int dccp_feat_activate(struct sock *sk, u8 feat_num, bool local, dccp_feat_val const *fval)

    Activate feature value on socket

    :param sk:
        fully connected DCCP socket (after handshake is complete)
    :type sk: struct sock \*

    :param feat_num:
        feature to activate, one of \ ``dccp_feature_numbers``\ 
    :type feat_num: u8

    :param local:
        whether local (1) or remote (0) \ ``feat_num``\  is meant
    :type local: bool

    :param fval:
        the value (SP or NN) to activate, or NULL to use the default value
    :type fval: dccp_feat_val const \*

.. _`dccp_feat_activate.description`:

Description
-----------

For general use this function is preferable over \__dccp_feat_activate().

.. _`dccp_feat_entry_new`:

dccp_feat_entry_new
===================

.. c:function:: struct dccp_feat_entry *dccp_feat_entry_new(struct list_head *head, u8 feat, bool local)

    Central list update routine (called by all others)

    :param head:
        list to add to
    :type head: struct list_head \*

    :param feat:
        feature number
    :type feat: u8

    :param local:
        whether the local (1) or remote feature with number \ ``feat``\  is meant
    :type local: bool

.. _`dccp_feat_entry_new.description`:

Description
-----------

This is the only constructor and serves to ensure the above invariants.

.. _`dccp_feat_push_change`:

dccp_feat_push_change
=====================

.. c:function:: int dccp_feat_push_change(struct list_head *fn_list, u8 feat, u8 local, u8 mandatory, dccp_feat_val *fval)

    Add/overwrite a Change option in the list

    :param fn_list:
        feature-negotiation list to update
    :type fn_list: struct list_head \*

    :param feat:
        one of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param local:
        whether local (1) or remote (0) \ ``feat_num``\  is meant
    :type local: u8

    :param mandatory:
        whether to use Mandatory feature negotiation options
    :type mandatory: u8

    :param fval:
        pointer to NN/SP value to be inserted (will be copied)
    :type fval: dccp_feat_val \*

.. _`dccp_feat_push_confirm`:

dccp_feat_push_confirm
======================

.. c:function:: int dccp_feat_push_confirm(struct list_head *fn_list, u8 feat, u8 local, dccp_feat_val *fval)

    Add a Confirm entry to the FN list

    :param fn_list:
        feature-negotiation list to add to
    :type fn_list: struct list_head \*

    :param feat:
        one of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param local:
        whether local (1) or remote (0) \ ``feat_num``\  is being confirmed
    :type local: u8

    :param fval:
        pointer to NN/SP value to be inserted or NULL
    :type fval: dccp_feat_val \*

.. _`dccp_feat_push_confirm.description`:

Description
-----------

Returns 0 on success, a Reset code for further processing otherwise.

.. _`dccp_feat_valid_nn_length`:

dccp_feat_valid_nn_length
=========================

.. c:function:: u8 dccp_feat_valid_nn_length(u8 feat_num)

    Enforce length constraints on NN options Length is between 0 and \ ``DCCP_OPTVAL_MAXLEN``\ . Used for outgoing packets only, incoming options are accepted as long as their values are valid.

    :param feat_num:
        *undescribed*
    :type feat_num: u8

.. _`dccp_feat_insert_opts`:

dccp_feat_insert_opts
=====================

.. c:function:: int dccp_feat_insert_opts(struct dccp_sock *dp, struct dccp_request_sock *dreq, struct sk_buff *skb)

    Generate FN options from current list state

    :param dp:
        for client during handshake and general negotiation
    :type dp: struct dccp_sock \*

    :param dreq:
        used by the server only (all Changes/Confirms in LISTEN/RESPOND)
    :type dreq: struct dccp_request_sock \*

    :param skb:
        next sk_buff to be sent to the peer
    :type skb: struct sk_buff \*

.. _`__feat_register_nn`:

\__feat_register_nn
===================

.. c:function:: int __feat_register_nn(struct list_head *fn, u8 feat, u8 mandatory, u64 nn_val)

    Register new NN value on socket

    :param fn:
        feature-negotiation list to register with
    :type fn: struct list_head \*

    :param feat:
        an NN feature from \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param mandatory:
        use Mandatory option if 1
    :type mandatory: u8

    :param nn_val:
        value to register (restricted to 4 bytes)
    :type nn_val: u64

.. _`__feat_register_nn.description`:

Description
-----------

Note that NN features are local by definition (RFC 4340, 6.3.2).

.. _`__feat_register_sp`:

\__feat_register_sp
===================

.. c:function:: int __feat_register_sp(struct list_head *fn, u8 feat, u8 is_local, u8 mandatory, u8 const *sp_val, u8 sp_len)

    Register new SP value/list on socket

    :param fn:
        feature-negotiation list to register with
    :type fn: struct list_head \*

    :param feat:
        an SP feature from \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param is_local:
        whether the local (1) or the remote (0) \ ``feat``\  is meant
    :type is_local: u8

    :param mandatory:
        use Mandatory option if 1
    :type mandatory: u8

    :param sp_val:
        SP value followed by optional preference list
    :type sp_val: u8 const \*

    :param sp_len:
        length of \ ``sp_val``\  in bytes
    :type sp_len: u8

.. _`dccp_feat_register_sp`:

dccp_feat_register_sp
=====================

.. c:function:: int dccp_feat_register_sp(struct sock *sk, u8 feat, u8 is_local, u8 const *list, u8 len)

    Register requests to change SP feature values

    :param sk:
        client or listening socket
    :type sk: struct sock \*

    :param feat:
        one of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param is_local:
        whether the local (1) or remote (0) \ ``feat``\  is meant
    :type is_local: u8

    :param list:
        array of preferred values, in descending order of preference
    :type list: u8 const \*

    :param len:
        length of \ ``list``\  in bytes
    :type len: u8

.. _`dccp_feat_nn_get`:

dccp_feat_nn_get
================

.. c:function:: u64 dccp_feat_nn_get(struct sock *sk, u8 feat)

    Query current/pending value of NN feature

    :param sk:
        DCCP socket of an established connection
    :type sk: struct sock \*

    :param feat:
        NN feature number from \ ``dccp_feature_numbers``\ 
    :type feat: u8

.. _`dccp_feat_nn_get.description`:

Description
-----------

For a known NN feature, returns value currently being negotiated, or
current (confirmed) value if no negotiation is going on.

.. _`dccp_feat_signal_nn_change`:

dccp_feat_signal_nn_change
==========================

.. c:function:: int dccp_feat_signal_nn_change(struct sock *sk, u8 feat, u64 nn_val)

    Update NN values for an established connection

    :param sk:
        DCCP socket of an established connection
    :type sk: struct sock \*

    :param feat:
        NN feature number from \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param nn_val:
        the new value to use
    :type nn_val: u64

.. _`dccp_feat_signal_nn_change.description`:

Description
-----------

This function is used to communicate NN updates out-of-band.

.. _`dccp_feat_propagate_ccid`:

dccp_feat_propagate_ccid
========================

.. c:function:: int dccp_feat_propagate_ccid(struct list_head *fn, u8 id, bool is_local)

    Resolve dependencies of features on choice of CCID

    :param fn:
        feature-negotiation list to update
    :type fn: struct list_head \*

    :param id:
        CCID number to track
    :type id: u8

    :param is_local:
        whether TX CCID (1) or RX CCID (0) is meant
    :type is_local: bool

.. _`dccp_feat_propagate_ccid.description`:

Description
-----------

This function needs to be called after registering all other features.

.. _`dccp_feat_finalise_settings`:

dccp_feat_finalise_settings
===========================

.. c:function:: int dccp_feat_finalise_settings(struct dccp_sock *dp)

    Finalise settings before starting negotiation

    :param dp:
        client or listening socket (settings will be inherited)
    :type dp: struct dccp_sock \*

.. _`dccp_feat_finalise_settings.description`:

Description
-----------

This is called after all registrations (socket initialisation, sysctls, and
sockopt calls), and before sending the first packet containing Change options
(ie. client-Request or server-Response), to ensure internal consistency.

.. _`dccp_feat_server_ccid_dependencies`:

dccp_feat_server_ccid_dependencies
==================================

.. c:function:: int dccp_feat_server_ccid_dependencies(struct dccp_request_sock *dreq)

    Resolve CCID-dependent features It is the server which resolves the dependencies once the CCID has been fully negotiated. If no CCID has been negotiated, it uses the default CCID.

    :param dreq:
        *undescribed*
    :type dreq: struct dccp_request_sock \*

.. _`dccp_feat_prefer`:

dccp_feat_prefer
================

.. c:function:: u8 dccp_feat_prefer(u8 preferred_value, u8 *array, u8 array_len)

    Move preferred entry to the start of array Reorder the \ ``array_len``\  elements in \ ``array``\  so that \ ``preferred_value``\  comes first. Returns >0 to indicate that \ ``preferred_value``\  does occur in \ ``array``\ .

    :param preferred_value:
        *undescribed*
    :type preferred_value: u8

    :param array:
        *undescribed*
    :type array: u8 \*

    :param array_len:
        *undescribed*
    :type array_len: u8

.. _`dccp_feat_reconcile`:

dccp_feat_reconcile
===================

.. c:function:: int dccp_feat_reconcile(dccp_feat_val *fv, u8 *arr, u8 len, bool is_server, bool reorder)

    Reconcile SP preference lists

    :param fv:
        SP list to reconcile into
    :type fv: dccp_feat_val \*

    :param arr:
        received SP preference list
    :type arr: u8 \*

    :param len:
        length of \ ``arr``\  in bytes
    :type len: u8

    :param is_server:
        whether this side is the server (and \ ``fv``\  is the server's list)
    :type is_server: bool

    :param reorder:
        whether to reorder the list in \ ``fv``\  after reconciling with \ ``arr``\ 
        When successful, > 0 is returned and the reconciled list is in \ ``fval``\ .
        A value of 0 means that negotiation failed (no shared entry).
    :type reorder: bool

.. _`dccp_feat_change_recv`:

dccp_feat_change_recv
=====================

.. c:function:: u8 dccp_feat_change_recv(struct list_head *fn, u8 is_mandatory, u8 opt, u8 feat, u8 *val, u8 len, const bool server)

    Process incoming ChangeL/R options

    :param fn:
        feature-negotiation list to update
    :type fn: struct list_head \*

    :param is_mandatory:
        whether the Change was preceded by a Mandatory option
    :type is_mandatory: u8

    :param opt:
        \ ``DCCPO_CHANGE_L``\  or \ ``DCCPO_CHANGE_R``\ 
    :type opt: u8

    :param feat:
        one of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param val:
        NN value or SP value/preference list
    :type val: u8 \*

    :param len:
        length of \ ``val``\  in bytes
    :type len: u8

    :param server:
        whether this node is the server (1) or the client (0)
    :type server: const bool

.. _`dccp_feat_confirm_recv`:

dccp_feat_confirm_recv
======================

.. c:function:: u8 dccp_feat_confirm_recv(struct list_head *fn, u8 is_mandatory, u8 opt, u8 feat, u8 *val, u8 len, const bool server)

    Process received Confirm options

    :param fn:
        feature-negotiation list to update
    :type fn: struct list_head \*

    :param is_mandatory:
        whether \ ``opt``\  was preceded by a Mandatory option
    :type is_mandatory: u8

    :param opt:
        \ ``DCCPO_CONFIRM_L``\  or \ ``DCCPO_CONFIRM_R``\ 
    :type opt: u8

    :param feat:
        one of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param val:
        NN value or SP value/preference list
    :type val: u8 \*

    :param len:
        length of \ ``val``\  in bytes
    :type len: u8

    :param server:
        whether this node is server (1) or client (0)
    :type server: const bool

.. _`dccp_feat_handle_nn_established`:

dccp_feat_handle_nn_established
===============================

.. c:function:: u8 dccp_feat_handle_nn_established(struct sock *sk, u8 mandatory, u8 opt, u8 feat, u8 *val, u8 len)

    Fast-path reception of NN options

    :param sk:
        socket of an established DCCP connection
    :type sk: struct sock \*

    :param mandatory:
        whether \ ``opt``\  was preceded by a Mandatory option
    :type mandatory: u8

    :param opt:
        \ ``DCCPO_CHANGE_L``\  \| \ ``DCCPO_CONFIRM_R``\  (NN only)
    :type opt: u8

    :param feat:
        NN number, one of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param val:
        NN value
    :type val: u8 \*

    :param len:
        length of \ ``val``\  in bytes
    :type len: u8

.. _`dccp_feat_handle_nn_established.description`:

Description
-----------

This function combines the functionality of change_recv/confirm_recv, with
the following differences (reset codes are the same):
- cleanup after receiving the Confirm;
- values are directly activated after successful parsing;
- deliberately restricted to NN features.
The restriction to NN features is essential since SP features can have non-
predictable outcomes (depending on the remote configuration), and are inter-
dependent (CCIDs for instance cause further dependencies).

.. _`dccp_feat_parse_options`:

dccp_feat_parse_options
=======================

.. c:function:: int dccp_feat_parse_options(struct sock *sk, struct dccp_request_sock *dreq, u8 mandatory, u8 opt, u8 feat, u8 *val, u8 len)

    Process Feature-Negotiation Options

    :param sk:
        for general use and used by the client during connection setup
    :type sk: struct sock \*

    :param dreq:
        used by the server during connection setup
    :type dreq: struct dccp_request_sock \*

    :param mandatory:
        whether \ ``opt``\  was preceded by a Mandatory option
    :type mandatory: u8

    :param opt:
        \ ``DCCPO_CHANGE_L``\  \| \ ``DCCPO_CHANGE_R``\  \| \ ``DCCPO_CONFIRM_L``\  \| \ ``DCCPO_CONFIRM_R``\ 
    :type opt: u8

    :param feat:
        one of \ ``dccp_feature_numbers``\ 
    :type feat: u8

    :param val:
        value contents of \ ``opt``\ 
    :type val: u8 \*

    :param len:
        length of \ ``val``\  in bytes
    :type len: u8

.. _`dccp_feat_parse_options.description`:

Description
-----------

Returns 0 on success, a Reset code for ending the connection otherwise.

.. _`dccp_feat_init`:

dccp_feat_init
==============

.. c:function:: int dccp_feat_init(struct sock *sk)

    Seed feature negotiation with host-specific defaults This initialises global defaults, depending on the value of the sysctls. These can later be overridden by registering changes via setsockopt calls. The last link in the chain is finalise_settings, to make sure that between here and the start of actual feature negotiation no inconsistencies enter.

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`dccp_feat_init.description`:

Description
-----------

All features not appearing below use either defaults or are otherwise
later adjusted through \ :c:func:`dccp_feat_finalise_settings`\ .

.. This file was automatic generated / don't edit.

